# Retouren-Report Demo-Brand

Datenstand 05.07.2026, Bestellungen Januar bis Juni 2026. Basis: 1.308 Retouren-Positionen aus 5.200 Bestellungen und 8.214 versendeten Artikeln. Ergebnis eines kompletten Skill-Durchlaufs auf dem synthetischen Demo-Datensatz.

## Verdict

Zwei Artikel kosten euch im Halbjahr rund 30.200 Euro, und keiner von beiden steht in einer Auffälligkeitsliste. Der Zip-Hoodie Heavy hat Quoten im Rahmen und kostet über sein Volumen 17.995 Euro, der Hoodie Classic 12.238 Euro. Beim Hoodie ist die Ursache dagegen eindeutig und billig zu beheben: Er fällt zu klein aus, 114 mal "zu klein" gegen 6 mal "zu groß". Dazu kommen 94 Sendungen, die nie abgeholt wurden, mit 7.403 Euro Schaden.

## Kennzahlen

Zwei Zahlenpaare, weil zwei verschiedene Dinge zurückkommen. Die Retourenquote zählt Kundenretouren, die Nichtabholquote die Sendungen, die nie ausgepackt wurden. Rechtlich ist das kein Widerruf, kostet aber Geld und steht deshalb in der Kostenrechnung.

| Kennzahl | Wert | Basis |
|---|---|---|
| Retourenquote nach Menge | 14,1 % | 1.159 von 8.214 Artikeln |
| Retourenquote nach Wert | 15,8 % | 83.029 von 524.829 EUR |
| Bestellungen mit Retoure | 20,6 % | 1.069 von 5.200 Bestellungen |
| Nichtabholquote | 1,8 % | 149 Artikel in 94 Sendungen |
| Alle Rückläufer zusammen | 15,9 % nach Menge, 17,7 % nach Wert | Bezug der Kostenrechnung |

Je Bestell-Kohorte, damit die Monate vergleichbar sind:

| Bestellmonat | nach Menge | nach Wert | nach Bestellungen | Status |
|---|---|---|---|---|
| Januar | 14,9 % | 16,6 % | 22,5 % | reif |
| Februar | 15,3 % | 17,5 % | 22,1 % | reif |
| März | 17,2 % | 20,1 % | 24,2 % | reif |
| April | 15,8 % | 17,1 % | 22,7 % | **noch nicht reif** |
| Mai | 14,3 % | 15,6 % | 20,6 % | **noch nicht reif**, hochgerechnet 16,2 % |
| Juni | 7,4 % | 8,5 % | 11,3 % | **noch nicht reif**, hochgerechnet 12,7 % |

Die drei jüngsten Monate sind unvollständig, ihre Zahlen sind vorläufig.

### Vom Umsatz zum Rohertrag nach Retouren

| Zeile | EUR |
|---|---|
| Umsatz der versendeten Ware | 524.829 |
| minus erstatteter Umsatz | −92.854 |
| Nettoumsatz | 431.974 |
| minus Wareneinsatz der behaltenen Ware | −156.997 |
| Rohertrag der behaltenen Ware | 274.977 |
| minus Retourenbearbeitung | −13.080 |
| minus abgeschriebene Defektware | −1.952 |
| **Rohertrag nach Retouren** | **259.945** |

Retourenkosten gesamt 70.793 Euro: 55.761 Euro entgangene Marge, 13.080 Euro Bearbeitung, 1.952 Euro Abschreibung. Der erstattete Umsatz zählt nicht als Kosten, die Ware liegt wieder im Lager.

## Findings

1. **Hoodie Classic fällt zu klein aus** `belegt` · 114 mal "zu klein" gegen 6 mal "zu groß", durchgehend über alle Größen von XS bis XL. Kein Streuungsmuster, sondern ein Schnittfehler des Artikels.
2. **Zip-Hoodie Heavy ist der teuerste Artikel im Sortiment** `belegt` · 17.995 Euro Retourenkosten aus 246 Vorgängen, bei Quoten zwischen 11,9 und 16,9 Prozent. Nicht die Quote ist das Problem, sondern das Volumen.
3. **94 Sendungen wurden nie abgeholt** `belegt` · 1,8 Prozent aller Bestellungen, 8,1 Prozent aller Retourenvorgänge. 6.463 Euro entgangene Marge plus 940 Euro Zusatzkosten.
4. **Chargen-Verdacht bei den Socken** `belegt` · 33 Defekt-Retouren im April, sonst rund eine pro Monat. `Hypothese` schlechte Charge. `fehlende Daten` mit einer Chargennummer wäre es beweisbar.
5. **Sommerkleid Print XS-Oliv passt nicht zum Foto** `belegt` · 41,5 Prozent Retourenquote (17 von 41), Hauptgründe "nicht wie beschrieben" und Farbe.
6. **Mehrgrößen-Bestellungen kommen anderthalbmal so oft zurück** `belegt` · 599 Bestellungen mit zwei Größen desselben Artikels, davon 32,7 Prozent mit Retoure gegen 20,6 Prozent im Schnitt.
7. **Eine Kundin mit 33 Retourenpositionen** `belegt` · K-10442, 19 Bestellungen, 18 davon mit Retoure. Prüffall für einen Menschen, keine Sanktion.

