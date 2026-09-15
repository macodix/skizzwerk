# swk-02: Bestand untersuchen

## Zweck

Der für die Projektidee relevante vorhandene Bestand wird systematisch
untersucht und nachvollziehbar dokumentiert.

Die Phase ermittelt, was bereits vorhanden, dokumentiert, nachgewiesen,
widersprüchlich oder unbekannt ist. Sie bewertet noch nicht, welche Lösung
gewählt oder wie das Projekt umgesetzt werden soll.

## Vorprüfung

Vor der Bearbeitung ist zu prüfen:

- die projektspezifische `idea.md` existiert,
- die projektspezifische `idea.md` hat den Status `accepted`,
- alle in dieser Phasendatei referenzierten Dateien existieren,
- keine benötigte Regel oder Vorlage ist leer oder offensichtlich unvollständig,
- `templates/inventory.json` ist als Vorlage verwendbar,
- `tools/inventory.py` ist ausführbar und seine Tests bestehen,
- `rules/quality-gates.md` enthält eine Qualitätsgrenze für `swk-02`,
- verwendete Kennungen entsprechen `rules/identifiers.md`.

Bei fehlgeschlagener Vorprüfung werden keine projektspezifischen
Ergebnisdateien angelegt oder verändert.

Die festgestellten Mängel werden mit Datei, Fundstelle und Begründung
dokumentiert.

## Eingaben

Erforderlich:

- projektspezifische `idea.md` mit Status `accepted`
- `templates/inventory.json`
- `tools/inventory.py`
- `rules/evidence.md`
- `rules/identifiers.md`
- `rules/status.md`
- `rules/quality-gates.md`

Zusätzliche Eingaben können sein:

- vom Ideengeber genannte Systeme, Installationen, Quelltexte oder Projekte,
- vorhandene Projekt- und Betriebsdokumentation,
- offizielle Dokumentation und Spezifikationen,
- vorhandene Quellcode-Repositories,
- vorhandene Tests und Testergebnisse,
- dokumentierte frühere Untersuchungen oder Versuche,
- Issues, Pull Requests und Entwicklungsdiskussionen,
- weitere Quellen, die unmittelbar für die Projektidee relevant sind.

Zusätzliche Eingaben müssen mit ihrer Herkunft dokumentiert werden.

## Untersuchungsumfang

Untersucht wird der Bestand, der für die in der akzeptierten `idea.md`
genannten Ziele, Funktionen, Einschränkungen, Systeme und offenen
Sachverhalte relevant ist.

Der Untersuchungsumfang wird aus der `idea.md` abgeleitet. Er darf nicht
stillschweigend um neue Anforderungen oder Lösungsziele erweitert werden.

Für jeden vorgesehenen Untersuchungsbereich wird dokumentiert:

- was untersucht werden soll,
- weshalb dieser Bereich für die Projektidee relevant ist,
- welche Quellen berücksichtigt wurden,
- welche Teile tatsächlich untersucht wurden,
- welche Teile nicht untersucht werden konnten,
- welche Einschränkungen die Untersuchung besitzt.

## Arbeitsauftrag

1. Lies die vollständige und akzeptierte projektspezifische `idea.md`.

2. Ermittle daraus die für die Bestandsuntersuchung relevanten:

   - vorhandenen Systeme und Installationen,
   - vorhandenen Programme, Komponenten und Projekte,
   - genannten Funktionen und Einschränkungen,
   - dokumentierten bisherigen Versuche,
   - unklaren oder unbekannten Sachverhalte,
   - möglichen vorhandenen Grundlagen, die ausdrücklich untersucht werden
     sollen.

3. Lege den Untersuchungsumfang fest. Begründe jeden aufgenommenen
   Untersuchungsbereich durch einen Verweis auf die projektspezifische
   `idea.md`.

4. Erfasse die verwendeten Quellen mit:

   - Quellenart gemäß `rules/evidence.md`,
   - genauer Bezeichnung,
   - reproduzierbarer Fundstelle,
   - Version, Commit oder Veröffentlichungsstand, soweit verfügbar,
   - Abruf- oder Prüfdatum,
   - Zugänglichkeit und erkannten Einschränkungen.

5. Untersuche die Quellen nur soweit, wie es für die Bestandsaufnahme
   erforderlich ist.

6. Dokumentiere jeden relevanten Befund mit einer eindeutigen
   `evd-nnn`-Kennung und dem Format aus `rules/evidence.md`.

7. Ordne jedem Befund einen Nachweisstatus gemäß `rules/evidence.md` zu.

8. Trenne eindeutig zwischen:

   - Aussagen des Ideengebers,
   - unmittelbar nachgewiesenen Tatsachen,
   - dokumentierten Behauptungen,
   - Ableitungen,
   - Annahmen,
   - unbekannten Sachverhalten,
   - widersprüchlichen oder widerlegten Aussagen.

9. Dokumentiere Widersprüche zwischen Quellen mit dem Status `CONFLICT`.
   Stelle die widersprechenden Aussagen und ihre Fundstellen gegenüber.

10. Dokumentiere fehlende oder nicht zugängliche Informationen als
    `UNKNOWN`. Ersetze sie nicht durch Vermutungen.

11. Dokumentiere nicht durchgeführte Prüfungen und die daraus entstehenden
    Grenzen der Aussagekraft.

12. Bezeichne eine Prüfung nur dann als unzulässig, wenn eine verbindliche
    Regel sie ausdrücklich verbietet. Unterscheide zwischen:

    - nicht erforderlich,
    - nicht vorgesehen,
    - nicht durchgeführt,
    - technisch nicht möglich,
    - wegen fehlenden Zugriffs nicht möglich,
    - durch eine konkrete Regel unzulässig.

13. Erstelle oder vervollständige die projektspezifische `inventory.json`
    anhand von `templates/inventory.json`. Diese Datei ist die verbindliche
    Datenquelle der Bestandsuntersuchung.

14. Validiere `inventory.json` mit `tools/inventory.py` und erzeuge daraus die
    projektspezifische `inventory.md`. Bearbeite die erzeugte Markdown-Datei
    nicht direkt.

15. Prüfe das Ergebnis anhand der Qualitätsgrenze für `swk-02` in
    `rules/quality-gates.md`.

## Verbindliche Regeln

- Erfinde keine Bestandsangaben.
- Leite aus fehlenden Informationen nicht auf das Fehlen einer Funktion oder
  Komponente.
- Stelle dokumentierte Behauptungen nicht als nachgewiesene Tatsachen dar.
- Werte vorhandenen Quellcode nicht ohne Prüfung als funktionsfähig.
- Werte einen erfolgreichen Build nicht als Nachweis fachlicher
  Funktionsfähigkeit.
- Werte vorhandene Tests nicht ohne Prüfung ihres Inhalts und Ergebnisses als
  Funktionsnachweis.
- Verwende ausschließlich Quellen, deren Herkunft und Fundstelle
  nachvollziehbar dokumentiert werden können.
- Kennzeichne unzugängliche, nicht untersuchte und nur teilweise untersuchte
  Bereiche.
- Triff keine Architekturentscheidung.
- Wähle keine technische Lösung aus.
- Formuliere keine neuen Anforderungen.
- Bewerte noch nicht, welche gefundene Grundlage bevorzugt werden soll.
- Verändere kein untersuchtes externes oder produktiv verwendetes System.
- Installiere oder aktualisiere keine Software auf einem untersuchten externen
  oder produktiv verwendeten System.
- Builds und Tests in einer getrennten, entbehrlichen Arbeitsumgebung sind
  zulässig, wenn:
  - sie für einen Befund des festgelegten Untersuchungsumfangs erforderlich
    sind,
  - sie kein externes oder produktiv verwendetes System verändern,
  - sie keine produktiven Zugangsdaten verwenden,
  - Durchführung und Ergebnis reproduzierbar dokumentiert werden.
