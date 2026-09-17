---
document: questions
process_phase: swk-04
project: "project-name"
status: input
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
basis:
  - idea.md
  - inventory.json
  - assessment.md
  - assumptions.md # nur wenn in assessment.md referenziert
---

# Entscheidungsfragen

## 1. Entscheidungsauftrag

Kurze Beschreibung des Auftrags und der verwendeten akzeptierten Eingaben.

## 2. Entscheidungsgrundlage

- akzeptierte `idea.md`:
- akzeptierte `inventory.json`:
- akzeptierte `assessment.md`:
- projektspezifische `assumptions.md`, sofern referenziert:

## 3. Übersicht

| Kennung | Entscheidungsbedarf | Entscheidungsfrage | Bezug zur assessment.md | Status |
|---|---|---|---|---|
| `que-nnn` | `dnd-nnn` | ... | Abschnitt / Punkt | offen |

## 4. Entscheidungsfragen

### que-nnn: Kurztitel

Zugehöriger Entscheidungsbedarf:

- `dnd-nnn`

Entscheidungsfrage:

- ...

Bezug zur `assessment.md`:

- ...

Relevante Befunde:

- `evd-nnn` / keine

Relevante Annahmen:

- `asm-nnn` / keine

Dokumentierte Optionen:

#### Option A

- Beschreibung:
- bekannte Vorteile:
- bekannte Nachteile oder Einschränkungen:
- unbekannte entscheidungsrelevante Sachverhalte:

#### Option B

- Beschreibung:
- bekannte Vorteile:
- bekannte Nachteile oder Einschränkungen:
- unbekannte entscheidungsrelevante Sachverhalte:

Abhängigkeiten zu anderen Entscheidungen:

- `que-nnn` / keine

Folgen einer Vertagung:

- ... / nicht aus den Vorphasen ableitbar

Fehlende Informationen:

- ... / keine

Erforderliche Behandlung fehlender Informationen:

- Rückkehr zu swk-03; dort gegebenenfalls Rückkehr zu swk-02 nach `rules/process.md`
- spätere Klärung
- keine

Status der Entscheidungsfrage:

- offen

## 5. Rückkehr- und Klärungsbedarf

| Entscheidungsfrage | Entscheidungsbedarf | Fehlende Information | Bestandsfrage? | Behandlung |
|---|---|---|---|---|
| `que-nnn` | `dnd-nnn` | ... | ja/nein | Rückkehr zu swk-03 / spätere Klärung |

Bei Rückkehr zu swk-03 wird ein weiterer Rückweg zu swk-02 ausschließlich
nach den Kriterien in `rules/process.md` und `phases/swk-03-assessment.md`
entschieden.

Wenn kein Rückkehr- oder Klärungsbedarf besteht: `keiner`.

## 6. Prüfergebnis swk-04

- Vorprüfung bestanden: ja/nein
- Qualitätsgrenze swk-04 bestanden: ja/nein
- nicht erfüllte Kriterien:
- Blockade:

## 7. Freigabestatus

- Ergebnis: `input|draft|review|accepted|blocked|superseded`
- geprüft am:
- geprüft durch:
- Anmerkungen:
