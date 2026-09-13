# Dokumentstatus

## Zweck

Der Status beschreibt den Bearbeitungs- und Freigabestand eines
projektspezifischen Dokuments.

## Verbindliche Statuswerte

| Status | Bedeutung |
|---|---|
| `input` | Eingabe wurde erfasst, aber noch nicht durch skizzwerk bearbeitet. |
| `draft` | Dokument wurde bearbeitet, aber noch nicht vollständig geprüft. |
| `review` | Bearbeitung und interne Prüfungen sind abgeschlossen. Eine Prüfung oder Entscheidung durch den Ideengeber ist erforderlich. |
| `accepted` | Dokument wurde vom Ideengeber inhaltlich bestätigt. |
| `blocked` | Die Bearbeitung kann wegen einer wesentlichen fehlenden Information oder Entscheidung nicht fortgesetzt werden. |
| `superseded` | Das Dokument wurde durch eine neuere Fassung oder Entscheidung ersetzt. |

## Zulässige Übergänge

| Von | Nach | Auslöser |
|---|---|---|
| neu | `input` | Eingabe wird angelegt |
| `input` | `draft` | skizzwerk beginnt die Bearbeitung |
| `draft` | `review` | Bearbeitung und interne Prüfung sind abgeschlossen |
| `review` | `accepted` | Ideengeber bestätigt den Inhalt |
| `review` | `draft` | Überarbeitung ist erforderlich |
| beliebig | `blocked` | Wesentliche Information oder Entscheidung fehlt |
| `blocked` | `draft` | Blockade wurde aufgelöst |
| `accepted` | `superseded` | Eine neue Fassung ersetzt das Dokument |

## Regeln

- Ein Status darf nur verwendet werden, wenn seine Voraussetzungen erfüllt sind.
- `review` bedeutet nicht, dass der Inhalt bereits freigegeben ist.
- `accepted` darf nicht allein durch die bearbeitende KI gesetzt werden.
- Der Wechsel zu `accepted` benötigt eine ausdrückliche menschliche Bestätigung.
- `blocked` benötigt eine dokumentierte Begründung.
- Bei `superseded` muss auf die ersetzende Fassung verwiesen werden.
