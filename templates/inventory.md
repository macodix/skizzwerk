---
document: inventory
process_phase: swk-02
project: ""
status: input
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
basis: idea.md
---

> Legacy-Vorlage für noch nicht migrierte Bestandsuntersuchungen. Neue und
> überarbeitete Bestandsuntersuchungen verwenden `templates/inventory.json`.
> Die zugehörige `inventory.md` wird mit `tools/inventory.py` erzeugt und nicht
> direkt bearbeitet.

# Bestandsuntersuchung

## 1. Grundlage und Untersuchungsauftrag

- zugrunde liegende `idea.md`:
- Status der `idea.md`:
- bestätigte Fassung vom:
- Beginn der Untersuchung:
- Stand der Untersuchung:

Kurze Beschreibung, welcher Bestand untersucht wird.

## 2. Untersuchungsumfang

Die Untersuchungsbereiche müssen aus der akzeptierten `idea.md` abgeleitet
werden.

| Untersuchungsbereich | Bezug zur `idea.md` | Begründung der Relevanz | Untersuchung vorgesehen |
|---|---|---|---|
| | Abschnitt oder Originalaussage | | ja / nein |

Nicht in den Untersuchungsumfang aufgenommene Bereiche:

| Bereich | Begründung |
|---|---|
| | |

## 3. Durchgeführte Untersuchung

| Untersuchungsbereich | Tatsächlich untersucht | Nicht untersucht | Einschränkungen |
|---|---|---|---|
| | | | |

## 4. Quellen

Für die Quellenarten gilt `rules/evidence.md`.

### Quelle: Bezeichnung

- Quellenart:
- Herausgeber oder Verantwortlicher:
- Titel oder Bezeichnung:
- Fundstelle:
- Version, Commit oder Veröffentlichungsstand:
- Abruf- oder Prüfdatum:
- tatsächlich untersuchter Teil:
- Zugänglichkeit:
- erkannte Einschränkungen:

<!-- Diesen Abschnitt für jede verwendete Quelle wiederholen. -->

## 5. Befundübersicht

| Kennung | Aussage | Nachweisstatus | wichtigste Quelle |
|---|---|---|---|
| `evd-001` | | | |

## 6. Einzelbefunde

Für jeden relevanten Befund ist ein eigener Abschnitt anzulegen.

### evd-001

Aussage:

Nachweisstatus:

Begründung des Nachweisstatus:

Quellen:

| Quellenart | Fundstelle | Version oder Commit | Prüfdatum | Beitrag zum Befund |
|---|---|---|---|---|
| | | | | |

Bei mehreren verwendeten Quellen erhält jede Quelle eine eigene Tabellenzeile.

Für Befunde mit dem Status `CONFLICT` müssen mindestens zwei Quellen
dokumentiert werden.

Prüfung:

- durchgeführte Prüfung:
- Ergebnis:
- nicht durchgeführte Prüfung:
- Einschränkung der Aussagekraft:

Bezug zur Projektidee:

- Abschnitt oder Originalaussage:
- Bedeutung für die Bestandsuntersuchung:

Folgerung:

<!--
Die Folgerung darf nur beschreiben, was aus dem Befund für den festgestellten
Bestand folgt. Sie darf keine Anforderung, Bewertung, Lösungsauswahl oder
Architekturentscheidung enthalten.
-->

### Zusätzliche Angaben bei CONFLICT

- Aussage 1:
- Quelle von Aussage 1:
- Aussage 2:
- Quelle von Aussage 2:
- gemeinsamer Sachverhalt:
- Bezugszeitpunkt oder Gültigkeitszeitraum:
- Geltungsbereich:
- konkrete logische Unvereinbarkeit:

Diese Angaben werden nur bei einem Befund mit dem Status `CONFLICT`
ausgefüllt.


## 7. Widersprüche

In diesem Abschnitt werden Befunde mit dem Nachweisstatus `CONFLICT`
zusammengeführt.

| Betroffene Befunde | Gegenstand des Widerspruchs | Widersprechende Quellen | Notwendige weitere Prüfung |
|---|---|---|---|
| | | | |

Wenn keine Widersprüche festgestellt wurden:

> Keine Widersprüche festgestellt.

Diese Aussage bedeutet nur, dass während der durchgeführten Untersuchung keine
Widersprüche erkannt wurden.

