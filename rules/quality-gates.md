# Qualitätsgrenzen

## Zweck

Qualitätsgrenzen legen fest, wann eine Phase abgeschlossen werden darf.

Eine Phase gilt nicht als abgeschlossen, nur weil alle vorgesehenen
Dokumentabschnitte Text enthalten.

## Allgemeine Regeln

- Jedes Ergebnis muss gegen die Qualitätsgrenze seiner Phase geprüft werden.
- Nicht erfüllte Kriterien müssen sichtbar dokumentiert werden.
- Die KI darf fehlende Informationen nicht erfinden.
- Ein Dokument mit wesentlichen Mängeln darf nicht den Status `review` erhalten.
- Ein Dokument darf nur durch ausdrückliche menschliche Bestätigung den Status
  `accepted` erhalten.
- Ein blockierter Abschluss muss mit einer konkreten Begründung dokumentiert werden.

## Qualitätsgrenze swk-01

`swk-01` darf den Status `review` erhalten, wenn:

- die Originalbeschreibung unverändert erhalten ist,
- Herkunft und Kontext unverändert erhalten sind,
- Originalaussagen und Interpretationen klar getrennt sind,
- Ziel und erwarteter Nutzen aus der Eingabe abgeleitet wurden,
- der erwartete Nutzen von Funktionen und Qualitätszielen getrennt ist,
- genannte Nutzer, Systeme, Funktionen und Einschränkungen erfasst wurden,
- mehrdeutige Begriffe sichtbar gekennzeichnet sind,
- jede genannte Mehrdeutigkeit eine konkrete wesentliche Auswirkung besitzt,
- keine Annahme als Tatsache dargestellt wird,
- keine zusätzliche Anforderung erfunden wurde,
- keine Architekturentscheidung getroffen wurde,
- keine konkrete technische Lösung ausgewählt wurde,
- offene Punkte sichtbar bleiben,
- alle Kennungen `rules/identifiers.md` entsprechen,
- Annahmen von Ableitungen und unbekannten Sachverhalten abgegrenzt sind,
- jede in `idea.md` referenzierte Annahme in `assumptions.md` existiert,
- eine vorhandene `assumptions.md` in Übersichts- und Einzelangaben
  widerspruchsfrei ist,
- `idea.md` der Vorlage `templates/idea.md` entspricht,
- eine vorhandene `assumptions.md` der Vorlage
  `templates/assumptions.md` entspricht,
- ohne erkannte Annahmen keine projektspezifische `assumptions.md`
  erforderlich ist.

## Qualitätsgrenze swk-02

`swk-02` darf den Status `review` erhalten, wenn:

- die zugrunde liegende projektspezifische `idea.md` den Status `accepted`
  besitzt,
- der Untersuchungsumfang nachvollziehbar aus der akzeptierten `idea.md`
  abgeleitet wurde,
- jeder Untersuchungsbereich einen konkreten Bezug zur `idea.md` besitzt,
- alle vorgesehenen Untersuchungsbereiche bearbeitet oder ausdrücklich als
  nicht beziehungsweise nur teilweise untersucht dokumentiert wurden,
- die Gründe für nicht oder nur teilweise untersuchte Bereiche dokumentiert
  sind,
- die Auswirkungen nicht durchgeführter Untersuchungen auf die Aussagekraft
  dokumentiert sind,
- alle verwendeten Quellen mit Quellenart, genauer Fundstelle und Abruf- oder
  Prüfdatum angegeben sind,
- Versionen, Commits oder Veröffentlichungsstände angegeben sind, soweit sie
  für die Reproduzierbarkeit erforderlich und verfügbar sind,
- bei jeder Quelle erkennbar ist, welcher Teil tatsächlich untersucht wurde,
- bei einem Befund mit mehreren verwendeten Quellen jede Quelle einzeln mit
  ihrer tatsächlichen Quellenart dokumentiert ist,
- keine gemeinsame Quellenart verwendet wird, wenn die Quellen
  unterschiedlichen Quellenarten angehören,
- bei jeder Quelle erkennbar ist, welchen Beitrag sie zum Befund leistet,
- jeder relevante Befund eine gültige `evd-nnn`-Kennung besitzt,
- jeder Befund einen Nachweisstatus gemäß `rules/evidence.md` besitzt,
- Befundübersicht und Einzelbefunde vollständig und widerspruchsfrei sind,
- Aussagen des Ideengebers mit `USER_PROVIDED` gekennzeichnet sind,
- unmittelbar durch Code, Test, Messung oder Primärquelle bestätigte Aussagen
  nur bei ausreichendem Nachweis mit `VERIFIED` gekennzeichnet sind,
- Angaben aus Dokumentationen höchstens mit `DOCUMENTED` gekennzeichnet sind,
  solange keine weitergehende Prüfung vorliegt,
- Ableitungen mit `INFERRED` gekennzeichnet und aus dokumentierten Befunden
  nachvollziehbar hergeleitet sind,
- unbekannte Sachverhalte mit `UNKNOWN` gekennzeichnet sind,
- widersprüchliche Quellen oder Befunde mit `CONFLICT` gekennzeichnet und gegenübergestellt sind,
- jeder Befund mit dem Status `CONFLICT` mindestens zwei belegte Aussagen mit
  genauer Quelle nennt,
- bei jedem `CONFLICT` der gemeinsame Sachverhalt, Bezugszeitpunkt und
  Geltungsbereich dokumentiert sind,
- bei jedem `CONFLICT` die logische Unvereinbarkeit der Aussagen konkret
  begründet ist,
- unterschiedliche Versionsangaben nicht ohne Prüfung ihrer Bedeutung als
  Konflikt behandelt wurden,
- historische und aktuelle Aussagen nicht allein wegen ihrer Abweichung als
  Konflikt behandelt wurden,
- das bloße Fehlen einer Zeichenkette oder eines erwarteten Codebestandteils
  nicht ohne weitere Begründung als Widerlegung einer Dokumentationsaussage
  behandelt wurde,
- widerlegte Aussagen mit `DISPROVED` gekennzeichnet und durch einen
  belastbaren Gegenbeleg belegt sind,
- fehlende Informationen nicht durch Annahmen oder plausible Formulierungen
  ersetzt wurden,
- nicht durchgeführte Prüfungen bei den betroffenen Befunden dokumentiert sind,
- nicht durchgeführte Prüfungen nicht ohne verbindliche Regel als unzulässig
  bezeichnet wurden,
- bei jeder nicht durchgeführten Prüfung zwischen fehlender Erforderlichkeit,
  fehlender Durchführung, technischer Unmöglichkeit, fehlendem Zugriff und
  ausdrücklichem Prozessverbot unterschieden wurde,
- ein erfolgreicher Build nicht als Nachweis fachlicher Funktionsfähigkeit
  gewertet wurde,
- vorhandener Quellcode nicht ohne geeignete Prüfung als funktionsfähig
  dargestellt wurde,
- vorhandene Tests nur entsprechend ihres geprüften Inhalts und ihres
  dokumentierten Ergebnisses als Nachweis verwendet wurden,
- die Grenzen der Bestandsuntersuchung sichtbar dokumentiert sind,
- keine neue Anforderung formuliert wurde,
- keine mögliche Lösung bewertet oder ausgewählt wurde,
- keine Architektur- oder Technologieentscheidung getroffen wurde,
- keine untersuchte externe Installation und kein externes Repository durch
  die Bestandsuntersuchung verändert wurde,
- alle Kennungen `rules/identifiers.md` entsprechen,
- der Dokumentstatus entsprechend `rules/status.md` gesetzt wurde,
- eine projektspezifische `inventory.json` vorhanden ist,
- `inventory.json` der Vorlage `templates/inventory.json` entspricht,
- `inventory.json` die Validierung durch `tools/inventory.py` ohne Fehler
  besteht,
- `inventory.md` aus der aktuellen `inventory.json` erzeugt wurde,
- die automatisch erzeugte `inventory.md` nicht manuell verändert wurde.

## Qualitätsgrenze swk-03

`swk-03` darf den Status `review` erhalten, wenn:

- die zugrunde liegende projektspezifische `idea.md` den Status `accepted` besitzt,
- die zugrunde liegende projektspezifische `inventory.json` den Status `accepted` besitzt,
- eine vorhandene projektspezifische `assumptions.md` berücksichtigt wurde,
- die Einzelkriterien der Vorprüfung dokumentiert und vollständig bestanden sind,
- die Bewertung ausschließlich auf der akzeptierten `idea.md`, der akzeptierten
  `inventory.json` und gegebenenfalls der projektspezifischen `assumptions.md`
  beruht,
- `rules/questions.md` bei der Abgrenzung von Wissenslücken,
  Anforderungsklärungen und Entscheidungsbedarfen beachtet wurde,
- `rules/clarifications.md` bei Durchführung und Dokumentation von
  Anforderungsklärungen beachtet wurde,
- Annahmen nicht als Befunde oder Tatsachen behandelt werden,
- vorhandene Annahmen mit wesentlicher Auswirkung darauf geprüft wurden, ob sie
  nach `rules/assumptions.md` einen Entscheidungsbedarf erzeugen,
- ein aus einer Annahme entstehender Entscheidungsbedarf mit der zugehörigen
  `asm-nnn`-Kennung dokumentiert ist,
- keine neue Bestandsrecherche durchgeführt wurde,
- jeder Bewertungsaspekt einen konkreten Bezug zur `idea.md` besitzt,
- jede Bewertung die verwendeten `evd-nnn`-Befunde nennt,
- die Belastbarkeit der Bewertung die Belastbarkeit ihrer Befundgrundlage nicht überschreitet,
- dokumentierte Behauptungen nicht als nachgewiesene Tatsachen dargestellt werden,
- unbekannte Sachverhalte und nicht durchgeführte Prüfungen sichtbar bleiben,
- ein fehlender Nachweis nicht als Nachweis einer fehlenden Funktion behandelt wird,
- eine dokumentierte Funktion nicht ohne geeigneten Nachweis als praktisch bestätigt behandelt wird,
- positive Beiträge und Einschränkungen nur dokumentiert werden, soweit sie aus Befunden ableitbar sind,
- Vergleiche zwischen Alternativen dieselben relevanten Bewertungsaspekte verwenden,
- die Darstellungsform einer Gegenüberstellung an die Zahl der Alternativen
  angepasst werden darf, ohne die Kriterienbasis zu verändern,
- keine numerischen Scores, Gewichtungen, Rangfolgen oder Gesamtnoten ohne ausdrücklich definierte Bewertungsmethode verwendet werden,
- keine bevorzugte Alternative als verbindliche Lösung ausgewählt wird,
- keine neue Anforderung formuliert wird,
- keine Architektur-, Technologie- oder Umsetzungsentscheidung getroffen wird,
- keine Annahme stillschweigend als Bewertungsgrundlage gesetzt wird,
- jeder wesentliche offene Punkt darauf geprüft wurde, ob weitere
  Bestandsuntersuchung, Anforderungsklärung, spätere Entscheidung oder eine
  spätere praktische Verifikation erforderlich ist,
- ein Rückkehrpunkt zu `swk-02` nur dann als erforderlich eingestuft wurde,
  wenn er mit vorhandenen oder mit vertretbarem Aufwand zugänglichen Quellen
  beziehungsweise bereits vorhandenen Prüfmöglichkeiten voraussichtlich
  geklärt oder genauer abgegrenzt werden kann,
- eine fehlende praktische Funktions-, Integrations- oder
  Kompatibilitätsprüfung nicht allein deshalb einen Rückkehrpunkt erzeugt,
  weil dafür erst neue erhebliche Test-, Integrations- oder Prüfinfrastruktur
  entworfen oder aufgebaut werden müsste,
- solche fehlenden praktischen Prüfungen stattdessen als Nachweisgrenze sichtbar
  dokumentiert und einer späteren geeigneten Phase zugeordnet sind,
- jeder erforderliche Rückkehrpunkt zu `swk-02` mit Sachverhalt, betroffenen Befunden, Bedeutung, zusätzlicher Untersuchung und Prüfweg dokumentiert ist,
- kein erforderlicher Rückkehrpunkt zu `swk-02` mehr offen ist,
- reine Wissenslücken und Anforderungsklärungen nicht als Entscheidungsbedarf
  umetikettiert wurden,
- jede erforderliche Anforderungsklärung eine gültige `clr-nnn`-Kennung besitzt
  und in der projektspezifischen `clarifications.md` dokumentiert ist,
- jede beantwortete `clr-nnn` die Antwort des Ideengebers als `USER_PROVIDED`
  dokumentiert und ihre Auswirkung auf `assessment.md` nachvollziehbar behandelt,
- keine für den Abschluss erforderliche `clr-nnn` unbeantwortet ist,
- Antworten auf `clr-nnn` nicht stillschweigend in die akzeptierte `idea.md`
  eingearbeitet wurden,
- bei Widerspruch zur akzeptierten `idea.md` oder materieller Änderung des
  Projektgegenstands der Rückwirkungsweg nach `rules/clarifications.md` und
  `rules/process.md` dokumentiert wurde,
- jeder echte Entscheidungsbedarf eine gültige `dnd-nnn`-Kennung besitzt,
- keine nicht definierte Kennungsart verwendet wurde,
- wesentliche nicht durch weitere Bestandsuntersuchung klärbare Punkte als
  Nachweisgrenze, Anforderungsklärung oder späterer Entscheidungsbedarf sichtbar dokumentiert sind,
- die projektspezifische `assessment.md` der Vorlage `templates/assessment.md` entspricht,
- eine bei vorhandenen Anforderungsklärungen erforderliche projektspezifische
  `clarifications.md` der Vorlage `templates/clarifications.md` entspricht,
- alle Kennungen `rules/identifiers.md` entsprechen,
- der Dokumentstatus entsprechend `rules/status.md` gesetzt wurde.

## Qualitätsgrenze swk-04

`swk-04` darf den Status `review` erhalten, wenn:

- die zugrunde liegende projektspezifische `idea.md` den Status `accepted` besitzt,
- die zugrunde liegende projektspezifische `inventory.json` den Status `accepted` besitzt,
- die zugrunde liegende projektspezifische `assessment.md` den Status `accepted` besitzt,
- `rules/questions.md` beachtet wurde,
- jeder Entscheidungsbedarf aus der akzeptierten `assessment.md` hergeleitet ist,
- jeder übernommene Entscheidungsbedarf eine gültige `dnd-nnn`-Kennung besitzt,
- jede daraus formulierte Entscheidungsfrage auf die zugehörige `dnd-nnn`
  verweist,
- die Prüfung eines übergebenen Entscheidungsbedarfs auf die formale
  Unterscheidung zwischen Entscheidung und Wissenslücke beschränkt bleibt,
- keine fachliche Neubewertung von Alternativen aus `swk-03` durchgeführt wird,
- keine bloße Wissenslücke ohne Auswahlbedarf als Entscheidungsfrage behandelt wird,
- jede Entscheidungsfrage eine gültige `que-nnn`-Kennung besitzt,
- jede Entscheidungsfrage klar abgegrenzt und als konkrete Frage formuliert ist,
- jede Entscheidungsfrage ihren Bezug zur `assessment.md` nennt,
- relevante `evd-nnn`-Befunde genannt sind, soweit sie für die Entscheidung benötigt werden,
- relevante `asm-nnn`-Annahmen genannt sind, soweit der Entscheidungsbedarf aus
  einer Annahme mit wesentlicher Auswirkung hervorgeht,
- jede dokumentierte Option auf akzeptierte Vorphasenergebnisse zurückgeführt werden kann,
- keine Option frei ergänzt oder erfunden wurde,
- bekannte Vor- und Nachteile beziehungsweise Einschränkungen nicht über die akzeptierte Bewertung hinaus erweitert wurden,
- unbekannte entscheidungsrelevante Sachverhalte sichtbar bleiben,
- fehlende Informationen darauf geprüft wurden, ob sie durch Bestandsuntersuchung klärbar sind,
- notwendiger Rückkehrbedarf zunächst zu `swk-03` dokumentiert ist,
- ein weiterer Rückweg von `swk-03` zu `swk-02` nur nach den dort definierten
  Rückkehrkriterien erfolgt,
- akzeptierte Vorphasenergebnisse bei Änderungen entsprechend
  `rules/process.md` erneut Qualitätsprüfung und menschliche Freigabe durchlaufen,
- Abhängigkeiten zwischen Entscheidungsfragen dokumentiert sind,
- Folgen einer Vertagung nur dokumentiert werden, soweit sie aus akzeptierten Vorphasenergebnissen ableitbar sind,
- keine Option als bevorzugt, empfohlen oder ausgewählt dargestellt wird,
- keine Entscheidung durch die KI getroffen wird,
- keine neue Anforderung formuliert wird,
- keine Architektur-, Technologie- oder Umsetzungsentscheidung getroffen wird,
- keine wesentliche Annahme stillschweigend als entschieden vorausgesetzt wird,
- die projektspezifische `questions.md` der Vorlage `templates/questions.md` entspricht,
- alle Kennungen `rules/identifiers.md` entsprechen,
- der Dokumentstatus entsprechend `rules/status.md` gesetzt wurde.

## Nichtbestehen der Qualitätsgrenze

Wird mindestens ein erforderliches Kriterium nicht erfüllt:

1. bleibt der Status `draft`,
2. wird der Mangel im Prüfergebnis genannt,
3. wird das Dokument überarbeitet oder als `blocked` gekennzeichnet.

## Menschliche Freigabe

Nach bestandener Qualitätsgrenze erhält das Dokument den Status `review`.

Der Ideengeber prüft anschließend:

- Wurde das Phasenergebnis korrekt und vollständig wiedergegeben?
- Fehlen wesentliche Angaben oder Befunde?
- Wurde etwas hinzugefügt, das nicht aus den Eingaben oder Nachweisen folgt?
- Sind Einschränkungen, Unklarheiten und offene Punkte sichtbar?
- Wurden die Grenzen der jeweiligen Phase eingehalten?

Erst danach darf der Status auf `accepted` gesetzt werden.
