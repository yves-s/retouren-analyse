# Was bei Retouren wirklich wirkt: die Evidenzlage

Gesammelte Ergebnisse aus A/B-Tests, Feldexperimenten und Meta-Analysen zu Retouren im Onlinehandel. Zweck: Empfehlungen an Messungen binden statt an Bauchgefühl, und die kursierenden Zahlen einordnen, die keiner Prüfung standhalten.

Kanonische Fassung dieses Wissens liegt bei Path to AI im WorkOS unter `06-wissen/retouren-evidenz.md`. Änderungen dort zuerst.

**Belegstufen, überall mitgeführt:**
- **[A] Kausal gemessen:** A/B-Test, randomisiertes Feldexperiment oder sauberes Quasi-Experiment
- **[B] Beobachtet:** Panel- oder Archivdaten, Korrelation, Wirkungsrichtung nicht gesichert
- **[C] Befragung:** Selbstauskunft von Händlern oder Verbrauchern, Einschätzung statt Messung
- **[D] Anbieterangabe:** wirtschaftliches Interesse, meist ohne Methodik

---

## 1. Was gemessen wirkt

### Artikelbezogener Größenhinweis ("fällt klein aus") [A]
Zalando, KDD 2021, A/B-Tests mit je über 180.000 Personen (Textil) und 720.000 (Schuhe), dazu fortlaufende Difference-in-Differences über 10.704 Textil- und 3.625 Schuh-Artikel.

| Test | Effekt auf größenbedingte Retouren |
|---|---|
| Textil, "fällt klein aus" | minus 4,3 Prozent |
| Textil, "fällt groß aus" | minus 6,6 Prozent |
| Schuhe | minus 3,8 Prozent |
| Textil, fortlaufend gemessen | minus 5,0 bis 8,2 Prozent |