## 8. Unbekannte Sachverhalte

Hier werden Befunde mit dem Nachweisstatus `UNKNOWN` zusammengeführt.

| Befund | Unbekannter Sachverhalt | Grund | Bedeutung für den weiteren Prozess |
|---|---|---|---|
| | | | |

Wenn keine unbekannten Sachverhalte festgestellt wurden:

> Keine unbekannten Sachverhalte festgestellt.

Diese Aussage gilt nur innerhalb des dokumentierten Untersuchungsumfangs.

## 9. Nicht oder nur teilweise untersuchte Bereiche

| Bereich | Nicht untersuchter Teil | Grund | Auswirkung auf die Aussagekraft |
|---|---|---|---|
| | | | |

Wenn alle vorgesehenen Bereiche vollständig untersucht wurden:

> Alle vorgesehenen Untersuchungsbereiche wurden innerhalb des festgelegten
> Untersuchungsumfangs bearbeitet.

## 10. Grenzen der Bestandsuntersuchung

- zeitliche Grenze:
- technische Grenze:
- nicht verfügbare Quellen:
- nicht mögliche Prüfungen:
- sonstige Einschränkungen:

## 11. Abgrenzung zu späteren Phasen

Diese Bestandsuntersuchung dokumentiert vorhandene Bestandteile, Aussagen,
Nachweise, Konflikte und unbekannte Sachverhalte.

Sie enthält keine:

- neuen Anforderungen,
- Rangfolge möglicher Lösungen,
- Auswahl eines Projekts oder einer Komponente,
- Architekturentscheidung,
- Technologieentscheidung,
- Umsetzungsplanung.

## 12. Prüfergebnis swk-02

### Vorprüfung

- [ ] Die projektspezifische `idea.md` existiert.
- [ ] Die `idea.md` besitzt den Status `accepted`.
- [ ] Alle von `phases/swk-02-inventory.md` referenzierten Dateien existieren.
- [ ] Keine benötigte Regel oder Vorlage ist leer oder unvollständig.
- [ ] Die Qualitätsgrenze für `swk-02` ist definiert.
- [ ] Verwendete Kennungen entsprechen `rules/identifiers.md`.

Ergebnis der Vorprüfung:

- Ergebnis: `offen`
- geprüft am:
- geprüft durch:
- festgestellte Mängel:

### Prüfung der Bestandsaufnahme

- [ ] Der Untersuchungsumfang wurde aus der akzeptierten `idea.md` abgeleitet.
- [ ] Jeder Untersuchungsbereich besitzt eine nachvollziehbare Begründung.
- [ ] Tatsächlich und nicht untersuchte Bereiche sind getrennt dokumentiert.
- [ ] Alle verwendeten Quellen besitzen reproduzierbare Fundstellen.
- [ ] Jeder relevante Befund besitzt eine gültige `evd-nnn`-Kennung.
- [ ] Jeder Befund besitzt einen Nachweisstatus gemäß `rules/evidence.md`.
- [ ] Aussagen des Ideengebers und externe Befunde sind getrennt.
- [ ] Dokumentierte Behauptungen werden nicht als nachgewiesene Tatsachen dargestellt.
- [ ] Widersprüche sind mit `CONFLICT` gekennzeichnet.
- [ ] Unbekannte Sachverhalte sind mit `UNKNOWN` gekennzeichnet.
- [ ] Fehlende Informationen wurden nicht durch Annahmen ersetzt.
- [ ] Nicht durchgeführte Prüfungen sind sichtbar.
- [ ] Grenzen der Untersuchung sind dokumentiert.
- [ ] Es wurden keine neuen Anforderungen formuliert.
- [ ] Es wurde keine Lösung ausgewählt oder bewertet.
- [ ] Es wurde keine Architekturentscheidung getroffen.
- [ ] Die Qualitätsgrenze für `swk-02` wurde vollständig geprüft.

Ergebnis der Prüfung:

- Ergebnis: `offen`
- geprüft am:
- geprüft durch:
- nicht erfüllte Kriterien:
- Begründung einer möglichen Blockade:

## 13. Freigabestatus

- Ergebnis: `offen`
- Dokumentstatus: `input`
- geprüft am:
- geprüft durch:
- Anmerkungen:
