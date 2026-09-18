# Grundkonzept von skizzwerk

## Ziel

skizzwerk unterstützt die strukturierte Entwicklung einer groben Idee zu
einem nachvollziehbaren und belastbaren Softwaredesign.

Der Workflow soll typische Fehler KI-gestützter Entwicklungsprozesse
verringern:

- unbelegte Behauptungen,
- verdeckte Annahmen,
- vorzeitige technische Entscheidungen,
- widersprüchliche Anforderungen,
- Verlust bereits getroffener Entscheidungen,
- Vermischung von Untersuchung und Bewertung,
- vorschnelle Fertigmeldungen.

Dass skizzwerk diese Fehler tatsächlich verringert, ist noch nicht
nachgewiesen. Dies wird anhand von Pilotprojekten untersucht.

## Verbindliche Grundlage

Die verbindlichen Prozessbestandteile befinden sich in:

- `phases/`: Arbeitsauftrag und Grenzen der einzelnen Phasen,
- `rules/`: phasenübergreifende Regeln,
- `templates/`: Vorlagen für projektspezifische Ergebnisdokumente,
- `pilots/`: Dokumente der Pilotprojekte.

`rules/process.md` definiert die Phasenfolge und die Voraussetzungen für
Phasenübergänge.

Die Dokumente unter `docs/` erläutern den Prozess. Bei einem Widerspruch sind
die Dateien unter `phases/`, `rules/` und `templates/` maßgeblich.

## Phasenprinzip

Jede Phase besitzt:

- einen abgegrenzten Zweck,
- definierte Eingaben,
- einen verbindlichen Arbeitsauftrag,
- ausdrücklich ausgeschlossene Tätigkeiten,
- ein oder mehrere Ergebnisdokumente,
- eine Qualitätsgrenze,
- einen dokumentierten Status.

Eine Phase darf keine Aufgaben späterer Phasen stillschweigend vorwegnehmen.

## Aktueller Phasenablauf

### swk-01: Idee aufnehmen

Die ursprüngliche Projektidee wird erfasst und strukturiert.

Dabei werden:

- Originalaussagen unverändert bewahrt,
- Ziel und erwarteter Nutzen als Interpretation gekennzeichnet,
- genannte Funktionen und Einschränkungen erfasst,
- Mehrdeutigkeiten sichtbar gemacht,
- Annahmen und unbekannte Sachverhalte getrennt.

In `swk-01` findet noch keine Bestandsrecherche statt. Es werden keine neuen
Anforderungen, technischen Lösungen oder Architekturentscheidungen erzeugt.

Ergebnis ist die projektspezifische `idea.md`.

### swk-02: Bestand untersuchen

Der für die akzeptierte Projektidee relevante vorhandene Bestand wird
systematisch untersucht.

Dabei werden:

- der Untersuchungsumfang aus der akzeptierten `idea.md` abgeleitet,
- Quellen und Fundstellen nachvollziehbar dokumentiert,
- Befunde mit `evd-nnn`-Kennungen erfasst,
- Aussagen nach ihrer Herkunft und Belastbarkeit klassifiziert,
- Widersprüche und unbekannte Sachverhalte sichtbar gemacht,
- nicht oder nur teilweise untersuchte Bereiche dokumentiert,
- Grenzen der Aussagekraft festgehalten.

`swk-02` beschreibt den Bestand. Die Phase bewertet noch nicht, welche
Lösung geeignet oder vorzuziehen ist.

Ergebnis ist die projektspezifische `inventory.md`.

### swk-03: Befunde bewerten

Die akzeptierten Befunde aus `swk-02` werden hinsichtlich ihrer Bedeutung für
die akzeptierte Projektidee bewertet.

Dabei werden:

- Bewertungsaspekte aus der `idea.md` abgeleitet,
- relevante `evd-nnn`-Befunde den Bewertungsaspekten zugeordnet,
- positive Beiträge und Einschränkungen aus der Befundlage abgeleitet,
- vorhandene Alternativen sachbezogen gegenübergestellt,
- wesentliche unbekannte oder nicht ausreichend untersuchte Sachverhalte
  sichtbar gehalten,
