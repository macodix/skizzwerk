# Beispiele für KI-Aufträge

## Zweck

Diese Datei enthält Beispielprompts für die Vorbereitung, Ausführung und
Prüfung von skizzwerk-Phasen.

Die Prompts sind nicht verbindlich. Maßgeblich sind die jeweils genannten
Dateien unter `phases/`, `rules/` und `templates/`.

Projektpfade und Phasenkennungen müssen an das jeweilige Vorhaben angepasst
werden.

## Prozessgrundlage einer Phase prüfen

Dieser Auftrag prüft, ob eine Phase ausführbar vorbereitet ist. Die Phase
selbst wird noch nicht ausgeführt.

```text
Wir bereiten swk-02 für den Pilot openclaw-xmpp vor.

Das verbindliche Repository ist:
https://github.com/macodix/skizzwerk

Prüfe zunächst, ob alle für swk-02 benötigten Phasen-, Regel- und
Vorlagendateien vorhanden, widerspruchsfrei und ausreichend definiert sind.

Verfolge alle Referenzen aus der Phasendatei zu den zugehörigen Regeln und
Vorlagen.

Führe swk-02 noch nicht aus und ändere keine Dateien.

Nenne jede festgestellte Lücke mit:
- genauer Datei,
- Überschrift oder Einfügestelle,
- konkreter Begründung,
- Auswirkung auf die Ausführbarkeit der Phase.

Trenne nachgewiesene Mängel von Sachverhalten, deren Notwendigkeit ohne
weitere Prozessentscheidung noch unbekannt ist.
```

## Phase swk-01 starten

```text
Führe die Phase swk-01 nach `phases/swk-01-idea.md` für
`pilots/openclaw-xmpp` aus.

Führe zuerst die in der Phasendatei vorgeschriebene Vorprüfung aus.

Wenn die Vorprüfung scheitert:
- bearbeite keine projektspezifische Ergebnisdatei,
- nenne jeden Mangel mit Datei und Fundstelle,
- beende die Ausführung von swk-01.

Wenn die Vorprüfung besteht:
- beachte alle referenzierten Regeln,
- verwende `templates/idea.md`,
- bearbeite die vorhandene projektspezifische `idea.md`,
- bewahre die Abschnitte `1. Originalbeschreibung` und
  `2. Herkunft und Kontext` inhaltlich unverändert,
- führe abschließend die Qualitätsprüfung für swk-01 durch.

Erfinde keine Anforderungen, Annahmen oder technischen Lösungen.
```

## Ergebnis von swk-01 prüfen

Dieser Auftrag prüft das vorhandene Ergebnis, ohne es zu verändern.

```text
Prüfe das Ergebnis von swk-01 für `pilots/openclaw-xmpp`.

Verwende als verbindliche Grundlage:
- `phases/swk-01-idea.md`,
- alle dort referenzierten Regeln,
- `templates/idea.md`,
- die Qualitätsgrenze für swk-01 in `rules/quality-gates.md`.

Verändere keine Datei.

Nenne jeden festgestellten Mangel mit:
- Datei,
- genauer Überschrift oder Textstelle,
- verletzter Regel oder nicht erfülltem Qualitätskriterium,
- konkreter Begründung.

Trenne eindeutig zwischen:
- nachgewiesenem Regelverstoß,
- möglichem Widerspruch,
- unbekanntem Sachverhalt,
- rein redaktionellem Hinweis.

Nenne abschließend, ob der Status `review` nach den verbindlichen Regeln
zulässig ist.
```

## Festgestellte Mängel in swk-01 korrigieren

