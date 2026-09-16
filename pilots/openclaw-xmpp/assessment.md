---
document: assessment
process_phase: swk-03
project: "openclaw-xmpp"
status: review
created: 2026-09-16
last_updated: 2026-09-16
basis:
  - idea.md
  - inventory.json
---

# Bewertung der Befunde

## 1. Bewertungsauftrag

Bewertet wird, welche Bedeutung die in der akzeptierten Bestandsuntersuchung
dokumentierten Befunde für die akzeptierte Projektidee haben. Verwendet werden
ausschließlich die akzeptierte `pilots/openclaw-xmpp/idea.md`, die akzeptierte
`pilots/openclaw-xmpp/inventory.json` und die daraus erzeugte
`pilots/openclaw-xmpp/inventory.md`. Eine projektspezifische `assumptions.md`
existiert für dieses Projekt nicht.

In dieser Phase wurde keine neue Bestandsrecherche durchgeführt. Es wurde kein
Befund verändert und kein Nachweisstatus umgestuft. Es wurde keine Anforderung
formuliert, keine Alternative ausgewählt und keine Architektur-, Technologie-
oder Umsetzungsentscheidung getroffen. Es werden keine Rangfolgen, Gewichtungen,
Gesamtnoten oder numerischen Scores verwendet, weil dafür keine Bewertungsmethode
festgelegt ist.

Aussagen, die über einen einzelnen Befund hinausgehen, stehen je Aspekt unter
„Ableitung“ und nennen ihre Befundgrundlage.

## 2. Bewertungsgrundlage

- akzeptierte `idea.md`: `pilots/openclaw-xmpp/idea.md`, Status `accepted`, bestätigt am 2026-09-14, Commit 4e46961
- akzeptierte `inventory.json`: `pilots/openclaw-xmpp/inventory.json`, Status `accepted`, angenommen am 2026-09-16 durch Martin Henkel; 54 Befunde `evd-001` bis `evd-054`
- projektspezifische `assumptions.md`, sofern vorhanden: nicht vorhanden; nach `pilots/openclaw-xmpp/idea.md` Abschnitt 11 wurden in swk-01 keine Annahmen erkannt. Es gibt daher keine `asm-nnn`, die nach `rules/assumptions.md` auf einen Entscheidungsbedarf zu prüfen wären.
- Stand der Bestandsuntersuchung: Untersuchung vom 2026-09-14, am 2026-09-15 unverändert in das strukturierte Format übertragen; Registerdaten, Commits und Trefferzahlen gelten für den 2026-09-14

## 3. Bewertungsaspekte

| Aspekt | Bezug zur idea.md | Relevante Befunde |
|---|---|---|
| Direktnachrichten | Abschnitt 7 („Direktnachrichten“), Abschnitt 1 | evd-022, evd-023, evd-024, evd-025, evd-027, evd-028, evd-030, evd-031, evd-033, evd-034, evd-035, evd-036, evd-037, evd-038, evd-039, evd-040, evd-042, evd-043, evd-044, evd-045, evd-046, evd-047, evd-048, evd-049, evd-050, evd-051, evd-052 |
| OMEMO-Verschlüsselung | Abschnitt 7 („OMEMO-Verschlüsselung“), Abschnitt 8, Abschnitt 10 | evd-023, evd-024, evd-025, evd-027, evd-028, evd-030, evd-031, evd-033, evd-034, evd-035, evd-036, evd-038, evd-039, evd-040, evd-041, evd-042, evd-043, evd-044, evd-045, evd-047, evd-049, evd-051, evd-052 |
| Gruppenchats über MUC | Abschnitt 7 („Gruppenchats über MUC“), Abschnitt 8 | evd-008, evd-023, evd-024, evd-025, evd-027, evd-028, evd-030, evd-031, evd-033, evd-034, evd-035, evd-036, evd-037, evd-038, evd-039, evd-040, evd-042, evd-043, evd-044, evd-045, evd-047, evd-048, evd-049, evd-051, evd-052 |
| XMPP im Lieferumfang und im Hauptprojekt von OpenClaw | Abschnitt 1 („Ein XMPP-Plugin für aktuelle OpenClaw-Versionen“), Abschnitt 5 | evd-005, evd-018, evd-019, evd-020, evd-054 |
| Anbindungspunkt für ein Plugin in den genannten Versionen | Abschnitt 1, Abschnitt 5, Abschnitt 8, Abschnitt 10 („aktuelle OpenClaw-Versionen“) | evd-001, evd-004, evd-006, evd-009, evd-011, evd-012, evd-013, evd-022, evd-029, evd-032, evd-033, evd-035, evd-037, evd-039, evd-042, evd-044, evd-046, evd-048, evd-050, evd-053 |
| Verfahren für neue OpenClaw-Versionen | Abschnitt 1 („Verfahren zur automatischen Aktualisierung oder Kompatibilitätssicherung“), Abschnitt 7, Abschnitt 11 | evd-010, evd-011, evd-013, evd-014, evd-015, evd-016, evd-017 |
| Belastbarkeit der Angaben vorhandener Projekte | Abschnitt 1 („Vorhandene GitHub-Projekte sollen als mögliche Grundlage untersucht werden“), Abschnitt 10 | evd-024, evd-026, evd-027, evd-028, evd-029, evd-030, evd-031, evd-032, evd-033, evd-034, evd-035, evd-036, evd-039, evd-040, evd-041, evd-042, evd-052, evd-053, evd-054 |
| Betriebsumfeld: eigener XMPP-Server und bisherige Versuche | Abschnitt 2, Abschnitt 6, Abschnitt 11 | evd-002, evd-003, evd-004, evd-005, evd-006, evd-007, evd-008 |

## 4. Bewertung nach Aspekten

### Direktnachrichten

Bezug zur `idea.md`:
Abschnitt 7 nennt Direktnachrichten als Funktion, Abschnitt 8 führt sie unter den
mit „muss“ genannten Funktionen. Abschnitt 10 hält offen, welcher Funktionsumfang
mit „unterstützen“ gemeint ist.

Verwendete Befunde:
- `evd-022`, `evd-023`, `evd-024`, `evd-025`, `evd-027`, `evd-028`, `evd-030`, `evd-031`, `evd-033`, `evd-034`, `evd-035`, `evd-036`, `evd-037`, `evd-038`, `evd-039`, `evd-040`, `evd-042`, `evd-043`, `evd-044`, `evd-045`, `evd-046`, `evd-047`, `evd-048`, `evd-049`, `evd-050`, `evd-051`, `evd-052`

