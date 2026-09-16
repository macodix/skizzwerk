# skizzwerk

Idea-to-Design-Workflow zur Verbesserung des Entwicklungsprozesses von Software mit KI.

Ziel: Der Entwicklungsprozess wird einfacher, schneller und qualitativ hochwertiger.

Arbeisanweisungen:

- Die Datei `rules/process.md` enthält die für skizzwerk verbindliche Prozessbeschreibung.
- Die verbindlichen Dokumentstatus sind in `rules/status.md` definiert.
- Strukturierte Bestandsuntersuchungen und ihre automatische Prüfung sind in
  `docs/structured-inventories.md` beschrieben.
- Beispielprompts für die Phasenbearbeitung stehen in `docs/prompt-examples.md`.

Aktuell definierte Phasen:

- `swk-01`: Idee aufnehmen
- `swk-02`: Bestand untersuchen
- `swk-03`: Befunde bewerten
- `swk-04`: Entscheidungsfragen erstellen

Verzeichnisstruktur:

```
skizzwerk/
├── README.md
├── docs/
│   ├── concepts.md
│   ├── prompt-examples.md
│   └── structured-inventories.md
├── phases/
│   ├── swk-01-idea.md
│   ├── swk-02-inventory.md
│   ├── swk-03-assessment.md
│   └── swk-04-decision-questions.md
├── rules/
│   ├── process.md
│   ├── evidence.md
│   ├── assumptions.md
│   ├── identifiers.md
│   ├── questions.md
│   ├── status.md
│   └── quality-gates.md
├── templates/
│   ├── idea.md
│   ├── inventory.md
│   ├── inventory.json
│   ├── assessment.md
│   ├── assumptions.md
│   ├── questions.md
│   ├── decisions.md
│   └── requirements.md
├── tools/
│   └── inventory.py
├── tests/
│   └── test_inventory.py
└── pilots/
    └── openclaw-xmpp/
```
