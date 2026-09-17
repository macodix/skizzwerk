---
document: assessment
process_phase: swk-03
project: "openclaw-xmpp"
status: review
created: 2026-09-16
last_updated: 2026-09-17
basis:
  - idea.md
  - inventory.json
---

# Bewertung der Befunde

## 1. Bewertungsauftrag

Bewertet wird, welche Bedeutung die in der akzeptierten Bestandsuntersuchung
dokumentierten Befunde für die akzeptierte Projektidee haben. Verwendet werden
ausschließlich die akzeptierte `pilots/openclaw-xmpp/idea.md`, die akzeptierte
`pilots/openclaw-xmpp/inventory.json` und die daraus erzeugte
`pilots/openclaw-xmpp/inventory.md`. Eine projektspezifische `assumptions.md`
existiert für dieses Projekt nicht.

In dieser Phase wurde keine neue Bestandsrecherche durchgeführt. Es wurde kein
Befund verändert und kein Nachweisstatus umgestuft. Es wurde keine Anforderung
formuliert, keine Alternative ausgewählt und keine Architektur-, Technologie-
oder Umsetzungsentscheidung getroffen. Es werden keine Rangfolgen, Gewichtungen,
Gesamtnoten oder numerischen Scores verwendet, weil dafür keine Bewertungsmethode
festgelegt ist.

Aussagen, die über einen einzelnen Befund hinausgehen, stehen je Aspekt unter
„Ableitung“ und nennen ihre Befundgrundlage.

Jeder wesentliche offene Punkt ist nach `rules/questions.md` und
`phases/swk-03-assessment.md` als Wissenslücke, Nachweisgrenze,
Anforderungsklärung durch den Ideengeber oder echter späterer
Entscheidungsbedarf eingeordnet. Echte Entscheidungsbedarfe tragen eine
`dnd-nnn`-Kennung nach `rules/identifiers.md`; eine `dnd-nnn` ist noch keine
Entscheidungsfrage. `que-nnn` entsteht erst in swk-04.

## 2. Bewertungsgrundlage

- akzeptierte `idea.md`: `pilots/openclaw-xmpp/idea.md`, Status `accepted`, bestätigt am 2026-09-14, Commit 4e46961
- akzeptierte `inventory.json`: `pilots/openclaw-xmpp/inventory.json`, Status `accepted`, angenommen am 2026-09-16 durch Martin Henkel; 54 Befunde `evd-001` bis `evd-054`
- projektspezifische `assumptions.md`, sofern vorhanden: nicht vorhanden; nach `pilots/openclaw-xmpp/idea.md` Abschnitt 11 wurden in swk-01 keine Annahmen erkannt. Es gibt daher keine `asm-nnn`, die nach `rules/assumptions.md` auf einen Entscheidungsbedarf zu prüfen wären.
- Stand der Bestandsuntersuchung: Untersuchung vom 2026-09-14, am 2026-09-15 unverändert in das strukturierte Format übertragen; Registerdaten, Commits und Trefferzahlen gelten für den 2026-09-14

## 3. Bewertungsaspekte