```text
Korrigiere die zuvor festgestellten Mängel im Ergebnis von swk-01 für
`pilots/openclaw-xmpp`.

Ändere ausschließlich die zuvor benannten Stellen.

Beachte:
- Die Abschnitte `1. Originalbeschreibung` und
  `2. Herkunft und Kontext` bleiben inhaltlich unverändert.
- Es werden keine neuen Anforderungen ergänzt.
- Es werden keine Annahmen als Tatsachen dargestellt.
- Es wird keine technische Lösung oder Architektur festgelegt.

Prüfe das Ergebnis danach erneut vollständig gegen die Qualitätsgrenze für
swk-01.

Dokumentiere:
- welche Stellen geändert wurden,
- welches Qualitätskriterium damit erfüllt wurde,
- welche Mängel gegebenenfalls bestehen bleiben.

Setze den Status nur entsprechend `rules/status.md`.
Setze den Status niemals selbstständig auf `accepted`.
```

## Menschliche Freigabe von swk-01 dokumentieren

Dieser Auftrag setzt eine bereits ausdrücklich erteilte Freigabe um. Die KI
darf die Freigabe nicht selbst erzeugen oder unterstellen.

```text
Ich habe die projektspezifische `idea.md` für `pilots/openclaw-xmpp`
inhaltlich geprüft und bestätige sie ausdrücklich.

Prüfe vor der Änderung:
- ob das Dokument den Status `review` besitzt,
- ob das dokumentierte Prüfergebnis die Qualitätsgrenze für swk-01 als
  bestanden ausweist.

Wenn beide Voraussetzungen erfüllt sind:
- setze den Dokumentstatus auf `accepted`,
- aktualisiere das Änderungsdatum,
- dokumentiere meine Freigabe im Abschnitt `Freigabestatus`.

Nimm keine weiteren inhaltlichen Änderungen vor.

Wenn eine Voraussetzung nicht erfüllt ist, ändere keine Datei und nenne den
konkreten Hinderungsgrund.
```

## Phase swk-02 starten

```text
Führe die Phase swk-02 nach `phases/swk-02-inventory.md` für
`pilots/openclaw-xmpp` aus.

Führe zuerst die in der Phasendatei vorgeschriebene Vorprüfung aus.

Wenn die Vorprüfung scheitert:
- lege keine projektspezifische `inventory.md` an,
- verändere keine projektspezifische Ergebnisdatei,
- nenne jeden Mangel mit Datei und Fundstelle,
- beende die Ausführung von swk-02.

Wenn die Vorprüfung besteht:
- lies die vollständige akzeptierte projektspezifische `idea.md`,
- leite den Untersuchungsumfang ausschließlich daraus ab,
- beachte alle von `phases/swk-02-inventory.md` referenzierten Regeln,
- verwende `templates/inventory.json`,
- untersuche den relevanten vorhandenen Bestand,
- dokumentiere alle Quellen reproduzierbar,
- erfasse jeden relevanten Befund mit einer gültigen `evd-nnn`-Kennung,
- verwende die Nachweisstatus aus `rules/evidence.md`,
- dokumentiere nicht oder nur teilweise untersuchte Bereiche,
- speichere die verbindlichen Befunddaten in der projektspezifischen
  `inventory.json`,
- führe `python tools/inventory.py validate pilots/openclaw-xmpp/inventory.json`
  aus,
- erzeuge `inventory.md` mit
  `python tools/inventory.py render pilots/openclaw-xmpp/inventory.json pilots/openclaw-xmpp/inventory.md`,
- führe danach
  `python tools/inventory.py check pilots/openclaw-xmpp/inventory.json pilots/openclaw-xmpp/inventory.md`
  aus,
- führe abschließend die Qualitätsprüfung für swk-02 durch.

Trenne eindeutig zwischen:
- Aussagen des Ideengebers,
- nachgewiesenen Tatsachen,
- dokumentierten Behauptungen,
- Ableitungen,
- Annahmen,
- unbekannten Sachverhalten,
- widersprüchlichen oder widerlegten Aussagen.

Bewerte oder bevorzuge keine gefundene Lösung.
Formuliere keine neuen Anforderungen.
Triff keine Architektur- oder Technologieentscheidung.
Verändere keine untersuchten externen Systeme oder Repositories.

Setze den Dokumentstatus nur entsprechend dem Prüfergebnis.
Setze den Status niemals selbstständig auf `accepted`.
```