Feststellbare positive Beiträge:
- In allen dreizehn untersuchten Projekten ist Code für 1:1-Nachrichten vorhanden: `evd-023`, `evd-025`, `evd-028`, `evd-031`, `evd-034`, `evd-036`, `evd-038`, `evd-040`, `evd-043`, `evd-045`, `evd-047`, `evd-049`, `evd-051`.
- Die Dokumentation der Projekte nennt Direktnachrichten durchgängig als Funktion: `evd-022`, `evd-024`, `evd-027`, `evd-030`, `evd-033`, `evd-035`, `evd-037`, `evd-039`, `evd-042`, `evd-044`, `evd-046`, `evd-048`, `evd-050`.

Feststellbare Einschränkungen oder Nachteile:
- Die Angaben sind dokumentierte Behauptungen und vorhandener Code; keine dieser Angaben ist praktisch bestätigt (`evd-052`).
- `rsaisankalp/clawdbotElyments` bindet nicht OpenClaw, sondern Clawdbot an eine andere Plattform an (`evd-050`); es ist für diesen Aspekt nur als Grenzfall erfasst.

Unbekannte oder nicht ausreichend untersuchte Punkte:
- Ob Direktnachrichten in einem der Projekte funktionsfähig sind, ist unbekannt (`evd-052`).
- Welcher Funktionsumfang nach `idea.md` Abschnitt 10 unter „unterstützen“ zu verstehen ist, ist nicht beschrieben; ein Abgleich mit den Befunden ist deshalb nur auf der Ebene „Code vorhanden“ möglich.

Bedeutung für spätere Entscheidungen:
- Direktnachrichten unterscheiden die vorhandenen Projekte nicht; sie sind für eine spätere Auswahl kein trennendes Merkmal, solange kein Funktionsnachweis vorliegt.

Ableitung:
- Aus `evd-023`, `evd-025`, `evd-028`, `evd-031`, `evd-034`, `evd-036`, `evd-038`, `evd-040`, `evd-043`, `evd-045`, `evd-047`, `evd-049` und `evd-051` folgt, dass diese Funktion in allen untersuchten Projekten angelegt ist. Die Ableitung reicht nur bis zum Vorhandensein von Code; `evd-052` begrenzt ihre Belastbarkeit.

### OMEMO-Verschlüsselung

Bezug zur `idea.md`:
Abschnitt 7 nennt OMEMO-Verschlüsselung als Funktion, Abschnitt 8 führt sie unter
den mit „muss“ genannten Funktionen. Abschnitt 2 nennt Sicherheit (OMEMO) als
Anforderung, an der bestehende Plugins scheiterten. Abschnitt 10 hält offen, ob
OMEMO für Direktnachrichten, für Gruppenchats oder für beides gelten soll.

Verwendete Befunde:
- `evd-023`, `evd-024`, `evd-025`, `evd-027`, `evd-028`, `evd-030`, `evd-031`, `evd-033`, `evd-034`, `evd-035`, `evd-036`, `evd-038`, `evd-039`, `evd-040`, `evd-041`, `evd-042`, `evd-043`, `evd-044`, `evd-045`, `evd-047`, `evd-049`, `evd-051`, `evd-052`

Feststellbare positive Beiträge:
- In fünf Projekten ist OMEMO-Code vorhanden: `toughworm/Openclaw-XMPP-Plugin` (`evd-025`), `icarito/openclaw-xmpp` (`evd-031`), `elmafioso79/xmpp-channel` (`evd-036`), `watkins-matt/xmpp-channel` (`evd-038`), `MrCPA/oc-xmpp` (`evd-043`).
- Zwei davon enthalten Code für den neueren Namensraum `urn:xmpp:omemo:2`: `evd-031`, `evd-043`.
- In `elmafioso79/xmpp-channel` ist OMEMO-Code auch für `groupchat` vorhanden (`evd-036`), in `watkins-matt/xmpp-channel` ist OMEMO-Code vorhanden (`evd-038`).

Feststellbare Einschränkungen oder Nachteile:
- In acht Projekten kommen OMEMO-Zeichenketten im untersuchten Quelltext nicht vor: `evd-028`, `evd-034`, `evd-040`, `evd-045`, `evd-047`, `evd-049`, `evd-051`, `evd-023`.
- `kazakhan/openclaw-xmpp` führt OMEMO in der eigenen Prüfliste als „Not Supported“ (`evd-027`), `soilDNRA/openclaw-xmpp` nennt OMEMO ausdrücklich als nicht unterstützt (`evd-033`), `Programmatore-Web/openclaw-xmpp-channel` schließt Ende-zu-Ende-Verschlüsselung aus und hat sie laut eigenem CHANGELOG entfernt (`evd-039`, `evd-041`).
- `toughworm/Openclaw-XMPP-Plugin` überspringt OMEMO bei `groupchat` (`evd-025`); die eigene Dokumentation nennt verschlüsselten Gruppenchat als offen (`evd-024`).
- `MrCPA/oc-xmpp` beschränkt OMEMO nach eigener Dokumentation auf Direktnachrichten und nennt Live-Tests als noch offen (`evd-042`).

Unbekannte oder nicht ausreichend untersuchte Punkte:
- Ob OMEMO in einem der Projekte funktionsfähig ist, ist unbekannt (`evd-052`).
- Ob die im Code von `MrCPA/oc-xmpp` angelegte Beschränkung auf Direktnachrichten zutrifft, wurde nicht geprüft (`evd-043`, dokumentierte nicht durchgeführte Prüfung).
- Ein fehlender Treffer nach OMEMO-Zeichenketten belegt nur das Fehlen der gesuchten Zeichenketten, nicht das Fehlen der Funktion (`evd-023`, `evd-028`, `evd-034`, `evd-040`, `evd-045`, `evd-047`, `evd-049`, `evd-051`).

Bedeutung für spätere Entscheidungen:
- OMEMO trennt die untersuchten Projekte deutlicher als Direktnachrichten; die Befundlage unterscheidet Projekte mit vorhandenem OMEMO-Code, Projekte mit ausdrücklichem Ausschluss und Projekte ohne Aussage.
- Die in `idea.md` Abschnitt 10 offene Frage, ob OMEMO auch in Gruppenchats gelten soll, wirkt unmittelbar darauf, welche Projekte für diesen Aspekt überhaupt in Betracht kommen. Sie ist in Abschnitt 8 als Entscheidungsbedarf aufgeführt.