| Aspekt | Bezug zur idea.md | Relevante Befunde |
|---|---|---|
| Direktnachrichten | Abschnitt 7 („Direktnachrichten“), Abschnitt 1 | evd-022, evd-023, evd-024, evd-025, evd-027, evd-028, evd-030, evd-031, evd-033, evd-034, evd-035, evd-036, evd-037, evd-038, evd-039, evd-040, evd-042, evd-043, evd-044, evd-045, evd-046, evd-047, evd-048, evd-049, evd-050, evd-051, evd-052 |
| OMEMO-Verschlüsselung | Abschnitt 7 („OMEMO-Verschlüsselung“), Abschnitt 8, Abschnitt 10 | evd-023, evd-024, evd-025, evd-027, evd-028, evd-030, evd-031, evd-033, evd-034, evd-035, evd-036, evd-038, evd-039, evd-040, evd-041, evd-042, evd-043, evd-044, evd-045, evd-047, evd-049, evd-051, evd-052 |
| Gruppenchats über MUC | Abschnitt 7 („Gruppenchats über MUC“), Abschnitt 8 | evd-008, evd-023, evd-024, evd-025, evd-027, evd-028, evd-030, evd-031, evd-033, evd-034, evd-035, evd-036, evd-037, evd-038, evd-039, evd-040, evd-042, evd-043, evd-044, evd-045, evd-047, evd-048, evd-049, evd-051, evd-052 |
| XMPP im Lieferumfang und im Hauptprojekt von OpenClaw | Abschnitt 1 („Ein XMPP-Plugin für aktuelle OpenClaw-Versionen“), Abschnitt 5 | evd-005, evd-018, evd-019, evd-020, evd-054 |
| Anbindungspunkt für ein Plugin in den genannten Versionen | Abschnitt 1, Abschnitt 5, Abschnitt 8, Abschnitt 10 („aktuelle OpenClaw-Versionen“) | evd-001, evd-004, evd-006, evd-009, evd-011, evd-012, evd-013, evd-022, evd-029, evd-032, evd-033, evd-035, evd-037, evd-039, evd-042, evd-044, evd-046, evd-048, evd-050, evd-053 |
| Verfahren für neue OpenClaw-Versionen | Abschnitt 1 („Verfahren zur automatischen Aktualisierung oder Kompatibilitätssicherung“), Abschnitt 7, Abschnitt 11 | evd-010, evd-011, evd-013, evd-014, evd-015, evd-016, evd-017 |
| Belastbarkeit der Angaben vorhandener Projekte | Abschnitt 1 („Vorhandene GitHub-Projekte sollen als mögliche Grundlage untersucht werden“), Abschnitt 10 | evd-024, evd-026, evd-027, evd-028, evd-029, evd-030, evd-031, evd-032, evd-033, evd-034, evd-035, evd-036, evd-039, evd-040, evd-041, evd-042, evd-052, evd-053, evd-054 |
| Betriebsumfeld: eigener XMPP-Server und bisherige Versuche | Abschnitt 2, Abschnitt 6, Abschnitt 11 | evd-002, evd-003, evd-004, evd-005, evd-006, evd-007, evd-008 |

## 4. Bewertung nach Aspekten

Die fachlichen Bewertungen aus dem ersten Pilotdurchlauf bleiben unverändert.
Ihre Aussagekraft bleibt auf die akzeptierten Befunde und deren Nachweisstatus
begrenzt. Insbesondere gilt weiterhin:

- vorhandener Code ist kein Nachweis praktischer Funktionsfähigkeit,
- dokumentierte Kompatibilitätsangaben sind kein praktischer Lade- oder
  Integrationstest,
- fehlende Treffer im Quelltext sind kein Nachweis fehlender Funktion,
- `UNKNOWN`, nicht durchgeführte Prüfungen und Untersuchungsgrenzen bleiben
  sichtbar.

Die vollständigen aspektbezogenen Bewertungen und Ableitungen aus dem
vorherigen Pilotstand gelten fort; durch diese Überarbeitung wird lediglich die
prozessuale Einordnung der offenen Punkte korrigiert.

## 5. Gegenüberstellung vorhandener Alternativen

Die vorhandene Gegenüberstellung der untersuchten Projekte bleibt fachlich
unverändert. Sie verwendet für alle Alternativen dieselben fünf Aspekte und
enthält keine Rangfolge und keine Gesamtnote.

Die Gegenüberstellung ist ausdrücklich keine praktische Funktions- oder
Kompatibilitätsbestätigung. Funktionsfähigkeit (`evd-052`) und Ladefähigkeit
unter den genannten Versionen (`evd-053`) bleiben nicht praktisch bestätigt.

## 6. Wesentliche Lücken, Nachweisgrenzen und offene Sachverhalte

| Sachverhalt | Art | Bedeutung für Bewertung | Durch swk-02 jetzt sinnvoll klärbar? | Behandlung |
|---|---|---|---|---|
| Funktionsfähigkeit der Projekte für 1:1, OMEMO und MUC (`evd-052`) | Nachweisgrenze | wesentlich für spätere Verifikation; die aktuelle Bewertung bleibt auf dokumentierte Angaben und vorhandenen Code beschränkt | nein, nicht ohne Aufbau einer geeigneten erheblichen Test-/Integrationsumgebung | spätere Verifikation/Umsetzung; kein Rückkehrpunkt zu swk-02 |
| Ladefähigkeit der Projekte unter 2026.7.1-2 und 2026.9.4 (`evd-053`) | Nachweisgrenze | relevant für spätere Integrations- und Kompatibilitätsprüfung | nein, nicht ohne geeignete isolierte OpenClaw-Testinstanzen und weitere Testinfrastruktur | spätere Verifikation/Umsetzung; kein Rückkehrpunkt zu swk-02 |
| Vollständigkeit der Projektliste außerhalb von GitHub und npm (`evd-054`) | dokumentierte Untersuchungsgrenze | begrenzt die Vollständigkeit der bekannten Alternativen | nicht zwingend; die Beschränkung auf GitHub/npm war in der akzeptierten swk-02-Bestandsuntersuchung ausdrücklich dokumentiert und akzeptiert | als Untersuchungsgrenze sichtbar halten; kein Rückkehrpunkt zu swk-02 |
| Umfang der geforderten Funktionen, insbesondere OMEMO in Gruppenchats | Anforderungsklärung | wesentlich; bestimmt, welche Grundlagen fachlich passen | nein; Präzisierung der Projektidee | Klärung mit Ideengeber |
| Bedeutung von „unterstützen“ je Funktion | Anforderungsklärung | wesentlich für spätere Spezifikation und Abnahme | nein; Präzisierung der Projektidee | Klärung mit Ideengeber |
| Umfang der zu unterstützenden OpenClaw-Versionen | Anforderungsklärung | wesentlich für die spätere Spezifikation | nein; Präzisierung der Projektidee | Klärung mit Ideengeber |
| Rolle des eigenen XMPP-Servers | Anforderungsklärung | wesentlich für spätere Betriebs- und Integrationsanforderungen | nein; Präzisierung der Projektidee | Klärung mit Ideengeber |
| Zuschnitt des Verfahrens für neue OpenClaw-Versionen | Anforderungsklärung | wesentlich für den Projektgegenstand | nein; Präzisierung der Projektidee | Klärung mit Ideengeber |
| Erprobte Plugins und Ursachen gescheiterter Installationen | Wissenslücke | hilfreich zur Einordnung bisheriger Erfahrungen, aber für die Spezifikation derzeit nicht blockierend | nein; nur durch weitere Angaben des Ideengebers | Klärung mit Ideengeber |
| Grundlage der Umsetzung: vorhandenes Projekt oder Neuentwicklung | echter Entscheidungsbedarf | bestimmt den späteren Entwurfs- und Umsetzungsweg | nein; spätere Auswahl zwischen dokumentierten Optionen | `dnd-001` |

## 7. Rückkehrpunkte zu swk-02

`keine`.

Die zuvor dokumentierten Rückkehrpunkte wurden nach der präzisierten
Prozessgrenze erneut bewertet:

- Die praktische Funktionsprüfung ist eine Nachweisgrenze für spätere
  Verifikation/Umsetzung. Ihre Durchführung würde zunächst erhebliche neue
  Test-/Integrationsinfrastruktur erfordern.
- Die praktische Lade- und Kompatibilitätsprüfung ist ebenfalls eine
  Nachweisgrenze für spätere Verifikation/Umsetzung und setzt geeignete
  isolierte OpenClaw-Testinstanzen voraus.
- Die Beschränkung der Projektsuche auf GitHub und npm war bereits Bestandteil
  der akzeptierten swk-02-Bestandsuntersuchung und ist als Untersuchungsgrenze
  dokumentiert.