## Ergebnis von swk-02 prüfen

Dieser Auftrag prüft die Bestandsuntersuchung, ohne sie zu verändern oder
fortzusetzen.

```text
Prüfe das Ergebnis von swk-02 für `pilots/openclaw-xmpp`.

Verwende als verbindliche Grundlage:
- `phases/swk-02-inventory.md`,
- alle dort referenzierten Regeln,
- `templates/inventory.json`,
- `tools/inventory.py`,
- die Qualitätsgrenze für swk-02 in `rules/quality-gates.md`.

Verändere keine Datei.
Führe keine zusätzliche Bestandsrecherche durch.
Führe die automatische Prüfung mit
`python tools/inventory.py check pilots/openclaw-xmpp/inventory.json pilots/openclaw-xmpp/inventory.md`
aus.

Prüfe insbesondere:
- ob der Untersuchungsumfang vollständig aus der akzeptierten `idea.md`
  abgeleitet wurde,
- ob jeder Untersuchungsbereich einen konkreten Bezug zur `idea.md` besitzt,
- ob alle Quellen reproduzierbar angegeben sind,
- ob Nachweisstatus und tatsächliche Belegbarkeit übereinstimmen,
- ob Befundübersicht und Einzelbefunde vollständig und widerspruchsfrei sind,
- ob nicht durchgeführte Prüfungen und Grenzen sichtbar sind,
- ob unbekannte Sachverhalte nicht durch Annahmen ersetzt wurden,
- ob Bewertung, Lösungsauswahl und Architekturentscheidungen unterblieben sind.

Nenne jeden festgestellten Mangel mit:
- Datei,
- genauer Überschrift oder Befundkennung,
- verletzter Regel oder nicht erfülltem Qualitätskriterium,
- konkreter Begründung.

Trenne eindeutig zwischen:
- nachgewiesenem Regelverstoß,
- möglichem Widerspruch,
- unbekanntem Sachverhalt,
- rein redaktionellem Hinweis.

Nenne abschließend, ob der Status `review` nach den verbindlichen Regeln
zulässig ist.
```

## Festgestellte Mängel in swk-02 korrigieren

```text
Korrigiere die zuvor festgestellten Mängel im Ergebnis von swk-02 für
`pilots/openclaw-xmpp`.

Ändere ausschließlich die zuvor benannten Stellen.

Bearbeite ausschließlich die projektspezifische `inventory.json`.
Bearbeite `inventory.md` nicht direkt.

Führe zusätzliche Recherche nur durch, wenn sie zur Behebung eines konkret
benannten Mangels erforderlich ist. Dokumentiere dabei jede neue Quelle nach
`rules/evidence.md`.

Beachte weiterhin die Grenzen von `phases/swk-02-inventory.md`:
- keine neuen Anforderungen,
- keine Bewertung oder Rangfolge möglicher Lösungen,
- keine Auswahl einer technischen Grundlage,
- keine Architektur- oder Technologieentscheidung,
- keine stillschweigenden Annahmen.

Prüfe das Ergebnis danach erneut vollständig gegen die Qualitätsgrenze für
swk-02.

Validiere `inventory.json`, erzeuge `inventory.md` neu und prüfe anschließend,
dass beide Dateien übereinstimmen.

Dokumentiere:
- welche Stellen geändert wurden,
- welches Qualitätskriterium damit erfüllt wurde,
- welche Mängel gegebenenfalls bestehen bleiben.

Setze den Status nur entsprechend `rules/status.md`.
Setze den Status niemals selbstständig auf `accepted`.
```

## Menschliche Freigabe von swk-02 dokumentieren