Nebenwirkung, die zwingend mitgemessen werden muss: Die Hinweise erhöhten Mehrgrößen-Bestellungen um 11,1 Prozent ("zu klein") und 19,0 Prozent ("zu groß").
Quelle: [arXiv:2106.03532](https://arxiv.org/abs/2106.03532). Autoren sind Zalando-Mitarbeitende, peer reviewed.

### Umwelt- und Kosten-Hinweis bei Auswahlbestellungen [A]
RESOLVE, BMUV-gefördertes Verbundprojekt, randomisierter Feldtest im echten OTTO-Shop, September bis November 2022, vier Gruppen.
- Anteil Mehrgrößen-Bestellungen: 30,2 Prozent mit Hinweis gegen 31,8 Prozent ohne
- Reduktion von Mehrfach- auf Einzelauswahl: 34,1 Prozent bei Hinweis im Warenkorb gegen 30,0 Prozent ohne
- **Der wichtigste Befund: Bestellungen, Artikel je Bestellung und Umsatz blieben unverändert.** Der Hinweis kostet nichts.
- Fazit der Autoren: bis zu 2 Prozentpunkte weniger Auswahlbestellungen

Wichtig: Die Feldergebnisse sind im Bericht deskriptiv berichtet, ohne Signifikanztests. Randomisierung und Nullbefund beim Umsatz machen es trotzdem zur belastbarsten deutschen Quelle.
Quelle: [RESOLVE Abschlussbericht 2023](https://verbraucherwissenschaften.de/wp-content/uploads/2023/08/RESOLVE_Abschlussbericht.pdf)

### Umwelt-Nudge allgemein [A]
Minus 2,6 Prozent Retouren ohne Umsatzverlust, n = 117.304, europäischer Fashion-Händler.
Quelle: von Zahn u.a., Marketing Science ("Smart Green Nudging")

### Zoom-Funktion auf der Produktseite [B]
Senkt Retouren messbar. Siehe Gegenbefund zu zusätzlichen Bildern unter Abschnitt 2.
Quelle: De, Hu, Rahman (2013), Information Systems Research 24(4)

### Kundenfotos im Nutzungskontext [B]
Senken Retouren stärker als Produktfotos ohne Kontext und stärker als reiner Text. Bilder helfen besonders bei Funktionalität, Text eher bei Ästhetik. Effektstärken nicht öffentlich.
Quelle: Wang, Kim, Ghoshal (2026), Production and Operations Management 35(4)

### Produktbewertungen [B]
Marginale Effekte auf die Retourenwahrscheinlichkeit, Datenbasis: nordamerikanischer Händler, drei Marken, zwei Jahre, je 14.000 Kunden.

| Veränderung | Effekt |
|---|---|
| 10 zusätzliche Bewertungen | minus 0,6 Prozent |
| plus 0,1 Sterne im Schnitt | minus 2,4 Prozent |
| plus 10 Prozent Streuung der Bewertungen | plus 4,0 Prozent |
| Kauf im Laden statt online | minus 12,6 Prozent |

Bemerkenswert: Die Autoren stellen ausdrücklich fest, dass der von Anbieterseite kursierende Claim "Bewertungen senken Retouren um 20,4 Prozent" in der Forschung keine Bestätigung findet. Der gemessene Effekt liegt um mehr als eine Größenordnung darunter.
Quelle: Sahoo, Dellarocas, Srinivasan (2018), Information Systems Research 29(3), [Working Paper frei](http://thearf-org-unified-admin.s3.amazonaws.com/MSI/2020/06/MSI_Report_16-101.pdf)

### Passform-Bewertungen mit Referenz [B]
"Fällt klein aus" allein wirkt nur, wenn viele Bewerter übereinstimmen. Wirksam wird es erst mit dem Bezugspunkt des Bewerters (Körpermaße plus getragene Größe). Gerade bei widersprüchlichen oder seltenen Bewertungen ist die Referenz entscheidend.
Quelle: Wang, Ramachandran, Sheng (2021), Information Systems Research 32(1)

### Begründung bei Verschärfung [A]
Restriktive Änderungen (kürzere Fristen, Rücksendegebühren) senken Vertrauen, Kaufabsicht und Weiterempfehlung. Eine mitgelieferte Begründung fängt das messbar ab. Ob auf Kosten oder auf Missbrauch abgestellt wird, macht keinen Unterschied.
Quelle: Abdulla, Ketzenberg, Abbey, Heim (2025), Journal of Operations Management 71(1)

---

## 2. Was nicht wirkt oder nach hinten losgeht

### Personalisierte Größenempfehlung senkt keine Retouren [A]
Zalandos eigener A/B-Test, über 300.000 Kunden je Gruppe: Conversion plus 2,1 Prozent, Warenkorb plus 1,8 Prozent, Umsatz je Besuch plus 2,1 Prozent, aber **keine statistisch signifikante Senkung größenbedingter Retouren** (unter 0,5 Prozent relativ). Das simple artikelbezogene Flag wirkte deutlich besser.

Bestätigend aus anderer Richtung [B]: Bei einer schwedischen High-End-Plattform (496.365 Artikel, sieben Jahre) retournierten Nutzer des Größenberaters **0,65 Prozent häufiger**, nicht seltener. Dafür stieg ihr Kundenwert deutlich (plus 7,5 Prozent im Folgequartal). Nicht kausal, Selbstselektion plausibel.
Quellen: [arXiv:2106.03532](https://arxiv.org/abs/2106.03532); Patel, Karlsson, Oghazi (2025), [Journal of Innovation & Knowledge 10](https://researchportal.hkr.se/ws/files/96462443/1-s2.0-S2444569X25001246-main.pdf)

**Konsequenz:** Größenberater-Software ist eine Conversion-Investition. Wer sie kauft, um Retouren zu senken, kauft womöglich das Falsche.

### Zusätzliche Produktbilder erhöhen Retouren [B]
In der einzigen Studie, die einzelne Bildfunktionen gegeneinander testet: Zoom senkt Retouren, **alternative Ansichten erhöhen sie**, Farb-Swatches wirken gar nicht. Plausible Erklärung: Zoom liefert Materialinformation, weitere Ansichten liefern Kaufanreiz.
Quelle: De, Hu, Rahman (2013), Information Systems Research 24(4)

Dazu passt die Einschätzung der Uni Bamberg (2019), dass bessere Beschreibungen, Bilder und Bewertungen ihr Potenzial weitgehend ausgeschöpft haben und neue Ansätze nötig sind [C].

### Marketing treibt Retouren [B]
Newsletter, Kataloge, Paid Search und kostenloser Versand erhöhen Retouren um bis zu 18 Prozent. Keines der untersuchten Marketinginstrumente senkt sie.
Quelle: El Kihal, Shehu, Journal of Retailing 98(3)

### Kostenlose Rücksendung kostet kurzfristig Geld [A]
Sauberes Quasi-Experiment: Ein Händler führte kostenlose Retouren nur in Dänemark ein, sechs Vergleichsländer blieben unverändert.

| Kennzahl | Effekt |
|---|---|
| Bestellwert | plus 9,15 Prozent |
| Produktvielfalt je Bestellung | plus 8,74 Prozent |
| Bruttomarge je Bestellung | plus 9,71 Prozent |
| Retouren je Bestellung | plus 7,86 Prozent |

Fazit der Autoren: Die Retourenkosten übersteigen kurzfristig den Margenzuwachs.
Quelle: Patel, Baldauf, Karlsson, Oghazi (2021), [Journal of Operations Management 67(4)](https://onlinelibrary.wiley.com/doi/10.1002/joom.1135)

### Zahlarten streichen bringt nichts [C, mit klarer Warnung]
Die Korrelation ist belegt: 25,3 Prozent Retourenquote bei Rechnungskauf gegen 13,1 Prozent bei Vorkasse (Asdecker, n = 538), im Fashion-Bereich 55,7 gegen 30,2 Prozent. Aber die Wirkungsrichtung ist umgekehrt: Laut ECC Köln zahlen 41 Prozent per Rechnung, **wenn die Retoure fest eingeplant ist**, doppelt so häufig wie sonst. Die Zahlart zieht das Verhalten an, sie erzeugt es nicht.

ibi research widerspricht der naheliegenden Konsequenz ausdrücklich: Wer Zahlarten wegnimmt, dessen Kunden weichen aus oder bestellen bei der Konkurrenz. Dann ist der ganze Umsatz weg, nicht nur die Retoure.

### Rücksendegebühren: die Angst ist zehnmal so groß wie der Effekt [C]
Händler ohne Gebühren befürchten 16,2 Prozent Umsatzrückgang. Händler, die bereits Gebühren erheben, berichten von durchschnittlich 1,4 Prozent (n = 21, nicht repräsentativ).

Zweiter Effekt: Bei 18- bis 29-Jährigen würden fast 50 Prozent nicht mehr online Mode kaufen. Die Quote sinkt dann, weil das Segment abwandert, nicht weil sich Verhalten ändert.

Die kursierende Zahl "2,95 Euro Gebühr vermeidet 16 Prozent der Retouren" ist eine Händler-Schätzung. Der bevh relativiert sie im eigenen Kompendium ausdrücklich als "Vermutung der befragten Personen" und weist auf einen Rechenfehler in der Hochrechnung hin.

---

## 3. Kulanz: fünf Regler, die gegeneinander laufen [A]

Meta-Analyse über mehr als 20 Studien. Kulanz hat fünf Dimensionen: Frist, Geld, Aufwand, Umfang, Umtausch. Sie wirken unterschiedlich:

- **Käufe steigern:** großzügige Geld-zurück-Regelung, wenig Aufwand für den Kunden
- **Retouren senken:** lange Frist, Umtausch statt Erstattung
- **Retouren treiben:** großzügiger Umfang, reine Geld-zurück-Garantie

Insgesamt steigert Kulanz Käufe stärker als Retouren.

**Praktische Konsequenz:** Wer Kulanz zurücknehmen will, sollte nicht die Frist kürzen. Die lange Frist ist die Dimension, die Käufe kaum bremst und Retouren sogar senkt. Wer den Umfang begrenzt, trifft dagegen den Hebel, der Retouren wirklich treibt.
Quelle: Janakiraman, Syrdal, Freling (2016), Journal of Retailing 92(2), [Verlagsseite](https://www.sciencedirect.com/science/article/abs/pii/S0022435915000822). Effektstärken hinter Paywall, Richtungsbefunde aus zwei unabhängigen Sekundärquellen.

---

## 4. Baselines zum Einordnen eigener Zahlen

**Retourenquoten nach Branche [C]** (Asdecker, via bevh-Retourenkompendium): Durchschnitt rund 20 Prozent. Lebensmittel, Bücher, Elektronik, DIY unter 10 Prozent. Drogerie, Spielwaren, Wohnen knapp 20 Prozent. Sport und Freizeit 30 Prozent. **Fashion und Accessoires fast 40 Prozent**, einzelne Modeartikel und Schuhe 70 bis 80 Prozent.

**Aus Verbrauchersicht [C]** (Bitkom Research 2024, 1.050 Online-Shopper, repräsentativ): 11 Prozent aller Käufe gehen zurück, 24 Prozent retournieren nie. Frauen 14, Männer 9 Prozent. 16 bis 29 Jahre 15 Prozent, ab 65 Jahre 7 Prozent.

**Retourengründe [C]** (dieselbe Erhebung, Mehrfachnennung): Größe passte nicht 67 Prozent, defekt oder beschädigt 56, gefiel nicht 50, **entsprach nicht Bild oder Beschreibung 41**, schlecht verarbeitet 37, falscher Artikel 29, bewusst zu viel bestellt 29, verspätete Lieferung 13.

**Kosten je Retoure [C]** (EHI, 124 bis 146 Händler DACH): über die Hälfte bis 10 Euro, knapp 14 Prozent bis 20 Euro, rund ein Viertel kann es nicht beziffern. Ältere Vollkostenrechnung der Uni Bamberg: 19,51 Euro je Sendung (9,85 Transport, 9,66 Bearbeitung). Die Differenz erklärt sich vermutlich über unterschiedliche Kostendefinitionen.

**Verwertung [C]:** 79 bis 93 Prozent der Retouren gehen als A-Ware zurück in den Verkauf, rund 4 Prozent werden entsorgt.

**Fehlgeschlagene Zustellung [C, Anbieter-Auftrag]:** In Deutschland scheitern rund 7 Prozent der Zustellungen im ersten Versuch (2017: 5 Prozent), Kosten durchschnittlich 14,69 Euro je Fall. Adressqualität im Onlinehandel: 8,7 Prozent der Kundenadressen fehlerhaft (Deutsche Post Direkt, rund 120 Millionen Adressen).

**Missbrauch [C]:** 3,6 Prozent der Verbraucher geben an, das Widerrufsrecht bewusst zweckwidrig genutzt zu haben. Händler schätzen den Anteil auf 19,1 Prozent. **Faktor fünf zwischen gefühlt und gemessen.**

---

## 5. Zahlen, die kursieren und nicht belegt sind

Diese Werte tauchen regelmäßig in Blogs und Verkaufsunterlagen auf. Keine davon hat einer Prüfung standgehalten:

| Behauptung | Status |
|---|---|
| "Bewertungen senken Retouren um 20,4 Prozent" | Anbieter-Claim, von Forschern ausdrücklich als unbestätigt bezeichnet |
| "Größenberatung senkt Retouren um 18 bis 64 Prozent" | Anbieterangaben ohne Methodik |
| "Filial-Routing senkt Rücksendungen um 64 Prozent" | Vendor-Aussage ohne Quelle, Datenbasis und Zeitraum |
| "Virtual Try-on senkt Retouren um 30 bis 40 Prozent" | zirkuläre Sekundärquellen, einzige Primärangabe ist ein Hersteller-Pilot ohne Setup-Beschreibung |
| "Zara hat mit Retourengebühren die Quote um X gesenkt" | keine öffentliche Messung, weder im Geschäftsbericht noch in der Fachpresse |
| "Größenberatung könnte 25 Prozent aller Retouren sparen" | Händler-Schätzung aus einer Umfrage, rund fünfmal höher als jede Messung |

**Faustregel:** Einstellige relative Senkungen je Maßnahme sind realistisch. Alles jenseits von 20 Prozent ohne Kontrollgruppe ist Marketing.

---

## 6. Rechtlicher Rahmen (Deutschland)

- **Annahmeverweigerung ist kein Widerruf.** Seit Juni 2014 verlangt das Gesetz eine eindeutige Widerrufserklärung. Wer die Annahme verweigert oder eine falsche Adresse angibt, gerät in Annahmeverzug (§§ 293 ff. BGB). Der Händler hat daraus Ansprüche, die bei einem regulären Widerruf nicht bestehen.
- **Rücksendekosten dürfen dem Kunden auferlegt werden** (§ 357 Abs. 6 BGB, seit 2014 ohne Wertgrenze).
- **Kontosperren wegen häufiger Widerrufe sind angreifbar**, weil sie die Ausübung eines gesetzlichen Rechts sanktionieren. Belastbare Rechtsprechung fehlt weitgehend.
- **Die Deckelung von Zahlarten ist der rechtlich sicherere Hebel:** Es besteht kein Anspruch auf eine bestimmte Zahlart, das Widerrufsrecht bleibt unangetastet. Genau deshalb ist die Praxis großer Händler dreistufig aufgebaut (Hinweis, dann Zahlarten-Einschränkung, erst zuletzt Sperre).
