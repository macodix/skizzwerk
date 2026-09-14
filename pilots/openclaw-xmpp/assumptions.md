---
document: assumptions
project: "openclaw-xmpp"
status: review
created: 2026-09-14
last_updated: 2026-09-14
---

# Annahmen

## Zweck

Dieses Dokument verwaltet Annahmen, die während der Bearbeitung des Projekts
erkannt werden.

Für die Behandlung und Bewertung von Annahmen gilt
`rules/assumptions.md`.

## Annahmenübersicht

| Kennung | Annahme | Status | Auswirkung bei Irrtum | Entscheidung erforderlich |
|---|---|---|---|---|
| asm-001 | Das Plugin soll mit dem vorhandenen eigenen XMPP-Server arbeiten. | `superseded` | beteiligte Systeme falsch eingegrenzt | nein |
| asm-002 | Das Plugin soll auf beiden aktiven OpenClaw-Installationen (2026.9.4 und 2026.7.1-2) laufen. | `superseded` | Umfang der Versionen zu klein oder zu groß | nein |
| asm-003 | „Aktuelle OpenClaw-Versionen“ umfasst mindestens Version 2026.9.4. | `superseded` | falsche Zielversion | nein |
| asm-004 | OMEMO-Verschlüsselung soll auch in Gruppenchats über MUC gelten. | `superseded` | Funktionsumfang falsch verstanden | nein |
| asm-005 | XMPP ist der Kommunikationsweg zwischen OpenClaw und Chatpartnern. | `superseded` | Projektgegenstand falsch verstanden | nein |

Zurzeit ist keine Annahme aktiv. asm-001 bis asm-005 sind nach dem Abschnitt
„Abgrenzung“ in `rules/assumptions.md` keine Annahmen: Sie werden in `swk-01`
nicht als vorläufige Arbeitsgrundlage benötigt. Sie sind in `idea.md` als
unbekannte Sachverhalte oder unklare Begriffe erfasst. Sie bleiben zur
Nachvollziehbarkeit erhalten. `INFERRED`

## Einzelbeschreibungen

### asm-001

- Aussage: Das Plugin soll mit dem vorhandenen eigenen XMPP-Server arbeiten.
- Herkunft oder Anlass: `idea.md` Abschnitt 2 nennt einen eigenen XMPP-Server,
  aber keine Rolle für das Plugin.
- Begründung: Die Nennung im Kontext legt einen Zusammenhang nahe, ohne ihn
  auszusprechen.
- Auswirkung bei Irrtum: Die beteiligten Systeme und die Untersuchung vorhandener
  Projekte werden falsch eingegrenzt.
- Bedeutung für den weiteren Prozess: keine als Annahme; als unbekannter
  Sachverhalt in `idea.md` Abschnitt 11 erfasst.
- Status: `superseded`
- Zugehörige Entscheidung: nicht erforderlich
- Nachweis oder Klärung: ersetzt durch die Einstufung als `UNKNOWN` in
  `idea.md` Abschnitt 11
- Erfasst am: 2026-09-14
- Zuletzt geändert: 2026-09-14

### asm-002

- Aussage: Das Plugin soll auf beiden aktiven OpenClaw-Installationen
  (2026.9.4 und 2026.7.1-2) laufen.
- Herkunft oder Anlass: `idea.md` Abschnitt 2 nennt zwei aktive Installationen
  mit unterschiedlichen Versionen, aber keine Rolle für das Plugin.
- Begründung: Die Nennung im Kontext legt nahe, dass beide Installationen
  betroffen sind.
- Auswirkung bei Irrtum: Der Umfang der zu unterstützenden Versionen ist zu
  klein oder zu groß.
- Bedeutung für den weiteren Prozess: keine als Annahme; als unbekannter
  Sachverhalt in `idea.md` Abschnitt 11 erfasst.
- Status: `superseded`
- Zugehörige Entscheidung: nicht erforderlich
- Nachweis oder Klärung: ersetzt durch die Einstufung als `UNKNOWN` in
  `idea.md` Abschnitt 11
- Erfasst am: 2026-09-14
- Zuletzt geändert: 2026-09-14

### asm-003

- Aussage: „Aktuelle OpenClaw-Versionen“ umfasst mindestens Version 2026.9.4.
- Herkunft oder Anlass: `idea.md` Abschnitt 1 nennt „aktuelle
  OpenClaw-Versionen“ ohne Versionsangabe; Abschnitt 2 nennt 2026.9.4 als
  höchste aktive Version.
- Begründung: Die höchste genannte Version liegt als Bezugspunkt nahe.
- Auswirkung bei Irrtum: Die Zielversion ist falsch gewählt.
- Bedeutung für den weiteren Prozess: keine als Annahme; als unklarer Begriff
  in `idea.md` Abschnitt 10 erfasst.
- Status: `superseded`
- Zugehörige Entscheidung: nicht erforderlich
- Nachweis oder Klärung: ersetzt durch die Erfassung als unklarer Begriff in
  `idea.md` Abschnitt 10
- Erfasst am: 2026-09-14
- Zuletzt geändert: 2026-09-14

### asm-004

- Aussage: OMEMO-Verschlüsselung soll auch in Gruppenchats über MUC gelten.
- Herkunft oder Anlass: `idea.md` Abschnitt 1 nennt OMEMO-Verschlüsselung und
  Gruppenchats über MUC nebeneinander, ohne Bezug zueinander.
- Begründung: Abschnitt 2 nennt Sicherheit (OMEMO) als Anforderung, ohne sie
  auf Direktnachrichten zu beschränken.
- Auswirkung bei Irrtum: Der Funktionsumfang ist falsch verstanden.
- Bedeutung für den weiteren Prozess: keine als Annahme; als unklarer Begriff
  in `idea.md` Abschnitt 10 erfasst.
- Status: `superseded`
- Zugehörige Entscheidung: nicht erforderlich
- Nachweis oder Klärung: ersetzt durch die Erfassung als unklarer Begriff in
  `idea.md` Abschnitt 10
- Erfasst am: 2026-09-14
- Zuletzt geändert: 2026-09-14

### asm-005

- Aussage: XMPP ist der Kommunikationsweg zwischen OpenClaw und Chatpartnern.
- Herkunft oder Anlass: `idea.md` Abschnitt 1 nennt XMPP nur im Wort
  „XMPP-Plugin“.
- Begründung: Die genannten Funktionen Direktnachrichten und Gruppenchats
  legen einen Nachrichtenaustausch über XMPP nahe.
- Auswirkung bei Irrtum: Der Projektgegenstand ist falsch verstanden.
- Bedeutung für den weiteren Prozess: keine als Annahme; als unklarer Begriff
  in `idea.md` Abschnitt 10 erfasst.
- Status: `superseded`
- Zugehörige Entscheidung: nicht erforderlich
- Nachweis oder Klärung: ersetzt durch die Erfassung als unklarer Begriff in
  `idea.md` Abschnitt 10
- Erfasst am: 2026-09-14
- Zuletzt geändert: 2026-09-14