```text
Ich habe die projektspezifische `inventory.md` für
`pilots/openclaw-xmpp` geprüft und bestätige Untersuchungsumfang und
dokumentiertes Ergebnis ausdrücklich.

Prüfe vor der Änderung:
- ob das Dokument den Status `review` besitzt,
- ob das dokumentierte Prüfergebnis die Qualitätsgrenze für swk-02 als
  bestanden ausweist.

Wenn beide Voraussetzungen erfüllt sind:
- setze den Dokumentstatus auf `accepted`,
- aktualisiere das Änderungsdatum,
- dokumentiere meine Freigabe im Abschnitt `Freigabestatus`.

Nimm keine weiteren inhaltlichen Änderungen oder Nachforschungen vor.

Wenn eine Voraussetzung nicht erfüllt ist, ändere keine Datei und nenne den
konkreten Hinderungsgrund.
```

## Phase swk-03 starten

```text
Führe die Phase swk-03 nach `phases/swk-03-assessment.md` für
`pilots/openclaw-xmpp` aus.

Führe zuerst die in der Phasendatei vorgeschriebene Vorprüfung aus.

Wenn die Vorprüfung scheitert:
- lege keine projektspezifische `assessment.md` an,
- verändere keine projektspezifische Ergebnisdatei,
- nenne jeden Mangel mit Datei und Fundstelle,
- beende die Ausführung von swk-03.

Wenn die Vorprüfung besteht:
- lies die vollständige akzeptierte `idea.md`,
- lies die vollständige akzeptierte `inventory.json`,
- lies eine vorhandene projektspezifische `assumptions.md`,
- leite Bewertungsaspekte nur aus der `idea.md` ab,
- ordne jedem Bewertungsaspekt konkrete `evd-nnn`-Befunde zu,
- dokumentiere positive Beiträge, Einschränkungen, unbekannte Punkte und ihre
  Bedeutung für spätere Entscheidungen,
- prüfe relevante `asm-nnn` mit wesentlicher Auswirkung darauf, ob daraus
  Entscheidungsbedarf entsteht,
- vergleiche Alternativen nur auf derselben dokumentierten Befundgrundlage,
- prüfe wesentliche Lücken auf eine notwendige Rückkehr zu swk-02,
- verwende `templates/assessment.md`,
- führe abschließend die Qualitätsprüfung für swk-03 durch.

Führe keine neue Bestandsrecherche durch.
Formuliere keine neuen Anforderungen.
Verwende keine Rangfolge oder Gesamtnote ohne definierte Bewertungsmethode.
Wähle keine bevorzugte Lösung aus.
Triff keine Architektur-, Technologie- oder Umsetzungsentscheidung.
Setze keine Annahme stillschweigend als Bewertungsgrundlage.

Setze den Dokumentstatus nur entsprechend dem Prüfergebnis.
Setze den Status niemals selbstständig auf `accepted`.
```

## Pilotprompt swk-03: openclaw-xmpp mit Claude

Dieser Prompt ist für den ersten praktischen Test von `swk-03` am Pilot
`openclaw-xmpp` gedacht. Ziel ist sowohl ein fachliches `assessment.md` als
auch die Prüfung, ob die neue Phase in der Praxis ausreichend klar und
vollständig definiert ist.

