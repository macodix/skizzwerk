# Strukturierte Bestandsuntersuchungen

## Entscheidung

Ergebnisse von `swk-02` werden künftig in einer projektspezifischen
`inventory.json` gepflegt. Die lesbare `inventory.md` wird daraus erzeugt und
nicht direkt bearbeitet.

JSON wurde statt YAML gewählt, weil es mit der Python-Standardbibliothek ohne
zusätzliche Pakete verarbeitet werden kann. Dadurch bleiben lokale Prüfung und
GitHub-CI reproduzierbar und unabhängig von Paketdownloads.

## Verbindliche Dateien

- `templates/inventory.json`: Ausgangsvorlage für strukturierte Daten
- `tools/inventory.py`: Validator und Markdown-Generator
- `.github/workflows/validate-inventories.yml`: automatische Prüfung
- `inventory.json`: verbindliche projektspezifische Quelldaten
- `inventory.md`: automatisch erzeugte lesbare Darstellung

Bei einem Widerspruch zwischen `inventory.json` und `inventory.md` ist
`inventory.json` maßgeblich. Ein solcher Widerspruch führt zum Fehlschlag der
automatischen Prüfung.

## Verwendung

Struktur prüfen:

```bash
python tools/inventory.py validate pilots/PROJEKT/inventory.json
```

Markdown erzeugen:

```bash
python tools/inventory.py render \
  pilots/PROJEKT/inventory.json \
  pilots/PROJEKT/inventory.md
```

Prüfen, ob das vorhandene Markdown dem Datenstand entspricht:

```bash
python tools/inventory.py check \
  pilots/PROJEKT/inventory.json \
  pilots/PROJEKT/inventory.md
```

## Automatisch geprüfte Regeln

Der Validator prüft insbesondere:

- erforderliche Metadaten und gültige Dokumentstatus,
- gültige und lückenlos nummerierte `evd-nnn`-Kennungen,
- eindeutige Befundkennungen,
- gültige Nachweisstatus und Quellenarten,
- Pflichtfelder jedes Befunds,
- einzelne Einträge für jede Quelle,
- Begründung und Beitrag jeder Quelle,
- mindestens zwei Quellen und vollständige Zusatzfelder bei `CONFLICT`,
- Verbot von Konfliktfeldern bei anderen Nachweisstatus,
- `USER_STATEMENT` bei `USER_PROVIDED`,
- `ANALYSIS` bei `INFERRED`,
- keine Vermischung von `VERIFIED` und `PROJECT_DOCUMENTATION` in einem
  einzelnen Befund,
- bestandene Vorprüfung und Qualitätsgrenze vor dem Status `review`,
- dokumentierte menschliche Freigabe vor dem Status `accepted`.

Die CI prüft zusätzlich, ob `inventory.md` exakt aus `inventory.json` erzeugt
wurde.

## Nicht automatisch entscheidbare Inhalte

Der Validator kann nicht sicher beurteilen:

- ob eine Quelle inhaltlich korrekt ausgewertet wurde,
- ob eine Ableitung logisch tragfähig ist,
- ob zwei Aussagen tatsächlich unvereinbar sind,
- ob der Untersuchungsumfang fachlich vollständig ist,
- ob ein Test die behauptete Funktion angemessen prüft.

Diese Punkte benötigen weiterhin eine unabhängige inhaltliche Prüfung.

## Statuswechsel

Der Status `review` darf nur gesetzt werden, wenn:

1. der Validator erfolgreich läuft,
2. `inventory.md` aktuell erzeugt wurde,
3. die fachlich nicht automatisierbaren Qualitätskriterien geprüft wurden.

Der Status `accepted` benötigt weiterhin eine ausdrückliche menschliche
Bestätigung.

## Übergang bestehender Dokumente

Bereits vorhandene, ausschließlich manuell gepflegte `inventory.md` bleiben
bis zu ihrer ausdrücklichen Migration erhalten. Sie werden nicht automatisch
verändert.

Bei der nächsten inhaltlichen Bearbeitung einer solchen Bestandsuntersuchung
wird sie nach `inventory.json` übertragen, validiert und anschließend neu als
Markdown erzeugt.