## Was sonst untergegangen wäre

**Die Retourenquote sieht aus, als würde sie sinken. Tut sie nicht.**
Die abgeschlossenen Bestellmonate liegen im Schnitt bei 15,8 Prozent, der Juni zeigt 7,4. Die 8,4 Punkte Differenz sind fehlende Reife, nicht Erfolg. Hochgerechnet landet der Juni bei 12,7 Prozent.
*Warum das im Standard-Report unsichtbar ist:* Wer Retouren eines Monats durch die Verkäufe desselben Monats teilt, misst junge Bestellungen mit, deren Rückgabefrist noch läuft.

**Der teuerste Artikel steht in keiner Auffälligkeitsliste.**
Der Zip-Hoodie Heavy hat Quoten zwischen 11,9 und 16,9 Prozent, also im Rahmen. Über zehn Varianten kostet er trotzdem 17.995 Euro, die teuerste einzelne Variante 2.760 Euro.
*Warum das unsichtbar ist:* Reports ranken nach Quote. Ein Bestseller mit normaler Quote taucht dort nie auf und kostet mehr als jeder Ausreißer.

**Ein Merkmal, das erst in der Kreuzung auffällt.**
Rechnungskauf macht 29,0 Prozent des Geschäfts aus, aber 70,2 Prozent der nicht abgeholten Sendungen (66 von 94). Die Retourenquote nach Zahlart liegt dagegen bei unauffälligen 24,6 Prozent.
*Warum das unsichtbar ist:* In der Gesamtsicht liegen alle Zahlarten dicht beieinander. Erst der Blick allein auf die nicht abgeholten Sendungen kippt das Bild.

**11,5 Prozent der Retouren haben keinen brauchbaren Grund.**
150 Fälle ohne verwertbare Angabe, die Häufung liegt bei der Regenjacke Tech.
*Warum das unsichtbar ist:* Leere und Sonstiges-Gründe landen als Restposten im Report. Dahinter steckt oft ein eigener Fall oder ein Prozessfehler.

**Ein Artikel, dessen Marge die Retouren nicht trägt.**
Regenjacke Tech, Variante L-Weiss: 2.944 Euro Deckungsbeitrag vor Retouren, 1.529 Euro danach. 14,4 Prozent des Variantenumsatzes gehen für Retouren drauf, der höchste Wert im Sortiment.
*Warum das unsichtbar ist:* Retourenkosten stehen nicht am Artikel. In der Sortimentsauswertung sieht er gesund aus.

## Maßnahmen

### 1. Zip-Hoodie Heavy: die Ursache hinter dem Volumen finden
**Was passiert:** 246 Retourenvorgänge über zehn Varianten, Quoten zwischen 11,9 und 16,9 Prozent. Keine Variante ist auffällig, die Summe ist der teuerste Posten im Sortiment.
**Warum es zählt:** Der Artikel steht in keiner Quoten-Rangliste und kostet trotzdem mehr als jeder Ausreißer. Schon ein Punkt weniger Quote ist hier mehr wert als eine halbierte Quote bei einem Kleinvolumen-Artikel.
**Größe des Hebels:** 17.995 Euro Retourenkosten im Halbjahr.
**Was zu tun ist:**
1. Retourengründe der zehn Varianten nebeneinander legen und prüfen, ob ein Grund dominiert oder sich alles gleichmäßig verteilt.
2. Dominiert ein Grund, ist die Maßnahme die des jeweiligen Musters (Größe, Foto, Qualität).
3. Verteilt es sich gleichmäßig, ist es eine Preis- und Margenfrage: bei diesem Volumen entscheidet die Rohmarge, ob eine normale Quote tragbar ist.
**Aufwand:** M für die Analyse, danach abhängig vom Befund.
**Wer:** Shop und Content, bei der Margenfrage der Einkauf.
**Woran du merkst, dass es wirkt:** Retourenkosten je Artikel, nächste vollständige Bestellkohorte.
**Was dabei nicht kaputtgehen darf:** Der Absatz. Der Artikel ist ein Bestseller, eine abschreckende Änderung kostet mehr, als sie spart.

### 2. Größenhinweis für den Hoodie Classic
**Was passiert:** 114 Retouren mit "zu klein" gegen 6 mit "zu groß", gleichmäßig über alle Größen. Der Artikel kostet 12.238 Euro im Halbjahr.
**Warum es zählt:** Das ist die am besten belegte Maßnahme im Retourenmanagement und die einzige, deren Wirkung sauber gemessen ist.
**Größe des Hebels:** 120 größenbedingte Retouren im Halbjahr. Zur Einordnung: In Zalandos A/B-Test senkte ein solcher Hinweis die größenbedingten Retouren um 4,3 bis 6,6 Prozent. Das ist ein Fremd-Benchmark aus anderem Kontext, keine Prognose.
**Was zu tun ist:**
1. Hinweis "fällt klein aus, wir empfehlen eine Größe größer" direkt an die Größenauswahl, nicht in die Größentabelle.
2. Maße des Artikels nachmessen und gegen die eigene Größentabelle halten.
3. Bei durchgehender Abweichung die Gradierung mit dem Lieferanten klären.
**Aufwand:** S für Schritt 1 und 2, L für Schritt 3.
**Wer:** Shop und Content, für Schritt 3 der Einkauf.
**Woran du merkst, dass es wirkt:** Anteil "zu klein" an den Retouren dieses Artikels, frühestens vier bis sechs Wochen nach der Änderung.
**Was dabei nicht kaputtgehen darf:** Die Zahl der Mehrgrößen-Bestellungen. Im selben Zalando-Test stiegen sie durch den Hinweis um 11,1 Prozent. Steigt das stärker als die Quote fällt, ist die Maßnahme unterm Strich negativ.

### 3. Nicht abgeholte Sendungen reduzieren
**Was passiert:** 94 Sendungen kamen ungeöffnet zurück. Rechnungskauf ist dabei mit 70,2 Prozent stark überrepräsentiert, im Gesamtgeschäft sind es 29,0 Prozent.
**Warum es zählt:** Doppelter Versand, volle Erstattung, kein Gegenwert. Der Fall taucht in keiner Versandstatistik als Problem auf, weil der Carrier ihn als zugestellt führt.
**Größe des Hebels:** 7.403 Euro (6.463 Euro entgangene Marge plus 940 Euro Zusatzkosten).
**Was zu tun ist:**
1. Abhol-Erinnerung auslösen, sobald der Carrier "im Paketshop hinterlegt" meldet. Die Frist beträgt bei DHL sieben Tage, bei Hermes bis zu zehn.
2. Adressprüfung im Checkout aktivieren.
3. Zustelloptionen anbieten (Wunschort, Paketshop-Wahl, Wunschtag).
4. Beim Rechnungskauf im Einzelfall Risiko steuern, aber die Zahlart nicht abschalten. Sie zieht das Verhalten an, sie erzeugt es nicht.
**Aufwand:** M für 1 und 3, S bis M für 2.
**Wer:** Logistik, für die Adressprüfung der Shop.
**Woran du merkst, dass es wirkt:** Anzahl nicht abgeholter Sendungen pro Monat und ihr Anteil an allen Sendungen.
**Was dabei nicht kaputtgehen darf:** Conversion im Checkout und der Umsatzanteil des Rechnungskaufs.

### 4. Socken-Charge prüfen
**Was passiert:** 33 Defekt-Retouren im April, sonst rund eine pro Monat.
**Warum es zählt:** Wenn die Charge noch im Lager liegt, produziert sie weiter Retouren und Ärger.
**Größe des Hebels:** 32 vermeidbare Retouren, sofern der Verdacht stimmt.
**Was zu tun ist:**
1. Restbestand prüfen und bei Bestätigung sperren.
2. Wareneingang des Zeitraums der Charge zuordnen.
3. Beim Lieferanten reklamieren, mit den Retourengründen als Beleg.
**Aufwand:** S bis M.
**Wer:** Einkauf und Logistik.
**Woran du merkst, dass es wirkt:** Defekt-Retouren dieses Artikels pro Monat, zurück auf das Niveau vor dem Ausschlag.
**Was dabei nicht kaputtgehen darf:** Lieferfähigkeit. Eine gesperrte Charge ohne Nachschub ist ein Umsatzloch.

