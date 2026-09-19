# swk-03: Befunde bewerten

## Zweck

Die in der akzeptierten Bestandsuntersuchung dokumentierten Befunde werden
hinsichtlich ihrer Bedeutung für die akzeptierte Projektidee bewertet.

Die Phase beantwortet insbesondere:

- welche Befunde für die Projektziele, Funktionen und Einschränkungen relevant sind,
- welche vorhandenen Grundlagen die genannten Funktionen und Einschränkungen ganz, teilweise oder nicht erkennbar abdecken,
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
- eine projektspezifische `assumptions.md` wurde berücksichtigt, sofern sie existiert,
- alle in dieser Phasendatei referenzierten Dateien existieren,
- keine benötigte Regel oder Vorlage ist leer oder offensichtlich unvollständig,
- `rules/quality-gates.md` enthält eine Qualitätsgrenze für `swk-03`,
- die in den Eingaben bereits vorhandenen Kennungen entsprechen `rules/identifiers.md`.

Die Einzelkriterien der Vorprüfung werden im Prüfergebnis dokumentiert.

Bei fehlgeschlagener Vorprüfung wird kein projektspezifisches Ergebnis von
swk-03 angelegt oder verändert.

## Eingaben

Erforderlich:

- projektspezifische `idea.md` mit Status `accepted`,
- projektspezifische `inventory.json` mit Status `accepted`,
- daraus erzeugte `inventory.md`,
- projektspezifische `assumptions.md`, sofern vorhanden,
- `rules/process.md`,
- `rules/evidence.md`,
- `rules/assumptions.md`,
- `rules/questions.md`,
- `rules/clarifications.md`,
- `rules/identifiers.md`,
- `rules/status.md`,
- `rules/quality-gates.md`,
- `templates/assessment.md`,
- `templates/clarifications.md`.

## Bewertungsgrundlage

Bewertet werden ausschließlich Sachverhalte, die in der akzeptierten
`inventory.json` dokumentiert sind, sowie ihre nachweisbare Bedeutung für die
akzeptierte `idea.md`.

Vorhandene projektspezifische Annahmen werden nicht als Befunde behandelt.
Sie werden nur darauf geprüft, ob nach `rules/assumptions.md` aufgrund ihrer
wesentlichen Auswirkung ein Entscheidungsbedarf besteht und ob dieser für den
weiteren Prozess relevant ist.

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
- wesentliche unbekannte oder nicht untersuchte Sachverhalte,
- vorhandene Annahmen mit wesentlicher Auswirkung, soweit daraus ein späterer
  Entscheidungsbedarf für das Projekt entsteht.

Ein Bewertungsaspekt darf nur verwendet werden, wenn sein Bezug zur akzeptierten
`idea.md` dokumentiert wird. Allgemeine Qualitätsvorstellungen dürfen nicht
stillschweigend als zusätzliche Anforderungen eingeführt werden.

## Arbeitsauftrag

1. Lies die vollständige akzeptierte `idea.md` und `inventory.json` sowie eine
   vorhandene projektspezifische `assumptions.md`.

2. Ermittle aus `idea.md` die für die Bewertung relevanten Ziele, genannten
   Funktionen, Einschränkungen und offenen Sachverhalte.

3. Ordne die Befunde aus `inventory.json` diesen Bewertungsaspekten zu.

4. Dokumentiere für jeden Bewertungsaspekt:

   - Bezug zur `idea.md`,
   - verwendete Befunde,
   - feststellbare positive Beiträge,
   - feststellbare Einschränkungen oder Nachteile,
   - unbekannte oder nicht ausreichend untersuchte Punkte,
   - Bedeutung für spätere Entscheidungen oder Klärungen.

5. Prüfe vorhandene `asm-nnn`-Annahmen mit wesentlicher Auswirkung darauf, ob
   sie nach `rules/assumptions.md` eine Entscheidung benötigen. Dokumentiere
   einen daraus entstehenden Entscheidungsbedarf mit Verweis auf die
   `asm-nnn`-Kennung, ohne die Annahme als Befund oder Tatsache zu behandeln.

6. Vergleiche Alternativen nur dort, wo dieselben relevanten Aspekte auf Basis
   dokumentierter Befunde gegenübergestellt werden können. Die Darstellung darf
   an die Zahl der Alternativen angepasst werden, solange die Kriterienbasis
   identisch bleibt.

7. Verwende keine numerischen Scores, Gewichtungen oder Rangfolgen, solange
   diese nicht ausdrücklich als Teil des Prozesses oder durch den Ideengeber
   vorgegeben sind.

8. Kennzeichne Aussagen, die über einen einzelnen Befund hinausgehen, als
   nachvollziehbare Ableitung und nenne ihre Befundgrundlage.