```text
Wir testen die Phase swk-03 des skizzwerk-Prozesses am Pilotprojekt
`openclaw-xmpp`.

Verbindliches Repository:
https://github.com/macodix/skizzwerk

Arbeite auf dem Branch `swk-03-draft`.

Verbindliche Grundlage sind insbesondere:
- `phases/swk-03-assessment.md`,
- `rules/process.md`,
- `rules/evidence.md`,
- `rules/assumptions.md`,
- `rules/questions.md`,
- `rules/identifiers.md`,
- `rules/status.md`,
- die Qualitätsgrenze für swk-03 in `rules/quality-gates.md`,
- `templates/assessment.md`,
- `pilots/openclaw-xmpp/idea.md`,
- `pilots/openclaw-xmpp/inventory.json`,
- die daraus erzeugte `pilots/openclaw-xmpp/inventory.md`,
- eine projektspezifische `pilots/openclaw-xmpp/assumptions.md`, falls sie existiert.

Führe zuerst ausschließlich die Vorprüfung aus, die in
`phases/swk-03-assessment.md` vorgeschrieben ist.

Wenn die Vorprüfung scheitert:
- lege keine `assessment.md` an und verändere keine projektspezifische Datei,
- nenne für jeden Mangel die genaue Datei und Fundstelle,
- nenne die verletzte Regel oder fehlende Voraussetzung,
- beende die Ausführung von swk-03.

Wenn die Vorprüfung besteht, führe swk-03 vollständig aus.

Dabei gelten insbesondere folgende Grenzen:
- Keine neue Bestandsrecherche durchführen.
- Keine Befunde aus `inventory.json` verändern oder neu einstufen.
- Keine neuen Anforderungen formulieren.
- Keine unbekannten Sachverhalte durch Vermutungen ersetzen.
- Keine Annahme als Tatsache oder Befund behandeln.
- Keine neue Annahme stillschweigend setzen.
- Keine Architektur-, Technologie- oder Umsetzungsentscheidung treffen.
- Keine Alternative als bevorzugte oder verbindliche Lösung auswählen.
- Keine Rangfolge, Gewichtung, Gesamtnote oder numerischen Scores verwenden,
  sofern dafür keine ausdrücklich definierte Methode existiert.

Erstelle `pilots/openclaw-xmpp/assessment.md` nach
`templates/assessment.md`.

Für jeden Bewertungsaspekt:
- nenne den konkreten Bezug zur akzeptierten `idea.md`,
- nenne die verwendeten `evd-nnn`-Befunde,
- trenne feststellbare positive Beiträge von Einschränkungen und Nachteilen,
- halte `UNKNOWN`, nicht durchgeführte Prüfungen und Untersuchungsgrenzen sichtbar,
- kennzeichne über einzelne Befunde hinausgehende Aussagen als Ableitung,
- dokumentiere die Bedeutung für spätere Entscheidungen.

Prüfe zusätzlich vorhandene `asm-nnn` mit wesentlicher Auswirkung. Wenn daraus
Entscheidungsbedarf entsteht, referenziere die Annahme ausdrücklich im
entsprechenden später zu entscheidenden Punkt. Die Annahme bleibt weiterhin
in `assumptions.md` verwaltet.

Prüfe bei jeder wesentlichen Wissenslücke ausdrücklich:
1. Ist sie für die Bewertung wesentlich?
2. Kann sie durch weitere Bestandsuntersuchung geklärt oder genauer abgegrenzt werden?
3. Muss deshalb nach den Regeln zu swk-02 zurückgekehrt werden?

Dokumentiere einen Rückkehrpunkt nur, wenn alle Voraussetzungen aus
`phases/swk-03-assessment.md` erfüllt sind.

Führe am Ende die vollständige Qualitätsprüfung für swk-03 aus.
Setze `assessment.md` höchstens auf `review`; niemals selbstständig auf
`accepted`.

Da dies ein Pilotlauf der neuen Phase ist, erstelle zusätzlich KEINE neue
Prozessdatei und ändere KEINE Datei unter `phases/`, `rules/`, `templates/`
oder `docs/`.

Berichte stattdessen nach der fachlichen Bearbeitung separat über beobachtete
Prozessprobleme. Trenne dabei strikt:

A. Fachliches Ergebnis des Piloten
- Ergebnis und Status von `assessment.md`
- notwendige Rückkehrpunkte zu swk-02
- späterer Entscheidungsbedarf

B. Beobachtete Probleme der Phase swk-03
Für jedes Problem:
- betroffene Prozessdatei,
- genaue Überschrift oder Regel,
- beobachtetes Problem,
- konkrete Auswirkung während des Pilotlaufs,
- ob es sich um einen nachgewiesenen Widerspruch, eine Lücke, eine Unklarheit
  oder lediglich einen Verbesserungsvorschlag handelt.

Schlage Prozessänderungen nur vor. Führe sie während dieses Pilotlaufs nicht
aus.

Erfinde keine fehlenden Prozessregeln.
```