- Nachweisgrenzen sichtbar gehalten,
- relevante `asm-nnn` mit wesentlicher Auswirkung auf möglichen
  Entscheidungsbedarf geprüft,
- notwendige Rückkehrpunkte zu `swk-02` erkannt,
- Anforderungsklärungen von echten Entscheidungsbedarfen getrennt,
- echte spätere Entscheidungsbedarfe als `dnd-nnn` benannt.

`swk-03` recherchiert keinen neuen Bestand und trifft noch keine Auswahl einer
bevorzugten Lösung, Architektur-, Technologie- oder Umsetzungsentscheidung.

Solange ein erforderlicher Rückkehrpunkt zu `swk-02` offen ist, ist swk-03
nicht review-fähig. Eine fehlende praktische Prüfung ist jedoch nicht allein
schon ein Rückkehrgrund, wenn dafür zunächst neue erhebliche Test-, Integrations-
oder Prüfinfrastruktur entworfen oder aufgebaut werden müsste.

Ergebnis ist die projektspezifische `assessment.md`.

### swk-04: Entscheidungsfragen erstellen

Die in der akzeptierten Bewertung aus `swk-03` dokumentierten `dnd-nnn`
werden als klar abgegrenzte `que-nnn` strukturiert.

Dabei werden:

- Entscheidungsbedarf von bloßen Wissenslücken und Anforderungsklärungen getrennt,
- dokumentierte Optionen den jeweiligen Entscheidungsfragen zugeordnet,
- bekannte Vor- und Nachteile beziehungsweise Einschränkungen aus `swk-03`
  übernommen,
- gegebenenfalls zugehörige `asm-nnn` referenziert,
- entscheidungsrelevante unbekannte Sachverhalte sichtbar gehalten,
- Abhängigkeiten zwischen Entscheidungen dokumentiert,
- notwendiger Rückkehr- oder weiterer Klärungsbedarf erkannt.

`swk-04` erweitert die Bewertung aus `swk-03` nicht und trifft keine
Entscheidung im Namen des Ideengebers.

Ergebnis ist die projektspezifische `questions.md`.

## Trennung von Untersuchung, Bewertung, Klärung und Entscheidungsfragen

Die Bestandsuntersuchung in `swk-02` beantwortet Fragen wie:

- Was ist vorhanden?
- Was wird dokumentiert behauptet?
- Was wurde unmittelbar nachgewiesen?
- Welche Quellen widersprechen sich?
- Was wurde nicht oder nur teilweise untersucht?
- Was bleibt unbekannt?

Die Bewertung in `swk-03` beantwortet Fragen wie:

- Welche Befunde sind für die Projektidee wesentlich?
- Welche vorhandenen Grundlagen tragen zu genannten Funktionen und Einschränkungen bei?
- Welche belegten Einschränkungen und Risiken bestehen?
- Welche Unterschiede zwischen Alternativen sind für spätere Entscheidungen relevant?
- Welche Wissenslücken verhindern eine belastbare Bewertung?
- Welche offenen Punkte benötigen eine Präzisierung der Projektidee?
- Welche Punkte benötigen tatsächlich eine spätere Auswahl, Festlegung oder ausdrückliche Bestätigung?
- Welche Aussagen bleiben mangels praktischer Prüfung nur dokumentiert oder unbekannt?

`swk-03` darf die Bedeutung dokumentierter Unterschiede bewerten, aber keine
Alternative als verbindliche Lösung auswählen.

Eine Anforderungsklärung ist keine Entscheidungsfrage. Sie dient dazu, eine
bereits vorhandene, aber unklare oder unvollständige Aussage der Projektidee
durch den Ideengeber zu präzisieren. Jede Anforderungsklärung erhält eine
`clr-nnn`-Kennung und wird in der projektspezifischen `clarifications.md`
dokumentiert. Die Antwort bleibt als `USER_PROVIDED` von Befunden, Ableitungen
und Annahmen unterscheidbar. Erst wenn danach eine echte Auswahl oder Festlegung
erforderlich bleibt, entsteht ein `dnd-nnn`.

Eine normale Präzisierung verändert die akzeptierte `idea.md` nicht. Sie ergänzt
ihre Aussage nachvollziehbar über `clr-nnn`; anschließend werden die betroffenen
Teile von `assessment.md` und die Qualitätsgrenze von swk-03 erneut geprüft.
Widerspricht eine Antwort der akzeptierten Idee oder verändert sie den
Projektgegenstand materiell, greift dagegen der Änderungslebenszyklus für den
betroffenen früheren Prozessstand.

### Nachweisgrenzen und spätere Verifikation

skizzwerk dient in den frühen Phasen der Entwicklung einer Idee zu einer
belastbaren Spezifikation beziehungsweise einem belastbaren Softwaredesign.
Deshalb darf der Prozess nicht stillschweigend verlangen, dass bereits vor der
Spezifikation umfangreiche Implementierungs-, Integrations- oder
Abnahmeinfrastruktur aufgebaut wird.

Eine fehlende praktische Funktions-, Integrations- oder Kompatibilitätsprüfung
bleibt als Nachweisgrenze sichtbar. Sie erzeugt nur dann einen Rückkehrpunkt zu
`swk-02`, wenn die Prüfung mit vorhandenen oder mit vertretbarem Aufwand
zugänglichen Quellen beziehungsweise bereits vorhandenen Prüfmöglichkeiten
möglich und für die Bewertung wesentlich ist.

Müsste für die Prüfung erst neue erhebliche Test-, Integrations- oder
Prüfinfrastruktur entworfen oder aufgebaut werden, ist dies kein automatischer
Rückkehrgrund. Die fehlende praktische Bestätigung wird dokumentiert und einer
späteren geeigneten Phase für Umsetzung, Verifikation oder Abnahme zugeordnet.

Damit bleibt beispielsweise zulässig, eine vorhandene Komponente auf Basis von
Code, Dokumentation und bekannten Einschränkungen als mögliche Grundlage zu
bewerten, ohne ihre tatsächliche Funktionsfähigkeit zu behaupten. Die spätere
Spezifikation kann anschließend festlegen, welche Testumgebung und welche
Abnahmekriterien für die Umsetzung benötigt werden.

`swk-04` beantwortet andere Fragen:

- Welche `dnd-nnn` sollen als konkrete `que-nnn` formuliert werden?
- Welche bereits dokumentierten Optionen gehören zu dieser Entscheidung?
- Welche entscheidungsrelevanten Informationen sind bekannt oder unbekannt?
- Welche Entscheidungen hängen voneinander ab?
- Muss vor einer Entscheidung noch untersucht oder geklärt werden?

`swk-04` strukturiert den Entscheidungsbedarf, trifft die Entscheidung aber
nicht selbst.

Eine Wissenslücke ist nicht allein deshalb eine Entscheidungsfrage. Ist eine
fehlende Information durch weitere Bestandsuntersuchung klärbar, wird der
Rückkehrbedarf dokumentiert. Eine bereits akzeptierte Vorphase wird dabei
nicht stillschweigend geändert; ihre Überarbeitung folgt den Regeln in
`rules/process.md` und durchläuft erneut Qualitätsprüfung und menschliche
Freigabe.

Diese Trennung verhindert, dass eine gefundene Möglichkeit bereits während
der Recherche oder Bewertung stillschweigend zur verbindlichen Lösung wird
oder eine KI aus einer Entscheidungsfrage selbst eine Entscheidung macht.

## Zentrale Schutzmechanismen

### Originalaussagen

Aussagen des Ideengebers werden von Interpretationen und externen Befunden
getrennt. Die KI darf Originalaussagen nicht überschreiben oder nachträglich
als eigene Ableitung darstellen.

### Anforderungsklärungen

`rules/clarifications.md` trennt spätere Präzisierungen durch den Ideengeber von
Wissenslücken, Annahmen und Entscheidungen. `clarifications.md` enthält
vollständige Frage, Antwort, Herkunft und Rückwirkung; `assessment.md`
referenziert die jeweilige `clr-nnn`.

