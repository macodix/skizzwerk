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
- `inventory.md` der Vorlage `templates/inventory.md` entspricht,
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