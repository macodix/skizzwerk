# Qualitätsgrenzen

## Zweck

Qualitätsgrenzen legen fest, wann eine Phase abgeschlossen werden darf.

Eine Phase gilt nicht als abgeschlossen, nur weil alle vorgesehenen
Dokumentabschnitte Text enthalten.

## Allgemeine Regeln

- Jedes Ergebnis muss gegen die Qualitätsgrenze seiner Phase geprüft werden.
- Nicht erfüllte Kriterien müssen sichtbar dokumentiert werden.
- Die KI darf fehlende Informationen nicht erfinden.
- Ein Dokument mit wesentlichen Mängeln darf nicht den Status `review` erhalten.
- Ein Dokument darf nur durch ausdrückliche menschliche Bestätigung den Status
  `accepted` erhalten.
- Ein blockierter Abschluss muss mit einer konkreten Begründung dokumentiert werden.

## Qualitätsgrenze swk-01

`swk-01` darf den Status `review` erhalten, wenn:

- die Originalbeschreibung unverändert erhalten ist,
- Herkunft und Kontext unverändert erhalten sind,
- Originalaussagen und Interpretationen klar getrennt sind,
- Ziel und erwarteter Nutzen aus der Eingabe abgeleitet wurden,
- genannte Nutzer, Systeme, Funktionen und Einschränkungen erfasst wurden,
- mehrdeutige Begriffe sichtbar gekennzeichnet sind,
- keine Annahme als Tatsache dargestellt wird,
- keine zusätzliche Anforderung erfunden wurde,
- keine Architekturentscheidung getroffen wurde,
- keine konkrete technische Lösung ausgewählt wurde,
- offene Punkte sichtbar bleiben,
- alle Kennungen `rules/identifiers.md` entsprechen,
- Annahmen von Ableitungen und unbekannten Sachverhalten abgegrenzt sind,
- jede in `idea.md` referenzierte Annahme in `assumptions.md` existiert,
- Übersichts- und Einzelangaben zu Annahmen widerspruchsfrei sind,
- `idea.md` und `assumptions.md` den jeweiligen Vorlagen entsprechen.


## Nichtbestehen der Qualitätsgrenze

Wird mindestens ein erforderliches Kriterium nicht erfüllt:

1. bleibt der Status `draft`,
2. wird der Mangel im Prüfergebnis genannt,
3. wird das Dokument überarbeitet oder als `blocked` gekennzeichnet.

## Menschliche Freigabe

Nach bestandener Qualitätsgrenze erhält das Dokument den Status `review`.

Der Ideengeber prüft anschließend:

- Wurde die Idee richtig verstanden?
- Fehlt eine ausdrücklich genannte Aussage?
- Wurde etwas hinzugefügt, das nicht aus der Eingabe folgt?
- Sind die erkannten Mehrdeutigkeiten tatsächlich vorhanden?

Erst danach darf der Status auf `accepted` gesetzt werden.