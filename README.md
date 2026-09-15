# skizzwerk

Idea-to-Design-Workflow zur Verbesserung des Entwicklungsprozesses von Software mit KI.

Ziel: Der Entwicklungsprozess wird einfacher, schneller und qualitativ hochwertiger.

Arbeisanweisungen:

- Die Datei rules/process.md enthält die für skizzwerk verbindliche Prozessbeschreibung.

- Die verbindlichen Dokumentstatus sind in `rules/status.md` definiert.

- Strukturierte Bestandsuntersuchungen und ihre automatische Prüfung sind in
  `docs/structured-inventories.md` beschrieben.

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
│   └── swk-02-inventory.md
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