Ableitung:
- Aus `evd-025`, `evd-036`, `evd-038`, `evd-039`, `evd-041` und `evd-042` folgt, dass OMEMO in Gruppenchats in den untersuchten Projekten seltener angelegt ist als OMEMO in Direktnachrichten. Die Aussage bleibt auf vorhandenen Code und dokumentierte Angaben beschränkt; `evd-052` begrenzt ihre Belastbarkeit.

### Gruppenchats über MUC

Bezug zur `idea.md`:
Abschnitt 7 nennt Gruppenchats über MUC als Funktion, Abschnitt 8 führt sie unter
den mit „muss“ genannten Funktionen. Abschnitt 2 nennt Kommunikation
(Gruppenchats/MUC) als Anforderung, an der bestehende Plugins scheiterten.

Verwendete Befunde:
- `evd-008`, `evd-023`, `evd-024`, `evd-025`, `evd-027`, `evd-028`, `evd-030`, `evd-031`, `evd-033`, `evd-034`, `evd-035`, `evd-036`, `evd-037`, `evd-038`, `evd-039`, `evd-040`, `evd-042`, `evd-043`, `evd-044`, `evd-045`, `evd-047`, `evd-048`, `evd-049`, `evd-051`, `evd-052`

Feststellbare positive Beiträge:
- In acht Projekten ist Code für MUC einschließlich eines Raumbeitritts vorhanden: `evd-028`, `evd-031`, `evd-036`, `evd-038`, `evd-040`, `evd-043`, `evd-045`, `evd-049`.
- Die Dokumentation nennt MUC oder Räume in `evd-027`, `evd-030`, `evd-035`, `evd-037`, `evd-039`, `evd-042`, `evd-044`, `evd-048`.

Feststellbare Einschränkungen oder Nachteile:
- In vier Projekten kommen MUC-Zeichenketten nicht vor oder nur in einem Hinweistext: `evd-023`, `evd-034`, `evd-047`, `evd-051`.
- `soilDNRA/openclaw-xmpp` nennt MUC ausdrücklich als nicht unterstützt und führt Gruppenchat-Optionen als bis zum Abschluss einer „MUC security gate“ nicht verfügbar (`evd-033`, `evd-034`).
- `toughworm/Openclaw-XMPP-Plugin` verarbeitet zwar `groupchat`, enthält aber keinen Raumbeitritt (`evd-025`), obwohl die Dokumentation Gruppenchat nennt (`evd-024`).
- `Programmatore-Web/openclaw-xmpp-channel` unterstützt laut Dokumentation nur fest eingestellte MUC-Räume (`evd-039`).
- `rsaisankalp/clawdbotElyments` verarbeitet `groupchat` ohne Raumbeitritt (`evd-051`).

Unbekannte oder nicht ausreichend untersuchte Punkte:
- Ob MUC in einem der Projekte funktionsfähig ist, ist unbekannt (`evd-052`).
- Ob der eigene XMPP-Server MUC bereitstellt, ist nicht untersucht (`evd-008`).

Bedeutung für spätere Entscheidungen:
- MUC trennt die untersuchten Projekte in solche mit angelegtem Raumbeitritt und solche ohne. Zusammen mit OMEMO ist dies der Aspekt mit den größten Unterschieden zwischen den Alternativen.

Ableitung:
- Aus `evd-025`, `evd-051` und `evd-034` folgt, dass die Verarbeitung des Nachrichtentyps `groupchat` und ein Raumbeitritt in den Befunden getrennt zu betrachten sind. Die Aussage stützt sich nur auf vorhandenen Code; ob ein Raumbeitritt für den gewünschten Betrieb nötig ist, wurde in `idea.md` nicht beschrieben.

### XMPP im Lieferumfang und im Hauptprojekt von OpenClaw

Bezug zur `idea.md`:
Abschnitt 1 nennt als Gegenstand ein XMPP-Plugin für aktuelle OpenClaw-Versionen,
Abschnitt 5 nennt dessen Entwicklung als Projektgegenstand.

Verwendete Befunde:
- `evd-005`, `evd-018`, `evd-019`, `evd-020`, `evd-054`

Feststellbare positive Beiträge:
- Keine, die sich auf eine vorhandene XMPP-Unterstützung durch den Hersteller stützen ließen.

Feststellbare Einschränkungen oder Nachteile:
- OpenClaw 2026.9.4 liefert keinen XMPP-Kanal mit (`evd-018`), und die Kanalübersicht der Dokumentation nennt kein XMPP-Plugin (`evd-019`).
- Im Hauptprojekt wurden drei Pull Requests für XMPP ohne Übernahme geschlossen, das Issue „[Feature]: XMPP support“ ist als `not_planned` geschlossen (`evd-020`).
- Die lokale Installationsdokumentation erwähnt XMPP nicht (`evd-005`).

Unbekannte oder nicht ausreichend untersuchte Punkte:
- Die Gründe für die Nichtübernahme der Pull Requests wurden nicht ausgewertet (`evd-020`, dokumentierte nicht durchgeführte Prüfung).
- Ob es XMPP-Anbindungen außerhalb von GitHub und npm gibt, etwa auf ClawHub, ist unbekannt (`evd-054`).

Bedeutung für spätere Entscheidungen:
- Eine XMPP-Anbindung muss nach der vorliegenden Befundlage aus einem Projekt außerhalb des Lieferumfangs kommen oder neu entstehen. Welche der beiden Wege gewählt wird, ist in Abschnitt 8 als Entscheidungsbedarf aufgeführt und wird hier nicht entschieden.

Ableitung:
- Aus `evd-018`, `evd-019` und `evd-020` folgt, dass zum Untersuchungszeitpunkt keine vom Hersteller getragene XMPP-Anbindung vorliegt. Der geschlossene Feature-Wunsch (`evd-020`) belegt nur den Status, nicht die künftige Ausrichtung des Herstellers.

### Anbindungspunkt für ein Plugin in den genannten Versionen

