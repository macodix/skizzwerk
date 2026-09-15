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

### Spätere Phasen

Die Prozessübersicht nennt anschließend:

- `swk-03`: Befunde bewerten,
- `swk-04`: Entscheidungsfragen erstellen.

Die konkrete Bearbeitung dieser Phasen beginnt erst, nachdem ihre
Phasendateien, Vorlagen und Qualitätsgrenzen definiert wurden.

## Trennung von Untersuchung und Bewertung

Die Bestandsuntersuchung in `swk-02` beantwortet Fragen wie:

- Was ist vorhanden?
- Was wird dokumentiert behauptet?
- Was wurde unmittelbar nachgewiesen?
- Welche Quellen widersprechen sich?
- Was wurde nicht oder nur teilweise untersucht?
- Was bleibt unbekannt?

Die spätere Bewertung beantwortet andere Fragen:

- Welcher Befund ist für das Projekt geeignet?
- Welche Vor- und Nachteile bestehen?
- Welche Lücken sind wesentlich?
- Welche Alternative soll weiterverfolgt werden?

Diese Trennung verhindert, dass eine gefundene Möglichkeit bereits während
der Recherche stillschweigend zur bevorzugten Lösung wird.

## Zentrale Schutzmechanismen

### Originalaussagen

Aussagen des Ideengebers werden von Interpretationen und externen Befunden
getrennt. Die KI darf Originalaussagen nicht überschreiben oder nachträglich
als eigene Ableitung darstellen.

### Annahmen

`rules/assumptions.md` verhindert, dass unbestätigte Annahmen als Tatsachen
oder Anforderungen behandelt werden.

Unbekannte Sachverhalte sind nicht automatisch Annahmen. Eine Annahme entsteht
erst, wenn eine unbestätigte Aussage als vorläufige Arbeitsgrundlage verwendet
werden soll.

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
| `review` | Bearbeitung und interne Prüfung sind abgeschlossen. |
| `accepted` | Der Ideengeber hat den Inhalt ausdrücklich bestätigt. |
| `blocked` | Eine wesentliche Information oder Entscheidung fehlt. |
| `superseded` | Das Dokument wurde durch eine neue Fassung ersetzt. |

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

## Beispielaufträge

Beispielprompts für die Ausführung und Prüfung einzelner Phasen stehen in
`docs/prompt-examples.md`.

Die Prompts sind Hilfsmittel. Verbindlich bleiben die jeweils referenzierten
Phasen-, Regel- und Vorlagendateien.

## Maschinenlesbare Ergebnisse und automatische Prüfung

Freie Markdown-Bearbeitung kann formale Fehler wie beschädigte Tabellen,
uneinheitliche Kennungen und Abweichungen zwischen Übersichten und
Einzelangaben erzeugen.

Für `swk-02` werden Befunde deshalb strukturiert in `inventory.json`
gespeichert. `inventory.md` wird automatisch daraus erzeugt.

Ein Validator und die GitHub-CI prüfen alle deterministisch prüfbaren Regeln.
Eine unabhängige inhaltliche Prüfung bleibt für semantische Aussagen
erforderlich.

Das Verfahren ist in `docs/structured-inventories.md` beschrieben.
