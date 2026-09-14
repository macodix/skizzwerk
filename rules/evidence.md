# Umgang mit Aussagen und Nachweisen

## Zweck

Diese Regeln verhindern, dass Angaben, Dokumentationsbehauptungen,
Ableitungen oder Vermutungen als gesicherte Tatsachen dargestellt werden.

## Grundsatz

Jede für das Projekt relevante Aussage muss erkennen lassen:

- woher sie stammt,
- wie belastbar sie ist,
- ob sie noch geprüft werden muss.

Die sprachliche Sicherheit einer Aussage darf ihre tatsächliche
Belegbarkeit nicht überschreiten.

## Nachweisstatus

| Status | Bedeutung |
|---|---|
| `USER_PROVIDED` | Aussage stammt vom Ideengeber oder Auftraggeber. |
| `VERIFIED` | Aussage wurde unmittelbar durch Code, Test, Messung oder Primärquelle bestätigt. |
| `DOCUMENTED` | Aussage steht in einer Projektdokumentation, wurde aber nicht praktisch bestätigt. |
| `INFERRED` | Aussage wurde nachvollziehbar aus anderen Befunden abgeleitet. |
| `ASSUMED` | Aussage wird vorläufig angenommen, besitzt aber keinen ausreichenden Nachweis. |
| `UNKNOWN` | Für die Aussage liegt noch keine ausreichende Information vor. |
| `CONFLICT` | Verfügbare Quellen oder Befunde widersprechen sich. |
| `DISPROVED` | Aussage wurde durch einen belastbaren Gegenbeleg widerlegt. |


## Anforderungen an CONFLICT

Der Nachweisstatus `CONFLICT` darf nur verwendet werden, wenn mindestens zwei
belegte Aussagen:

- denselben Sachverhalt betreffen,
- denselben relevanten Bezugszeitpunkt oder Gültigkeitszeitraum betreffen,
- denselben Geltungsbereich besitzen,
- logisch nicht gleichzeitig zutreffen können.

Für jeden Konflikt müssen dokumentiert werden:

- die erste Aussage mit genauer Quelle,
- die zweite Aussage mit genauer Quelle,
- der gemeinsame Sachverhalt,
- Bezugszeitpunkt oder Gültigkeitszeitraum,
- Geltungsbereich,
- die konkrete logische Unvereinbarkeit.

Kein ausreichender Nachweis für `CONFLICT` sind allein:

- unterschiedliche Versionsnummern mit möglicherweise unterschiedlicher
  Bedeutung,
- eine historische Aussage und ein davon abweichender aktueller Stand,
- eine Dokumentationsaussage und das bloße Fehlen einer erwarteten
  Zeichenkette im Quellcode,
- fehlende Informationen,
- unterschiedliche Formulierungen,
- eine nicht durchgeführte Funktionsprüfung.

Ist die Unvereinbarkeit nicht nachgewiesen, wird kein `CONFLICT` gesetzt.
Der Sachverhalt wird entsprechend seiner tatsächlichen Belegbarkeit als
`DOCUMENTED`, `INFERRED` oder `UNKNOWN` dokumentiert.


## Quellenarten

| Quellenart | Beispiele |
|---|---|
| `USER_STATEMENT` | Originalbeschreibung, Gespräch, ausdrückliche Entscheidung |
| `SOURCE_CODE` | tatsächlich untersuchter Programmcode |
| `AUTOMATED_TEST` | reproduzierbarer Testlauf |
| `MANUAL_TEST` | dokumentierter manueller Test |
| `PRIMARY_DOCUMENTATION` | offizielle Dokumentation oder Spezifikation |
| `PROJECT_DOCUMENTATION` | README, Wiki oder Beschreibung eines Drittprojekts |
| `ISSUE_OR_PR` | Issue, Pull Request oder Entwicklungsdiskussion |
| `SECONDARY_SOURCE` | Bericht oder Erläuterung eines Dritten |
| `ANALYSIS` | nachvollziehbare Ableitung durch skizzwerk |
| `NONE` | noch keine Quelle vorhanden |