Bezug zur `idea.md`:
Abschnitt 1 nennt „aktuelle OpenClaw-Versionen“ als Ziel, Abschnitt 8 nennt dies
als Einschränkung, Abschnitt 2 nennt die aktiven Versionen 2026.9.4 und
2026.7.1-2, Abschnitt 10 hält offen, welche Versionen gemeint sind.

Verwendete Befunde:
- `evd-001`, `evd-004`, `evd-006`, `evd-009`, `evd-011`, `evd-012`, `evd-013`, `evd-022`, `evd-029`, `evd-032`, `evd-033`, `evd-035`, `evd-037`, `evd-039`, `evd-042`, `evd-044`, `evd-046`, `evd-048`, `evd-050`, `evd-053`

Feststellbare positive Beiträge:
- In 2026.9.4 ist eine Schnittstelle für Kanal-Plugins vorhanden (`evd-012`), und die Dokumentation beschreibt Manifest und Kompatibilitätsfelder (`evd-013`).
- Beide vom Ideengeber genannten Versionen sind im npm-Register veröffentlicht (`evd-009`); eine Installation der Version 2026.9.4 ist auf srv001 vorhanden und aktiv (`evd-004`).
- Mehrere Projekte deklarieren Versionsbereiche, die 2026.8.2 oder neuer einschließen: `evd-033`, `evd-037`, `evd-039`; weitere nennen ältere Untergrenzen: `evd-029`, `evd-032`, `evd-035`, `evd-044`.

Feststellbare Einschränkungen oder Nachteile:
- Ob die Projekte unter 2026.7.1-2 oder 2026.9.4 laden, ist unbekannt; es liegen nur deklarierte Angaben vor (`evd-053`).
- Zwei Projekte machen keine Angabe zur OpenClaw-Version (`evd-022`, `evd-046`), eines deklariert `openclaw "*"` (`evd-042`), eines hängt von einer Arbeitsbereichsversion ab (`evd-048`), eines bezieht sich auf Clawdbot (`evd-050`).
- Innerhalb einzelner Projekte bestehen unterschiedliche Versionsangaben mit unterschiedlichem Bezug (`evd-029`, `evd-032`).

Unbekannte oder nicht ausreichend untersuchte Punkte:
- Welche Versionen „aktuelle OpenClaw-Versionen“ umfassen soll, ist nach `idea.md` Abschnitt 10 offen.
- Wo die Installation mit 2026.7.1-2 läuft, ist unbekannt (`evd-006`).
- Der Paketinhalt von 2026.7.1-2 wurde nicht geladen (`evd-011`, dokumentierte nicht durchgeführte Prüfung).

Bedeutung für spätere Entscheidungen:
- Der Umfang der zu unterstützenden Versionen bestimmt, welche Projekte nach ihren deklarierten Angaben überhaupt in Betracht kommen. Er ist in Abschnitt 8 als Entscheidungsbedarf aufgeführt.

Ableitung:
- Aus `evd-009`, `evd-012` und `evd-013` folgt, dass für 2026.9.4 ein dokumentierter Anbindungspunkt für Kanal-Plugins vorliegt. Für 2026.7.1-2 liegt kein entsprechender Befund aus dem Paketinhalt vor (`evd-011`), sodass die Aussage nicht auf diese Version übertragen werden kann.

### Verfahren für neue OpenClaw-Versionen

Bezug zur `idea.md`:
Abschnitt 1 nennt den Bedarf an einem Verfahren zur automatischen Aktualisierung
oder Kompatibilitätssicherung für neue OpenClaw-Versionen, Abschnitt 7 führt es
als genannte Funktion, Abschnitt 11 hält offen, ob und wie oft neue Versionen
Änderungen bringen, die das Plugin betreffen.

Verwendete Befunde:
- `evd-010`, `evd-011`, `evd-013`, `evd-014`, `evd-015`, `evd-016`, `evd-017`

Feststellbare positive Beiträge:
- Die Kompatibilitätsangaben eines Plugins werden laut Dokumentation bei der Installation ausgewertet (`evd-013`).
- Die Dokumentation beschreibt Kompatibilitätsadapter mit Status und Entfernungsfristen (`evd-015`), das CHANGELOG nennt Abkündigungen mit Terminen (`evd-016`).

Feststellbare Einschränkungen oder Nachteile:
- Alle Plugin-APIs sind laut Hersteller experimentell und können sich zwischen Versionen ändern; Plugin-Autoren sollen jede angegebene Host-Version testen (`evd-014`).
- Zwischen den beiden genannten Versionen sind 17 Versionen erschienen, davon fünf stabile (`evd-010`).
- Einstiegspfade der Plugin-Schnittstelle sind im untersuchten Zeitraum weggefallen (`evd-011`), und Plugins, die entfernte Pfade nutzen, laden laut Dokumentation nicht mehr (`evd-015`, `evd-017`).

Unbekannte oder nicht ausreichend untersuchte Punkte:
- Das CHANGELOG wurde nicht vollständig gelesen (`evd-016`, dokumentierte nicht durchgeführte Prüfung); weitere Schnittstellenänderungen sind damit nicht ausgeschlossen.
- Ob und wie oft künftige Versionen das Plugin betreffen, ist nach `idea.md` Abschnitt 11 unbekannt; die Befunde belegen nur die Vergangenheit.

Bedeutung für spätere Entscheidungen:
- Die Befundlage zeigt einen laufenden Änderungsbedarf an der Schnittstelle. Der Zuschnitt des in `idea.md` genannten Verfahrens, einschließlich der Frage nach KI-Agenten (`idea.md` Abschnitt 10), ist in Abschnitt 8 als Entscheidungsbedarf aufgeführt.

Ableitung:
- Aus `evd-010`, `evd-011`, `evd-014`, `evd-015` und `evd-016` folgt, dass ein Plugin für dieses Umfeld wiederkehrend an neue Versionen angepasst werden muss. Die Ableitung beschreibt den dokumentierten Bestand und enthält keine Aussage darüber, wie ein solches Verfahren auszusehen hat.

### Belastbarkeit der Angaben vorhandener Projekte

Bezug zur `idea.md`:
Abschnitt 1 verlangt, vorhandene GitHub-Projekte als mögliche Grundlage zu
untersuchen. Abschnitt 10 hält offen, ob Übernahme, Weiterentwicklung oder
Nutzung als Vorlage gemeint ist.