Diese Datei ist kein allgemeines Fragenprotokoll. Wissenslücken, Annahmen und
Entscheidungen bleiben in ihren eigenen Prozessmechanismen.

### Annahmen

`rules/assumptions.md` verhindert, dass unbestätigte Annahmen als Tatsachen
oder Anforderungen behandelt werden.

Unbekannte Sachverhalte sind nicht automatisch Annahmen. Eine Annahme entsteht
erst, wenn eine unbestätigte Aussage als vorläufige Arbeitsgrundlage verwendet
werden soll.

Annahmen mit wesentlicher Auswirkung können Entscheidungsbedarf erzeugen. Sie
werden in `assumptions.md` verwaltet und bei Bedarf über ihre `asm-nnn`-Kennung
in `assessment.md` und `questions.md` referenziert. Sie werden dadurch weder
zu Befunden noch zu Tatsachen.

### Entscheidungsbedarf und Entscheidungsfragen

Ein in `swk-03` festgestellter echter Entscheidungsbedarf erhält eine
`dnd-nnn`-Kennung. Diese Kennung bedeutet nur, dass später etwas entschieden
werden muss.

`rules/questions.md` enthält die phasenübergreifenden Regeln für
Entscheidungsfragen.

Eine `que-nnn` dokumentiert in `swk-04`, was zu einem `dnd-nnn` konkret
entschieden werden muss. Sie ist keine Entscheidung und darf weder eine
bevorzugte Option vorgeben noch eine reine Wissenslücke oder
Anforderungsklärung in eine Auswahlfrage umdeuten.

Die eigentliche Entscheidung wird erst in einer später dafür definierten
Phase als `dec-nnn` dokumentiert. Diese spätere Entscheidungsphase ist im
aktuellen Prozessstand noch nicht definiert.

### Nachweise

`rules/evidence.md` legt fest, wie Aussagen nach Herkunft und Belastbarkeit
klassifiziert werden.

Verbindliche Nachweisstatus sind:

| Status | Bedeutung |
|---|---|
| `USER_PROVIDED` | Aussage stammt vom Ideengeber oder Auftraggeber. |
| `VERIFIED` | Aussage wurde unmittelbar durch Code, Test, Messung oder Primärquelle bestätigt. |
| `DOCUMENTED` | Aussage ist dokumentiert, wurde aber nicht praktisch bestätigt. |
| `INFERRED` | Aussage wurde nachvollziehbar aus anderen Befunden abgeleitet. |
| `ASSUMED` | Aussage wird vorläufig angenommen, besitzt aber keinen ausreichenden Nachweis. |
| `UNKNOWN` | Es liegt keine ausreichende Information vor. |
| `CONFLICT` | Verfügbare Quellen oder Befunde widersprechen sich. |
| `DISPROVED` | Aussage wurde durch einen belastbaren Gegenbeleg widerlegt. |

Die sprachliche Sicherheit einer Aussage darf ihre tatsächliche
Belegbarkeit nicht überschreiten.

### Qualitätsgrenzen

`rules/quality-gates.md` bestimmt, wann ein Phasenergebnis den Status `review`
erhalten darf.

Ein vollständig ausgefülltes Dokument besteht die Qualitätsgrenze nicht
automatisch. Entscheidend ist, ob alle inhaltlichen Kriterien erfüllt sind.

Für `swk-03` gilt zusätzlich: Ein dokumentierter erforderlicher Rückkehrpunkt
zu `swk-02` verhindert den Status `review`, solange er offen ist. Eine bloße
Nachweisgrenze verhindert `review` dagegen nicht, wenn sie korrekt dokumentiert
ist und keine mit vertretbarem Aufwand noch ausstehende Bestandsuntersuchung
verbirgt.

### Menschliche Freigabe

Die KI darf ein Dokument nach bestandener Qualitätsgrenze auf `review`
setzen.

Der Status `accepted` benötigt eine ausdrückliche menschliche Bestätigung.
Erst danach erfolgt der reguläre Übergang in die nächste Phase.

