#!/usr/bin/env python3
"""Erzeugt aus analysis.json ein eigenstaendiges HTML-Dashboard.

Keine externen Abhaengigkeiten, keine Netzwerkzugriffe, nur Python-Stdlib.
Charts sind inline SVG. Farblogik: eine Datenfarbe (Emerald) plus ein Akzent
(Signal) ausschliesslich fuer das, was auffaellt. Keine kategorische Palette,
weil jeder Chart genau eine Serie hat.
"""

import argparse
import html
import json
import sys

PAPER = "#FAFAF7"
INK = "#083A2A"
EMERALD = "#0B6E4F"
EMERALD_HELL = "#10A26B"
MOSS = "#D4EDE0"
SIGNAL = "#F2653C"


def esc(x):
    return html.escape(str(x))


def pct(x, digits=1):
    if x is None:
        return "n/a"
    return f"{x * 100:.{digits}f}".replace(".", ",") + " %"


def eur(x, digits=0):
    if x is None:
        return "n/a"
    s = f"{x:,.{digits}f}"
    return s.replace(",", "_").replace(".", ",").replace("_", ".") + " EUR"


def num(x):
    return f"{x:,.0f}".replace(",", ".")


def bars(rows, value_key, label_key, fmt, highlight=None, height=26, gap=10, label_w=None):
    """Horizontale Balken als SVG. rows: Liste von dicts. highlight: Funktion -> bool.

    Das Label-Feld waechst mit dem laengsten Label mit, damit nichts ueberlaeuft.
    """
    if not rows:
        return "<p class='leer'>Keine Daten.</p>"
    vals = [abs(r[value_key] or 0) for r in rows]
    vmax = max(vals) or 1
    if label_w is None:
        laengste = max(len(str(r[label_key])) for r in rows)
        label_w = max(150, min(330, int(laengste * 7.4) + 14))
    bar_w = 430
    total_h = len(rows) * (height + gap)
    out = [f'<svg viewBox="0 0 {label_w + bar_w + 100} {total_h}" role="img" class="chart">']
    for i, r in enumerate(rows):
        y = i * (height + gap)
        v = r[value_key] or 0
        w = max(2, abs(v) / vmax * bar_w)
        farbe = SIGNAL if (highlight and highlight(r)) else "var(--serie)"
        titel = f"{r[label_key]}: {fmt(v)}"
        out.append(
            f'<text x="0" y="{y + height * 0.7}" class="lbl">{esc(r[label_key])}</text>'
            f'<g class="mark"><title>{esc(titel)}</title>'
            f'<rect x="{label_w}" y="{y}" width="{w:.1f}" height="{height}" rx="4" fill="{farbe}"/></g>'
            f'<text x="{label_w + w + 10:.1f}" y="{y + height * 0.7}" class="val">{esc(fmt(v))}</text>'
        )
    out.append("</svg>")
    return "".join(out)


def kohorten_chart(kohorten):
    """Senkrechte Balken je Bestellmonat. Unreife Kohorten schraffiert plus Label."""
    if not kohorten:
        return ""
    w_bar, gap, h = 62, 26, 190
    vals = [k["beta_quote"] or 0 for k in kohorten]
    vmax = max(vals) or 1
    breite = len(kohorten) * (w_bar + gap)
    out = [
        f'<svg viewBox="0 0 {breite} {h + 62}" role="img" class="chart">',
        '<defs><pattern id="unreif" width="7" height="7" patternTransform="rotate(45)" '
        'patternUnits="userSpaceOnUse">'
        f'<rect width="7" height="7" fill="var(--serie)" opacity="0.28"/>'
        f'<line x1="0" y1="0" x2="0" y2="7" stroke="var(--serie)" stroke-width="3"/>'
        "</pattern></defs>",
    ]
    for i, k in enumerate(kohorten):
        x = i * (w_bar + gap)
        v = k["beta_quote"] or 0
        bh = max(3, v / vmax * h)
        y = h - bh
        fill = "url(#unreif)" if not k["mature"] else "var(--serie)"
        note = " (unvollständig)" if not k["mature"] else ""
        out.append(
            f'<g class="mark"><title>{esc(k["kohorte"])}: {esc(pct(v))}{esc(note)}</title>'
            f'<rect x="{x}" y="{y:.1f}" width="{w_bar}" height="{bh:.1f}" rx="4" fill="{fill}"/></g>'
            f'<text x="{x + w_bar / 2}" y="{y - 9:.1f}" class="val mitte">{esc(pct(v))}</text>'
            f'<text x="{x + w_bar / 2}" y="{h + 20}" class="lbl mitte">{esc(k["kohorte"][5:])}.{esc(k["kohorte"][2:4])}</text>'
        )
        if not k["mature"]:
            out.append(
                f'<text x="{x + w_bar / 2}" y="{h + 38}" class="mini mitte">unvollständig</text>'
            )
    out.append("</svg>")
    return "".join(out)


def kachel(label, wert, zusatz="", akzent=False):
    kl = " akzent" if akzent else ""
    z = f'<div class="zusatz">{esc(zusatz)}</div>' if zusatz else ""
    return (
        f'<div class="kachel{kl}"><div class="klabel">{esc(label)}</div>'
        f'<div class="kwert">{esc(wert)}</div>{z}</div>'
    )


def build(d, titel):
    q = d["quoten"]
    meta = d["meta"]
    kosten = d["kosten_top"]
    kosten_summe = sum(c["gesamt"] for c in kosten)
    np_ = d["nicht_abgeholt"]

    # --- KPI-Zeile
    kacheln = [
        kachel("Retouren nach Menge", pct(q["gesamt_beta"]), "Beta-Quote"),
        kachel("Retouren nach Wert", pct(q["gesamt_gamma"]), "Gamma-Quote"),
        kachel("Bestellungen mit Retoure", pct(q["gesamt_bestellquote"]), f'{num(meta["bestellungen"])} Bestellungen'),
        kachel("Kosten der Top-Artikel", eur(kosten_summe), "erstattet, Prozess, Wertverlust", akzent=True),
    ]

    # --- Blinde Flecken
    flecken = []
    for b in d.get("blinde_flecken", []):
        detail = b.get("befund", "")
        if not detail and b.get("artikel"):
            a = b["artikel"][0]
            if "db_nach_retouren" in a:
                detail = (f'{a["name"]} ({a["sku"]}): {eur(a["db_vor_retouren"])} vor Retouren, '
                          f'{eur(a["db_nach_retouren"])} danach.')
            else:
                detail = f'{a["name"]} ({a["sku"]}): Quote {pct(a["beta_quote"])}, Kosten {eur(a["kosten"])}.'
        if not detail and b.get("kontraste"):
            k = b["kontraste"][0]
            detail = (f'{k["merkmal"]}: {pct(k["anteil_bei_nicht_abgeholt"])} der nicht abgeholten Sendungen, '
                      f'aber nur {pct(k["anteil_im_gesamtgeschaeft"])} des Gesamtgeschäfts.')
        if not detail and b.get("anteil") is not None:
            detail = f'{num(b["anzahl"])} Retouren, {pct(b["anteil"])} aller Fälle.'
        flecken.append(
            f'<article class="fleck"><h3>{esc(b["titel"])}</h3>'
            f'<p class="befund">{esc(detail)}</p>'
            f'<p class="warum"><span class="warum-lbl">Warum das im Standard-Report fehlt</span>'
            f'{esc(b["warum_uebersehen"])}</p></article>'
        )

    # --- Charts
    gruende = [{"grund": k.replace("_", " "), "n": v} for k, v in list(d["gruende"].items())[:8]]
    chart_gruende = bars(gruende, "n", "grund", lambda v: num(v),
                         highlight=lambda r: "nicht abgeholt" in r["grund"] or "sonstiges" in r["grund"])

    kosten_rows = [{"art": f'{c["name"]} · {c["sku"].split("-")[-1]}', "wert": c["gesamt"],
                    "neg": c.get("deckungsbeitrag_nach_retouren") is not None
                           and c["deckungsbeitrag_nach_retouren"] < 0}
                   for c in kosten[:8]]
    chart_kosten = bars(kosten_rows, "wert", "art", lambda v: eur(v),
                        highlight=lambda r: r["neg"])

    zahlart = []
    kontrast = None
    for b in d.get("blinde_flecken", []):
        if b.get("kontraste"):
            kontrast = b["kontraste"][0]
    if kontrast:
        zahlart = [
            {"was": "Anteil am Gesamtgeschäft", "v": kontrast["anteil_im_gesamtgeschaeft"], "hot": False},
            {"was": "Anteil bei nicht abgeholt", "v": kontrast["anteil_bei_nicht_abgeholt"], "hot": True},
        ]
    chart_zahlart = bars(zahlart, "v", "was", lambda v: pct(v), highlight=lambda r: r["hot"]) if zahlart else ""

    laeufer = d.get("groessen_laeufer", [])
    chart_laeufer = ""
    if laeufer:
        l = laeufer[0]
        rows = [{"g": f'Größe {g}', "n": c.get("zu_klein", 0)} for g, c in sorted(l["je_groesse"].items())]
        chart_laeufer = bars(rows, "n", "g", lambda v: num(v))

    # --- Annahmen
    annahmen = "".join(f"<li>{esc(a)}</li>" for a in meta["annahmen"])
    fehlend = "".join(f'<li><code>{esc(m["spalte"])}</code> würde ermöglichen: {esc(m["entfallene_analyse"])}</li>'
                      for m in meta["fehlende_spalten"])

    return f"""<!doctype html>
<html lang="de"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(titel)}</title>
<style>
  :root {{
    --paper: {PAPER}; --ink: {INK}; --serie: {EMERALD}; --moss: {MOSS}; --signal: {SIGNAL};
    --bg: var(--paper); --text: var(--ink); --panel: #fff; --linie: rgba(8,58,42,.12);
    --gedaempft: rgba(8,58,42,.62);
  }}
  @media (prefers-color-scheme: dark) {{
    :root {{ --bg: {INK}; --text: {PAPER}; --serie: {EMERALD_HELL};
      --panel: rgba(212,237,224,.06); --linie: rgba(212,237,224,.16); --gedaempft: rgba(250,250,247,.66); }}
  }}
  * {{ box-sizing: border-box; }}
  body {{ margin: 0; background: var(--bg); color: var(--text);
    font-family: ui-sans-serif, system-ui, "Inter", sans-serif; line-height: 1.55;
    font-feature-settings: "tnum" 1; }}
  .wrap {{ max-width: 1120px; margin: 0 auto; padding: 48px 24px 80px; }}
  .eyebrow {{ font-family: ui-monospace, "JetBrains Mono", monospace; font-size: 11px;
    letter-spacing: .14em; text-transform: uppercase; color: var(--gedaempft); margin: 0 0 10px; }}
  h1 {{ font-size: 30px; line-height: 1.2; margin: 0 0 6px; font-weight: 600; letter-spacing: -.01em; }}
  h1 .punkt {{ color: var(--signal); }}
  .meta {{ color: var(--gedaempft); font-size: 14px; margin: 0 0 40px; }}
  h2 {{ font-size: 19px; margin: 46px 0 4px; font-weight: 600; letter-spacing: -.005em; }}
  h2 + .hint {{ color: var(--gedaempft); font-size: 14px; margin: 0 0 18px; }}
  .kacheln {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(210px, 1fr)); gap: 14px; }}
  .kachel {{ background: var(--panel); border: 1px solid var(--linie); padding: 18px 18px 16px; }}
  .kachel.akzent {{ border-top: 3px solid var(--signal); }}
  .klabel {{ font-family: ui-monospace, monospace; font-size: 10.5px; letter-spacing: .12em;
    text-transform: uppercase; color: var(--gedaempft); }}
  .kwert {{ font-size: 32px; font-weight: 600; letter-spacing: -.02em; margin-top: 6px; }}
  .zusatz {{ font-size: 13px; color: var(--gedaempft); margin-top: 2px; }}
  .flecken {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 14px; }}
  .fleck {{ background: var(--panel); border: 1px solid var(--linie); border-left: 3px solid var(--signal);
    padding: 18px 20px; }}
  .fleck h3 {{ font-size: 15.5px; margin: 0 0 8px; font-weight: 600; }}
  .befund {{ margin: 0 0 10px; }}
  .warum {{ margin: 0; font-size: 13.5px; color: var(--gedaempft); }}
  .warum-lbl {{ display: block; font-family: ui-monospace, monospace; font-size: 10px;
    letter-spacing: .12em; text-transform: uppercase; margin-bottom: 3px; }}
  .chart {{ width: 100%; height: auto; overflow: visible; margin-top: 6px; }}
  .chart .lbl {{ font-size: 13px; fill: var(--text); }}
  .chart .val {{ font-size: 12.5px; fill: var(--gedaempft); }}
  .chart .mini {{ font-size: 10px; fill: var(--signal); font-family: ui-monospace, monospace; }}
  .chart .mitte {{ text-anchor: middle; }}
  .chart .mark {{ transition: opacity .12s; }}
  .chart .mark:hover {{ opacity: .72; }}
  table {{ width: 100%; border-collapse: collapse; font-size: 14px; margin-top: 8px; }}
  th, td {{ text-align: left; padding: 9px 10px 9px 0; border-bottom: 1px solid var(--linie); }}
  th {{ font-family: ui-monospace, monospace; font-size: 10.5px; letter-spacing: .1em;
    text-transform: uppercase; color: var(--gedaempft); font-weight: 400; }}
  td.zahl, th.zahl {{ text-align: right; padding-right: 0; }}
  td.neg {{ color: var(--signal); font-weight: 600; }}
  .fuss {{ margin-top: 56px; padding-top: 22px; border-top: 1px solid var(--linie);
    font-size: 13.5px; color: var(--gedaempft); }}
  .fuss ul {{ margin: 6px 0 18px; padding-left: 18px; }}
  .leer {{ color: var(--gedaempft); font-size: 14px; }}
  code {{ font-family: ui-monospace, monospace; font-size: .92em; }}
</style></head>
<body>
<div class="wrap">
  <p class="eyebrow">Retouren-Analyse</p>
  <h1>{esc(titel)}<span class="punkt">.</span></h1>
  <p class="meta">{num(meta["retouren_positionen"])} Retouren-Positionen aus {num(meta["bestellungen"])} Bestellungen ·
     Datenstand {esc(meta["zeitraum_bis"])}</p>

  <div class="kacheln">{"".join(kacheln)}</div>

  <h2>Was sonst untergegangen wäre</h2>
  <p class="hint">Befunde, die ein normaler Retouren-Report strukturell nicht zeigt.</p>
  <div class="flecken">{"".join(flecken)}</div>

  <h2>Retourenquote je Bestellmonat</h2>
  <p class="hint">Zugeordnet nach Bestellung, nicht nach Retourendatum. Schraffierte Monate sind noch
     nicht vollständig, ihre Quote sieht besser aus als sie ist.</p>
  {kohorten_chart(q["je_kohorte"])}

  <h2>Was die Retouren kostet</h2>
  <p class="hint">Erstattung plus Prozesskosten plus Wertverlust je Artikelvariante.
     Orange markiert: verdient nach Retouren nichts mehr.</p>
  {chart_kosten}

  <h2>Retourengründe</h2>
  <p class="hint">Orange markiert: Gründe, hinter denen sich ein eigener Fall verbergen kann.</p>
  {chart_gruende}

  {"<h2>Nicht abgeholte Sendungen</h2><p class='hint'>" +
   esc(f'{num(np_["sendungen"])} Sendungen, {eur(np_["verlorener_umsatz"])} Umsatz plus {eur(np_["zusatzkosten_versand_annahme"])} Prozesskosten. Der Kontrast zeigt sich erst, wenn man nur diese Fälle betrachtet.') +
   "</p>" + chart_zahlart if chart_zahlart else ""}

  {"<h2>Größenbedingte Retouren je Größe</h2><p class='hint'>" +
   esc(f'{laeufer[0]["style"]}: {laeufer[0]["zu_klein"]} mal zu klein gegen {laeufer[0]["zu_gross"]} mal zu groß. Der Artikel {laeufer[0]["richtung"]}.') +
   "</p>" + chart_laeufer if chart_laeufer else ""}

  <h2>Artikel im Detail</h2>
  <p class="hint">Dieselben Zahlen als Tabelle, damit sie kopierbar und prüfbar sind.</p>
  <table><thead><tr><th>Artikel</th><th>Variante</th><th class="zahl">Retouren</th>
    <th class="zahl">Kosten</th><th class="zahl">DB nach Retouren</th></tr></thead><tbody>
    {"".join(f'<tr><td>{esc(c["name"])}</td><td><code>{esc(c["sku"])}</code></td>'
             f'<td class="zahl">{num(c["retouren_vorgaenge"])}</td>'
             f'<td class="zahl">{esc(eur(c["gesamt"]))}</td>'
             f'<td class="zahl{" neg" if (c.get("deckungsbeitrag_nach_retouren") or 0) < 0 else ""}">'
             f'{esc(eur(c["deckungsbeitrag_nach_retouren"]) if c.get("deckungsbeitrag_nach_retouren") is not None else "n/a")}</td></tr>'
             for c in kosten)}
  </tbody></table>

  <div class="fuss">
    <strong>Annahmen</strong><ul>{annahmen}</ul>
    <strong>Was mit weiteren Spalten möglich wäre</strong><ul>{fehlend}</ul>
    <p>Jede Zahl stammt aus <code>analysis.json</code>. Nichts davon ist geschätzt.</p>
  </div>
</div>
</body></html>"""


def main():
    p = argparse.ArgumentParser(description="Dashboard aus analysis.json bauen")
    p.add_argument("--analyse", default="analysis.json")
    p.add_argument("--out", default="dashboard.html")
    p.add_argument("--titel", default="Retouren-Report")
    a = p.parse_args()

    with open(a.analyse, encoding="utf-8") as f:
        d = json.load(f)
    with open(a.out, "w", encoding="utf-8") as f:
        f.write(build(d, a.titel))
    print(f"OK: {a.out} geschrieben")
    return 0


if __name__ == "__main__":
    sys.exit(main())
