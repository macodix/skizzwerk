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
- verwende `templates/inventory.md`,
- untersuche den relevanten vorhandenen Bestand,
- dokumentiere alle Quellen reproduzierbar,
- erfasse jeden relevanten Befund mit einer gültigen `evd-nnn`-Kennung,
- verwende die Nachweisstatus aus `rules/evidence.md`,
- dokumentiere nicht oder nur teilweise untersuchte Bereiche,
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
- `templates/inventory.md`,
- die Qualitätsgrenze für swk-02 in `rules/quality-gates.md`.

Verändere keine Datei.
Führe keine zusätzliche Bestandsrecherche durch.

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