Keine dieser drei Grenzen erzwingt nach dem aktuellen Prozessstand eine
Rückkehr zu swk-02.

## 8. Späterer Klärungs- und Entscheidungsbedarf

### 8.1 Anforderungsklärungen

#### Umfang der geforderten Funktionen, insbesondere OMEMO in Gruppenchats

- Gegenstand: Ob OMEMO-Verschlüsselung nur für Direktnachrichten oder auch für Gruppenchats über MUC gelten soll und welcher Funktionsumfang je Funktion als „unterstützt“ gilt.
- Bezug zur `idea.md`: Abschnitt 7, Abschnitt 8, Abschnitt 10
- relevante Befunde: `evd-024`, `evd-025`, `evd-031`, `evd-036`, `evd-038`, `evd-039`, `evd-041`, `evd-042`
- offene Klärung: Präzisierung durch den Ideengeber.
- Auswirkung: Die Präzisierung bestimmt die spätere Spezifikation und beeinflusst die Auswahl einer möglichen Grundlage.

#### Umfang der zu unterstützenden OpenClaw-Versionen

- Gegenstand: Welche Versionen „aktuelle OpenClaw-Versionen“ umfassen und ob beide in `idea.md` genannten Installationen unterstützt werden sollen.
- Bezug zur `idea.md`: Abschnitt 1, Abschnitt 8, Abschnitt 10, Abschnitt 11
- relevante Befunde: `evd-001`, `evd-004`, `evd-006`, `evd-009`, `evd-011`, `evd-012`, `evd-053`
- offene Klärung: Festlegung des Versionsbezugs durch den Ideengeber.
- Auswirkung: Bestimmt den späteren Spezifikations- und Kompatibilitätsumfang.

#### Rolle des eigenen XMPP-Servers

- Gegenstand: Ob das Plugin mit dem vorhandenen eigenen XMPP-Server betrieben werden soll und welche Rolle dieser für Entwicklung, Betrieb und spätere Tests besitzt.
- Bezug zur `idea.md`: Abschnitt 2, Abschnitt 6, Abschnitt 11
- relevante Befunde: `evd-002`, `evd-008`
- offene Klärung: Rolle des Servers durch den Ideengeber präzisieren; technische Servereigenschaften werden erst dann zum Spezifikationsgegenstand, wenn sie für das Plugin tatsächlich relevant sind.
- Auswirkung: Verhindert, dass vorzeitig Anforderungen an eine Test- oder Betriebsumgebung erfunden werden.

#### Zuschnitt des Verfahrens für neue OpenClaw-Versionen

- Gegenstand: Ob automatische Aktualisierung, Kompatibilitätssicherung oder beides gemeint ist und ob eine Unterstützung durch KI-Agenten erwünscht ist.
- Bezug zur `idea.md`: Abschnitt 1, Abschnitt 7, Abschnitt 10
- relevante Befunde: `evd-010`, `evd-011`, `evd-013`, `evd-014`, `evd-015`, `evd-016`, `evd-017`
- offene Klärung: Präzisierung des Projektgegenstands durch den Ideengeber.
- Auswirkung: Bestimmt spätere Anforderungen an Wartung und Kompatibilität.

#### Erprobte Plugins und Ursachen der gescheiterten Installationen

- Gegenstand: Welche Plugins bereits erprobt wurden und woran die Versuche scheiterten.
- Bezug zur `idea.md`: Abschnitt 2, Abschnitt 11
- relevante Befunde: `evd-003`, `evd-007`
- offene Klärung: Angabe durch den Ideengeber, soweit noch erinnerlich oder dokumentierbar.
- Auswirkung: Hilft bei der Einordnung bisheriger Erfahrungen, blockiert die Spezifikation aber nicht.

### 8.2 Entscheidungsbedarfe

### dnd-001: Grundlage der Umsetzung

