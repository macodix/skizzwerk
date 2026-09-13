---
document: idea
process_phase: swk-01
project: "openclaw-xmpp"
status: draft
created: 2026-09-13
last_updated: 2026-09-13
---

# Projektidee

## 1. Originalbeschreibung

Ein XMPP-Plugin für aktuelle OpenClaw-Versionen entwickeln.

Das Plugin muss muss Direktnachrichten, OMEMO-Verschlüsselung und
Gruppenchats über MUC unterstützen.

Vorhandene GitHub-Projekte sollen als mögliche Grundlage untersucht werden.

Für neue OpenClaw-Versionen wird ein Verfahren zur automatischen
Aktualisierung oder Kompatibilitätssicherung benötigt. Dies kann ggf. auch
mit KI-Agenten unterstützt werden.

## 2. Herkunft und Kontext

- Verfasser: Martin Henkel
- Datum: 2026-09-13
- ergänzende Gespräche oder Dokumente:
- bekannte Ausgangssituation:
  - Ein eigener XMPP-Server ist vorhanden
  - z. Z. sind 2 OpenClaw Installationen, Versionen 2026.9.4 und  2026.7.1-2, aktiv
  - bestehende Plugins konnten z. T. nicht installiert werden
    oder erfüllten nicht die Anforderungen an Sicherheit (OMEMO)
    oder Kommunikation (Gruppenchats/MUC)
  - darüber hinaus dient dieses Projekt auch als Pilot für das
    Projekt skizzwerk

## 3. Verstandenes Ziel

Kennzeichnung der Aussagen nach `rules/evidence.md`: `USER_PROVIDED (Original)`
stammt aus Abschnitt 1, `USER_PROVIDED (Kontext)` aus Abschnitt 2, `INFERRED`
ist eine Ableitung durch skizzwerk, `UNKNOWN` ist aus der Eingabe nicht
ableitbar.

Für aktuelle OpenClaw-Versionen soll ein XMPP-Plugin entstehen, das
Direktnachrichten, OMEMO-Verschlüsselung und Gruppenchats über MUC unterstützt.
Das Plugin soll auch mit neuen OpenClaw-Versionen nutzbar bleiben. Daneben
dient das Projekt als Pilot für skizzwerk. `INFERRED`

Diese Darstellung ist eine Interpretation der Originalbeschreibung.

## 4. Erwarteter Nutzen

- Die Eingabe nennt keinen Nutzen ausdrücklich. `UNKNOWN`
- OpenClaw kann über XMPP genutzt werden, mit OMEMO-Verschlüsselung und
  Gruppenchats über MUC. Bestehende Plugins leisteten dies laut Kontext nicht
  oder waren nicht installierbar. `INFERRED`
- Das Plugin bleibt bei neuen OpenClaw-Versionen nutzbar. `INFERRED`
- Das Projekt liefert Erfahrungen für skizzwerk. `INFERRED`

## 5. Genannter Projektgegenstand

- Ein XMPP-Plugin für aktuelle OpenClaw-Versionen soll entwickelt werden.
  `USER_PROVIDED (Original)`
- Für neue OpenClaw-Versionen wird ein Verfahren zur automatischen
  Aktualisierung oder Kompatibilitätssicherung benötigt.
  `USER_PROVIDED (Original)`
- Vorhandene GitHub-Projekte sollen als mögliche Grundlage untersucht werden.
  `USER_PROVIDED (Original)`
- Ob die Untersuchung Teil des Projektgegenstands oder nur Vorarbeit ist, geht
  aus der Eingabe nicht hervor. `UNKNOWN`

## 6. Genannte Nutzer und beteiligte Systeme

| Nutzer oder System | Genannte Rolle |
|---|---|
| Martin Henkel | Verfasser der Idee `USER_PROVIDED (Kontext)` |
| OpenClaw | System, für das das Plugin entwickelt wird `USER_PROVIDED (Original)` |
| 2 OpenClaw-Installationen (2026.9.4 und 2026.7.1-2) | zurzeit aktiv; Rolle für das Plugin nicht genannt `USER_PROVIDED (Kontext)` |
| XMPP | Kommunikationsweg des Plugins `USER_PROVIDED (Original)` |
| eigener XMPP-Server | vorhanden; Rolle für das Plugin nicht genannt `USER_PROVIDED (Kontext)` |
| bestehende Plugins | teils nicht installierbar, teils ohne OMEMO oder MUC `USER_PROVIDED (Kontext)` |
| vorhandene GitHub-Projekte | mögliche Grundlage `USER_PROVIDED (Original)` |
| KI-Agenten | können das Aktualisierungsverfahren gegebenenfalls unterstützen `USER_PROVIDED (Original)` |
| skizzwerk | Projekt, für das dieses Projekt als Pilot dient `USER_PROVIDED (Kontext)` |
| Nutzer des Plugins und Chatpartner | nicht genannt `UNKNOWN` |

## 7. Genannte Funktionen

- Direktnachrichten `USER_PROVIDED (Original)`
- OMEMO-Verschlüsselung `USER_PROVIDED (Original)`
- Gruppenchats über MUC `USER_PROVIDED (Original)`
- Verfahren zur automatischen Aktualisierung oder Kompatibilitätssicherung für
  neue OpenClaw-Versionen `USER_PROVIDED (Original)`
- gegebenenfalls Unterstützung dieses Verfahrens durch KI-Agenten
  `USER_PROVIDED (Original)`

## 8. Genannte Einschränkungen

- Das Plugin ist für aktuelle OpenClaw-Versionen bestimmt.
  `USER_PROVIDED (Original)`
- Direktnachrichten, OMEMO-Verschlüsselung und Gruppenchats über MUC sind als
  „muss“ genannt. `USER_PROVIDED (Original)`
- Zurzeit sind die OpenClaw-Versionen 2026.9.4 und 2026.7.1-2 im Einsatz.
  `USER_PROVIDED (Kontext)`
- Die Unterstützung durch KI-Agenten ist mit „kann ggf.“ genannt, also nicht
  zwingend. `INFERRED`

## 9. Ausdrücklich ausgeschlossen

- Die Eingabe nennt keine ausgeschlossenen Inhalte. `UNKNOWN`

## 10. Unklare Begriffe und mögliche Mehrdeutigkeiten

| Begriff oder Aussage | Unklarheit | Mögliche Auswirkung |
|---|---|---|
| „aktuelle OpenClaw-Versionen“ | Welche Versionen gemeint sind, ist offen. Ob 2026.7.1-2 dazugehört, ist offen. | Umfang der zu unterstützenden Versionen |
| „neue OpenClaw-Versionen“ | Abgrenzung zu „aktuelle OpenClaw-Versionen“ ist offen. | Umfang des Aktualisierungsverfahrens |
| „automatische Aktualisierung oder Kompatibilitätssicherung“ | Ob beides oder eines von beiden gemeint ist, ist offen. Was aktualisiert wird und was „automatisch“ umfasst, ist offen. | Projektumfang und Aufwand |
| „Dies kann ggf. auch mit KI-Agenten unterstützt werden“ | Ob KI-Agenten erwünscht oder nur möglich sind, ist offen. | Umfang des Verfahrens |
| „unterstützen“ (Plugin muss … unterstützen) | Welcher Funktionsumfang je Funktion gemeint ist, ist nicht beschrieben. | Abgrenzung, wann eine Funktion als erfüllt gilt |
| „Direktnachrichten“ | Zwischen wem die Nachrichten ausgetauscht werden, ist nicht genannt. | Nutzerkreis |
| „OMEMO-Verschlüsselung“ | Ob sie für Direktnachrichten, Gruppenchats oder beide gilt, ist offen. | Funktionsumfang |
| „Anforderungen an Sicherheit (OMEMO)“ | Ob Sicherheit über OMEMO hinaus gemeint ist, ist offen. | Umfang der Sicherheitsanforderungen |
| „als mögliche Grundlage untersucht“ | Ob Übernahme, Weiterentwicklung oder nur Vorlage gemeint ist, ist offen. Welche Projekte gemeint sind, ist offen. | Vorgehen und Umfang der Bestandsuntersuchung |
| „entwickeln“ | Ob Neuentwicklung oder Anpassung eines vorhandenen Projekts gemeint ist, ist offen. | Projektumfang |
| „Ein eigener XMPP-Server ist vorhanden“ | Ob das Plugin mit diesem Server arbeiten soll, ist nicht genannt. | beteiligte Systeme |
| „2 OpenClaw Installationen … aktiv“ | Ob das Plugin auf beiden Installationen laufen soll, ist nicht genannt. | Umfang der zu unterstützenden Versionen |
| „konnten z. T. nicht installiert werden“ | Ursache und Bedeutung für dieses Projekt sind nicht genannt. | Bewertung vorhandener Projekte |
| „Pilot für das Projekt skizzwerk“ | Ob daraus Vorgaben für dieses Projekt folgen, ist offen. | Vorgehen |