### 5. Retourengründe vollständig erfassen
**Was passiert:** Bei 150 Retouren (11,5 Prozent) steht kein verwertbarer Grund. Auffällig ist die Häufung bei der Regenjacke Tech, dem Artikel mit dem höchsten Kostenanteil am Umsatz.
**Warum es zählt:** Jede fehlende Angabe ist eine Analyse, die nicht stattfinden kann.
**Größe des Hebels:** nicht bezifferbar, aber Voraussetzung für alles Weitere.
**Was zu tun ist:**
1. Prüfen, an welcher Stelle der Grund verloren geht (Retourenportal, Wareneingang, manuelle Erfassung).
2. Pflichtfeld mit wenigen, klaren Auswahlmöglichkeiten statt Freitext.
3. Freitext zusätzlich anbieten, aber nicht als einzige Option.
**Aufwand:** M, hängt am System.
**Wer:** Logistik und Kundenservice.
**Woran du merkst, dass es wirkt:** Anteil der Retouren ohne Grund, Ziel unter 5 Prozent.
**Was dabei nicht kaputtgehen darf:** Die Bearbeitungszeit im Wareneingang.

## Was auffällig aussieht, aber in Ordnung ist

- **Die Kanäle unterscheiden sich nicht.** Eigener Shop 22,1 Prozent, Amazon 23,4, Zalando 21,3. Die Marktplatz-Listings scheinen zum Shop zu passen.
- **Die Zahlarten liegen in der Gesamtsicht dicht beieinander.** Vorkasse 20,6 Prozent, PayPal 21,0, Kreditkarte 22,7, Rechnungskauf 24,6. Der Rechnungskauf ist nur bei den nicht abgeholten Sendungen auffällig, nicht bei Retouren allgemein.
- **14 Artikel wurden bewusst nicht bewertet**, weil ihre Verkaufsbasis unter dem Mindest-N liegt. Eine Quote aus drei Verkäufen ist Zufall, keine Information.
- **Die Gesamtquote ist für ein Fashion-Sortiment unauffällig.** 14,1 Prozent nach Menge liegt deutlich unter dem, was für die Branche typisch ist.
- **Der Preisvergleich ist erklärbar.** Retournierte Artikel sind im Schnitt 11 Prozent teurer als versendete (70,99 gegen 63,89 Euro). Das passt zum Sortiment, teurere Artikel kommen häufiger zurück, und ist kein eigenes Muster.

## Offene Fragen

1. War der April-Ausschlag bei den Socken wirklich eine Charge, oder gab es in dem Zeitraum eine Kampagne oder einen Verpackungswechsel?
2. Ist die dünne Marge der Regenjacke so gewollt (Einstiegsartikel, Wettbewerbsdruck) oder ein Kalkulationsfehler?
3. Warum fehlt gerade bei der Regenjacke besonders oft der Retourengrund? Anderer Rückgabeweg, anderes Lager?
4. Ist K-10442 eine Privatkundin, oder steckt dort ein Wiederverkäufer oder ein Testkonto dahinter?
5. Ist beim Zip-Hoodie die Quote strukturell oder saisonal? Dafür brauchen wir eine zweite Periode zum Vergleich.

## Annahmen und fehlende Daten

**Annahmen:** 10,00 Euro Prozesskosten je Retouren-Vorgang (EHI-Kernbereich 5 bis 20 Euro, anpassbar), 60 Tage Rückgabefrist, 21 Tage Reifepuffer, mindestens 3 Retouren bevor ein Artikel bewertet wird. Retourenkosten sind die entgangene Marge der zurückgeschickten Stücke plus Prozesskosten plus abgeschriebene Defektware; der erstattete Umsatz zählt nicht als Kosten, weil die Ware wieder ins Lager geht.

**Was mit weiteren Spalten möglich wäre:**

| Fehlende Spalte | Was damit ginge |
|---|---|
| `delivered_date` | Zeit zwischen Zustellung und Rücksendung, damit das Wardrobing-Fenster |
| `batch` | Chargen eindeutig zuordnen statt zeitlich schätzen |
| `refund_type` | Umtausch gegen Erstattung unterscheiden |
| `condition` | Wertverlust echt rechnen statt über die Defekt-Meldung schätzen |
