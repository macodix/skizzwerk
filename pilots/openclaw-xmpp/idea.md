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

- Die Betreiber der vorhandenen OpenClaw-Installationen sind nicht mehr auf
  bestehende Plugins angewiesen, die sich teils nicht installieren ließen oder
  ihren Ansprüchen nicht genügten. `INFERRED`
- Die Betreiber können neue OpenClaw-Versionen einsetzen, ohne die
  XMPP-Anbindung jedes Mal selbst wiederherstellen zu müssen. `INFERRED`
- Das Projekt skizzwerk erhält Erfahrungen aus einem echten Vorhaben.
  `INFERRED`

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
| „aktuelle OpenClaw-Versionen“ | Welche Versionen gemeint sind, ist offen. Abschnitt 2 nennt zwei aktive Installationen mit unterschiedlichen Versionen. | Projektumfang: Anzahl der zu unterstützenden Versionen; Abnahme: auf welchen Versionen geprüft wird |
| „automatische Aktualisierung oder Kompatibilitätssicherung“ | Ob beides oder eines von beiden gemeint ist, ist offen. | Projektumfang: ein oder zwei Verfahren; spätere Entscheidung zwischen beiden |
| „Dies kann ggf. auch mit KI-Agenten unterstützt werden“ | Ob KI-Agenten erwünscht oder nur möglich sind, ist offen. | Anforderungen: KI-Unterstützung verpflichtend oder freiwillig |
| „unterstützen“ (Das Plugin muss … unterstützen) | Welcher Funktionsumfang je Funktion gemeint ist, ist nicht beschrieben. | Abnahme: wann eine Funktion als erfüllt gilt |
| „OMEMO-Verschlüsselung“ | Ob sie für Direktnachrichten, Gruppenchats über MUC oder beide gilt, ist offen. Abschnitt 1 nennt beide nebeneinander. | Anforderungen und Abnahme: Verschlüsselung in Gruppenchats ja oder nein |
| „als mögliche Grundlage untersucht“ | Ob ein vorhandenes Projekt übernommen, weiterentwickelt oder nur als Vorlage genutzt werden soll, ist offen. | Projektumfang: Neuentwicklung oder Anpassung; spätere Entscheidung über die Grundlage |

## 11. Abgrenzung zu Annahmen

In dieser Datei werden keine stillschweigenden Annahmen als Bestandteil der
Idee behandelt. Notwendige Annahmen werden in `assumptions.md` erfasst.

Aktive Annahmen: keine. Die früher erfassten Annahmen asm-001 bis asm-005
sind in `assumptions.md` als `superseded` geführt. `INFERRED`

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
- Ob das Plugin mit dem vorhandenen eigenen XMPP-Server arbeiten soll, ist
  unbekannt. `UNKNOWN`
- Ob das Plugin auf beiden aktiven OpenClaw-Installationen laufen soll, ist
  unbekannt. `UNKNOWN`

## 12. Prüfergebnis swk-01

- [x] Originalbeschreibung wurde unverändert übernommen.
- [x] Interpretation und Original sind klar getrennt.
- [x] Keine zusätzlichen Anforderungen wurden erfunden.
- [x] Keine technische Lösung wurde vorweggenommen.
- [x] Unklare Begriffe wurden gekennzeichnet.
- [x] Genannte Ziele, Funktionen und Einschränkungen wurden vollständig erfasst.

Vorprüfung nach `phases/swk-01-idea.md`: bestanden. Alle referenzierten
Dateien existieren und sind nicht leer. Regeln und Vorlagen verwenden gültige
Kennungen. Abschnitt 1 und 2 sind ausgefüllt.

Prüfung gegen die Qualitätsgrenze swk-01 in `rules/quality-gates.md`:

- [x] Originalbeschreibung unverändert erhalten
- [x] Herkunft und Kontext unverändert erhalten
- [x] Originalaussagen und Interpretationen klar getrennt
- [x] Ziel und erwarteter Nutzen aus der Eingabe abgeleitet
- [x] erwarteter Nutzen von Funktionen und Qualitätszielen getrennt
- [x] genannte Nutzer, Systeme, Funktionen und Einschränkungen erfasst
- [x] mehrdeutige Begriffe sichtbar gekennzeichnet
- [x] jede genannte Mehrdeutigkeit hat eine konkrete wesentliche Auswirkung
- [x] keine Annahme als Tatsache dargestellt
- [x] keine zusätzliche Anforderung erfunden
- [x] keine Architekturentscheidung getroffen
- [x] keine konkrete technische Lösung ausgewählt
- [x] offene Punkte sichtbar
- [x] alle Kennungen entsprechen `rules/identifiers.md`
- [x] Annahmen von Ableitungen und unbekannten Sachverhalten abgegrenzt
- [x] jede in `idea.md` referenzierte Annahme existiert in `assumptions.md`
- [x] vorhandene `assumptions.md` in Übersichts- und Einzelangaben widerspruchsfrei
- [x] `idea.md` entspricht `templates/idea.md`
- [x] vorhandene `assumptions.md` entspricht `templates/assumptions.md`
- [x] ohne erkannte Annahmen keine `assumptions.md` erforderlich

Ergebnis: Alle Kriterien sind erfüllt. Zurzeit ist keine Annahme aktiv. Die
vorhandene `assumptions.md` enthält nur die als `superseded` geführten
asm-001 bis asm-005 und bleibt zur Nachvollziehbarkeit erhalten. Das Dokument
erhält den Status `review`.

## 13. Freigabestatus

- Ergebnis: `offen`
- geprüft am:
- geprüft durch:
- Anmerkungen:
