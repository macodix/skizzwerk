# swk-03: Befunde bewerten

## Zweck

Die in der akzeptierten Bestandsuntersuchung dokumentierten Befunde werden
hinsichtlich ihrer Bedeutung für die akzeptierte Projektidee bewertet.

Die Phase beantwortet insbesondere:

- welche Befunde für die Projektziele, Funktionen und Einschränkungen relevant sind,
- welche vorhandenen Grundlagen die genannten Anforderungen ganz, teilweise oder nicht erkennbar abdecken,
- welche wesentlichen Lücken, Risiken und offenen Sachverhalte bestehen,
- welche Unterschiede zwischen untersuchten Alternativen für spätere Entscheidungen relevant sind,
- ob die Bestandsgrundlage für eine belastbare Bewertung ausreicht.

swk-03 trifft noch keine Architektur-, Technologie- oder Umsetzungsentscheidung.
Sie formuliert keine neuen Anforderungen und ersetzt unbekannte Sachverhalte
nicht durch Annahmen.

## Vorprüfung

Vor der Bearbeitung ist zu prüfen:

- die projektspezifische `idea.md` existiert und besitzt den Status `accepted`,
- die projektspezifische `inventory.json` existiert und besitzt den Status `accepted`,
- die aus `inventory.json` erzeugte `inventory.md` ist vorhanden,
- alle in dieser Phasendatei referenzierten Dateien existieren,
- keine benötigte Regel oder Vorlage ist leer oder offensichtlich unvollständig,
- `rules/quality-gates.md` enthält eine Qualitätsgrenze für `swk-03`,
- verwendete Kennungen entsprechen `rules/identifiers.md`.

Bei fehlgeschlagener Vorprüfung wird kein projektspezifisches Ergebnis von
swk-03 angelegt oder verändert.

## Eingaben

Erforderlich:

- projektspezifische `idea.md` mit Status `accepted`,
- projektspezifische `inventory.json` mit Status `accepted`,
- daraus erzeugte `inventory.md`,
- `rules/process.md`,
- `rules/evidence.md`,
- `rules/assumptions.md`,
- `rules/identifiers.md`,
- `rules/status.md`,
- `rules/quality-gates.md`,
- `templates/assessment.md`.

## Bewertungsgrundlage

Bewertet werden ausschließlich Sachverhalte, die in der akzeptierten
`inventory.json` dokumentiert sind, sowie ihre nachweisbare Bedeutung für die
akzeptierte `idea.md`.

Eine Bewertung darf sich auf mehrere Befunde stützen. Jede Bewertung muss die
verwendeten `evd-nnn`-Kennungen nennen.

Die Belastbarkeit einer Bewertung darf die Belastbarkeit der zugrunde liegenden
Befunde nicht überschreiten.

`UNKNOWN`, nicht durchgeführte Prüfungen und dokumentierte Untersuchungsgrenzen
bleiben sichtbar und werden bei der Bewertung berücksichtigt.

## Bewertungsgegenstände

Bewertet werden nur für die Projektidee relevante Aspekte. Dazu gehören je nach
vorhandenem Bestand insbesondere:

- Abdeckung genannter Funktionen und Einschränkungen,
- erkennbare Kompatibilität mit genannten Systemen und Versionen,
- dokumentierte technische Voraussetzungen und Abhängigkeiten,
- belegte Einschränkungen und bekannte Risiken,
- Wartungs- und Änderungsabhängigkeiten, soweit sie durch Befunde belegt sind,
- Unterschiede zwischen vorhandenen Alternativen,
- wesentliche unbekannte oder nicht untersuchte Sachverhalte.

Ein Bewertungsaspekt darf nur verwendet werden, wenn sein Bezug zur akzeptierten
`idea.md` dokumentiert wird. Allgemeine Qualitätsvorstellungen dürfen nicht
stillschweigend als zusätzliche Anforderungen eingeführt werden.

## Arbeitsauftrag

1. Lies die vollständige akzeptierte `idea.md` und `inventory.json`.

2. Ermittle aus `idea.md` die für die Bewertung relevanten Ziele, genannten
   Funktionen, Einschränkungen und offenen Sachverhalte.

3. Ordne die Befunde aus `inventory.json` diesen Bewertungsaspekten zu.

4. Dokumentiere für jeden Bewertungsaspekt:

   - Bezug zur `idea.md`,
   - verwendete Befunde,
   - feststellbare positive Beiträge,
   - feststellbare Einschränkungen oder Nachteile,
   - unbekannte oder nicht ausreichend untersuchte Punkte,
   - Bedeutung für spätere Entscheidungen.

5. Vergleiche Alternativen nur dort, wo dieselben relevanten Aspekte auf Basis
   dokumentierter Befunde gegenübergestellt werden können.

6. Verwende keine numerischen Scores, Gewichtungen oder Rangfolgen, solange
   diese nicht ausdrücklich als Teil des Prozesses oder durch den Ideengeber
   vorgegeben sind.

7. Kennzeichne Aussagen, die über einen einzelnen Befund hinausgehen, als
   nachvollziehbare Ableitung und nenne ihre Befundgrundlage.

8. Prüfe für jeden wesentlichen offenen Punkt, ob:

   - die vorhandene Bestandsgrundlage für die Bewertung ausreicht,
   - weitere Bestandsuntersuchung in swk-02 den Sachverhalt klären kann,
   - der Sachverhalt nicht durch weitere Bestandsuntersuchung klärbar ist und
     deshalb einer späteren Entscheidung oder Anforderungsklärung vorbehalten
     bleibt.

9. Dokumentiere erforderliche Rückkehrpunkte zu swk-02 mit:

   - betroffenem Sachverhalt,
   - betroffenen Befunden,
   - Bedeutung für die Bewertung,
   - zusätzlich benötigter Untersuchung,
   - voraussichtlich verfügbaren Quellen oder Prüfwegen.

10. Erstelle oder vervollständige die projektspezifische `assessment.md`
    anhand von `templates/assessment.md`.

11. Prüfe das Ergebnis anhand der Qualitätsgrenze für `swk-03` in
    `rules/quality-gates.md`.

## Verbindliche Regeln

- Erfinde keine Anforderungen, Bewertungskriterien oder Tatsachen.
- Verwende ausschließlich die akzeptierte `idea.md` und die akzeptierte
  `inventory.json` als projektspezifische Grundlage.
- Führe in swk-03 keine neue Bestandsrecherche durch.
- Verändere keine Befunde aus swk-02.
- Stufe Nachweisstatus aus swk-02 nicht ohne Rückkehr zu swk-02 um.
- Stelle dokumentierte Behauptungen nicht als nachgewiesene Tatsachen dar.
- Ersetze `UNKNOWN` nicht durch plausible Vermutungen.
- Setze keine Annahme stillschweigend als Bewertungsgrundlage.
- Formuliere keine neue Anforderung.
- Triff keine Architektur-, Technologie- oder Umsetzungsentscheidung.
- Wähle keine Alternative als verbindliche Lösung aus.
- Verwende keine Rangfolge oder Gesamtnote ohne ausdrücklich definierte
  Bewertungsmethode.
- Eine festgestellte Eignung gilt immer nur für den konkret dokumentierten
  Bewertungsaspekt und die vorhandene Befundlage.
- Ein fehlender Nachweis ist nicht gleichbedeutend mit fehlender Funktion.
- Eine dokumentierte Funktion ist nicht automatisch praktisch bestätigt.
- Ändere den Dokumentstatus nur entsprechend `rules/status.md` und dem
  Prüfergebnis.

## Rückkehr zu swk-02

Eine Rückkehr zu `swk-02` ist erforderlich, wenn ein Sachverhalt:

- für die Bewertung wesentlich ist,
- mit der vorhandenen Bestandsgrundlage nicht nachvollziehbar bewertet werden
  kann,
- und durch weitere Bestandsuntersuchung voraussichtlich geklärt oder genauer
  abgegrenzt werden kann.

Keine Rückkehr ist allein deshalb erforderlich, weil ein Sachverhalt mit
`UNKNOWN` gekennzeichnet ist.

Kann ein wesentlicher Sachverhalt nicht durch weitere Bestandsuntersuchung
geklärt werden, bleibt er offen und wird für die spätere Behandlung sichtbar
dokumentiert.

## Abgrenzung zu swk-04

swk-03 bereitet Entscheidungen vor, trifft sie aber nicht.

Zulässig sind:

- sachbezogene Gegenüberstellungen,
- dokumentierte Vor- und Nachteile,
- Feststellung relevanter Lücken und Risiken,
- Benennung von Punkten, die eine Entscheidung benötigen.

Nicht Bestandteil von swk-03 sind:

- Auswahl einer bevorzugten Lösung,
- Festlegung einer Architektur oder Technologie,
- Entscheidung zwischen offenen Alternativen,
- Formulierung verbindlicher neuer Anforderungen,
- Setzen wesentlicher Annahmen als Arbeitsgrundlage.

Diese Punkte werden in den dafür vorgesehenen späteren Phasen behandelt.

## Ergebnis

Ergebnis ist eine projektspezifische `assessment.md`.

Sie enthält mindestens:

- die verwendete Bewertungsgrundlage,
- die aus `idea.md` abgeleiteten Bewertungsaspekte,
- die Zuordnung relevanter `evd-nnn`-Befunde,
- Bewertung je Aspekt,
- dokumentierte Vor- und Nachteile beziehungsweise Einschränkungen,
- wesentliche unbekannte und nicht ausreichend untersuchte Sachverhalte,
- gegebenenfalls Rückkehrpunkte zu swk-02,
- Punkte, die in einer späteren Phase entschieden werden müssen,
- das Prüfergebnis für swk-03.

## Abschlusskriterien

swk-03 ist abgeschlossen, wenn:

- die Bewertungsgrundlage vollständig aus akzeptierter `idea.md` und
  `inventory.json` stammt,
- jeder Bewertungsaspekt einen nachvollziehbaren Bezug zur `idea.md` besitzt,
- jede Bewertung auf konkret genannten `evd-nnn`-Befunden beruht,
- Nachweisgrenzen und unbekannte Sachverhalte sichtbar geblieben sind,
- keine neue Bestandsrecherche durchgeführt wurde,
- keine neue Anforderung erfunden wurde,
- keine Lösung ausgewählt oder Architekturentscheidung getroffen wurde,
- alle wesentlichen bewertungsrelevanten Lücken entweder als Rückkehrpunkt zu
  swk-02 oder als später zu behandelnder offener Punkt dokumentiert wurden,
- die Qualitätsgrenze für `swk-03` erfüllt ist,
- die projektspezifische `assessment.md` den Status `accepted` erhalten hat.
