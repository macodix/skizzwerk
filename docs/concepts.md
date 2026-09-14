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
- vorschnelle Fertigmeldungen.

## Zentrale Schutzmechanismen

### Annahmen

`rules/assumptions.md` verhindert, dass unbestätigte Annahmen als Tatsachen
oder Anforderungen behandelt werden.

### Nachweise

`rules/evidence.md` legt fest, wie Aussagen nach Herkunft und Belastbarkeit
klassifiziert werden.

### Qualitätsgrenzen

`rules/quality-gates.md` bestimmt, wann eine Phase tatsächlich abgeschlossen
ist.

## Grenzen dieser Mechanismen

Die Regeln allein belegen noch keine Qualitätsverbesserung.

Die Pilotprojekte müssen zeigen:

- ob die KI alle Regeln berücksichtigt,
- ob sie die Regeln konsistent anwendet,
- ob Regelverstöße zuverlässig erkannt werden,
- ob zusätzliche unabhängige Prüfungen notwendig sind,
- ob der Workflow mehr Zeit spart als verursacht.