Verwendete Befunde:
- `evd-024`, `evd-026`, `evd-027`, `evd-028`, `evd-029`, `evd-030`, `evd-031`, `evd-032`, `evd-033`, `evd-034`, `evd-035`, `evd-036`, `evd-039`, `evd-040`, `evd-041`, `evd-042`, `evd-052`, `evd-053`, `evd-054`

Feststellbare positive Beiträge:
- Für jedes Projekt liegen getrennte Befunde zu dokumentierten Angaben und zu vorhandenem Code vor, sodass beide Ebenen unterscheidbar sind.
- Einzelne Projekte dokumentieren ihre Grenzen ausdrücklich: `evd-027` (OMEMO „Not Supported“), `evd-033` (MUC und OMEMO nicht unterstützt), `evd-039` und `evd-041` (Ende-zu-Ende-Verschlüsselung ausgeschlossen und entfernt), `evd-042` (Live-Tests offen).

Feststellbare Einschränkungen oder Nachteile:
- Bei `toughworm/Openclaw-XMPP-Plugin` beschreibt die Dokumentation Pfade und Testskripte, die im untersuchten Stand nicht vorliegen, und ein npm-Paket, das nicht veröffentlicht ist (`evd-026`).
- Bei `kazakhan/openclaw-xmpp` und `icarito/openclaw-xmpp` stehen Versionsangaben mit unterschiedlichem Bezug nebeneinander (`evd-029`, `evd-032`).
- Bei `icarito/openclaw-xmpp` lädt der Produktivbetrieb nach eigener Angabe einen separat abgeglichenen Verzeichnisbaum, nicht das untersuchte Repository (`evd-030`).

Unbekannte oder nicht ausreichend untersuchte Punkte:
- Funktionsfähigkeit (`evd-052`) und Ladefähigkeit unter den genannten Versionen (`evd-053`) sind unbekannt.
- Projekte außerhalb von GitHub und npm sind nicht erfasst (`evd-054`).
- Geschlossene Issues und mehrere Forks wurden nicht untersucht (dokumentierte Untersuchungsgrenzen in `inventory.json`).

Bedeutung für spätere Entscheidungen:
- Die Belastbarkeit der Projektangaben ist unterschiedlich. Für eine spätere Entscheidung über eine Grundlage ist sichtbar, welche Angaben geprüft und welche nur dokumentiert sind.

Ableitung:
- Aus `evd-026`, `evd-029`, `evd-030` und `evd-032` folgt, dass Dokumentationsangaben einzelner Projekte nicht durchgehend den untersuchten Stand beschreiben. Die Aussage gilt nur für die genannten Projekte und die dort geprüften Stellen.

### Betriebsumfeld: eigener XMPP-Server und bisherige Versuche

Bezug zur `idea.md`:
Abschnitt 2 nennt einen eigenen XMPP-Server, zwei aktive Installationen und
gescheiterte Versuche mit bestehenden Plugins. Abschnitt 6 führt Server und
Installationen als beteiligte Systeme, Abschnitt 11 hält ihre Rolle offen.

Verwendete Befunde:
- `evd-002`, `evd-003`, `evd-004`, `evd-005`, `evd-006`, `evd-007`, `evd-008`

Feststellbare positive Beiträge:
- Eine aktive Installation der Version 2026.9.4 ist belegt (`evd-004`), sodass für diese Version eine Umgebung vorhanden ist.

Feststellbare Einschränkungen oder Nachteile:
- Die Angaben zum Server (`evd-002`) und zu den gescheiterten Versuchen (`evd-003`) sind Aussagen des Ideengebers und wurden nicht bestätigt.
- Die lokale Dokumentation beschreibt keine XMPP-Anbindung (`evd-005`).

Unbekannte oder nicht ausreichend untersuchte Punkte:
- Software, Standort und unterstützte Erweiterungen des Servers sind unbekannt (`evd-008`).
- Die erprobten Plugins und die Ursachen der gescheiterten Installationen sind unbekannt, weil das Konfigurationsverzeichnis nicht lesbar war (`evd-007`).
- Die Zuordnung der zweiten Installation ist unbekannt (`evd-006`).

Bedeutung für spätere Entscheidungen:
- Ohne Angaben zum Server lässt sich nicht beurteilen, ob dort MUC verfügbar ist und welche Voraussetzungen für OMEMO gelten. Die Rolle des Servers ist in Abschnitt 8 als Entscheidungsbedarf aufgeführt.

Ableitung:
- Aus `evd-007` und `evd-008` folgt, dass die Erfahrungen aus den bisherigen Versuchen für die Bewertung nicht nutzbar sind. Ein fehlender Nachweis bedeutet dabei nicht, dass die Versuche nicht stattgefunden haben; `evd-003` bleibt eine Aussage des Ideengebers.

## 5. Gegenüberstellung vorhandener Alternativen

Gegenübergestellt werden die untersuchten Projekte anhand derselben Aspekte, für
die Befunde vorliegen. Die Tabelle enthält keine Rangfolge und keine Gesamtnote.
„Code vorhanden“ bedeutet nur, dass entsprechender Quelltext gefunden wurde;
Funktionsfähigkeit ist für kein Projekt nachgewiesen (`evd-052`), und die
Ladefähigkeit unter den genannten Versionen ist unbekannt (`evd-053`).

| Aspekt | ksmith211/openclaw-xmpp | toughworm/Openclaw-XMPP-Plugin | kazakhan/openclaw-xmpp | icarito/openclaw-xmpp | Befundgrundlage |
|---|---|---|---|---|---|
| 1:1-Code | vorhanden | vorhanden | vorhanden | vorhanden | evd-023, evd-025, evd-028, evd-031 |
| MUC-Code mit Raumbeitritt | nicht gefunden | nicht gefunden | vorhanden | vorhanden | evd-023, evd-025, evd-028, evd-031 |
| OMEMO-Code | nicht gefunden | vorhanden, bei groupchat übersprungen | nicht gefunden | vorhanden, auch `urn:xmpp:omemo:2` | evd-023, evd-025, evd-028, evd-031 |
| deklarierte OpenClaw-Version | keine Angabe | keine Angabe | README 2026.8.2+, Paket >=2026.6.1 | Paket >=2026.7.1, AGENTS.md 2026.6.9 | evd-022, evd-024, evd-029, evd-032 |
| Testdateien im Repository | keine | 2 | 33 | 6 | evd-023, evd-025, evd-028, evd-031 |

