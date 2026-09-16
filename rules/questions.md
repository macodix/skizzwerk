# Umgang mit Entscheidungsfragen

## Zweck

Diese Regeln legen fest, wie Entscheidungsbedarf dokumentiert und als
`que-nnn`-Entscheidungsfrage strukturiert wird.

## Definition

Eine Entscheidungsfrage liegt vor, wenn für den weiteren Prozess eine Auswahl,
Festlegung oder ausdrückliche Bestätigung zwischen dokumentierten
Handlungsoptionen erforderlich ist.

Keine Entscheidungsfrage ist allein:

- ein unbekannter Sachverhalt,
- eine noch nicht durchgeführte Untersuchung,
- ein Widerspruch zwischen Quellen,
- eine fehlende Anforderungsklärung,
- eine Annahme ohne wesentliche Auswirkung,
- ein Sachverhalt, der durch weitere Bestandsuntersuchung geklärt werden kann.

## Regeln

- Jede Entscheidungsfrage erhält eine eindeutige `que-nnn`-Kennung.
- Der Entscheidungsbedarf muss aus einem akzeptierten Vorphasenergebnis
  nachvollziehbar hergeleitet werden.
- Jede Entscheidungsfrage muss den konkreten Entscheidungsgegenstand nennen.
- Dokumentierte Optionen müssen auf akzeptierte Vorphasenergebnisse
  zurückgeführt werden können.
- Optionen dürfen nicht frei erfunden oder stillschweigend ergänzt werden.
- Bekannte Vor- und Nachteile oder Einschränkungen dürfen nur entsprechend der
  akzeptierten Bewertungsgrundlage wiedergegeben werden.
- Unbekannte entscheidungsrelevante Sachverhalte bleiben sichtbar.
- Abhängigkeiten zu anderen Entscheidungsfragen werden dokumentiert.
- Die KI darf keine Option als bevorzugt, empfohlen oder ausgewählt darstellen,
  solange die dafür vorgesehene Entscheidungsphase dies nicht ausdrücklich
  vorsieht.
- Eine Entscheidungsfrage darf keine Entscheidung vorwegnehmen.
- Eine bloße Wissenslücke darf nicht in eine Entscheidungsfrage umformuliert
  werden.
- Ist eine wesentliche fehlende Information durch Bestandsuntersuchung klärbar,
  wird Rückkehrbedarf dokumentiert statt eine Auswahl zu erzwingen.

## Bezug zu Annahmen

Nach `rules/assumptions.md` benötigen Annahmen mit wesentlicher Auswirkung eine
Entscheidung.

Eine solche Annahme erzeugt nicht automatisch eine Entscheidungsfrage. Der
Entscheidungsbedarf muss in der dafür vorgesehenen Bewertungsphase ausdrücklich
geprüft und dokumentiert werden.

Wird daraus eine Entscheidungsfrage, verweist diese auf die zugehörige
`asm-nnn`-Kennung. Die Annahme selbst bleibt in `assumptions.md` verwaltet.

## Abgrenzung zur Entscheidung

Eine `que-nnn`-Entscheidungsfrage dokumentiert, was entschieden werden muss.

Die eigentliche Entscheidung erhält erst in der dafür vorgesehenen späteren
Phase eine `dec-nnn`-Kennung. Bis dahin bleibt die Entscheidungsfrage offen.
