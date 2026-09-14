---
document: idea
process_phase: swk-01
project: "openclaw-xmpp"
status: review
created: 2026-09-13
last_updated: 2026-09-14
---

# Projektidee

## 1. Originalbeschreibung

Ein XMPP-Plugin für aktuelle OpenClaw-Versionen entwickeln.

Das Plugin muss Direktnachrichten, OMEMO-Verschlüsselung und
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

Kennzeichnung nach `rules/evidence.md`:

- `USER_PROVIDED (Original)`: Aussage aus Abschnitt 1
- `USER_PROVIDED (Kontext)`: Aussage aus Abschnitt 2
- `INFERRED`: Ableitung oder Interpretation durch skizzwerk
- `UNKNOWN`: Sachverhalt, zu dem die Eingabe keine Information enthält
- `asm-nnn`: Kennung einer Annahme in `assumptions.md`

Ein XMPP-Plugin für aktuelle OpenClaw-Versionen soll entstehen. Es soll die in
Abschnitt 7 genannten Funktionen erfüllen und auch mit neuen
OpenClaw-Versionen nutzbar bleiben. Daneben dient das Projekt als Pilot für
skizzwerk. `INFERRED`

Diese Darstellung ist eine Interpretation der Originalbeschreibung.

## 4. Erwarteter Nutzen

- Die in Abschnitt 2 beschriebene Lage wird behoben: Bestehende Plugins
  konnten teils nicht installiert werden oder erfüllten die Anforderungen an
  Sicherheit oder Kommunikation nicht. `INFERRED`
- Neue OpenClaw-Versionen machen das Plugin nicht unbrauchbar. `INFERRED`
- Das Projekt liefert als Pilot Erfahrungen für skizzwerk. `INFERRED`

## 5. Genannter Projektgegenstand

- Ein XMPP-Plugin für aktuelle OpenClaw-Versionen soll entwickelt werden.
  `USER_PROVIDED (Original)`
- Für neue OpenClaw-Versionen wird ein Verfahren zur automatischen
  Aktualisierung oder Kompatibilitätssicherung benötigt.
  `USER_PROVIDED (Original)`
- Vorhandene GitHub-Projekte sollen als mögliche Grundlage untersucht werden.
  `USER_PROVIDED (Original)`

## 6. Genannte Nutzer und beteiligte Systeme

| Nutzer oder System | Genannte Rolle |
|---|---|
| Martin Henkel | Verfasser der Idee `USER_PROVIDED (Kontext)` |
| OpenClaw | System, für das das Plugin entwickelt wird `USER_PROVIDED (Original)` |
| 2 OpenClaw-Installationen (2026.9.4 und 2026.7.1-2) | zurzeit aktiv; Rolle für das Plugin nicht genannt `USER_PROVIDED (Kontext)` |
| eigener XMPP-Server | vorhanden; Rolle für das Plugin nicht genannt `USER_PROVIDED (Kontext)` |
| bestehende Plugins | konnten teils nicht installiert werden oder erfüllten nicht die Anforderungen an Sicherheit (OMEMO) oder Kommunikation (Gruppenchats/MUC) `USER_PROVIDED (Kontext)` |
| vorhandene GitHub-Projekte | mögliche Grundlage `USER_PROVIDED (Original)` |
| KI-Agenten | können das Verfahren für neue OpenClaw-Versionen gegebenenfalls unterstützen `USER_PROVIDED (Original)` |
| skizzwerk | Projekt, für das dieses Projekt als Pilot dient `USER_PROVIDED (Kontext)` |

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
- Direktnachrichten, OMEMO-Verschlüsselung und Gruppenchats über MUC sind mit
  „muss“ genannt. `USER_PROVIDED (Original)`

## 9. Ausdrücklich ausgeschlossen

- Abschnitt 1 und 2 nennen keine ausgeschlossenen Inhalte. Ob Inhalte
  ausgeschlossen sind, ist unbekannt. `UNKNOWN`

## 10. Unklare Begriffe und mögliche Mehrdeutigkeiten

Die erste Spalte zitiert Abschnitt 1 oder 2. Die Angaben zu Unklarheit und
möglicher Auswirkung sind Ableitungen. `INFERRED`