9. Prüfe für jeden wesentlichen offenen Punkt, ob:

   - die vorhandene Bestandsgrundlage für die Bewertung ausreicht,
   - weitere Bestandsuntersuchung in swk-02 den Sachverhalt mit vorhandenen oder
     mit vertretbarem Aufwand zugänglichen Quellen beziehungsweise bereits
     vorhandenen Prüfmöglichkeiten klären kann,
   - eine Präzisierung oder Bestätigung der Projektidee durch den Ideengeber
     erforderlich ist,
   - eine fehlende Bestands- oder Kontextinformation durch eine
     Tatsachenaussage des Ideengebers geklärt werden kann,
   - eine weitergehende praktische Verifikation erst durch den Aufbau neuer
     erheblicher Test-, Integrations- oder Prüfinfrastruktur möglich wäre,
   - oder tatsächlich eine spätere Auswahl, Festlegung oder ausdrückliche
     Bestätigung zwischen dokumentierten Optionen erforderlich ist.

10. Behandle eine für die Bewertung wesentliche fehlende Bestands- oder
    Kontextinformation, die durch eine Tatsachenaussage des Ideengebers
    geklärt werden kann, als Wissenslücke und Rückkehrpunkt zu swk-02, nicht
    als Anforderungsklärung. Die spätere Aussage wird in swk-02 nach
    `rules/evidence.md` als `USER_PROVIDED` / `USER_STATEMENT` und eigener
    `evd-nnn` in `inventory.json` aufgenommen.

11. Dokumentiere erforderliche Rückkehrpunkte zu swk-02 mit:

   - betroffenem Sachverhalt,
   - betroffenen Befunden,
   - Bedeutung für die Bewertung,
   - zusätzlich benötigter Untersuchung,
   - voraussichtlich verfügbaren Quellen oder Prüfwegen.

12. Eine Rückkehr zu swk-02 ist nicht allein deshalb erforderlich, weil eine
    praktische Funktions-, Integrations- oder Kompatibilitätsprüfung zusätzliche
    erhebliche Test- oder Prüfinfrastruktur voraussetzen würde, die im Projekt
    noch nicht spezifiziert oder vorhanden ist. In diesem Fall bleibt die
    fehlende praktische Bestätigung als Nachweisgrenze sichtbar und wird für
    spätere Verifikation, Umsetzung oder Abnahme dokumentiert.

13. Trenne Anforderungsklärungen von Wissenslücken, Annahmen und echten
    Entscheidungsbedarfen. Jede erforderliche Anforderungsklärung erhält eine
    `clr-nnn`-Kennung und wird nach `rules/clarifications.md` in der
    projektspezifischen `clarifications.md` dokumentiert.

14. Führe offene `clr-nnn` mit dem Ideengeber durch. Übernimm seine Antwort
    ausschließlich als `USER_PROVIDED`. Erfinde keine Antwort und leite aus
    einer unvollständigen Antwort keine Annahme ab. Prüfe danach die betroffenen
    Teile von `assessment.md` erneut. Widerspricht die Antwort der akzeptierten
    `idea.md` oder verändert sie den Projektgegenstand materiell, behandle sie
    nach `rules/clarifications.md` und `rules/process.md` als Rückwirkung auf
    einen früheren Prozessstand statt als normale Präzisierung.

15. Jeder echte Entscheidungsbedarf erhält eine gültige `dnd-nnn`-Kennung nach
    `rules/identifiers.md`. Ein `dnd-nnn` bezeichnet nur den festgestellten
    Bedarf; die Entscheidungsfrage entsteht erst in swk-04 als `que-nnn`.

16. Erstelle oder vervollständige die projektspezifische `assessment.md`
    anhand von `templates/assessment.md`.

17. Prüfe das Ergebnis anhand der Qualitätsgrenze für `swk-03` in
    `rules/quality-gates.md`.

## Verbindliche Regeln

- Erfinde keine Anforderungen, Bewertungskriterien oder Tatsachen.
- Verwende ausschließlich die akzeptierte `idea.md`, die akzeptierte
  `inventory.json` und gegebenenfalls die projektspezifische `assumptions.md`
  als projektspezifische Grundlage.
- Beachte `rules/questions.md` bei der Abgrenzung von Wissenslücke,
  Anforderungsklärung und Entscheidungsbedarf.
- Beachte `rules/clarifications.md` für Kennung, Durchführung, Dokumentation und
  Rückwirkung von Anforderungsklärungen.
- Behandle Tatsachen- und Kontextfragen an den Ideengeber nicht als
  Anforderungsklärung. Wesentliche neue Bestandsinformationen werden über
  `swk-02` in die Evidenzbasis aufgenommen.
- Behandle Annahmen nicht als Befunde oder Tatsachen.
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
- Der Aufbau neuer erheblicher Test-, Integrations- oder Prüfinfrastruktur ist
  nicht Bestandteil von swk-03 und wird durch swk-03 nicht stillschweigend als
  Voraussetzung für die Spezifikation eingeführt.
- Erfinde keine eigenen Kennungsarten.
- Ändere den Dokumentstatus nur entsprechend `rules/status.md` und dem
  Prüfergebnis.

## Rückkehr zu swk-02

Eine Rückkehr zu `swk-02` ist erforderlich, wenn ein Sachverhalt:

- für die Bewertung wesentlich ist,
- mit der vorhandenen Bestandsgrundlage nicht nachvollziehbar bewertet werden
  kann,
- und durch weitere Bestandsuntersuchung mit vorhandenen oder mit vertretbarem
  Aufwand zugänglichen Quellen beziehungsweise bereits vorhandenen
  Prüfmöglichkeiten voraussichtlich geklärt oder genauer abgegrenzt werden kann.

Keine Rückkehr ist allein deshalb erforderlich, weil ein Sachverhalt mit
`UNKNOWN` gekennzeichnet ist.

Keine Rückkehr ist allein deshalb erforderlich, weil ein praktischer Nachweis
nur nach Entwurf oder Aufbau neuer erheblicher Test-, Integrations- oder
Prüfinfrastruktur möglich wäre. Diese Grenze wird als fehlende praktische
Bestätigung dokumentiert und in einer späteren geeigneten Phase behandelt.

Kann ein wesentlicher Sachverhalt nicht durch weitere Bestandsuntersuchung im
obigen Sinn geklärt werden, bleibt er offen und wird als Nachweisgrenze,
Anforderungsklärung oder späterer Entscheidungsbedarf dokumentiert.

Solange mindestens ein erforderlicher Rückkehrpunkt zu `swk-02` offen ist, ist
die Qualitätsgrenze von `swk-03` nicht bestanden. `assessment.md` darf dann
nicht den Status `review` erhalten.

## Abgrenzung zu swk-04

swk-03 bereitet Entscheidungen vor, trifft sie aber nicht.

Zulässig sind:

- sachbezogene Gegenüberstellungen,
- dokumentierte Vor- und Nachteile,
- Feststellung relevanter Lücken und Risiken,
- Dokumentation fehlender praktischer Bestätigung als Nachweisgrenze,
- Benennung erforderlicher Anforderungsklärungen,
- Benennung echter Entscheidungsbedarfe als `dnd-nnn`,
- Benennung von Entscheidungsbedarf aus vorhandenen `asm-nnn`-Annahmen mit
  wesentlicher Auswirkung.

Nicht Bestandteil von swk-03 sind:

- Auswahl einer bevorzugten Lösung,
- Festlegung einer Architektur oder Technologie,
- Entscheidung zwischen offenen Alternativen,
- Formulierung verbindlicher neuer Anforderungen,
- Setzen wesentlicher Annahmen als Arbeitsgrundlage,
- Formulierung einer `que-nnn`-Entscheidungsfrage,
- Entwurf oder Aufbau neuer erheblicher Test-, Integrations- oder
  Prüfinfrastruktur.

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
- dokumentierte Nachweisgrenzen, insbesondere fehlende praktische Bestätigung,
- gegebenenfalls Rückkehrpunkte zu swk-02,
- erforderliche Anforderungsklärungen mit `clr-nnn` und Verweis auf die
  projektspezifische `clarifications.md`,
- echte spätere Entscheidungsbedarfe als `dnd-nnn`,
- dabei gegebenenfalls Verweise auf entscheidungsrelevante `asm-nnn`,
- das Prüfergebnis für swk-03.

## Abschlusskriterien

swk-03 ist abgeschlossen, wenn:

- die Bewertungsgrundlage vollständig aus akzeptierter `idea.md`,
  `inventory.json` und gegebenenfalls der projektspezifischen
  `assumptions.md` stammt,
- jeder Bewertungsaspekt einen nachvollziehbaren Bezug zur `idea.md` besitzt,
- jede Bewertung auf konkret genannten `evd-nnn`-Befunden beruht,
- vorhandene Annahmen mit wesentlicher Auswirkung auf einen erforderlichen
  Entscheidungsbedarf geprüft wurden,
- Nachweisgrenzen und unbekannte Sachverhalte sichtbar geblieben sind,
- keine neue Bestandsrecherche durchgeführt wurde,
- keine neue Anforderung erfunden wurde,
- keine Lösung ausgewählt oder Architekturentscheidung getroffen wurde,
- alle wesentlichen offenen Punkte als Rückkehrpunkt, Nachweisgrenze,
  Anforderungsklärung oder echter Entscheidungsbedarf korrekt klassifiziert sind,
- alle für den Abschluss erforderlichen Anforderungsklärungen als `clr-nnn`
  dokumentiert, beantwortet und in den betroffenen Bewertungen berücksichtigt
  sind,
- kein erforderlicher Rückkehrpunkt zu `swk-02` mehr offen ist,
- fehlende praktische Tests nicht als durchgeführt oder bestanden dargestellt
  werden,
- fehlende erhebliche Test- oder Prüfinfrastruktur nicht stillschweigend als
  Voraussetzung für den Abschluss von swk-03 eingeführt wurde,
- die Qualitätsgrenze für `swk-03` erfüllt ist,
- die projektspezifische `assessment.md` den Status `accepted` erhalten hat.