## 11. Abgrenzung zu Annahmen

In dieser Datei werden keine stillschweigenden Annahmen als Bestandteil der
Idee behandelt. Notwendige Annahmen werden in `assumptions.md` erfasst.

Erkannte Annahmen, Status `identified`, Nachweisstatus `ASSUMED`. Sie sind noch
nicht in `assumptions.md` erfasst, weil diese Datei für das Projekt nicht
existiert. Kennungen werden bei der Erfassung vergeben.

- Das Plugin soll mit dem eigenen XMPP-Server betrieben werden.
- Das Plugin soll auf beiden aktiven OpenClaw-Installationen laufen.
- „Aktuelle OpenClaw-Versionen“ umfasst mindestens Version 2026.9.4.
- OMEMO-Verschlüsselung soll auch in Gruppenchats über MUC gelten.
- Kein vorhandenes GitHub-Projekt erfüllt bereits alle genannten Funktionen.

## 12. Prüfergebnis SKW-01

- [x] Originalbeschreibung wurde unverändert übernommen.
- [x] Interpretation und Original sind klar getrennt.
- [x] Keine zusätzlichen Anforderungen wurden erfunden.
- [x] Keine technische Lösung wurde vorweggenommen.
- [x] Unklare Begriffe wurden gekennzeichnet.
- [x] Genannte Ziele, Funktionen und Einschränkungen wurden vollständig erfasst.

Prüfung gegen die Qualitätsgrenze swk-01 in `rules/quality-gates.md`:

- [x] Originalbeschreibung unverändert erhalten
- [x] Herkunft und Kontext unverändert erhalten
- [x] Originalaussagen und Interpretationen klar getrennt
- [x] Ziel und erwarteter Nutzen aus der Eingabe abgeleitet
- [x] genannte Nutzer, Systeme, Funktionen und Einschränkungen erfasst
- [x] mehrdeutige Begriffe sichtbar gekennzeichnet
- [x] keine Annahme als Tatsache dargestellt
- [x] keine zusätzliche Anforderung erfunden
- [x] keine Architekturentscheidung getroffen
- [x] keine konkrete technische Lösung ausgewählt
- [x] offene Punkte sichtbar

Mangel: Die erkannten Annahmen sind nicht nach `rules/assumptions.md` in
`assumptions.md` erfasst, weil die Datei fehlt. Die Bearbeitung ist deshalb
nicht abgeschlossen; der Status bleibt `draft`.

## 13. Freigabestatus

- Ergebnis: `offen`
- geprüft am:
- geprüft durch:
- Anmerkungen:
