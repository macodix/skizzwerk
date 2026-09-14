# Umgang mit Annahmen

## Definition

Eine Annahme ist eine Aussage, die für die weitere Bearbeitung verwendet
werden könnte, aber weder ausdrücklich vorgegeben noch ausreichend belegt ist.

## Regeln

- Annahmen dürfen nicht als Tatsachen oder Anforderungen dargestellt werden.
- Jede erkannte Annahme muss ausdrücklich als Annahme gekennzeichnet werden.
- Annahmen werden zentral in der projektspezifischen `assumptions.md` verwaltet.
- In anderen Dokumenten wird nur über ihre Kennung auf sie verwiesen.
- Die KI darf reversible Annahmen vorschlagen, aber nicht stillschweigend setzen.
- Annahmen mit wesentlicher Auswirkung benötigen eine Entscheidung.
- Widerlegte oder bestätigte Annahmen bleiben aus Gründen der Nachvollziehbarkeit erhalten.

## Abgrenzung

Eine Annahme ist eine unbestätigte Aussage, die als vorläufige Arbeitsgrundlage
für die weitere Bearbeitung benötigt wird.

Keine Annahmen sind:

- unmittelbar aus der Eingabe folgende Aussagen,
- reine Umformulierungen der Eingabe,
- unbekannte Sachverhalte, die vorerst nicht als Arbeitsgrundlage benötigt werden,
- zu untersuchende Tatsachenfragen,
- bloße Möglichkeiten oder Hypothesen.

Im Zweifel wird ein Sachverhalt als `UNKNOWN` dokumentiert und nicht als
Annahme angelegt.

## Angaben pro Annahme

Jede Annahme erhält:

- eindeutige Kennung
- Aussage
- Herkunft oder Anlass
- Begründung
- Auswirkung bei Irrtum
- Bedeutung für den weiteren Prozess
- Status
- gegebenenfalls zugehörige Entscheidung

## Zugehörige Entscheidungen

Für das Feld `Zugehörige Entscheidung` sind folgende Werte zulässig:

- `noch nicht vorhanden`, wenn eine Entscheidung erforderlich ist, aber noch
  nicht getroffen wurde;
- `nicht erforderlich`, wenn keine Entscheidung benötigt wird;
- eine gültige `dec-nnn`-Kennung, sobald die Entscheidung dokumentiert ist.

Der Wert `keine` ist unzulässig. Er unterscheidet nicht zwischen einer noch
ausstehenden und einer nicht erforderlichen Entscheidung.

Die Angabe muss mit dem Feld `Entscheidung erforderlich` in der
Annahmenübersicht übereinstimmen.

## Statuswerte

| Status | Bedeutung |
|---|---|
| `identified` | Annahme wurde erkannt. |
| `proposed` | Annahme wurde als vorläufige Arbeitsgrundlage vorgeschlagen. |
| `accepted` | Annahme wurde ausdrücklich bestätigt. |
| `rejected` | Annahme wurde ausdrücklich verworfen. |
| `verified` | Annahme wurde durch einen belastbaren Nachweis bestätigt. |
| `superseded` | Annahme wurde durch eine neuere Aussage ersetzt. |

## Einschränkung für swk-01

Während `swk-01` werden Annahmen nur erkannt und gekennzeichnet.

Sie dürfen in dieser Phase:

- nicht als Anforderung übernommen,
- nicht technisch umgesetzt,
- nicht selbstständig bestätigt werden.