### Nachvollziehbare Änderungen

Eine spätere Phase darf akzeptierte Ergebnisse einer früheren Phase nicht
stillschweigend verändern.

Wird ein akzeptiertes Ergebnis überarbeitet, muss die neue Fassung erneut
geprüft und menschlich bestätigt werden. Die bisherige Fassung bleibt
nachvollziehbar erhalten.

## Dokumentstatus

Die verbindlichen Statuswerte stehen in `rules/status.md`.

| Status | Bedeutung im Prozess |
|---|---|
| `input` | Die Eingabe wurde erfasst, aber noch nicht bearbeitet. |
| `draft` | Das Dokument wird bearbeitet oder weist noch Mängel auf. |
| `review` | Bearbeitung und interne Prüfungen sind abgeschlossen. |
| `accepted` | Der Ideengeber hat den Inhalt ausdrücklich bestätigt. |
| `blocked` | Die Bearbeitung kann wegen einer wesentlichen fehlenden Information oder Entscheidung nicht fortgesetzt werden. |
| `superseded` | Das Dokument wurde durch eine neuere Fassung ersetzt. |

## Grenzen der Schutzmechanismen

Die Regeln allein belegen noch keine Qualitätsverbesserung.

Die Pilotprojekte müssen zeigen:

- ob die KI alle Regeln berücksichtigt,
- ob sie die Regeln konsistent anwendet,
- ob Regelverstöße zuverlässig erkannt werden,
- ob die Trennung der Phasen praktisch funktioniert,
- ob die Ergebnisse für den Ideengeber nachvollziehbar bleiben,
- ob zusätzliche unabhängige Prüfungen notwendig sind,
- ob der Workflow mehr Zeit spart als verursacht.

## Pilotbefunde aus openclaw-xmpp

Der erste praktische Durchlauf von `swk-03` am Pilot `openclaw-xmpp` hat
mehrere konkrete Prozessprobleme sichtbar gemacht:

- offene Rückkehrpunkte waren mit dem Status `review` nicht eindeutig
  ausgeschlossen,
- die Vorlage für Alternativen skalierte nur auf zwei Alternativen,
- die Vorprüfung war nur als Gesamtwert dokumentierbar,
- die Abgrenzung zwischen Anforderungsklärung und Entscheidungsbedarf war
  nicht ausreichend explizit,
- für den in `swk-03` festgestellten Entscheidungsbedarf fehlte eine definierte
  Kennungsart,
- die Vorprüfung formulierte unklar, welche Kennungen zu prüfen sind,
- `rules/questions.md` war in `swk-03` nicht als Eingabe referenziert,
- die zunächst verwendete Rückkehrregel konnte umfangreiche praktische Tests
  und damit den Aufbau neuer Testinfrastruktur bereits während der
  Spezifikationsarbeit erzwingen,
- für in swk-03 erkannte Anforderungsklärungen fehlten Kennung, dauerhaftes
  Projektdokument, Antwortlebenszyklus und definierte Rückwirkung auf die
  Bewertung.

Die ersten Punkte wurden als Prozessänderungen übernommen. Für den letzten Punkt
wurde die Grenze zwischen Bestandsuntersuchung und späterer praktischer
Verifikation präzisiert: Neue erhebliche Test-, Integrations- oder
Prüfinfrastruktur ist kein automatischer Bestandteil von swk-02 oder swk-03.
Für Anforderungsklärungen wurde ein eigener `clr-nnn`-Lebenszyklus eingeführt,
der `idea.md`, Wissenslücken, Annahmen und Entscheidungen getrennt hält.

Der Pilot zeigte außerdem, dass bei einer umfangreichen `assessment.md` formale
Vollständigkeitsfehler bei Befundreferenzen ohne zusätzliche Prüfung leicht
unentdeckt bleiben können. Ob daraus eine strukturierte Quelldatei und ein
Validator für `swk-03` entstehen sollen, bleibt eine ausdrücklich noch zu
prüfende Prozessänderung.