- Ist ein Build oder Test nicht erforderlich oder nicht durchgeführt worden,
  wird dies als `nicht durchgeführt` dokumentiert.
- Aus einer nicht durchgeführten Prüfung darf kein Prozessverbot abgeleitet
  werden.
- Setze keine Annahme stillschweigend als Arbeitsgrundlage.
- Ändere den Dokumentstatus nur entsprechend `rules/status.md` und dem
  Prüfergebnis.
- Bearbeite Befunddaten ausschließlich in `inventory.json`.
- Erzeuge `inventory.md` ausschließlich mit `tools/inventory.py`.
- Umgehe oder deaktiviere keine fehlgeschlagene Validierung.

## Abgrenzung zur Bewertung

`swk-02` beschreibt den festgestellten Bestand und die Belastbarkeit der
Befunde.

Nicht Bestandteil von `swk-02` sind:

- Bewertung oder Rangfolge möglicher Lösungen,
- Auswahl eines vorhandenen Projekts oder einer Komponente,
- Architektur- und Technologieentscheidungen,
- Formulierung neuer Anforderungen,
- Festlegung der späteren Umsetzung,
- Entscheidung über offene Alternativen.

Diese Arbeiten erfolgen erst in den dafür vorgesehenen späteren Phasen.

## Ergebnis

Ergebnisse sind:

- eine projektspezifische `inventory.json` als verbindliche Datenquelle,
- eine daraus automatisch erzeugte projektspezifische `inventory.md` als
  lesbare Darstellung.

Die strukturierte Datenquelle und die erzeugte Darstellung enthalten
mindestens:

- den aus der `idea.md` abgeleiteten Untersuchungsumfang,
- die untersuchten Quellen und ihre genauen Fundstellen,
- die einzelnen Befunde mit `evd-nnn`-Kennungen,
- den Nachweisstatus jedes Befunds,
- erkannte Konflikte,
- unbekannte und nicht untersuchte Sachverhalte,
- Grenzen der Untersuchung,
- das Prüfergebnis für `swk-02`.

Mögliche Dokumentstatus:

- `input`: Eine noch nicht untersuchte Bestandsangabe liegt vor.
- `draft`: Die Bestandsuntersuchung wurde begonnen oder weist noch Mängel auf.
- `review`: Die Untersuchung und die interne Prüfung sind abgeschlossen.
- `accepted`: Der Ideengeber hat Umfang und dokumentiertes Ergebnis bestätigt.
- `blocked`: Eine wesentliche Quelle oder notwendige Information ist nicht
  verfügbar und verhindert den sinnvollen Abschluss.

## Abschlusskriterien

`swk-02` ist abgeschlossen, wenn:

- der Untersuchungsumfang aus der akzeptierten `idea.md` nachvollziehbar
  abgeleitet wurde,
- alle vorgesehenen Untersuchungsbereiche bearbeitet oder ausdrücklich als
  nicht untersuchbar dokumentiert wurden,
- alle verwendeten Quellen reproduzierbar angegeben sind,
- jeder relevante Befund eine gültige Kennung und einen Nachweisstatus besitzt,
- dokumentierte Behauptungen und nachgewiesene Tatsachen getrennt sind,
- Widersprüche sichtbar dokumentiert sind,
- unbekannte Sachverhalte nicht durch Annahmen ersetzt wurden,
- Grenzen der Untersuchung sichtbar sind,
- keine Anforderung, Architekturentscheidung oder Lösungsauswahl
  vorweggenommen wurde,
- die Qualitätsgrenze für `swk-02` erfüllt ist,
- `inventory.json` die automatische Validierung besteht,
- `inventory.md` nachweislich aus der aktuellen `inventory.json` erzeugt wurde,
- die projektspezifische Bestandsuntersuchung den Status `accepted` erhalten
  hat.
