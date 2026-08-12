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
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import befunde as befunde_mod  # noqa: E402

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
    """Balken je Bestellmonat. Unvollständige Monate zeigen den Ist-Wert dunkel und
    die Hochrechnung auf den erwarteten Endwert hell darüber."""
    if not kohorten:
        return ""
    w_bar, gap, h = 66, 30, 190
    vals = [max(k.get("beta_hochgerechnet") or 0, k["beta_quote"] or 0) for k in kohorten]
    vmax = max(vals) or 1
    breite = len(kohorten) * (w_bar + gap)
    out = [f'<svg viewBox="0 0 {breite} {h + 70}" role="img" class="chart">']
    for i, k in enumerate(kohorten):
        x = i * (w_bar + gap)
        v = k["beta_quote"] or 0
        hoch = k.get("beta_hochgerechnet")
        bh = max(3, v / vmax * h)
        y = h - bh
        titel = f'{k["kohorte"]}: {pct(v)} bisher'
        if hoch:
            gesamt_h = hoch / vmax * h
            y_h = h - gesamt_h
            titel += f', hochgerechnet {pct(hoch)} bei {pct(k["reifegrad"], 0)} Reife'
            out.append(
                f'<rect x="{x}" y="{y_h:.1f}" width="{w_bar}" height="{(gesamt_h - bh):.1f}" '
                f'fill="var(--serie)" opacity="0.22"/>'
                f'<line x1="{x}" y1="{y_h:.1f}" x2="{x + w_bar}" y2="{y_h:.1f}" '
                f'stroke="var(--signal)" stroke-width="2" stroke-dasharray="4 3"/>'
                f'<text x="{x + w_bar / 2}" y="{y_h - 8:.1f}" class="mini mitte">{esc(pct(hoch))}</text>'
            )
        out.append(
            f'<g class="mark"><title>{esc(titel)}</title>'
            f'<rect x="{x}" y="{y:.1f}" width="{w_bar}" height="{bh:.1f}" fill="var(--serie)"/></g>'
            f'<text x="{x + w_bar / 2}" y="{h + 20}" class="lbl mitte">'
            f'{esc(k["kohorte"][5:])}.{esc(k["kohorte"][2:4])}</text>'
        )
        if hoch:
            out.append(f'<text x="{x + w_bar / 2}" y="{h + 38}" class="mini mitte">'
                       f'{esc(pct(k["reifegrad"], 0))} da</text>')
        else:
            out.append(f'<text x="{x + w_bar / 2}" y="{y + bh * 0.5 + 5:.1f}" class="val-inv mitte">'
                       f'{esc(pct(v))}</text>')
    out.append("</svg>")
    return "".join(out)


GRUND_NAMEN = {
    "zu_klein": "Zu klein",
    "zu_gross": "Zu groß",
    "passform_schnitt": "Passform oder Schnitt",
    "farbe_optik_gefaellt_nicht": "Farbe oder Optik gefällt nicht",
    "nicht_wie_beschrieben": "Nicht wie beschrieben",
    "qualitaet_defekt": "Qualität oder Defekt",
    "transportschaden": "Transportschaden",
    "falscher_artikel": "Falscher Artikel geliefert",
    "zu_spaet_geliefert": "Zu spät geliefert",
    "reue_nicht_benoetigt": "Doch nicht benötigt",
    "nicht_abgeholt_annahme_verweigert": "Nicht abgeholt oder verweigert",
    "sonstiges_unbekannt": "Kein Grund erfasst",
}


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
    ertrag_nach = sum(c["deckungsbeitrag_nach_retouren"] for c in kosten
                      if c.get("deckungsbeitrag_nach_retouren") is not None)
    np_ = d["nicht_abgeholt"]

    # --- KPI-Zeile
    kacheln = [
        kachel("Retouren nach Menge", pct(q["gesamt_beta"]), "Beta-Quote"),
        kachel("Retouren nach Wert", pct(q["gesamt_gamma"]), "Gamma-Quote"),
        kachel("Bestellungen mit Retoure", pct(q["gesamt_bestellquote"]), f'{num(meta["bestellungen"])} Bestellungen'),
        kachel("Ertrag nach Retouren", eur(ertrag_nach),
               f"Rohertrag der ausgewerteten Artikel minus {eur(kosten_summe)} Retourenkosten", akzent=True),
    ]

    # --- Charts
    gruende = [{"grund": GRUND_NAMEN.get(k, k.replace("_", " ")), "n": v}
               for k, v in list(d["gruende"].items())[:8]]
    chart_gruende = bars(gruende, "n", "grund", lambda v: num(v),
                         highlight=lambda r: "Nicht abgeholt" in r["grund"] or "Kein Grund" in r["grund"])

    kosten_rows = [{"art": f'{c["name"]} · {c["sku"]}', "wert": c["gesamt"],
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
        m = kontrast["merkmal"]
        zahlart = [
            {"was": f"{m}: Anteil an allen Bestellungen", "v": kontrast["anteil_im_gesamtgeschaeft"], "hot": False},
            {"was": f"{m}: Anteil an den nicht abgeholten", "v": kontrast["anteil_bei_nicht_abgeholt"], "hot": True},
        ]
    chart_zahlart = bars(zahlart, "v", "was", lambda v: pct(v), highlight=lambda r: r["hot"]) if zahlart else ""

    laeufer = d.get("groessen_laeufer", [])
    chart_laeufer = ""
    if laeufer:
        l = laeufer[0]
        rows = [{"g": f'Größe {g}', "n": c.get("zu_klein", 0)} for g, c in sorted(l["je_groesse"].items())]
        chart_laeufer = bars(rows, "n", "g", lambda v: num(v))

    # --- Befund-Karten: Zahl, Bedeutung, Maßnahme
    befunde = [b for b in befunde_mod.sammle(d)
               if not b["titel"].startswith("Die letzten Monate")
               and not b["titel"].startswith("Retouren ohne")]
    karten = []
    for i, b in enumerate(befunde, 1):
        schritte = "".join(f"<li>{esc(s)}</li>" for s in b["schritte"])
        unsichtbar = (
            f'<p class="unsichtbar"><span class="mini-lbl">Warum das im Standard-Report fehlt</span>'
            f'{esc(b["unsichtbar"])}</p>' if b.get("unsichtbar") else ""
        )
        beleg = (f'<p class="beleg"><span class="mini-lbl">Belegt</span>{esc(b["beleg"])}</p>'
                 if b.get("beleg") else "")
        einschr = (f'<p class="beleg"><span class="mini-lbl">Einschränkung</span>{esc(b["einschraenkung"])}</p>'
                   if b.get("einschraenkung") else "")
        chart, chart_titel, chart_hint = "", "", ""
        t = b["titel"]
        if "verdient nach Retouren" in t or "unauffällige Quote" in t:
            chart, chart_titel = chart_kosten, "Retourenkosten je Artikelvariante"
            chart_hint = ("Erstattung plus Bearbeitung plus Wertverlust. Orange markiert: Von dem, was "
                          "die Variante im Verkauf verdient hat, bleibt danach nichts übrig.")
        elif "abgeholt" in t:
            chart, chart_titel = chart_zahlart, "Rechnungskauf: normal gegen auffällig"
            chart_hint = ("Dieselbe Zahlart zweimal gemessen. Je weiter die Balken auseinanderliegen, "
                          "desto stärker hängt das Nichtabholen mit ihr zusammen.")
        elif "fällt" in t and chart_laeufer:
            chart = chart_laeufer
            chart_titel = b["titel"].split(" fällt")[0] + ': Retouren "zu klein" je Größe'
            chart_hint = ("Verteilt sich das über alle Größen, liegt es am Schnitt des Artikels. "
                          "Trifft es nur einzelne Größen, ist es die Gradierung.")
        chart_block = (f'<div class="metrik"><p class="metrik-titel">{esc(chart_titel)}</p>'
                       f'<p class="metrik-hint">{esc(chart_hint)}</p>{chart}</div>') if chart else ""
        karten.append(f"""
        <section class="befund-gruppe">
        {chart_block}
        <article class="befund-karte">
          <div class="bk-kopf">
            <span class="bk-nr">{i:02d}</span>
            <h3>{esc(b["titel"])}</h3>
            <span class="bk-hebel">{esc(b["hebel_text"])}</span>
          </div>
          <div class="bk-body">
            <div class="bk-spalte">
              <p class="mini-lbl">Was in den Daten steht</p>
              <p>{esc(b["was"])}</p>
              <p class="mini-lbl">Warum das zählt</p>
              <p>{esc(b["warum"])}</p>
              {unsichtbar}{beleg}{einschr}
            </div>
            <div class="bk-spalte">
              <p class="mini-lbl">Was zu tun ist</p>
              <ol>{schritte}</ol>
              <dl class="bk-meta">
                <dt>Aufwand</dt><dd>{esc(b["aufwand"])}</dd>
                <dt>Wer</dt><dd>{esc(b["wer"])}</dd>
                <dt>Woran du merkst, dass es wirkt</dt><dd>{esc(b["messung"])}</dd>
                <dt class="gegen">Was dabei nicht kaputtgehen darf</dt><dd>{esc(b["gegen"])}</dd>
              </dl>
            </div>
          </div>
        </article>
        </section>""")
    hebel_summe = sum(b["hebel"] for b in befunde if b["hebel"])

    # Retouren ohne Grund sind kein Geschäftsbefund, sondern eine Datenqualitätsaussage.
    # Sie gehört als Warnung an die Gründe-Auswertung, nicht in die Befundliste.
    og = next((f for f in d.get("blinde_flecken", []) if "keinen brauchbaren Grund" in f["titel"]), None)
    datenqualitaet = ""
    if og:
        datenqualitaet = (
            f'<div class="warnung"><span class="mini-lbl">Datenqualität</span>'
            f'Bei {num(og["anzahl"])} Retouren ({pct(og["anteil"])} aller Fälle) wurde kein verwertbarer '
            f'Grund erfasst. Die Verteilung unten ist entsprechend unsicher, und die Lücken verteilen '
            f'sich selten gleichmäßig. Lohnt zu prüfen, ob sie sich auf einzelne Artikel oder '
            f'Rückgabewege häufen, dort steckt dann meist ein eigener Fall.</div>')

    # --- Annahmen und fehlende Spalten, in Klartext
    ERKLAERT = {
        "delivered_date": ("Zustelldatum",
                           "Damit ließe sich messen, wie viele Tage zwischen Zustellung und Rücksendung "
                           "liegen. Sehr späte Rücksendungen kurz vor Fristende sind ein anderer Fall als "
                           "sofortige, und getragene Ware kommt typischerweise spät zurück."),
        "batch": ("Chargennummer",
                  "Damit wäre ein Qualitäts-Ausschlag eindeutig einer Lieferung zuzuordnen. Ohne sie "
                  "bleibt es bei der zeitlichen Vermutung: viele Defekte in einem Monat, vermutlich "
                  "dieselbe Charge."),
        "refund_type": ("Art der Erstattung",
                        "Also ob der Kunde Geld zurückbekam, einen Gutschein nahm oder umtauschte. "
                        "Damit ließe sich rechnen, wie viel Umsatz bei einer Retoure tatsächlich "
                        "verloren geht und wie viel im Haus bleibt."),
        "condition": ("Zustand der Rückware",
                      "Also ob der Artikel wieder als neu verkauft werden kann, als B-Ware rausgeht "
                      "oder entsorgt wird. Damit wäre der Wertverlust echt gerechnet statt geschätzt."),
    }
    annahmen = "".join(f"<li>{esc(a)}</li>" for a in meta["annahmen"])
    fehlend = ""
    for m in meta["fehlende_spalten"]:
        name, erkl = ERKLAERT.get(m["spalte"], (m["spalte"], m["entfallene_analyse"]))
        fehlend += (f'<li><strong>{esc(name)}</strong> <code>{esc(m["spalte"])}</code><br>{esc(erkl)}</li>')

    return f"""<!doctype html>
<html lang="de"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(titel)}</title>
<style>
  :root {{
    --paper: {PAPER}; --ink: {INK}; --serie: {EMERALD}; --moss: {MOSS}; --signal: {SIGNAL};
    --bg: var(--paper); --text: var(--ink); --panel: #fff; --linie: rgba(8,58,42,.12);
    --gedaempft: rgba(8,58,42,.62); --moss-flaeche: {MOSS}; --paper-fest: {PAPER};
  }}
  @media (prefers-color-scheme: dark) {{
    :root {{ --bg: {INK}; --text: {PAPER}; --serie: {EMERALD_HELL};
      --panel: rgba(212,237,224,.06); --linie: rgba(212,237,224,.16); --gedaempft: rgba(250,250,247,.66);
      --moss-flaeche: rgba(212,237,224,.14); }}
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
  .befund-karte {{ background: var(--panel); border: 1px solid var(--linie); }}
  .bk-kopf {{ display: flex; align-items: baseline; gap: 14px; flex-wrap: wrap;
    padding: 16px 22px; border-bottom: 1px solid var(--linie); }}
  .bk-nr {{ font-family: ui-monospace, monospace; font-size: 12px; color: var(--signal); }}
  .bk-kopf h3 {{ font-size: 17px; margin: 0; font-weight: 600; flex: 1 1 260px; letter-spacing: -.005em; }}
  .bk-hebel {{ font-family: ui-monospace, monospace; font-size: 12px; color: var(--text);
    background: var(--moss-flaeche); padding: 5px 10px; white-space: nowrap; }}
  .bk-body {{ display: grid; grid-template-columns: 1fr 1fr; gap: 26px; padding: 20px 22px 22px; }}
  @media (max-width: 720px) {{ .bk-body {{ grid-template-columns: 1fr; gap: 14px; }} }}
  .bk-spalte p {{ margin: 0 0 12px; }}
  .bk-spalte ol {{ margin: 0 0 14px; padding-left: 20px; }}
  .bk-spalte li {{ margin-bottom: 6px; }}
  .mini-lbl {{ display: block; font-family: ui-monospace, monospace; font-size: 10px;
    letter-spacing: .12em; text-transform: uppercase; color: var(--gedaempft);
    margin: 0 0 4px !important; }}
  .unsichtbar, .beleg {{ font-size: 13.5px; color: var(--gedaempft); border-left: 2px solid var(--linie);
    padding-left: 12px; }}
  .bk-meta {{ margin: 0; font-size: 13.5px; }}
  .bk-meta dt {{ font-family: ui-monospace, monospace; font-size: 10px; letter-spacing: .1em;
    text-transform: uppercase; color: var(--gedaempft); margin-top: 10px; }}
  .bk-meta dt.gegen {{ color: var(--signal); }}
  .bk-meta dd {{ margin: 2px 0 0; }}
  .chart {{ width: 100%; height: auto; overflow: visible; margin-top: 6px; }}
  .chart .lbl {{ font-size: 13px; fill: var(--text); }}
  .chart .val {{ font-size: 12.5px; fill: var(--gedaempft); }}
  .chart .mini {{ font-size: 10px; fill: var(--signal); font-family: ui-monospace, monospace; }}
  .chart .mitte {{ text-anchor: middle; }}
  .chart .mark {{ transition: opacity .12s; }}
  .chart .mark:hover {{ opacity: .72; }}
  .tabelle-wrap {{ overflow-x: auto; margin-top: 8px; }}
  table {{ width: 100%; border-collapse: collapse; font-size: 14px; min-width: 760px; }}
  th, td {{ text-align: left; padding: 10px 18px 10px 0; border-bottom: 1px solid var(--linie);
    vertical-align: top; }}
  th:last-child, td:last-child {{ padding-right: 0; }}
  th {{ font-family: ui-monospace, monospace; font-size: 10.5px; letter-spacing: .1em;
    text-transform: uppercase; color: var(--gedaempft); font-weight: 400; }}
  td.zahl, th.zahl {{ text-align: right; white-space: nowrap; padding-left: 22px; }}
  td.neg {{ color: var(--signal); font-weight: 600; }}
  .fuss {{ margin-top: 56px; padding-top: 22px; border-top: 1px solid var(--linie);
    font-size: 13.5px; color: var(--gedaempft); }}
  .fuss ul {{ margin: 6px 0 18px; padding-left: 18px; }}
  .leer {{ color: var(--gedaempft); font-size: 14px; }}
  .befund-gruppe {{ margin-bottom: 42px; }}
  .metrik {{ padding: 0 0 20px; }}
  .metrik-titel {{ font-size: 15px; font-weight: 600; margin: 0 0 2px; }}
  .metrik-hint {{ font-size: 13.5px; color: var(--gedaempft); margin: 0 0 14px; max-width: 720px; }}
  .metrik .chart {{ max-width: 820px; }}
  .warnung {{ background: var(--moss-flaeche); border-left: 3px solid var(--signal);
    padding: 14px 18px; margin: 10px 0 18px; font-size: 14px; }}
  .chart .val-inv {{ font-size: 12.5px; fill: var(--paper-fest); font-weight: 600; }}
  .glossar {{ margin: 8px 0 0; display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 4px 28px; font-size: 14px; }}
  .glossar dt {{ font-weight: 600; margin-top: 12px; }}
  .glossar dd {{ margin: 2px 0 0; color: var(--gedaempft); }}
  .fuss ul.fehlend li {{ margin-bottom: 9px; }}
  code {{ font-family: ui-monospace, monospace; font-size: .92em; }}
</style></head>
<body>
<div class="wrap">
  <p class="eyebrow">Retouren-Analyse</p>
  <h1>{esc(titel)}<span class="punkt">.</span></h1>
  <p class="meta">{num(meta["retouren_positionen"])} Retouren-Positionen aus {num(meta["bestellungen"])} Bestellungen ·
     Datenstand {esc(meta["zeitraum_bis"])}</p>

  <div class="kacheln">{"".join(kacheln)}</div>

  <h2>Retourenquote je Bestellmonat</h2>
  <p class="hint">Jede Retoure zählt zu dem Monat, in dem bestellt wurde, nicht zu dem, in dem sie
     eintrifft. Nur so sind Monate vergleichbar. Bei den jüngsten Monaten fehlen noch Retouren; dort
     steht der dunkle Balken für das, was da ist, und die gestrichelte Linie für den erwarteten Endwert,
     hochgerechnet aus dem zeitlichen Verlauf der abgeschlossenen Monate.</p>
  {kohorten_chart(q["je_kohorte"])}

  <h2>Befunde und was zu tun ist</h2>
  <p class="hint">Nach Geldwert sortiert. Jeder Block enthält die Zahl, ihre Bedeutung und die
     Maßnahme, damit nichts an anderer Stelle nachgeschlagen werden muss.</p>
  {"".join(karten)}

  <h2>Retourengründe</h2>
  <p class="hint">Gezählt in <strong>Retourenpositionen</strong>, also je zurückgeschicktem Artikel.
     Eine Sendung mit drei Artikeln zählt hier dreimal.</p>
  {datenqualitaet}
  {chart_gruende}

  <h2>Artikel im Detail</h2>
  <p class="hint">Dieselben Zahlen als Tabelle, kopierbar und nachrechenbar. "Ertrag nach Retouren" ist
     der Rohertrag dieser Variante abzüglich aller Retourenkosten. Steht dort eine negative Zahl, kostet
     der Artikel im Zeitraum mehr, als er eingebracht hat.</p>
  <div class="tabelle-wrap"><table><thead><tr><th>Artikel</th><th>Variante</th><th class="zahl">Retouren</th>
    <th class="zahl">Umsatz</th><th class="zahl">Retourenkosten</th><th class="zahl">davon vom Umsatz</th>
    <th class="zahl">Ertrag nach Retouren</th></tr></thead><tbody>
    {"".join(f'<tr><td>{esc(c["name"])}</td><td><code>{esc(c["sku"])}</code></td>'
             f'<td class="zahl">{num(c["retouren_vorgaenge"])}</td>'
             f'<td class="zahl">{esc(eur(c.get("umsatz")))}</td>'
             f'<td class="zahl">{esc(eur(c["gesamt"]))}</td>'
             f'<td class="zahl">{esc(pct(c.get("kosten_anteil_am_umsatz")))}</td>'
             f'<td class="zahl{" neg" if (c.get("deckungsbeitrag_nach_retouren") or 0) < 0 else ""}">'
             f'{esc(eur(c["deckungsbeitrag_nach_retouren"]) if c.get("deckungsbeitrag_nach_retouren") is not None else "n/a")}</td></tr>'
             for c in kosten)}
  </tbody></table></div>

  <h2>Begriffe</h2>
  <p class="hint">Damit die Zahlen oben eindeutig sind.</p>
  <dl class="glossar">
    <dt>Retouren nach Menge</dt>
    <dd>Zurückgeschickte Artikel geteilt durch verschickte Artikel. Die gängigste Sicht, gut für die
        Frage "wie viel Ware kommt zurück".</dd>
    <dt>Retouren nach Wert</dt>
    <dd>Erstatteter Betrag geteilt durch verschickten Warenwert. Liegt diese Zahl über der Mengensicht,
        kommen überdurchschnittlich teure Artikel zurück.</dd>
    <dt>Bestellungen mit Retoure</dt>
    <dd>Anteil der Bestellungen, aus denen mindestens ein Artikel zurückkam. Die Sicht auf den Prozess:
        wie oft läuft eine Bestellung nicht glatt durch.</dd>
    <dt>Bestellmonat statt Retourenmonat</dt>
    <dd>Jede Retoure wird der Bestellung zugerechnet, aus der sie stammt, nicht dem Monat, in dem sie
        eintrifft. Nur so vergleicht man Gleiches mit Gleichem. Der Preis dafür: Die jüngsten Monate
        sind noch unvollständig und werden hier gekennzeichnet.</dd>
    <dt>Ertrag nach Retouren</dt>
    <dd>Was von einer Artikelvariante übrig bleibt, wenn man vom Rohertrag alle Retourenkosten abzieht.
        Negativ heißt: Der Artikel hat im Zeitraum Geld gekostet.</dd>
    <dt>Position gegen Sendung</dt>
    <dd>Eine Retourenposition ist ein zurückgeschickter Artikel, eine Sendung ist das Paket dazu.
        Kommt ein Paket mit drei Artikeln zurück, sind das drei Positionen und eine Sendung. Die
        Gründe-Auswertung zählt Positionen, die nicht abgeholten Fälle zählen Sendungen.</dd>
    <dt>Retourenkosten</dt>
    <dd>Erstatteter Betrag plus Bearbeitungskosten je Vorgang plus Wertverlust bei defekter Ware.
        Der Bearbeitungssatz ist eine Annahme und unten aufgeführt.</dd>
  </dl>

  <div class="fuss">
    <strong>Annahmen</strong><ul>{annahmen}</ul>
    <strong>Was mit weiteren Spalten im Export möglich wäre</strong><ul class="fehlend">{fehlend}</ul>
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