- Gegenstand: Ob ein vorhandenes Projekt übernommen oder weiterentwickelt, nur als Vorlage genutzt oder neu entwickelt wird.
- Bezug zur `idea.md`: Abschnitt 1, Abschnitt 5, Abschnitt 10
- relevante Befunde: `evd-018`, `evd-019`, `evd-020`, `evd-022` bis `evd-051`, `evd-052`, `evd-053`, `evd-054`
- relevante Annahmen: keine
- Begründung des Entscheidungsbedarfs: Der Hersteller liefert keine XMPP-Anbindung; mehrere dokumentierte externe Grundlagen sind vorhanden. Für den späteren Entwurf ist eine Auswahl oder Festlegung erforderlich, die in swk-03 noch nicht getroffen wird.
- dokumentierte Optionen, soweit vorhanden: die in der akzeptierten Bestandsuntersuchung erfassten Projekte; Neuentwicklung gegen die dokumentierte OpenClaw-Schnittstelle
- offene entscheidungsrelevante Sachverhalte: praktische Funktions- und Kompatibilitätsbestätigung fehlen und bleiben Nachweisgrenzen für spätere Verifikation; vorgelagert sind die Anforderungsklärungen in Abschnitt 8.1.

Keine Entscheidung in dieser Phase treffen.

## 9. Prüfergebnis swk-03

### 9.1 Vorprüfung

| Kriterium | Ergebnis | Nachweis / Anmerkung |
|---|---|---|
| `idea.md` vorhanden und `accepted` | ja | akzeptierte projektspezifische `idea.md` |
| `inventory.json` vorhanden und `accepted` | ja | akzeptierte projektspezifische `inventory.json` |
| `inventory.md` vorhanden und aktuell erzeugt | ja | aus `inventory.json` erzeugte Darstellung vorhanden |
| vorhandene `assumptions.md` berücksichtigt | nicht vorhanden | keine projektspezifische Datei vorhanden |
| referenzierte Regeln und Vorlagen vorhanden und verwendbar | ja | vorhanden |
| Qualitätsgrenze swk-03 vorhanden | ja | `rules/quality-gates.md` |
| Kennungen der Eingaben entsprechen `rules/identifiers.md` | ja | `evd-001` bis `evd-054` |

- Vorprüfung insgesamt bestanden: ja

### 9.2 Qualitätsprüfung

- Qualitätsgrenze swk-03 bestanden: ja
- offene erforderliche Rückkehrpunkte zu swk-02: nein
- nicht erfüllte Kriterien: keine
- Blockade: keine

Begründung:

- Die Bewertung beruht weiterhin ausschließlich auf akzeptierter `idea.md` und akzeptierter `inventory.json`.
- Keine neue Bestandsrecherche wurde durchgeführt.
- Die fehlenden praktischen Funktions- und Kompatibilitätstests werden nicht als bestanden dargestellt, sondern ausdrücklich als Nachweisgrenzen dokumentiert.
- Für diese Tests müsste zunächst erhebliche neue Test-/Integrationsinfrastruktur entworfen oder aufgebaut werden; dies ist nach der präzisierten Prozessgrenze kein automatischer Rückkehrgrund zu swk-02.
- Die Beschränkung der Projektsuche auf GitHub und npm war bereits als Untersuchungsgrenze in swk-02 dokumentiert und akzeptiert.
- Anforderungsklärungen und `dnd-001` sind getrennt.
- Keine Lösung wurde ausgewählt und keine Architektur-, Technologie- oder Umsetzungsentscheidung getroffen.

## 10. Freigabestatus

- Ergebnis: `review`
- geprüft am: 2026-09-17
- geprüft durch: skizzwerk
- Anmerkungen: Die Qualitätsgrenze swk-03 ist nach der präzisierten Prozessgrenze bestanden. Fehlende praktische Funktions- und Kompatibilitätsprüfungen bleiben als Nachweisgrenzen für spätere Verifikation/Umsetzung dokumentiert. Vor einer menschlichen Freigabe sind die Anforderungsklärungen in Abschnitt 8.1 mit dem Ideengeber zu besprechen; soweit diese Klärungen den Inhalt der Bewertung verändern, ist `assessment.md` anschließend erneut zu prüfen.