| Aspekt | soilDNRA/openclaw-xmpp | elmafioso79/xmpp-channel | watkins-matt/xmpp-channel | Programmatore-Web/openclaw-xmpp-channel | Befundgrundlage |
|---|---|---|---|---|---|
| 1:1-Code | vorhanden | vorhanden | vorhanden | vorhanden | evd-034, evd-036, evd-038, evd-040 |
| MUC-Code mit Raumbeitritt | nicht gefunden, nur Hinweistext | vorhanden | vorhanden | vorhanden, feste Räume | evd-034, evd-036, evd-038, evd-039, evd-040 |
| OMEMO-Code | nicht gefunden, ausdrücklich nicht unterstützt | vorhanden, auch bei groupchat | vorhanden | nicht gefunden, ausdrücklich ausgeschlossen | evd-033, evd-034, evd-036, evd-038, evd-039, evd-040, evd-041 |
| deklarierte OpenClaw-Version | >=2026.8.2 | ^2026.2.2-3 | >=2026.8.2 | ^2026.8.2 | evd-033, evd-035, evd-037, evd-039 |
| Testdateien im Repository | 12 und CI | keine | 2 | 33 | evd-034, evd-036, evd-038, evd-040 |

| Aspekt | MrCPA/oc-xmpp | chitozzz/xmpp-adapter-openclaw | weijia/xmpp-connector | processone/openclaw, Zweig xmpp-support | Befundgrundlage |
|---|---|---|---|---|---|
| 1:1-Code | vorhanden | vorhanden | vorhanden | vorhanden | evd-043, evd-045, evd-047, evd-049 |
| MUC-Code mit Raumbeitritt | vorhanden | vorhanden | nicht gefunden | vorhanden | evd-043, evd-045, evd-047, evd-049 |
| OMEMO-Code | vorhanden, `urn:xmpp:omemo:2` | nicht gefunden | nicht gefunden | nicht gefunden | evd-043, evd-045, evd-047, evd-049 |
| deklarierte OpenClaw-Version | `*` | >=2026.6.9 | keine Angabe | Arbeitsbereichsversion | evd-042, evd-044, evd-046, evd-048 |
| Testdateien im Repository | 6 | 1 | keine | 2 | evd-043, evd-045, evd-047, evd-049 |

`rsaisankalp/clawdbotElyments` ist nicht in die Gegenüberstellung aufgenommen,
weil es nach `evd-050` Clawdbot an eine andere Plattform anbindet und damit nicht
denselben Bewertungsaspekten unterliegt.

## 6. Wesentliche Lücken und offene Sachverhalte

| Sachverhalt | Bedeutung für Bewertung | Durch swk-02 klärbar? | Behandlung |
|---|---|---|---|
| Funktionsfähigkeit der Projekte für 1:1, OMEMO und MUC (`evd-052`) | wesentlich; ohne sie bleibt jede Aussage zu Funktionen auf dokumentierte Angaben und vorhandenen Code beschränkt | ja; Build und Test in einer getrennten, entbehrlichen Arbeitsumgebung sind nach `phases/swk-02-inventory.md` zulässig | Rückkehr zu swk-02 (Rückkehrpunkt 1) |
| Ladefähigkeit der Projekte unter 2026.7.1-2 und 2026.9.4 (`evd-053`) | wesentlich für den in `idea.md` Abschnitt 1 genannten Versionsbezug | ja; Laden in getrennten OpenClaw-Instanzen der beiden Versionen | Rückkehr zu swk-02 (Rückkehrpunkt 2) |
| Vollständigkeit der Projektliste außerhalb von GitHub und npm (`evd-054`) | wesentlich für die in `idea.md` Abschnitt 1 verlangte Untersuchung vorhandener Projekte | ja; Suche auf ClawHub, GitLab und Codeberg | Rückkehr zu swk-02 (Rückkehrpunkt 3) |
| Software und Erweiterungen des eigenen XMPP-Servers (`evd-008`, `evd-002`) | wesentlich für die Beurteilung von MUC und OMEMO im Betrieb | nein; Standort und Zugang sind unbekannt und nur vom Ideengeber zu benennen | spätere Phase; Entscheidungsbedarf E5 |
| Erprobte Plugins und Ursachen gescheiterter Installationen (`evd-007`, `evd-003`) | wesentlich, um die Aussage aus `idea.md` Abschnitt 2 auf die untersuchten Projekte zu beziehen | nein; das Konfigurationsverzeichnis ist nicht lesbar, es gibt keine Aufzeichnung | spätere Phase; Klärung durch den Ideengeber |
| Zuordnung der zweiten Installation mit 2026.7.1-2 (`evd-006`) | wesentlich für den Umfang der Zielversionen | nein; der Rechner ist nicht benannt | spätere Phase; Entscheidungsbedarf E2 |
| Umfang von OMEMO in Gruppenchats (`idea.md` Abschnitt 10; `evd-025`, `evd-036`, `evd-042`) | wesentlich; bestimmt, welche Projekte für diesen Aspekt in Betracht kommen | nein; es ist eine Festlegung des Ideengebers, kein Bestand | spätere Phase; Entscheidungsbedarf E1 |
| Bedeutung von „unterstützen“ je Funktion (`idea.md` Abschnitt 10) | wesentlich für die Abnahme | nein; Festlegung des Ideengebers | spätere Phase; Entscheidungsbedarf E1 |

## 7. Rückkehrpunkte zu swk-02

### Rückkehrpunkt 1: Funktionsprüfung der untersuchten Projekte

- Sachverhalt: Ob die untersuchten Projekte Direktnachrichten, OMEMO und MUC funktionsfähig bereitstellen, ist unbekannt.
- betroffene Befunde: `evd-052`; mittelbar `evd-023`, `evd-025`, `evd-028`, `evd-031`, `evd-034`, `evd-036`, `evd-038`, `evd-040`, `evd-043`, `evd-045`, `evd-047`, `evd-049`
- Bedeutung für die Bewertung: Ohne Funktionsnachweis bleibt die Bewertung aller drei in `idea.md` Abschnitt 7 genannten Funktionen auf dokumentierte Angaben und vorhandenen Code beschränkt.
- zusätzlich benötigte Untersuchung: Build und Ausführung der vorhandenen Tests sowie ein Funktionstest je Projekt in einer getrennten, entbehrlichen Arbeitsumgebung mit eigener OpenClaw-Instanz und Test-XMPP-Server, ohne produktive Zugangsdaten.
- voraussichtlich verfügbare Quellen oder Prüfwege: die bereits erfassten Repositorys mit ihren Commit-Ständen; die in den Repositorys vorhandenen Testdateien (`evd-028`, `evd-034`, `evd-040`, `evd-043`, `evd-045`, `evd-049`); ein eigens aufgesetzter XMPP-Test-Server.

### Rückkehrpunkt 2: Ladefähigkeit unter den genannten OpenClaw-Versionen

- Sachverhalt: Ob die untersuchten Projekte unter OpenClaw 2026.7.1-2 und 2026.9.4 laden, ist unbekannt; es liegen nur deklarierte Versionsangaben vor.
- betroffene Befunde: `evd-053`; mittelbar `evd-011`, `evd-013`, `evd-014`, `evd-015`, `evd-017`, `evd-029`, `evd-032`, `evd-033`, `evd-035`, `evd-037`, `evd-039`, `evd-042`, `evd-044`, `evd-048`
- Bedeutung für die Bewertung: Der in `idea.md` Abschnitt 1 genannte Versionsbezug lässt sich sonst nur anhand der Selbstauskunft der Projekte beurteilen.
- zusätzlich benötigte Untersuchung: Laden der Projekte in je einer getrennten OpenClaw-Instanz der Versionen 2026.7.1-2 und 2026.9.4; zusätzlich Auswertung des Paketinhalts von 2026.7.1-2, der bisher nicht geladen wurde (`evd-011`).
- voraussichtlich verfügbare Quellen oder Prüfwege: npm-Register mit beiden Versionen (`evd-009`); Kompatibilitätsfelder der Projekte (`evd-013`); die erfassten Repository-Stände.

### Rückkehrpunkt 3: Projektquellen außerhalb von GitHub und npm

- Sachverhalt: Ob es weitere XMPP-Anbindungen für OpenClaw gibt, etwa auf ClawHub, GitLab oder Codeberg, ist unbekannt.
- betroffene Befunde: `evd-054`; mittelbar `evd-033` (verweist auf einen ClawHub-Eintrag) und `evd-005` (ClawHub wird lokal bereits für ein Plugin genutzt)
- Bedeutung für die Bewertung: `idea.md` Abschnitt 1 verlangt die Untersuchung vorhandener Projekte als mögliche Grundlage; eine unvollständige Liste begrenzt jede Gegenüberstellung.
- zusätzlich benötigte Untersuchung: Suche auf ClawHub, GitLab und Codeberg nach XMPP-Anbindungen für OpenClaw sowie Prüfung des in `evd-033` genannten ClawHub-Eintrags.
- voraussichtlich verfügbare Quellen oder Prüfwege: ClawHub-Marktplatz und die Plugin-Suche von OpenClaw (`evd-013`); die öffentlichen Suchfunktionen von GitLab und Codeberg.

## 8. Später zu entscheidende Punkte

### E1: Umfang der geforderten Funktionen, insbesondere OMEMO in Gruppenchats

- Gegenstand: Ob OMEMO-Verschlüsselung nur für Direktnachrichten oder auch für Gruppenchats über MUC gelten soll und welcher Funktionsumfang je Funktion als „unterstützt“ gilt.
- Bezug zur `idea.md`: Abschnitt 7, Abschnitt 8, Abschnitt 10 („OMEMO-Verschlüsselung“, „unterstützen“)
- relevante Befunde: `evd-024`, `evd-025`, `evd-031`, `evd-036`, `evd-038`, `evd-039`, `evd-041`, `evd-042`
- relevante Annahmen: keine; für dieses Projekt existiert keine `assumptions.md`
- Begründung des Entscheidungsbedarfs: Die Befunde unterscheiden Projekte mit OMEMO nur für Direktnachrichten, mit OMEMO auch bei Gruppenchats und ohne OMEMO. Ohne Festlegung des Umfangs lässt sich nicht bestimmen, welche Projekte den Aspekt abdecken.
- dokumentierte Optionen, soweit vorhanden: OMEMO nur für Direktnachrichten (`evd-025`, `evd-042`); OMEMO auch bei Gruppenchats (`evd-036`); kein OMEMO (`evd-039`, `evd-040`)
- offene entscheidungsrelevante Sachverhalte: Funktionsfähigkeit ist nicht nachgewiesen (`evd-052`); Voraussetzungen des eigenen Servers sind unbekannt (`evd-008`)

### E2: Umfang der zu unterstützenden OpenClaw-Versionen

- Gegenstand: Welche Versionen „aktuelle OpenClaw-Versionen“ umfassen und ob beide aktiven Installationen unterstützt werden sollen.
- Bezug zur `idea.md`: Abschnitt 1, Abschnitt 8, Abschnitt 10 („aktuelle OpenClaw-Versionen“), Abschnitt 11
- relevante Befunde: `evd-001`, `evd-004`, `evd-006`, `evd-009`, `evd-011`, `evd-012`, `evd-053`
- relevante Annahmen: keine
- Begründung des Entscheidungsbedarfs: Die Schnittstelle unterscheidet sich zwischen den beiden genannten Versionen (`evd-011`, `evd-017`); die Projekte deklarieren unterschiedliche Untergrenzen (`evd-029`, `evd-032`, `evd-033`, `evd-035`, `evd-037`, `evd-039`, `evd-042`, `evd-044`).
- dokumentierte Optionen, soweit vorhanden: nur 2026.9.4 als belegte aktive Installation (`evd-004`); beide genannten Versionen (`evd-001`, `evd-009`)
- offene entscheidungsrelevante Sachverhalte: Standort der Installation mit 2026.7.1-2 (`evd-006`); Ladefähigkeit der Projekte (`evd-053`)

### E3: Grundlage der Umsetzung

