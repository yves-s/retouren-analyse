# Retouren-Report Demo-Brand · Januar bis Juni 2026

Beispiel-Output des Skills auf dem synthetischen Demo-Datensatz (1.420 Retouren-Positionen, 5.200 Bestellungen). So sieht Phase 3 aus, wenn das Script gerechnet hat.

## Verdict

Drei Muster kosten euch richtig Geld. Der Hoodie Classic fällt klein aus und produziert allein über 10.500 EUR Retourenkosten im Halbjahr. 100 Sendungen wurden nie abgeholt (8.100 EUR verlorener Umsatz plus rund 1.000 EUR Prozesskosten), davon drei Viertel Rechnungskauf. Und im April kam eine Socken-Charge mit 37 Defekt-Retouren zurück, die vorher bei rund einer pro Monat lag: Das war eine schlechte Charge, kein Zufall.

## Kennzahlen

| Kohorte (Bestellmonat) | Beta-Quote | Bestellquote | Status |
|---|---|---|---|
| 2026-01 | 19,2 % | 25,6 % | reif |
| 2026-02 | 18,2 % | 25,7 % | reif |
| 2026-03 | 17,0 % | 25,0 % | reif |
| 2026-04 | 19,2 % | 25,3 % | reif |
| 2026-05 | 16,4 % | 22,9 % | **unreif, vorläufig** |
| 2026-06 | 14,3 % | 20,1 % | **unreif, vorläufig** |

Gesamt: Beta 17,4 %, Gamma 19,4 %, Bestellquote 24,1 %. Die scheinbar sinkenden Quoten im Mai und Juni sind kein Trend, sondern unreife Kohorten (Rückgabefenster läuft noch). Genau dieser Fehler steht in den meisten Dashboards.

## Muster-Findings

1. **Größen-Läufer Hoodie Classic** `export`: 203 mal "zu klein" gegen 12 mal "zu groß", konsistent über alle Größen (XS bis XL). Der Artikel fällt klein aus; sechs seiner Varianten stehen in den Kosten-Top-10 (zusammen über 10.500 EUR).
2. **Nicht abgeholte Sendungen** `export`: 100 Sendungen (1,9 % aller Bestellungen), 8.100 EUR verlorener Umsatz. Zahlart-Verteilung der Nicht-Abholer: 75 Prozent Rechnungskauf gegen 30 Prozent Rechnungskauf-Anteil im Gesamtgeschäft. Dieses Muster ist in Carrier-Statistiken unsichtbar (läuft dort als zugestellt).
3. **Chargen-Verdacht Sneaker Socken** `export`: 37 Defekt-Retouren im April gegen Basis rund 1 pro Monat. `hypothesis`: eine fehlerhafte Charge aus dem März-Wareneingang; mit einer Chargen-Spalte im Export wäre das exakt zuordenbar (`needs_data`).
4. **Foto-Mismatch Sommerkleid Print** `export`: "entspricht nicht dem Foto" und Farb-Gründe konzentrieren sich auf diesen Style; vier Varianten in den Kosten-Top-10.
5. **Serien-Retournierung** `export`: Kundin K-10442 mit 23 Bestellungen, 22 davon mit Retoure (61 Positionen, meist Mehrgrößen-Bestellungen). Review-Fall, keine automatische Maßnahme.
6. **Bracketing** `export`: 565 Mehrgrößen-Bestellungen, davon 37,7 % mit Retoure (Basis: 24,1 %).
7. **Kanäle unauffällig** `export`: 23,6 bis 25,4 % Bestellquote je Kanal, kein Handlungsbedarf.

## Maßnahmen (nach Euro-Impact)

1. Hoodie Classic: PDP-Hinweis "fällt klein aus", Größentabelle korrigieren, mittelfristig Gradierung mit dem Lieferanten prüfen. Owner: Shop, Einkauf.
2. Nicht-Abholer: proaktive Abhol-Erinnerung bei Status "hinterlegt", Adressvalidierung im Checkout, Zahlart-Risiko-Scoring bei Häufung (Conversion-Effekt gegenrechnen). Owner: Logistik, Finance.
3. Socken-Charge: Rest-Charge im Lager prüfen und sperren, Lieferanten-Reklamation. Owner: Einkauf.
4. Sommerkleid: Produktfotos auf Farbtreue prüfen, Beschreibung schärfen. Owner: Shop.
5. K-10442: menschlicher Review, differenzierte Kulanz. Owner: CS.

## Annahmen und fehlende Daten

- Prozesskostensatz 10,00 EUR je Retoure (EHI-Kernbereich 5 bis 20, kalibrierbar), Rückgabefenster 60 Tage, Reifepuffer 21 Tage, Mindest-N 3 (12 SKUs unter der Schwelle, nicht gerankt).
- Mit `delivered_date` käme die Wardrobing-Analyse dazu, mit `batch` die exakte Chargen-Zuordnung, mit `refund_type` die Revenue-Recovery-Rate, mit `condition` der reale Wertverlust statt der Annahme.
