# Maßnahmen: von Findings zu Handlungen

Diese Datei liefert das Format und die fachliche Substanz für den Maßnahmen-Teil des Reports. Grundlage: RESOLVE-Projekt (BMUV-gefördert, feldgetestet mit OTTO), Uni-Bamberg-Retourenforschung, EHI, bevh-Retourenkompendium.

## Das Format je Maßnahme

Immer diese Felder, immer in dieser Reihenfolge. Ein Report ohne Maßnahmen ist nur ein Bericht.

```
### [Kurzer Name der Maßnahme]
**Was passiert:** zwei bis drei Sätze, was in den Daten steht.
**Warum es zählt:** was das fürs Geschäft bedeutet, nicht nur für die Quote.
**Größe des Hebels:** die Zahl aus der Analyse, in Euro. Nie geschätzt, nie hochgerechnet.
**Was zu tun ist:** nummerierte Schritte, konkret genug zum Weiterreichen.
**Aufwand:** S (Stunden), M (Tage), L (Wochen), plus Abhängigkeiten.
**Wer:** Shop, Content, Einkauf, Logistik, Finance, Kundenservice.
**Woran du merkst, dass es wirkt:** eine Kennzahl plus Zeitfenster, in dem sie sich zeigen muss.
**Was dabei nicht kaputtgehen darf:** die Gegen-Kennzahl.
```

## Regeln für den Maßnahmen-Teil

- **Eine Ursache, eine Maßnahme.** Wenn sechs Varianten desselben Artikels auffallen, ist das ein Größenproblem des Artikels, nicht sechs Aufgaben. Cluster bilden, nicht Zeilen zählen.
- **Reihenfolge nach Geld und Aufwand.** Was viel kostet und schnell zu ändern ist, kommt zuerst. Was viel kostet, aber ein Projekt ist, kommt danach mit ehrlicher Zeitangabe.
- **Nie eine Ersparnis versprechen.** "Bis zu X Euro, wenn das Muster verschwindet" ist zulässig, "spart X Euro" nicht.
- **Strengere Rückgabebedingungen sind niemals die Standardempfehlung.** Sie senken die Quote und den Umsatz gleich mit.
- **Lücke benennen statt schätzen.** Fehlt eine Spalte, wird gesagt, was damit möglich wäre. Eine erfundene Zahl ist schlimmer als eine fehlende.
- **Immer eine Gegen-Kennzahl mitgeben.** Fast jede Retouren-Maßnahme kann die Conversion kosten. Wer das nicht mitmisst, optimiert sich in den Umsatzverlust.
- **Höchstens fünf Maßnahmen.** Alles darunter kommt in einen Block "Beobachten". Eine Liste mit zwanzig Empfehlungen wird nicht umgesetzt.
- **Effekt-Schätzungen nur mit sichtbarer Rechnung und markierter Herkunft.** Wenn ein Fremd-Benchmark als Faktor einfließt, muss dabeistehen, aus welchem Kontext er stammt und dass er keine Prognose für diesen Shop ist. Ohne Beleg lieber nur die Kostenzahl aus den eigenen Daten nennen.

## Die Maßnahmen je Muster

### Größen-Läufer (Artikel fällt zu klein oder zu groß aus)
**Was zu tun ist:**
1. Hinweis direkt an der Größenauswahl der Produktseite, nicht in der Größentabelle versteckt ("fällt klein aus, wir empfehlen eine Größe größer").
2. Maße des Artikels gegen die eigene Größentabelle prüfen. Weicht der Artikel ab, ist die Tabelle das Problem, nicht der Kunde.
3. Bei durchgehender Abweichung über alle Größen: Gradierung mit dem Lieferanten klären, das ist ein Produktionsthema.
4. Erst danach über Größenberater oder Fit-Finder nachdenken. Werkzeug ohne saubere Maße verschiebt das Problem nur.

**Aufwand:** Schritt 1 ist S, Schritt 2 ist M, Schritt 3 ist L mit Lieferanten-Abhängigkeit.
**Wer:** Shop und Content für 1 und 2, Einkauf für 3.
**Woran du merkst, dass es wirkt:** Anteil "zu klein" an den Retouren dieses Artikels, sichtbar in den Bestellungen der nächsten vier bis sechs Wochen (nicht früher, die Retouren laufen nach).
**Was nicht kaputtgehen darf:** Absatz des Artikels. Ein Hinweis, der abschreckt, senkt die Quote und den Umsatz.
**Beleg:** Passform ist laut Uni-Bamberg-Retourenforschung der häufigste Retourengrund bei Bekleidung. Laut RESOLVE haben 82 Prozent der untersuchten Händler eine Größenberatung, aber nur 43 Prozent einen artikelbezogenen Hinweis der Art "fällt größer aus". Genau dort liegt der ungenutzte Hebel. Gemessene Effektstärken siehe unten.

### Nicht abgeholte Sendungen
**Was zu tun ist:**
1. Erinnerung auslösen, sobald der Carrier "im Paketshop hinterlegt" meldet. Die Abholfristen liegen typischerweise bei sieben bis vierzehn Tagen, danach geht das Paket automatisch zurück.
2. Adressqualität im Checkout prüfen (Validierung, Vorschläge, Tippfehler-Erkennung).
3. Zustelloptionen anbieten: Wunschort, Paketshop-Wahl, Wunschtag.
4. Wenn eine Zahlart auffällig überrepräsentiert ist, das Risiko dort gezielt steuern, nicht die Zahlart abschalten.
5. Rechtlich einordnen: Eine Annahmeverweigerung ist kein Widerruf. Der Mehraufwand ist grundsätzlich geltend zu machen, praktisch bleibt der Händler meist darauf sitzen. Deshalb ist Vermeidung der einzige verlässliche Hebel.

**Aufwand:** 1 und 3 sind M, 2 ist S bis M, 4 ist M mit Finance.
**Wer:** Logistik für 1 und 3, Shop für 2, Finance für 4.
**Woran du merkst, dass es wirkt:** Anzahl nicht abgeholter Sendungen pro Monat und ihr Anteil an allen Sendungen.
**Was nicht kaputtgehen darf:** Conversion im Checkout und Anteil der betroffenen Zahlart am Umsatz.
**Warum das übersehen wird:** Beim Carrier läuft der Fall als zugestellt und danach retourniert. In der Versandstatistik ist alles grün, sichtbar wird es nur im eigenen Retourendatensatz.

### Chargen-Verdacht (Defekt-Häufung in einem Zeitraum)
**Was zu tun ist:**
1. Restbestand der betroffenen Artikel im Lager prüfen und bei Bestätigung sperren, bevor weiter verkauft wird.
2. Wareneingang und Chargennummer des Zeitraums zuordnen.
3. Beim Lieferanten reklamieren, mit den Retourengründen als Beleg.
4. Betroffene Kunden proaktiv anschreiben, wenn es ein Sicherheits- oder Qualitätsthema ist.

**Aufwand:** S bis M, hängt an der Rückverfolgbarkeit.
**Wer:** Einkauf und Logistik.
**Woran du merkst, dass es wirkt:** Defekt-Retouren dieses Artikels pro Monat, zurück auf das Niveau vor dem Ausschlag.
**Was nicht kaputtgehen darf:** Lieferfähigkeit. Eine gesperrte Charge ohne Nachschub ist ein Umsatzloch.
**Einschränkung:** Ohne Chargenspalte ist die Zuordnung eine zeitliche Näherung, kein Beweis. Das gehört so in den Report.

### Erwartungs-Mismatch (Foto oder Beschreibung passt nicht)
**Was zu tun ist:**
1. Produktfotos gegen den echten Artikel halten: Farbtreue, Maßstab, Material, Anwendungssituation.
2. Beschreibung um genau die Angaben ergänzen, die in den Retourengründen fehlen (Materialstärke, Passform, Maße am Modell).
3. Bewertungen und Freitext-Retourengründe nach wiederkehrenden Formulierungen durchsehen, das ist die billigste Quelle für den Fix.
4. Bei Marktplatz-Kanälen prüfen, ob dort dieselben Bilder und Texte laufen.

**Aufwand:** S bis M je Artikel.
**Wer:** Content und Shop.
**Woran du merkst, dass es wirkt:** Anteil "nicht wie beschrieben" und "Farbe" an den Retouren des Artikels.
**Was nicht kaputtgehen darf:** Conversion der Produktseite.

### Mehrgrößen-Bestellungen (Bracketing)
**Was zu tun ist:**
1. Erst die Ursache angehen: Wer die richtige Größe sicher findet, bestellt keine zwei.
2. Hinweis im Warenkorb bei mehreren Größen desselben Artikels, sachlich formuliert, nicht belehrend.
3. Wenn die Marke dazu passt, die Folgen benennen (Kosten, Umwelt). Das ist im RESOLVE-Feldtest der wirksamste der informatorischen Hebel gewesen.
4. Reservierungs- oder Anprobier-Optionen nur prüfen, wenn Logistik und Zahlungsabwicklung das tragen.