## Mehrere Quellen eines Befunds

Verwendet ein Befund mehrere Quellen, muss jede Quelle einzeln dokumentiert
werden.

Für jede Quelle sind anzugeben:

- Quellenart,
- genaue Fundstelle,
- Version oder Commit, soweit verfügbar und relevant,
- Abruf- oder Prüfdatum,
- Beitrag der Quelle zum Befund.

Eine gemeinsame Quellenart für mehrere unterschiedlich geartete Quellen ist
unzulässig.

Beispiel:

- Eine Aussage aus einer README erhält die Quellenart
  `PROJECT_DOCUMENTATION`.
- Eine Feststellung aus `package.json` oder dem Programmcode erhält die
  Quellenart `SOURCE_CODE`.
- Eine unmittelbar geprüfte Angabe aus einem offiziellen Register erhält die
  Quellenart `PRIMARY_DOCUMENTATION`.

Der Nachweisstatus des gesamten Befunds richtet sich nach der tatsächlich
durchgeführten Prüfung. Er darf nicht allein aus der belastbarsten verwendeten
Quellenart abgeleitet werden.

## Regeln für swk-01

Während `swk-01` findet grundsätzlich keine Bestandsrecherche statt.

Aussagen aus der Originalbeschreibung erhalten den Status:

`USER_PROVIDED`

Kontextangaben des Ideengebers erhalten ebenfalls:

`USER_PROVIDED`

Interpretationen durch skizzwerk erhalten:

`INFERRED`

Nicht aus der Eingabe ableitbare Sachverhalte erhalten:

`UNKNOWN`

Skizzwerk darf eine Aussage des Ideengebers nicht selbstständig auf
`VERIFIED` setzen.

## Regeln ab swk-02

- README-Angaben erhalten höchstens `DOCUMENTED`.
- Vorhandener Quellcode belegt nur, dass eine Implementierung vorhanden ist.
- Quellcode allein belegt nicht, dass die Implementierung korrekt funktioniert.
- Eine als implementiert bezeichnete Funktion erhält erst nach geeigneter Prüfung
  den Status `VERIFIED`.
- Ein erfolgreicher Build belegt keine fachliche Funktionsfähigkeit.
- Ein vorhandener Test belegt nichts, solange sein Inhalt und sein Ergebnis nicht
  geprüft wurden.
- Aussagen aus Issues und Pull Requests sind Hinweise, keine gesicherten Tatsachen.
- Widersprüche zwischen Dokumentation, Code und Testergebnis erhalten `CONFLICT`.
- Fehlende Nachweise dürfen nicht durch plausible Formulierungen ersetzt werden.
- Eine nicht durchgeführte Prüfung wird als `nicht durchgeführt` dokumentiert.
- Aus einer nicht durchgeführten Prüfung darf nicht abgeleitet werden, dass
  diese Prüfung durch den Prozess verboten ist.
- Eine Prüfung darf nur als `unzulässig` bezeichnet werden, wenn eine
  verbindliche Regel sie ausdrücklich verbietet.
- Quellen müssen so angegeben werden, dass der Befund erneut geprüft werden kann.

## Format eines Befunds

```markdown
### evd-001

Aussage:
Das untersuchte Plugin unterstützt MUC-Gruppenchats.

Status:
DOCUMENTED

Quellen:

| Quellenart | Fundstelle | Version oder Commit | Prüfdatum | Beitrag zum Befund |
|---|---|---|---|---|
| PROJECT_DOCUMENTATION | README, Abschnitt „Features“ | Commit abc123 | YYYY-MM-DD | Behauptung der MUC-Unterstützung |


Prüfung:
Noch kein Funktionstest durchgeführt.

Folgerung:
Die behauptete MUC-Unterstützung muss während der Bestandsaufnahme im
Quellcode und durch einen Integrationstest geprüft werden.
```