- Gegenstand: Ob ein vorhandenes Projekt übernommen, weiterentwickelt, nur als Vorlage genutzt oder neu entwickelt wird.
- Bezug zur `idea.md`: Abschnitt 1 („Vorhandene GitHub-Projekte … als mögliche Grundlage“), Abschnitt 5, Abschnitt 10 („als mögliche Grundlage untersucht“, „entwickeln“)
- relevante Befunde: `evd-018`, `evd-019`, `evd-020`, `evd-022` bis `evd-051`, `evd-052`, `evd-053`, `evd-054`
- relevante Annahmen: keine
- Begründung des Entscheidungsbedarfs: Der Hersteller liefert keine XMPP-Anbindung (`evd-018`, `evd-019`, `evd-020`); es liegen dreizehn erfasste Projekte mit unterschiedlicher Abdeckung und unterschiedlicher Belastbarkeit ihrer Angaben vor. Die Auswahl ist nach `phases/swk-03-assessment.md` nicht Teil dieser Phase.
- dokumentierte Optionen, soweit vorhanden: die in Abschnitt 5 gegenübergestellten Projekte; Neuentwicklung gegen die in `evd-012` und `evd-013` dokumentierte Schnittstelle
- offene entscheidungsrelevante Sachverhalte: Funktionsfähigkeit (`evd-052`), Ladefähigkeit (`evd-053`), Vollständigkeit der Projektliste (`evd-054`), Lizenzlage der Projekte (in `inventory.json` nur als Quellenangabe erfasst, nicht als Befund)

### E4: Zuschnitt des Verfahrens für neue OpenClaw-Versionen

- Gegenstand: Ob automatische Aktualisierung, Kompatibilitätssicherung oder beides umgesetzt wird und ob KI-Agenten dabei vorgesehen sind.
- Bezug zur `idea.md`: Abschnitt 1, Abschnitt 7, Abschnitt 10 („automatische Aktualisierung oder Kompatibilitätssicherung“, „Dies kann ggf. auch mit KI-Agenten unterstützt werden“)
- relevante Befunde: `evd-010`, `evd-011`, `evd-013`, `evd-014`, `evd-015`, `evd-016`, `evd-017`
- relevante Annahmen: keine
- Begründung des Entscheidungsbedarfs: Die Befunde belegen häufige Versionswechsel und Änderungen an der Plugin-Schnittstelle. Welcher Weg gewählt wird, ist eine Umsetzungsentscheidung und in dieser Phase ausgeschlossen.
- dokumentierte Optionen, soweit vorhanden: Nutzung der dokumentierten Kompatibilitätsfelder (`evd-013`); Beobachtung der dokumentierten Abkündigungsfristen (`evd-015`, `evd-016`)
- offene entscheidungsrelevante Sachverhalte: künftige Änderungen sind unbekannt; das CHANGELOG wurde nicht vollständig ausgewertet (`evd-016`)

### E5: Rolle des eigenen XMPP-Servers

- Gegenstand: Ob das Plugin mit dem vorhandenen eigenen XMPP-Server betrieben werden soll und welche Voraussetzungen dieser erfüllen muss.
- Bezug zur `idea.md`: Abschnitt 2, Abschnitt 6, Abschnitt 11 („Ob das Plugin mit dem vorhandenen eigenen XMPP-Server arbeiten soll, ist unbekannt“)
- relevante Befunde: `evd-002`, `evd-008`
- relevante Annahmen: keine
- Begründung des Entscheidungsbedarfs: Der Server ist genannt, seine Rolle ist offen, und seine Eigenschaften sind unbekannt. Ohne diese Festlegung bleibt offen, welche serverseitigen Voraussetzungen für MUC und OMEMO gelten.
- dokumentierte Optionen, soweit vorhanden: keine; die Befundlage enthält keine Angaben zum Server
- offene entscheidungsrelevante Sachverhalte: Software, Standort und unterstützte Erweiterungen des Servers (`evd-008`)

## 9. Prüfergebnis swk-03

- Vorprüfung bestanden: ja
- Qualitätsgrenze swk-03 bestanden: ja
- nicht erfüllte Kriterien: keine
- Blockade: keine

Einzelnachweis der Vorprüfung nach `phases/swk-03-assessment.md`:

- `pilots/openclaw-xmpp/idea.md` vorhanden, Status `accepted` (Zeile 5)
- `pilots/openclaw-xmpp/inventory.json` vorhanden, Status `accepted`, Freigabe durch den Ideengeber am 2026-09-16
- `pilots/openclaw-xmpp/inventory.md` vorhanden; `tools/inventory.py check` meldet „current“
- projektspezifische `assumptions.md` nicht vorhanden; nach `idea.md` Abschnitt 11 wurden keine Annahmen erkannt
- alle in der Phasendatei referenzierten Regeln und Vorlagen vorhanden und nicht leer
- `rules/quality-gates.md` enthält eine Qualitätsgrenze für `swk-03`
- verwendete Kennungen `evd-001` bis `evd-054` entsprechen `rules/identifiers.md`

Prüfung gegen die Qualitätsgrenze swk-03:

- Bewertung beruht ausschließlich auf akzeptierter `idea.md` und akzeptierter `inventory.json`; keine neue Bestandsrecherche
- kein Befund verändert, kein Nachweisstatus umgestuft
- jeder Bewertungsaspekt nennt Bezug zur `idea.md` und die verwendeten `evd-nnn`
- dokumentierte Behauptungen sind als solche benannt; vorhandener Code ist nicht als Funktionsnachweis dargestellt
- fehlende Treffer im Quelltext sind nicht als Nachweis fehlender Funktionen behandelt
- `UNKNOWN`, nicht durchgeführte Prüfungen und Untersuchungsgrenzen bleiben sichtbar
- keine Rangfolge, Gewichtung, Gesamtnote oder numerischen Scores
- keine Auswahl einer Alternative, keine neue Anforderung, keine Architektur-, Technologie- oder Umsetzungsentscheidung
- Annahmen: keine vorhanden; daher kein Entscheidungsbedarf aus `asm-nnn`
- jeder wesentliche offene Punkt ist in Abschnitt 6 auf weitere Bestandsuntersuchung geprüft; drei Rückkehrpunkte sind in Abschnitt 7 dokumentiert
- Aufbau entspricht `templates/assessment.md`
- Status nach `rules/status.md`: `review`; `accepted` ist dem Ideengeber vorbehalten

## 10. Freigabestatus

- Ergebnis: `review`
- geprüft am: 2026-09-16
- geprüft durch: skizzwerk
- Anmerkungen: Die Bewertung wartet auf die inhaltliche Prüfung durch den Ideengeber. Die drei Rückkehrpunkte zu swk-02 in Abschnitt 7 sind noch nicht bearbeitet.
