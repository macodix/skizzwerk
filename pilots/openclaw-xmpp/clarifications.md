---
document: clarifications
project: "openclaw-xmpp"
status: draft
created: 2026-09-18
last_updated: 2026-09-18
---

# Anforderungsklärungen

Diese Datei enthält ausschließlich Anforderungsklärungen nach
`rules/clarifications.md`.

## Übersicht

| Kennung | Gegenstand | Status |
|---|---|---|
| `clr-001` | Umfang von OMEMO | offen |
| `clr-002` | Bedeutung von „unterstützen“ je Funktion | offen |
| `clr-003` | Umfang der zu unterstützenden OpenClaw-Versionen | offen |
| `clr-004` | Rolle des eigenen XMPP-Servers | offen |
| `clr-005` | Verfahren für neue OpenClaw-Versionen | offen |
| `clr-006` | Erprobte Plugins und Ursachen der gescheiterten Installationen | offen |

## Klärungen

### clr-001: Umfang von OMEMO

- Gegenstand: Ob OMEMO-Verschlüsselung für Direktnachrichten, für Gruppenchats über MUC oder für beides gelten soll.
- Bezug zur `idea.md`: Abschnitt 7 („OMEMO-Verschlüsselung“), Abschnitt 10 („OMEMO-Verschlüsselung“: Geltungsbereich offen)
- relevante Befunde: `evd-024`, `evd-025`, `evd-031`, `evd-036`, `evd-038`, `evd-039`, `evd-041`, `evd-042`
- Ausgangsfrage: Soll OMEMO-Verschlüsselung für Direktnachrichten gelten, für Gruppenchats über MUC oder für beides?
- Antwort des Ideengebers: noch nicht vorhanden
- Herkunft der Antwort: noch nicht vorhanden
- Status: offen
- Auswirkung auf `assessment.md`: betrifft Abschnitt 4 „OMEMO-Verschlüsselung“, Abschnitt 5 und die offenen entscheidungsrelevanten Sachverhalte von `dnd-001`
- Folgeprozess: noch nicht bestimmbar
- Anmerkungen: für den Abschluss von swk-03 erforderlich

### clr-002: Bedeutung von „unterstützen“ je Funktion

- Gegenstand: Welcher Funktionsumfang bei Direktnachrichten, Gruppenchats über MUC und OMEMO als „unterstützt“ gilt.
- Bezug zur `idea.md`: Abschnitt 1 („Das Plugin muss Direktnachrichten, OMEMO-Verschlüsselung und Gruppenchats über MUC unterstützen.“), Abschnitt 8, Abschnitt 10 („unterstützen“)
- relevante Befunde: keine
- Ausgangsfrage: Was muss das Plugin bei Direktnachrichten, bei Gruppenchats über MUC und bei OMEMO jeweils können, damit du die Funktion als „unterstützt“ ansiehst?
- Antwort des Ideengebers: noch nicht vorhanden
- Herkunft der Antwort: noch nicht vorhanden
- Status: offen
- Auswirkung auf `assessment.md`: betrifft Abschnitt 4 „Direktnachrichten“, „OMEMO-Verschlüsselung“ und „Gruppenchats über MUC“
- Folgeprozess: noch nicht bestimmbar
- Anmerkungen: für den Abschluss von swk-03 erforderlich

### clr-003: Umfang der zu unterstützenden OpenClaw-Versionen

- Gegenstand: Welche Versionen „aktuelle OpenClaw-Versionen“ umfassen, ob beide genannten Installationen unterstützt werden sollen und wo diese laufen.
- Bezug zur `idea.md`: Abschnitt 1 („aktuelle OpenClaw-Versionen“), Abschnitt 2 („2 OpenClaw Installationen, Versionen 2026.9.4 und 2026.7.1-2, aktiv“), Abschnitt 10
- relevante Befunde: `evd-001`, `evd-004`, `evd-006`, `evd-009`, `evd-011`, `evd-012`, `evd-053`
- Ausgangsfrage: a) Welche Versionen meinst du mit „aktuelle OpenClaw-Versionen“? b) Soll das Plugin auf beiden in Abschnitt 2 genannten Installationen laufen, also 2026.9.4 und 2026.7.1-2? c) Ist srv001 eine dieser beiden Installationen, und wo läuft die mit 2026.7.1-2?
- Antwort des Ideengebers: noch nicht vorhanden
- Herkunft der Antwort: noch nicht vorhanden
- Status: offen
- Auswirkung auf `assessment.md`: betrifft Abschnitt 4 „Anbindungspunkt für ein Plugin in den genannten Versionen“ und „Betriebsumfeld“ sowie die offenen Sachverhalte von `dnd-001`
- Folgeprozess: noch nicht bestimmbar
- Anmerkungen: für den Abschluss von swk-03 erforderlich

### clr-004: Rolle des eigenen XMPP-Servers

- Gegenstand: Ob das Plugin mit dem vorhandenen eigenen XMPP-Server arbeiten soll und in welcher Rolle.
- Bezug zur `idea.md`: Abschnitt 2 („Ein eigener XMPP-Server ist vorhanden“), Abschnitt 6, Abschnitt 11
- relevante Befunde: `evd-002`, `evd-008`
- Ausgangsfrage: Soll das Plugin mit deinem vorhandenen XMPP-Server arbeiten, und wenn ja, in welcher Rolle?
- Antwort des Ideengebers: noch nicht vorhanden
- Herkunft der Antwort: noch nicht vorhanden
- Status: offen
- Auswirkung auf `assessment.md`: betrifft Abschnitt 4 „Gruppenchats über MUC“ und „Betriebsumfeld“
- Folgeprozess: noch nicht bestimmbar
- Anmerkungen: für den Abschluss von swk-03 erforderlich

### clr-005: Verfahren für neue OpenClaw-Versionen

- Gegenstand: Ob automatische Aktualisierung, Kompatibilitätssicherung oder beides gemeint ist, was dabei automatisch geschehen soll und welche Rolle KI-Agenten haben.
- Bezug zur `idea.md`: Abschnitt 1 („Verfahren zur automatischen Aktualisierung oder Kompatibilitätssicherung … ggf. auch mit KI-Agenten“), Abschnitt 10
- relevante Befunde: `evd-010`, `evd-011`, `evd-013`, `evd-014`, `evd-015`, `evd-016`, `evd-017`
- Ausgangsfrage: a) Meinst du mit „automatische Aktualisierung oder Kompatibilitätssicherung“ das eine, das andere oder beides? b) Was soll dabei jeweils automatisch geschehen? c) Sollen KI-Agenten dabei eingesetzt werden, oder hast du sie nur als Möglichkeit genannt?
- Antwort des Ideengebers: noch nicht vorhanden
- Herkunft der Antwort: noch nicht vorhanden
- Status: offen
- Auswirkung auf `assessment.md`: betrifft Abschnitt 4 „Verfahren für neue OpenClaw-Versionen“
- Folgeprozess: noch nicht bestimmbar
- Anmerkungen: für den Abschluss von swk-03 erforderlich

### clr-006: Erprobte Plugins und Ursachen der gescheiterten Installationen

- Gegenstand: Welche Plugins bereits erprobt wurden und woran ihre Installation scheiterte.
- Bezug zur `idea.md`: Abschnitt 2 („bestehende Plugins konnten z. T. nicht installiert werden …“), Abschnitt 11
- relevante Befunde: `evd-003`, `evd-007`
- Ausgangsfrage: Welche Plugins hast du erprobt, und woran ist die Installation jeweils gescheitert?
- Antwort des Ideengebers: noch nicht vorhanden
- Herkunft der Antwort: noch nicht vorhanden
- Status: offen
- Auswirkung auf `assessment.md`: betrifft Abschnitt 4 „Betriebsumfeld“ und die Einordnung der Projekte in Abschnitt 5
- Folgeprozess: noch nicht bestimmbar
- Anmerkungen: für den Abschluss von swk-03 nicht erforderlich; nach `assessment.md` Abschnitt 6 hilfreich zur Einordnung, aber nicht blockierend
