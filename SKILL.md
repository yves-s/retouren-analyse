---
name: retouren-analyse
description: Erkennt Muster in E-Commerce-Retourendaten (CSV-Export aus ERP- oder Shop-System) und leitet priorisierte Maßnahmen ab. Nutzen bei "Retouren analysieren", "Retourenquote", "warum kommen Produkte zurück", "Retouren-Report", oder wenn ein Retouren-/Returns-Export als CSV vorliegt. Arbeitet system-agnostisch (Xentral, Shopify, WooCommerce, generisch), braucht keine API und keine sensiblen Live-Zugänge.
---

# Retouren-Analyse

Du analysierst Retourendaten eines E-Commerce-Shops und findest die Muster, die in Dashboards unsichtbar bleiben: Größen-Läufer, Chargen-Probleme, Serien-Retournierer, nicht abgeholte Sendungen, Kosten-Fresser. Das Prinzip: **das Script rechnet, du interpretierst.** Du rechnest niemals selbst Quoten oder Summen im Kopf; jede Zahl im Report stammt aus `analysis.json`.

## Ablauf

### Phase 1: Mapping (immer zuerst)

1. Lies die Kopfzeilen der gelieferten CSV-Dateien (Retouren-Positionen plus Verkaufs-Positionen). Ohne Verkaufsbasis keine Quoten: dann nur Struktur-Analyse fahren und das prominent sagen.
2. Mappe die Spalten auf das kanonische Schema (siehe `reference/schema.md`). Frag bei Mehrdeutigkeit nach, rate nicht.
3. Kläre drei Dinge, bevor du rechnest (beim Demo-Datensatz entfällt das):
   - Sind die Retourengründe kundengewählt, servicegewählt oder Freitext?
   - Wie lang ist das Rückgabefenster (Policy)?
   - Deckt der Verkaufs-Export den Retouren-Zeitraum plus Rückgabefenster nach vorn ab?
4. Benenne fehlende optionale Spalten und liste explizit, welche Analysen dadurch entfallen.

### Phase 2: Rechnen

Führe das Analyse-Script aus:

```bash
python3 scripts/retouren_analyse.py --retouren <retouren.csv> --verkaeufe <verkaeufe.csv> --out analysis.json
```

Relevante Parameter (Defaults sind markierte Annahmen): `--prozesskosten` (EUR je Retoure, Default 10.00, EHI-Kernbereich 5 bis 20), `--rueckgabefenster` (Tage, Default 60), `--min-retouren` (Mindest-N je SKU, Default 3), `--reifepuffer` (Tage, Default 21).

### Phase 3: Dashboard erzeugen

```bash
python3 scripts/dashboard.py --analyse analysis.json --out dashboard.html --titel "<Shop> · <Zeitraum>"
```

Erzeugt eine eigenständige HTML-Datei ohne externe Abhängigkeiten (Kennzahlen, blinde Flecken, Kohorten-Chart, Kosten je Artikel, Retourengründe, Zahlart-Kontrast, Größen-Verteilung, dazu alle Zahlen als Tabelle). Öffnet sich im Browser, hat einen Dunkelmodus und lässt sich weiterreichen. Sag dem Nutzer den Dateipfad.

### Phase 4: Interpretieren und berichten

Der Report ist die Erzählung zum Dashboard. Schreib ihn aus `analysis.json` in dieser Struktur:

1. **Verdict:** zwei, drei Sätze. Das teuerste Muster zuerst, in Euro.
2. **Kennzahlen:** Beta-, Gamma- und Bestellquote je Bestell-Kohorte. Unreife Kohorten (Flag `mature: false`) immer als vorläufig kennzeichnen.
3. **Muster-Findings:** je Finding eine Zeile Kern-Aussage, dann Beleg. Jedes Finding trägt ein Evidenz-Tag:
   - `export`: direkt aus den Daten belegt (Zahl aus analysis.json)
   - `hypothesis`: plausible Deutung, aus den Daten allein nicht beweisbar
   - `needs_data`: erst mit zusätzlicher Spalte oder Quelle prüfbar
4. **Was sonst untergegangen wäre:** der Abschnitt `blinde_flecken` aus der Analyse. Das sind Befunde, die ein normaler Retouren-Report strukturell nicht zeigt, etwa ein Scheintrend durch unreife Kohorten, ein Merkmal das erst in der Kreuzung auffällt, oder ein Artikel der brutto verdient und nach Retouren nichts übrig lässt. Je Befund immer beides sagen: was da ist, und warum es im Standard-Report unsichtbar bleibt. Dieser Abschnitt ist der eigentliche Grund, warum jemand die Analyse fährt; schreib ihn nicht als Fußnote.
5. **Maßnahmen:** je bestätigtem Muster eine Maßnahme im Format aus `reference/massnahmen.md`. Pflichtfelder je Maßnahme: Was passiert, Warum es zählt, Größe des Hebels in Euro, Was zu tun ist (nummerierte Schritte), Aufwand, Wer, Woran du merkst dass es wirkt, Was dabei nicht kaputtgehen darf. Reihenfolge nach Geld und Aufwand: teuer und schnell zuerst.
6. **Was auffällig aussieht, aber in Ordnung ist:** Pflichtabschnitt. Nenne mindestens zwei Dinge, die du geprüft und für unbedenklich befunden hast, mit der Zahl dazu (etwa Kanäle oder Zahlarten, die dicht beieinander liegen). Bleibt der Abschnitt leer, hast du nicht genau genug hingeschaut. Er verhindert, dass jede Zahl zum Problem erklärt wird.
7. **Offene Fragen:** was du aus den Daten allein nicht entscheiden kannst und der Mensch beantworten muss (etwa ob ein Ausschlag eine Charge war oder eine Kampagne). Fragen stellen statt behaupten.
8. **Annahmen und fehlende Daten:** alle Default-Annahmen (Prozesskostensatz usw.) und alles, was mit weiteren Spalten möglich würde.

## Guardrails (hart)

- Nie eine SKU-Quote ranken oder anprangern, deren Verkaufsbasis unter dem Mindest-N liegt.
- Kohorten-Quoten nie mit Perioden-Quoten mischen; unreife Kohorten nie als Trend verkaufen.
- Serien-Retournierer und Wardrobing sind eine Review-Liste für Menschen, nie eine automatische Sanktion und nie eine Beschuldigung.
- Eine strengere Retouren-Policy ist niemals die Default-Empfehlung.
- Keine Konversions- oder Ersparnis-Versprechen ("spart X Prozent"). Impact immer als "bis zu, wenn Muster abgestellt" mit der Zahl aus den Daten.
- Jede Zahl im Report muss in analysis.json stehen. Fehlt sie dort, gehört sie nicht in den Report.
- Eine Ursache ergibt eine Maßnahme. Sechs auffällige Varianten desselben Artikels sind ein Größenproblem, nicht sechs Aufgaben.
- Jede Maßnahme bekommt eine Gegen-Kennzahl. Fast jeder Retouren-Hebel kann Conversion oder Umsatz kosten.
- Eine benannte Lücke ist eine vollständige Antwort. Nie eine Zahl schätzen, damit der Report rund wirkt.

## Demo

`demo/generate_demo_data.py` erzeugt einen synthetischen Datensatz im Stil eines ERP-Berichte-Exports (Spalten wie bei Xentral üblich, funktioniert aber generisch) mit eingebauten Mustern. Für die Live-Demo: Daten generieren, Script laufen lassen, Report schreiben.