**Aufwand:** 2 ist S, 1 und 4 sind M bis L.
**Wer:** Shop.
**Woran du merkst, dass es wirkt:** Anteil der Bestellungen mit mehreren Größen desselben Artikels.
**Was nicht kaputtgehen darf:** Warenkorbwert und Conversion. Bracketing ist auch ein Kaufanreiz.

### Serien-Retournierer
**Was zu tun ist:**
1. Liste ansehen, nicht automatisch handeln. Hinter hohen Quoten stecken oft Stammkunden mit hohem Nettoumsatz.
2. Nettobeitrag je Kunde rechnen, bevor irgendetwas passiert.
3. Bei echten Ausreißern persönlich ansprechen, oft löst das mehr als jede Regel.
4. Erst danach über Steuerung nachdenken (Zahlarten, Kulanzgrenzen), immer als Einzelfall.

**Aufwand:** S für die Sichtung, M für alles Weitere.
**Wer:** Kundenservice, bei Zahlarten Finance.
**Woran du merkst, dass es wirkt:** Nettobeitrag der betroffenen Kunden, nicht ihre Retourenquote.
**Was nicht kaputtgehen darf:** Die Kundenbeziehung. Ein zu Unrecht sanktionierter Stammkunde kostet mehr als seine Retouren.
**Harte Regel:** Diese Liste ist ein Prüfvorschlag für Menschen, kein Urteil. Niemand wird auf Basis dieser Analyse gesperrt.

### Artikel, der nach Retouren nichts mehr verdient
**Was zu tun ist:**
1. Erst die Ursache im Retourengrund suchen. In den meisten Fällen ist es eines der Muster oben, dann ist die Maßnahme dort.
2. Lässt sich die Ursache nicht abstellen, wird es eine Sortiments- oder Preisfrage.
3. Vor jeder Auslistung prüfen, welche Rolle der Artikel im Sortiment spielt (Einstiegsartikel, Kombikäufe).

**Aufwand:** M, Entscheidung liegt höher.
**Wer:** Einkauf, Entscheidung Geschäftsführung.
**Woran du merkst, dass es wirkt:** Deckungsbeitrag nach Retouren je Artikel.
**Was nicht kaputtgehen darf:** Sortimentsbreite und Warenkorbgröße.

## Belegte Effektstärken (für realistische Erwartungen)

Diese Zahlen dienen der Kalibrierung, nicht der Prognose. Sie stammen aus einem anderen Shop-Kontext und dürfen nie als erwartetes Ergebnis für den analysierten Shop ausgegeben werden.

**Größenhinweis am Artikel** (Zalando, KDD 2021, [arXiv:2106.03532](https://arxiv.org/abs/2106.03532), A/B-Tests mit je über 180.000 Personen, peer reviewed, Autoren sind Zalando-Mitarbeitende):
- Textil: 4,3 Prozent relative Senkung der größenbedingten Retouren bei "fällt klein aus", 6,6 Prozent bei "fällt groß aus". Schuhe: 3,8 Prozent.
- Über 10.704 Textil-Artikel fortlaufend gemessen: rund 5 Prozent, im Schnitt 1,5 gesparte Retouren je Artikel.
- **Wichtige Gegenbewegung:** Die Hinweise erhöhten Auswahlbestellungen (zwei Größen im Warenkorb) um 11,1 Prozent bei "zu klein" und 19,0 Prozent bei "zu groß". Genau deshalb ist die Anzahl der Mehrgrößen-Bestellungen die Gegen-Kennzahl dieser Maßnahme. Steigt sie stärker als die Retourenquote fällt, ist die Maßnahme netto negativ.
- **Überraschender Negativbefund:** Eine personalisierte Größenempfehlung aus der Bestellhistorie brachte Conversion plus 2,1 Prozent, aber keine statistisch signifikante Retourensenkung. Das simple artikelbezogene Flag schlägt die aufwendige Personalisierung.

**Einordnung Gesamtmarkt** ([Uni Bamberg, Pressemitteilung 12/2019](https://www.uni-bamberg.de/presse/pm/artikel/massnahmen-retouren-2019/), Befragung von 139 Händlern): Größenberatung plus standardisierte Größenangaben könnten bis zu 25 Prozent der Retouren einsparen. Das ist eine **Einschätzung der befragten Händler, keine gemessene Wirkung**, und liegt um ein Vielfaches über allem, was tatsächlich gemessen wurde. Als Potenzial-Argument brauchbar, als Erwartung nicht.

**Nicht zitieren:** Zahlen wie "18 Prozent Rückgang" oder "bis zu 64 Prozent weniger größenbedingte Retouren" stammen von Anbietern von Größenberatungs-Software ohne offengelegte Methodik.

**Faustregel:** Realistisch sind einstellige relative Senkungen je Maßnahme, nicht zweistellige.
