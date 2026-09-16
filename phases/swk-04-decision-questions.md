# swk-04: Entscheidungsfragen erstellen

## Zweck

Die in der akzeptierten Bewertung aus `swk-03` als entscheidungsrelevant
dokumentierten Punkte werden in klar abgegrenzte Entscheidungsfragen
überführt.

Die Phase beantwortet insbesondere:

- welche Entscheidungen auf Grundlage der bisherigen Ergebnisse tatsächlich
  erforderlich sind,
- welche dokumentierten Optionen zu einer Entscheidung gehören,
- welche Folgen und offenen Punkte je Option bereits aus `swk-03` bekannt
  sind,
- welche Informationen für eine belastbare menschliche Entscheidung noch
  fehlen,
- welche Entscheidungen voneinander abhängig sind.

`swk-04` trifft die Entscheidungen nicht selbst. Die Phase formuliert keine
neuen Anforderungen und ergänzt keine Optionen, die nicht aus den akzeptierten
Ergebnissen der vorherigen Phasen ableitbar sind.

## Vorprüfung

Vor der Bearbeitung ist zu prüfen:

- die projektspezifische `idea.md` existiert und besitzt den Status `accepted`,
- die projektspezifische `inventory.json` existiert und besitzt den Status
  `accepted`,
- die projektspezifische `assessment.md` existiert und besitzt den Status
  `accepted`,
- alle in dieser Phasendatei referenzierten Dateien existieren,
- keine benötigte Regel oder Vorlage ist leer oder offensichtlich
  unvollständig,
- `rules/quality-gates.md` enthält eine Qualitätsgrenze für `swk-04`,
- verwendete Kennungen entsprechen `rules/identifiers.md`.

Bei fehlgeschlagener Vorprüfung wird kein projektspezifisches Ergebnis von
`swk-04` angelegt oder verändert.

## Eingaben

Erforderlich:

- projektspezifische `idea.md` mit Status `accepted`,
- projektspezifische `inventory.json` mit Status `accepted`,
- projektspezifische `assessment.md` mit Status `accepted`,
- `rules/process.md`,
- `rules/evidence.md`,
- `rules/assumptions.md`,
- `rules/identifiers.md`,
- `rules/status.md`,
- `rules/quality-gates.md`,
- `templates/questions.md`.

## Entscheidungsgrundlage

Eine Entscheidungsfrage darf nur entstehen, wenn ihr Entscheidungsbedarf aus
der akzeptierten `assessment.md` hervorgeht.

Jede Entscheidungsfrage muss auf die zugehörige Bewertung und soweit relevant
auf die zugrunde liegenden `evd-nnn`-Befunde verweisen.

Optionen dürfen nur aufgenommen werden, wenn sie in den akzeptierten
Vorphasenergebnissen dokumentiert oder daraus unmittelbar und nachvollziehbar
ableitbar sind.

Eine fehlende Option darf nicht durch eine frei erfundene Alternative ersetzt
werden.

## Arbeitsauftrag

1. Lies die vollständige akzeptierte `assessment.md` sowie die darin
   referenzierten relevanten Stellen aus `idea.md` und `inventory.json`.

2. Ermittle alle Punkte, die in `assessment.md` ausdrücklich als später zu
   entscheiden dokumentiert sind.

3. Prüfe für jeden solchen Punkt, ob tatsächlich eine Entscheidung erforderlich
   ist oder ob lediglich ein unbekannter beziehungsweise ungeklärter Sachverhalt
   vorliegt.

4. Formuliere für jeden bestätigten Entscheidungsbedarf genau eine klar
   abgegrenzte Entscheidungsfrage.

5. Dokumentiere je Entscheidungsfrage:

   - Bezug zur `assessment.md`,
   - gegebenenfalls relevante `evd-nnn`-Befunde,
   - den konkreten Entscheidungsgegenstand,
   - dokumentierte Optionen,
   - bereits bekannte Vor- und Nachteile oder Einschränkungen je Option,
   - entscheidungsrelevante unbekannte Sachverhalte,
   - Abhängigkeiten zu anderen Entscheidungen,
   - Folgen einer vertagten Entscheidung, soweit aus den Vorphasen ableitbar.

6. Prüfe, ob für die Entscheidung notwendige Informationen fehlen.