## Ergebnis von swk-03 prüfen

```text
Prüfe das Ergebnis von swk-03 für `pilots/openclaw-xmpp`.

Verwende als verbindliche Grundlage:
- `phases/swk-03-assessment.md`,
- alle dort referenzierten Regeln,
- `templates/assessment.md`,
- die Qualitätsgrenze für swk-03 in `rules/quality-gates.md`,
- die akzeptierte `idea.md`,
- die akzeptierte `inventory.json`,
- eine vorhandene projektspezifische `assumptions.md`.

Verändere keine Datei.
Führe keine zusätzliche Bestandsrecherche durch.

Prüfe insbesondere:
- ob jeder Bewertungsaspekt aus `idea.md` ableitbar ist,
- ob jede Bewertung auf konkret genannten `evd-nnn`-Befunden beruht,
- ob die Belastbarkeit der Bewertung die Befundlage nicht überschreitet,
- ob Annahmen und Befunde getrennt geblieben sind,
- ob relevante Annahmen mit wesentlicher Auswirkung auf Entscheidungsbedarf
  geprüft wurden,
- ob `UNKNOWN` und nicht durchgeführte Prüfungen sichtbar bleiben,
- ob Vergleiche dieselben relevanten Aspekte verwenden,
- ob keine Rangfolge, Gesamtnote oder bevorzugte Lösung ohne Prozessgrundlage
  erzeugt wurde,
- ob notwendige Rückkehrpunkte zu swk-02 erkannt wurden,
- ob Entscheidungsbedarf nur benannt und nicht bereits entschieden wurde.

Nenne jeden festgestellten Mangel mit:
- Datei,
- genauer Überschrift oder Bewertungsaspekt,
- verletzter Regel oder nicht erfülltem Qualitätskriterium,
- konkreter Begründung.

Nenne abschließend, ob der Status `review` nach den verbindlichen Regeln
zulässig ist.
```

## Festgestellte Mängel in swk-03 korrigieren

```text
Korrigiere ausschließlich die zuvor festgestellten Mängel in
`pilots/openclaw-xmpp/assessment.md`.

Führe keine neue Bestandsrecherche durch.
Ändere keine akzeptierte Vorphasendatei.
Ändere keine Prozessdatei.

Wenn ein Mangel nur durch eine Änderung von `idea.md`, `inventory.json`,
`assumptions.md` oder einer skizzwerk-Prozessdatei behoben werden kann,
ändere diese Datei nicht. Dokumentiere stattdessen die erforderliche Rückkehr
oder den Änderungsvorschlag.

Prüfe das korrigierte Ergebnis danach erneut vollständig gegen die
Qualitätsgrenze für swk-03.

Setze den Status höchstens auf `review` und niemals selbstständig auf
`accepted`.
```

## Menschliche Freigabe von swk-03 dokumentieren

```text
Ich habe die projektspezifische `assessment.md` für
`pilots/openclaw-xmpp` inhaltlich geprüft und bestätige sie ausdrücklich.

Prüfe vor der Änderung:
- ob `assessment.md` den Status `review` besitzt,
- ob das dokumentierte Prüfergebnis die Qualitätsgrenze für swk-03 als
  bestanden ausweist.

Wenn beide Voraussetzungen erfüllt sind:
- setze den Dokumentstatus auf `accepted`,
- aktualisiere das Änderungsdatum,
- dokumentiere meine Freigabe im Abschnitt `Freigabestatus`.

Nimm keine weitere inhaltliche Änderung vor.

Wenn eine Voraussetzung nicht erfüllt ist, ändere keine Datei und nenne den
konkreten Hinderungsgrund.
```
