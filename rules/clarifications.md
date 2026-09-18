# Anforderungsklärungen

## Zweck

Anforderungsklärungen dokumentieren Präzisierungen oder Bestätigungen einer
bereits vorhandenen, aber unklaren oder unvollständigen Aussage der
Projektidee durch den Ideengeber.

Sie halten neues Anforderungswissen nachvollziehbar fest, ohne die akzeptierte
`idea.md` stillschweigend zu verändern.

## Abgrenzung

Eine Anforderungsklärung ist:

- keine Bestands- oder Wissenslücke,
- keine Annahme,
- kein Entscheidungsbedarf und keine Entscheidung,
- kein externer Befund.

Wissenslücken, Annahmen und Entscheidungen bleiben in ihren jeweils
vorgesehenen Prozessmechanismen.

Eine Anforderungsklärung darf nicht verwendet werden, um eine dieser Kategorien
umzudeklarieren oder zu umgehen.

## Kennung

Jede Anforderungsklärung erhält eine eindeutige Kennung `clr-nnn` nach
`rules/identifiers.md`.

## Projektdokument

Anforderungsklärungen werden projektspezifisch in `clarifications.md` nach
`templates/clarifications.md` geführt.

Für jede Klärung werden mindestens dokumentiert:

- `clr-nnn`,
- Gegenstand,
- Ausgangsfrage,
- Bezug zur `idea.md`,
- relevante `evd-nnn`, soweit vorhanden,
- Antwort des Ideengebers,
- Herkunft der Antwort als `USER_PROVIDED`,
- Auswirkung auf die Bewertung,
- gegebenenfalls erkannter Folgeprozess.

Eine unbeantwortete Klärung bleibt ausdrücklich offen. Die KI darf keine
Antwort ergänzen oder aus anderen Angaben vermuten.

## Verhältnis zur akzeptierten idea.md

Eine Antwort, die eine bereits vorhandene Aussage der akzeptierten `idea.md`
präzisiert oder bestätigt, ändert die akzeptierte `idea.md` nicht. Die
ursprüngliche Aussage bleibt erhalten; die Präzisierung wird über `clr-nnn`
nachvollziehbar ergänzt.

Widerspricht eine Antwort der akzeptierten `idea.md`, verändert sie den
Projektgegenstand materiell oder führt sie eine neue, bisher nicht angelegte
Projektanforderung ein, darf sie nicht als normale Anforderungsklärung
übernommen werden. Der betroffene frühere Prozessstand ist zu bestimmen und
nach `rules/process.md` erneut zu bearbeiten.

## Rückwirkung auf swk-03

Nach jeder beantworteten Anforderungsklärung prüft swk-03:

- welche Aussagen und Ableitungen in `assessment.md` betroffen sind,
- ob Bewertungsaspekte ergänzt oder präzisiert werden müssen,
- ob sich die Einordnung von Wissenslücken, Nachweisgrenzen oder
  Entscheidungsbedarfen ändert,
- ob ein Rückkehrbedarf in eine frühere Phase entstanden ist.

Betroffene Teile von `assessment.md` werden nachvollziehbar aktualisiert.
Nicht betroffene Bewertungen werden nicht ohne Grund verändert.

Anschließend wird die Qualitätsgrenze swk-03 erneut vollständig geprüft.

## Traceability

Spätere Anforderungen und Entscheidungen können auf `clr-nnn` verweisen.
Dadurch bleibt unterscheidbar, welche Aussage aus der ursprünglichen
`idea.md` stammt und welche erst durch eine spätere Anforderungsklärung vom
Ideengeber präzisiert wurde.