7. Wenn fehlende Informationen durch erneute Bestandsuntersuchung geklärt
   werden können, dokumentiere einen Rückkehrbedarf zu `swk-02` über `swk-03`.

8. Wenn fehlende Informationen keine Bestandsfrage sind, dokumentiere sie als
   offene Klärung für eine spätere geeignete Phase oder für den Ideengeber.

9. Erstelle oder vervollständige die projektspezifische `questions.md` anhand
   von `templates/questions.md`.

10. Prüfe das Ergebnis anhand der Qualitätsgrenze für `swk-04` in
    `rules/quality-gates.md`.

## Verbindliche Regeln

- Erfinde keine Entscheidungsbedarfe.
- Erfinde keine Optionen.
- Erfinde keine Anforderungen, Tatsachen oder Bewertungskriterien.
- Verändere keine akzeptierten Ergebnisse früherer Phasen.
- Formuliere eine Entscheidungsfrage nur, wenn ihr Bedarf aus der akzeptierten
  `assessment.md` hervorgeht.
- Halte bekannte Tatsachen, dokumentierte Behauptungen, Ableitungen, Annahmen
  und unbekannte Sachverhalte getrennt.
- Stelle keine Option als bevorzugt, empfohlen oder ausgewählt dar.
- Triff keine Entscheidung im Namen des Ideengebers.
- Triff keine Architektur-, Technologie- oder Umsetzungsentscheidung.
- Setze keine wesentliche Annahme stillschweigend als entschieden voraus.
- Verlange keine Entscheidung, wenn tatsächlich weitere Untersuchung statt
  einer Auswahl erforderlich ist.
- Ändere den Dokumentstatus nur entsprechend `rules/status.md` und dem
  Prüfergebnis.

## Abgrenzung zu swk-03

`swk-03` bewertet Befunde und dokumentiert die Bedeutung von Unterschieden,
Lücken, Risiken und offenen Punkten.

`swk-04` übernimmt ausschließlich die in der akzeptierten Bewertung erkannten
Entscheidungsbedarfe und strukturiert sie als Entscheidungsfragen.

`swk-04` bewertet die vorhandenen Alternativen nicht erneut und erweitert die
Bewertung nicht um neue Kriterien.

Eine Aussage wie "Alternative A ist hinsichtlich Aspekt X durch Befund Y
besser belegt als Alternative B" gehört, sofern durch die Befunde gedeckt, in
`swk-03`.

Eine Frage wie "Welche der dokumentierten Alternativen soll für den weiteren
Entwurf zugrunde gelegt werden?" gehört in `swk-04`, sofern die Auswahl nach
`swk-03` tatsächlich erforderlich ist.

## Ergebnis

Ergebnis ist eine projektspezifische `questions.md`.

Sie enthält mindestens:

- die verwendete Entscheidungsgrundlage,
- alle bestätigten Entscheidungsbedarfe,
- je Entscheidungsbedarf eine gültige `que-nnn`-Kennung,
- Bezug zur `assessment.md`,
- dokumentierte Optionen,
- bekannte entscheidungsrelevante Vor- und Nachteile beziehungsweise
  Einschränkungen,
- offene entscheidungsrelevante Sachverhalte,
- Abhängigkeiten zwischen Entscheidungen,
- gegebenenfalls Rückkehr- oder Klärungsbedarf,
- das Prüfergebnis für `swk-04`.

## Abschlusskriterien

`swk-04` ist abgeschlossen, wenn:

- jede Entscheidungsfrage aus der akzeptierten `assessment.md` hergeleitet ist,
- keine bloße Wissenslücke fälschlich als Entscheidungsfrage behandelt wurde,
- jede Entscheidungsfrage klar abgegrenzt ist,
- alle dokumentierten Optionen auf akzeptierte Vorphasenergebnisse
  zurückgeführt werden können,
- keine Option erfunden oder bevorzugt wurde,
- relevante unbekannte Sachverhalte sichtbar geblieben sind,
- Abhängigkeiten zwischen Entscheidungsfragen dokumentiert sind,
- keine Entscheidung durch die KI getroffen wurde,
- keine neue Anforderung erfunden wurde,
- die Qualitätsgrenze für `swk-04` erfüllt ist,
- die projektspezifische `questions.md` den Status `accepted` erhalten hat.