| Begriff oder Aussage | Unklarheit | Mögliche Auswirkung |
|---|---|---|
| „XMPP-Plugin“ | XMPP wird nur in diesem Wort genannt. Welche Rolle XMPP für das Plugin hat, ist nicht beschrieben (siehe asm-005). | Verständnis des Projektgegenstands |
| „aktuelle OpenClaw-Versionen“ | Welche Versionen gemeint sind, ist offen (siehe asm-003). | Umfang der zu unterstützenden Versionen |
| „neue OpenClaw-Versionen“ | Die Abgrenzung zu „aktuelle OpenClaw-Versionen“ ist offen. | Umfang des Verfahrens für neue Versionen |
| „automatische Aktualisierung oder Kompatibilitätssicherung“ | Ob beides oder eines von beiden gemeint ist, ist offen. Was aktualisiert wird und was „automatisch“ umfasst, ist offen. | Projektumfang und Aufwand |
| „Dies kann ggf. auch mit KI-Agenten unterstützt werden“ | Ob KI-Agenten erwünscht oder nur möglich sind, ist offen. | Umfang des Verfahrens |
| „unterstützen“ (Das Plugin muss … unterstützen) | Welcher Funktionsumfang je Funktion gemeint ist, ist nicht beschrieben. | Abgrenzung, wann eine Funktion als erfüllt gilt |
| „OMEMO-Verschlüsselung“ | Ob sie für Direktnachrichten, Gruppenchats oder beide gilt, ist offen (siehe asm-004). | Funktionsumfang |
| „Anforderungen an Sicherheit (OMEMO)“ | Ob Sicherheit über OMEMO hinaus gemeint ist, ist offen. | Umfang der Sicherheitsanforderungen |
| „als mögliche Grundlage untersucht“ | Ob Übernahme, Weiterentwicklung oder nur Vorlage gemeint ist, ist offen. Welche Projekte gemeint sind, ist offen. Ob die Untersuchung Teil des Projektgegenstands oder Vorarbeit ist, ist offen. | Vorgehen und Projektumfang |
| „entwickeln“ | Ob Neuentwicklung oder Anpassung eines vorhandenen Projekts gemeint ist, ist offen. | Projektumfang |
| „Ein eigener XMPP-Server ist vorhanden“ | Ob das Plugin mit diesem Server arbeiten soll, ist nicht genannt (siehe asm-001). | beteiligte Systeme |
| „2 OpenClaw Installationen … aktiv“ | Ob das Plugin auf beiden Installationen laufen soll, ist nicht genannt (siehe asm-002). | Umfang der zu unterstützenden Versionen |
| „Pilot für das Projekt skizzwerk“ | Ob daraus Vorgaben für dieses Projekt folgen, ist offen. | Vorgehen |

## 11. Abgrenzung zu Annahmen

In dieser Datei werden keine stillschweigenden Annahmen als Bestandteil der
Idee behandelt. Notwendige Annahmen werden in `assumptions.md` erfasst.

Erkannte Annahmen: asm-001, asm-002, asm-003, asm-004, asm-005.

### Unbekannte Sachverhalte

Diese Punkte sind keine Annahmen. Die Eingabe enthält dazu keine Information.

- Ob ein vorhandenes GitHub-Projekt alle genannten Funktionen erfüllt, ist
  unbekannt. `UNKNOWN`
- Welche bestehenden Plugins erprobt wurden und woran ihre Installation
  scheiterte, ist unbekannt. `UNKNOWN`
- Wer das Plugin nutzt und mit wem darüber kommuniziert wird, ist unbekannt.
  `UNKNOWN`
- Welchen Nutzen der Ideengeber ausdrücklich erwartet, ist unbekannt.
  `UNKNOWN`
- Ob und wie oft neue OpenClaw-Versionen Änderungen bringen, die das Plugin
  betreffen, ist unbekannt. `UNKNOWN`

## 12. Prüfergebnis swk-01

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

Ergebnis: Alle Kriterien sind erfüllt. Die Annahmen sind mit Kennung in
`assumptions.md` erfasst. Das Dokument erhält den Status `review`.

## 13. Freigabestatus

- Ergebnis: `offen`
- geprüft am:
- geprüft durch:
- Anmerkungen:
