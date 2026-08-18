# Retouren-Analyse

Ein Claude Skill, der Muster in E-Commerce-Retourendaten findet und in priorisierte Maßnahmen übersetzt. CSV-Export rein (aus Xentral, Shopify, WooCommerce oder jedem anderen System), Analyse und Maßnahmen-Report raus. Keine API, kein Backend-Zugriff, keine sensiblen Live-Daten.

Von [Path to AI](https://www.path-to-ai.com/) (Yves Schleich). Gebaut, weil es dafür nichts Brauchbares gab.
Erklärt und mit Beispielen: [path-to-ai.com/skills/retouren-analyse](https://www.path-to-ai.com/skills/retouren-analyse/).

**Dies ist ein ordnerbasierter Claude-Skill.** Er besteht nicht nur aus der `SKILL.md`, sondern braucht `scripts/` und `reference/` daneben, sonst kann er nicht rechnen. Zum Installieren gehört deshalb immer der komplette Ordner ins Skill-Verzeichnis, siehe unten.

## Was er findet

- **Quoten sauber gerechnet:** Beta-, Gamma- und Bestellquote je Bestell-Kohorte (nicht der übliche Zeitfenster-Fehler), unreife Kohorten markiert
- **Größen-Läufer:** welcher Artikel fällt klein oder groß aus
- **Chargen-Probleme:** Defekt-Spikes, die auf eine schlechte Charge zeigen
- **Nicht abgeholte Sendungen:** der Retouren-Typ, der in Carrier-Statistiken unsichtbar ist, inklusive Zahlart-Korrelation
- **Serien-Retournierer und Bracketing:** als Review-Liste, nie als automatische Sanktion
- **Kosten-Attribution:** welche SKU nach Retouren noch Geld verdient und welche nicht

Prinzip: das Python-Script rechnet deterministisch, die AI interpretiert und schreibt den Report. Jedes Finding trägt ein Evidenz-Tag, jede Annahme ist markiert.

## Installation

**Claude Code**, im Terminal wie in der Desktop-App. Der ganze Ordner kommt ins Skill-Verzeichnis:

| Ziel | Ordner |
|---|---|
| in allen Projekten verfügbar | `~/.claude/skills/retouren-analyse/` |
| nur in einem Projekt | `.claude/skills/retouren-analyse/` im Projekt |

Danach Claude einmal neu starten. Aufrufen muss man den Skill nicht, die `description` im Frontmatter löst ihn aus, sobald es um Retouren geht.

**claude.ai, Claude-Chat und Cowork:** Repo als ZIP laden (Code → Download ZIP), in Claude unter Customize → Skills über + → Create skill → Upload a skill hochladen. Für die Rechenschritte muss die Code-Ausführung aktiv sein.

## Nutzung

Retouren- und Verkaufs-CSV bereitstellen und die Analyse anstoßen, den Rest macht der Skill. Details in `SKILL.md`.

Nur das Script, ohne AI:

```bash
python3 scripts/retouren_analyse.py --retouren retouren.csv --verkaeufe verkaeufe.csv --out analysis.json
```

## Demo

```bash
python3 demo/generate_demo_data.py
python3 scripts/retouren_analyse.py --retouren demo/retouren.csv --verkaeufe demo/verkaeufe.csv --out demo/analysis.json
```

Der synthetische Datensatz (Stil eines ERP-Berichte-Exports) enthält eingebaute Muster: einen Größen-Läufer, einen Chargen-Defekt, eine Serien-Retournierin, einen Foto-Mismatch und nicht abgeholte Sendungen mit Rechnungskauf-Häufung. `demo/beispiel-report.md` zeigt, was der Skill daraus macht.

## Fachliche Grundlage

Quoten-Taxonomie nach der Forschungsgruppe Retourenmanagement der Uni Bamberg (Alpha/Beta/Gamma), Maßnahmen u. a. aus dem BMUV-Projekt RESOLVE (feldgetestet mit OTTO), Kosten-Anker aus EHI-Händlerbefragungen. Quellen in `reference/`.

## Lizenz

MIT
