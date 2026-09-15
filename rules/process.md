# Skizzwerk-Prozess

## Zweck

Diese Datei definiert die Reihenfolge der skizzwerk-Phasen und die
Voraussetzungen für den Übergang zwischen ihnen.

Die inhaltliche Bearbeitung einer Phase richtet sich nach der jeweiligen
Datei unter `phases/`. Für Nachweise, Dokumentstatus und Qualitätsgrenzen
gelten zusätzlich die Dateien unter `rules/`.

## Prozessübersicht

```mermaid
flowchart TD
    A["swk-01: Idee aufnehmen"] --> B["swk-02: Bestand untersuchen"]
    B --> C["swk-03: Befunde bewerten"]
    C --> D["swk-04: Entscheidungsfragen erstellen"]
    C -->|Bestand unvollständig| B
```

## Allgemeine Regeln für Phasenübergänge

- Eine Phase beginnt erst, wenn ihre in der jeweiligen Phasendatei genannten
  Eingaben und Eintrittsvoraussetzungen erfüllt sind.
- Eine Phase gilt erst als abgeschlossen, wenn ihre Abschlusskriterien erfüllt
  sind.
- Das Ergebnis einer Phase muss die zugehörige Qualitätsgrenze in
  `rules/quality-gates.md` erfüllen.
- Der Status `review` erlaubt noch keinen regulären Übergang in die nächste
  Phase.
- Ein regulärer Übergang in die nächste Phase erfolgt erst, wenn das
  erforderliche Ergebnisdokument den Status `accepted` besitzt.
- `accepted` darf nur nach ausdrücklicher menschlicher Bestätigung gesetzt
  werden.
- Ist eine Eintrittsvoraussetzung nicht erfüllt, beginnt die nachfolgende Phase
  nicht.
- Fehlende Voraussetzungen werden mit konkreter Begründung dokumentiert.
- Fehlende Informationen dürfen nicht durch Annahmen ersetzt werden.
- Eine spätere Phase darf Ergebnisse einer früheren Phase nicht
  stillschweigend verändern.

## Übergang von swk-01 zu swk-02

Der Übergang zu `swk-02` erfolgt, wenn:

- die projektspezifische `idea.md` vollständig bearbeitet wurde,
- die Qualitätsgrenze für `swk-01` erfüllt ist,
- die projektspezifische `idea.md` den Status `accepted` besitzt.

`swk-02` verwendet die akzeptierte `idea.md` als verbindliche Grundlage für
die Abgrenzung der Bestandsuntersuchung.

## Übergang von swk-02 zu swk-03

Der Übergang zu `swk-03` erfolgt, wenn:

- die projektspezifische `inventory.md` vollständig bearbeitet wurde,
- die Qualitätsgrenze für `swk-02` erfüllt ist,
- die projektspezifische `inventory.md` den Status `accepted` besitzt.

`swk-03` bewertet ausschließlich Befunde, Quellen, Konflikte, unbekannte
Sachverhalte und Untersuchungsgrenzen, die in der akzeptierten
`inventory.md` dokumentiert sind.

## Rückkehr von swk-03 zu swk-02

`swk-03` kehrt zu `swk-02` zurück, wenn die Bestandsgrundlage für eine
nachvollziehbare Bewertung unvollständig ist und eine weitere
Bestandsuntersuchung erforderlich ist.

Eine Rückkehr erfordert die Dokumentation:

- des fehlenden oder unzureichend untersuchten Sachverhalts,
- der betroffenen Befunde,
- der Bedeutung für die Bewertung,
- der zusätzlich benötigten Untersuchung,
- der voraussichtlich verfügbaren Quellen oder Prüfwege.

Ein mit `UNKNOWN` gekennzeichneter Sachverhalt führt nicht automatisch zur
Rückkehr. Die Rückkehr erfolgt nur, wenn der Sachverhalt für die Bewertung
wesentlich ist und durch eine weitere Bestandsuntersuchung geklärt oder
genauer abgegrenzt werden kann.

Kann ein wesentlicher Sachverhalt nicht durch weitere Bestandsuntersuchung
geklärt werden, wird er nicht durch eine Annahme ersetzt. Seine weitere
Behandlung richtet sich nach den dafür vorgesehenen späteren Phasen.

## Aktualisierung eines akzeptierten Phasenergebnisses

Muss ein bereits akzeptiertes Phasenergebnis ergänzt oder geändert werden:

- bleibt die bisher akzeptierte Fassung nachvollziehbar erhalten,
- wird eine neue Fassung als zu prüfende Arbeitsfassung erstellt,
- durchläuft die neue Fassung erneut die Qualitätsgrenze der betroffenen
  Phase,
- benötigt die neue Fassung erneut eine ausdrückliche menschliche Bestätigung,
- erhält die ersetzte Fassung erst bei Annahme der neuen Fassung den Status
  `superseded`,
- müssen nachfolgende Ergebnisse erneut geprüft werden, wenn ihre Grundlage
  verändert wurde.

## Maschinenlesbare Phasenergebnisse

Wenn eine Phase eine strukturierte Quelldatei und eine daraus erzeugte
Darstellung festlegt, ist ausschließlich die strukturierte Quelldatei zu
bearbeiten.

Die erzeugte Darstellung darf nicht manuell geändert werden. Vor einem
Statuswechsel zu `review` müssen die strukturierte Datei validiert und die
Darstellung neu erzeugt werden. Eine fehlgeschlagene Validierung verhindert
den Statuswechsel.

## Übergang von swk-03 zu swk-04

Der Übergang zu `swk-04` erfolgt, wenn:

- die Bewertung der Befunde entsprechend der Phasendatei für `swk-03`
  abgeschlossen ist,
- keine für die Bewertung notwendige und durch weitere Bestandsuntersuchung
  klärbare Lücke besteht,
- die Qualitätsgrenze für `swk-03` erfüllt ist,
- das Ergebnisdokument von `swk-03` den Status `accepted` besitzt.

Die genaue Bearbeitung von `swk-04` richtet sich nach der zugehörigen
Phasendatei.
