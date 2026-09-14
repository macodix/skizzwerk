# swk-01: Projektidee erfassen und strukturieren

## Zweck

Eine frei formulierte Projektidee wird strukturiert, ohne Anforderungen,
Lösungsarchitektur oder technische Entscheidungen vorwegzunehmen.

## Eingaben

Erforderlich:

- projektspezifische `idea.md`
- ausgefüllte Abschnitte `1. Originalbeschreibung`
- ausgefüllter Abschnitt `2. Herkunft und Kontext`

Zusätzliche Eingaben:

- `templates/idea.md`
- `templates/assumptions.md`
- `rules/evidence.md`
- `rules/assumptions.md`
- `rules/quality-gates.md`

## Arbeitsauftrag

1. Lies die vollständige projektspezifische `idea.md`.
2. Bewahre die Abschnitte 1 und 2 inhaltlich unverändert.
3. Ermittle aus der Originalbeschreibung:
   - das verstandene Ziel,
   - den erwarteten Nutzen,
   - den genannten Projektgegenstand,
   - bekannte Nutzer und beteiligte Systeme,
   - ausdrücklich genannte Funktionen,
   - ausdrücklich genannte Einschränkungen,
   - ausdrücklich ausgeschlossene Inhalte.
4. Identifiziere mehrdeutige Begriffe und Aussagen.
5. Trenne eindeutig zwischen:
   - Originalaussagen,
   - Kontextinformationen,
   - Ableitungen,
   - Annahmen,
   - unbekannten Sachverhalten.
6. Erfasse jede erkannte Annahme mit eindeutiger Kennung in der
   projektspezifischen `assumptions.md`.
7. Verweise in `idea.md` ausschließlich über diese Kennungen auf die
   erfassten Annahmen.
8. Ergänze die fehlenden Abschnitte anhand von `templates/idea.md`.
9. Prüfe das Ergebnis anhand des Qualitätskatalogs für `swk-01`.

## Verbindliche Regeln

- Erfinde keine Anforderungen.
- Triff keine Architekturentscheidung.
- Wähle keine Software, Bibliothek oder technische Lösung aus.
- Recherchiere noch keine möglichen Lösungen.
- Behandle Annahmen nicht als Tatsachen.
- Formuliere noch keine Rückfragen an den Ideengeber.
- Kennzeichne jede Interpretation ausdrücklich.
- Überschreibe keine Originalaussage.
- Ändere den Status nur entsprechend dem Prüfergebnis.
- Für Statuswerte und Statusübergänge gilt `rules/status.md`.

## Ergebnis

- eine vervollständigte projektspezifische `idea.md`
- eine angelegte oder ergänzte projektspezifische `assumptions.md`

Mögliche Statuswerte:

- `input`: Nur die Eingabe des Ideengebers liegt vor.
- `draft`: Die KI hat die Idee strukturiert.
- `review`: Das Dokument wartet auf Prüfung durch den Ideengeber.
- `accepted`: Der Ideengeber hat die Erfassung bestätigt.
- `blocked`: Die Idee ist nicht ausreichend erfassbar.

## Abschlusskriterien

`swk-01` ist abgeschlossen, wenn:

- Original und Interpretation getrennt sind,
- keine unbegründeten Anforderungen ergänzt wurden,
- mehrdeutige Aussagen sichtbar sind,
- alle Abschnitte der Vorlage bearbeitet wurden,
- keine Architekturentscheidung getroffen wurde,
- das Dokument den Status `accepted` erhalten hat.
