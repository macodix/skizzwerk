---
document: assessment
process_phase: swk-03
project: "project-name"
status: input
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
basis:
  - idea.md
  - inventory.json
  - assumptions.md # nur wenn vorhanden
  - clarifications.md # nur wenn vorhanden
---

# Bewertung der Befunde

## 1. Bewertungsauftrag

Kurze Beschreibung des Bewertungsauftrags und der verwendeten akzeptierten Eingaben.

## 2. Bewertungsgrundlage

- akzeptierte `idea.md`:
- akzeptierte `inventory.json`:
- projektspezifische `assumptions.md`, sofern vorhanden:
- Stand der Bestandsuntersuchung:

## 3. Bewertungsaspekte

| Aspekt | Bezug zur idea.md | Relevante Befunde |
|---|---|---|
| Bewertungsaspekt | Abschnitt oder Aussage | evd-nnn |

## 4. Bewertung nach Aspekten

### Bewertungsaspekt

Bezug zur `idea.md`:

Verwendete Befunde:
- `evd-nnn`

Feststellbare positive Beiträge:
- ...

Feststellbare Einschränkungen oder Nachteile:
- ...

Unbekannte oder nicht ausreichend untersuchte Punkte:
- ...

Bedeutung für spätere Entscheidungen oder Klärungen:
- ...

Ableitung:
- ...

## 5. Gegenüberstellung vorhandener Alternativen

Nur verwenden, wenn mehrere Alternativen anhand derselben relevanten Aspekte
und dokumentierter Befunde gegenübergestellt werden können.

Die Darstellung darf an die Anzahl der Alternativen angepasst werden. Zulässig
sind insbesondere eine breite Tabelle oder mehrere Tabellen mit identischen
Bewertungsaspekten. Die Darstellung darf keine unterschiedliche Kriterienbasis
für einzelne Alternativen erzeugen.

Beispiel:

| Aspekt | Alternative A | Alternative B | weitere Alternativen ... | Befundgrundlage |
|---|---|---|---|---|
| ... | ... | ... | ... | evd-nnn, evd-nnn |

Keine Rangfolge und keine Gesamtnote ohne ausdrücklich definierte Bewertungsmethode.

## 6. Wesentliche Lücken und offene Sachverhalte

| Sachverhalt | Art | Bedeutung für Bewertung | Durch swk-02 klärbar? | Behandlung |
|---|---|---|---|---|
| ... | Wissenslücke / Anforderungsklärung / möglicher Entscheidungsbedarf | ... | ja/nein | Rückkehr zu swk-02 / Klärung mit Ideengeber / spätere Phase |

## 7. Rückkehrpunkte zu swk-02

Für jeden erforderlichen Rückkehrpunkt:

### Rückkehrpunkt

- Sachverhalt:
- betroffene Befunde:
- Bedeutung für die Bewertung:
- zusätzlich benötigte Untersuchung:
- voraussichtlich verfügbare Quellen oder Prüfwege:

Wenn keine Rückkehr erforderlich ist: `keine`.

## 8. Späterer Klärungs- und Entscheidungsbedarf

### 8.1 Anforderungsklärungen

Für Punkte, die eine Präzisierung oder Bestätigung der Projektidee durch den
Ideengeber benötigen, aber noch keine Auswahl zwischen dokumentierten Optionen
sind. Die vollständige Frage und Antwort stehen in `clarifications.md`.

- `clr-nnn`: Gegenstand — Status: offen / beantwortet — Auswirkung auf Bewertung: ...

Wenn keine Anforderungsklärung erforderlich ist: `keine`.

### 8.2 Entscheidungsbedarfe

Für jeden echten Entscheidungsbedarf:

### dnd-nnn: Kurztitel

- Gegenstand:
- Bezug zur `idea.md`:
- relevante Befunde: `evd-nnn` / keine
- relevante Annahmen: `asm-nnn` / keine
- Begründung des Entscheidungsbedarfs:
- dokumentierte Optionen, soweit vorhanden:
- offene entscheidungsrelevante Sachverhalte:

Ein `dnd-nnn` darf nur angelegt werden, wenn tatsächlich eine spätere Auswahl,
Festlegung oder ausdrückliche Bestätigung erforderlich ist. Eine reine
Wissenslücke oder Anforderungsklärung erhält keine `dnd-nnn`-Kennung.

Keine Entscheidung in dieser Phase treffen.

## 9. Prüfergebnis swk-03

### 9.1 Vorprüfung

| Kriterium | Ergebnis | Nachweis / Anmerkung |
|---|---|---|
| `idea.md` vorhanden und `accepted` | ja/nein | ... |
| `inventory.json` vorhanden und `accepted` | ja/nein | ... |
| `inventory.md` vorhanden und aktuell erzeugt | ja/nein | ... |
| vorhandene `assumptions.md` berücksichtigt | ja/nein/nicht vorhanden | ... |
| referenzierte Regeln und Vorlagen vorhanden und verwendbar | ja/nein | ... |
| Qualitätsgrenze swk-03 vorhanden | ja/nein | ... |
| Kennungen der Eingaben entsprechen `rules/identifiers.md` | ja/nein | ... |

- Vorprüfung insgesamt bestanden: ja/nein

### 9.2 Qualitätsprüfung

- Qualitätsgrenze swk-03 bestanden: ja/nein
- offene erforderliche Rückkehrpunkte zu swk-02: ja/nein
- offene erforderliche Anforderungsklärungen: ja/nein
- nicht erfüllte Kriterien:
- Blockade:

## 10. Freigabestatus

- Ergebnis: `input|draft|review|accepted|blocked|superseded`
- geprüft am:
- geprüft durch:
- Anmerkungen:
