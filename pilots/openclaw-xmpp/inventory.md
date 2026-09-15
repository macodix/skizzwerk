---
document: inventory
process_phase: swk-02
project: "openclaw-xmpp"
status: review
created: 2026-09-14
last_updated: 2026-09-15
basis: idea.md
---

# Bestandsuntersuchung

<!-- Automatisch erzeugt. Nicht direkt bearbeiten. -->

## 1. Grundlage und Untersuchungsauftrag

Grundlage ist `pilots/openclaw-xmpp/idea.md` (Commit 4e46961, Status `accepted`, bestätigt am 2026-09-14). Die Untersuchung begann und endete am 2026-09-14; am 2026-09-15 wurde sie ohne neue Bestandsrecherche in das strukturierte Format übertragen. Untersucht wird der vorhandene Bestand zu einer XMPP-Anbindung an OpenClaw: die vorhandenen OpenClaw-Installationen, die Plugin-Schnittstelle der genannten OpenClaw-Versionen und ihre Änderungen, XMPP im Lieferumfang und im Hauptprojekt von OpenClaw, vorhandene öffentliche Projekte sowie die Angaben zum eigenen XMPP-Server und zu bisherigen Versuchen. Kennzeichnung nach `rules/evidence.md`: `USER_PROVIDED` (Aussage des Ideengebers), `VERIFIED` (unmittelbar durch Code, Befehlsausgabe oder Primärquelle bestätigt), `DOCUMENTED` (dokumentierte Behauptung), `INFERRED` (Ableitung), `UNKNOWN` (unbekannt). Es wurden keine Annahmen gesetzt, keine Aussage widerlegt und kein Widerspruch nach den Anforderungen an `CONFLICT` nachgewiesen; die in einer früheren Fassung als `CONFLICT` geführten Befunde evd-026, evd-029, evd-032 und evd-041 sind nach ihrer tatsächlichen Belegbarkeit eingestuft. Die Befunde enthalten keine neuen Anforderungen, keine Rangfolge oder Auswahl möglicher Lösungen und keine Architektur-, Technologie- oder Umsetzungsentscheidung.

## 2. Untersuchungsumfang

| Untersuchungsbereich | Bezug zur Idee | Begründung der Relevanz |
|---|---|---|
| Vorhandene OpenClaw-Installationen | idea.md, Abschnitt 2 („2 OpenClaw Installationen … aktiv“), Abschnitt 6, Abschnitt 11 | vorhandene Systeme, für die das Plugin bestimmt ist |
| Plugin- und Kanalschnittstelle von OpenClaw | idea.md, Abschnitt 1 („Ein XMPP-Plugin für aktuelle OpenClaw-Versionen“), Abschnitt 5 | vorhandene Grundlage, an die ein Plugin anschließt |
| Versionen und Schnittstellenänderungen zwischen 2026.7.1-2 und 2026.9.4 | idea.md, Abschnitt 1 („Für neue OpenClaw-Versionen …“), Abschnitt 10 („aktuelle OpenClaw-Versionen“), Abschnitt 11 („Ob und wie oft neue OpenClaw-Versionen Änderungen bringen“) | Bestand zu Häufigkeit und Art von Änderungen |
| XMPP im Lieferumfang und im Hauptprojekt von OpenClaw | idea.md, Abschnitt 1, Abschnitt 5 | vorhandene XMPP-Unterstützung durch den Hersteller |
| Vorhandene öffentliche XMPP-Projekte für OpenClaw | idea.md, Abschnitt 1 („Vorhandene GitHub-Projekte sollen als mögliche Grundlage untersucht werden“), Abschnitt 7, Abschnitt 11 | ausdrücklich zu untersuchende mögliche Grundlagen |
| Eigener XMPP-Server | idea.md, Abschnitt 2 („Ein eigener XMPP-Server ist vorhanden“), Abschnitt 6, Abschnitt 11 | genanntes vorhandenes System |
| Bisherige Versuche mit bestehenden Plugins | idea.md, Abschnitt 2 („bestehende Plugins konnten z. T. nicht installiert werden …“), Abschnitt 11 | dokumentierter bisheriger Versuch |

## 3. Durchgeführte Untersuchung

| Untersuchungsbereich | Untersucht | Nicht untersucht | Einschränkungen |
|---|---|---|---|
| Vorhandene OpenClaw-Installationen | Version und Dienststatus auf srv001; lokale Installationsdokumentation unter `/srv/aixlab/docs` | Konfiguration und installierte Plugins auf srv001: wegen fehlenden Zugriffs nicht möglich; Installation mit 2026.7.1-2: nicht durchgeführt, da kein Rechner genannt ist | `/var/lib/openclaw/.openclaw` nicht lesbar; zweite Installation nicht auffindbar (evd-006, evd-007) |
| Plugin- und Kanalschnittstelle von OpenClaw | `package.json`, Typdefinitionen und `docs/plugins/` im Paket 2026.9.4 | Paketinhalt 2026.7.1-2: nicht durchgeführt; `src/plugins/compat/registry.ts`: nicht durchgeführt; Website docs.openclaw.ai: nicht durchgeführt | Beschreibung aus Dateien, kein Plugin gebaut; Vergleich der Versionen beruht auf Registermetadaten und Dokumentation (evd-011, evd-017) |
| Versionen und Schnittstellenänderungen zwischen 2026.7.1-2 und 2026.9.4 | npm-Registerdaten; Git-Tags `v2026.7.1-2` und `v2026.9.4`; CHANGELOG am Tag `v2026.9.4`, Einträge zu Plugin-SDK und Kanälen | vollständiges CHANGELOG (rund 24 000 Zeilen): nicht durchgeführt | CHANGELOG am Tag `v2026.9.4` enthält keine Abschnitte 2026.7.1-1 und 2026.7.1-2; weitere Schnittstellenänderungen sind möglich, aber nicht erfasst (evd-016) |
| XMPP im Lieferumfang und im Hauptprojekt von OpenClaw | `dist/extensions/` und Volltextsuche im Paket 2026.9.4; `extensions/` auf `main` (Commit df663a946582); Status der PRs #9741, #20998, #21015 und des Issues #29046 | Inhalte der PR- und Issue-Diskussionen: nicht durchgeführt | Gründe für die Nichtübernahme sind unbekannt (evd-020) |
| Vorhandene öffentliche XMPP-Projekte für OpenClaw | 12 Projekte und 1 Grenzfall auf GitHub: Dokumentation, Paketmetadaten, Quelltext (Klon mit `--depth 1` in getrennter Arbeitsumgebung, nur gelesen); npm-Register: Paketdaten und Suche; GitHub-Suche: `gh search repos` („openclaw xmpp“ 6, „openclaw jabber“ 0, „openclaw prosody“ 0, „openclaw omemo“ 0, „clawdbot xmpp“ 0, „moltbot xmpp“ 0, „openclaw-channel xmpp“ 0, „xmpp openclaw plugin“ 0, „openclaw ejabberd“ 0); `gh api search/repositories` (`xmpp in:name,description,readme openclaw` 176, `xmpp clawdbot in:readme` 10, `xmpp moltbot in:readme` 7, `topic:openclaw topic:xmpp` 4, `omemo openclaw in:readme` 12, `jabber openclaw in:readme` 24, `openclaw xmpp fork:true` 21, `xmpp in:name claw` 5); `gh api search/code` (`openclaw @xmpp/client filename:package.json` 5, `openclaw xmpp filename:openclaw.plugin.json` 2, `openclaw urn:xmpp:omemo` 2, `openclaw muc groupchat xmpp` 19, `"channels.xmpp" openclaw` 18); `gh search prs/issues --repo openclaw/openclaw xmpp` (je 7); Stand 2026-09-14; npm-Suche: https://registry.npmjs.org/-/v1/search mit `openclaw xmpp`, `openclaw jabber`, `openclaw omemo`, `openclaw prosody`, `clawdbot xmpp`, `moltbot xmpp`, `keywords:openclaw` (seitenweise), `keywords:clawdbot`, `keywords:moltbot`, `keywords:openclaw-plugin`, `keywords:openclaw-channel`, `text=xmpp`, `text=omemo`, `text=jabber`; Direktabfragen `@openclaw/xmpp`, `openclaw-xmpp`, `openclaw-channel-xmpp`, `@openclaw/channel-xmpp`, `clawdbot-xmpp`, `moltbot-xmpp`; Stand 2026-09-14 | Build, Tests und Funktionstest der Projekte: nicht durchgeführt; in einer getrennten, entbehrlichen Arbeitsumgebung nach `phases/swk-02-inventory.md` zulässig; Laden der Projekte unter 2026.7.1-2 und 2026.9.4: nicht durchgeführt; ClawHub, GitLab, Codeberg und allgemeine Websuche: nicht durchgeführt; Forks cronus42, kitschmensch, zhgzhg, jerry-harm, indorri: nicht durchgeführt; geschlossene Issues: nicht durchgeführt; OMEMO-Beschränkung im Code von MrCPA/oc-xmpp: nicht durchgeführt | Quelltext nur auf Vorhandensein geprüft; Aussagen zu Funktionen reichen höchstens bis `DOCUMENTED` oder bis zum Vorhandensein von Code (evd-052, evd-053); GitHub-Codesuche nur auf Standard-Branches; npm `keywords:openclaw`: 134 von 5134 Einträgen nicht abrufbar (Suchgrenze 5000); Projektliste auf GitHub und npm beschränkt (evd-054) |
| Eigener XMPP-Server | Suche in `/srv/aixlab/docs`; Dienstliste auf srv001 | Server selbst: wegen fehlenden Zugriffs nicht möglich, da Standort und Zugang unbekannt | keine Angaben zu Server-Software und Erweiterungen (evd-008) |
| Bisherige Versuche mit bestehenden Plugins | Suche in `/srv/aixlab/docs`; Versuch, `/var/lib/openclaw/.openclaw` auf srv001 zu lesen | Plugin-Liste der Installationen: wegen fehlenden Zugriffs nicht möglich; `openclaw plugins list` auf dem produktiv verwendeten srv001: nicht durchgeführt | die vom Ideengeber erprobten Plugins sind nicht identifizierbar (evd-003, evd-007) |

## 4. Befundübersicht

| Kennung | Aussage | Nachweisstatus |
|---|---|---|
| `evd-001` | Zurzeit sind zwei OpenClaw-Installationen mit den Versionen 2026.9.4 und 2026.7.1-2 aktiv. | `USER_PROVIDED` |
| `evd-002` | Ein eigener XMPP-Server ist vorhanden. | `USER_PROVIDED` |
| `evd-003` | Bestehende Plugins konnten zum Teil nicht installiert werden oder erfüllten nicht die Anforderungen an Sicherheit (OMEMO) oder Kommunikation (Gruppenchats/MUC). | `USER_PROVIDED` |
| `evd-004` | Auf dem Rechner srv001 ist OpenClaw 2026.9.4 (Commit 3a9d69d) als globales npm-Paket installiert; der Dienst `openclaw.service` ist aktiv. | `VERIFIED` |
| `evd-005` | Die lokale Installationsanleitung beschreibt OpenClaw mit dem mitgelieferten WebChat und Authelia sowie ein über ClawHub installiertes Provider-Plugin; XMPP wird dort nicht erwähnt. | `DOCUMENTED` |
| `evd-006` | Ob srv001 eine der beiden vom Ideengeber genannten Installationen ist und wo die Installation mit Version 2026.7.1-2 läuft, ist unbekannt. | `UNKNOWN` |
| `evd-007` | Welche Plugins in den vorhandenen Installationen installiert oder erprobt wurden und woran ihre Installation scheiterte, ist unbekannt. | `UNKNOWN` |
| `evd-008` | Software, Standort und unterstützte XMPP-Erweiterungen des eigenen XMPP-Servers sind unbekannt. | `UNKNOWN` |
| `evd-009` | Die Versionen 2026.7.1-2 (veröffentlicht 2026-07-18T03:53:48Z, Tag-Commit 0790d9f593ad) und 2026.9.4 (veröffentlicht 2026-09-11T02:44:59Z, Tag-Commit 3a9d69db306c) sind im npm-Register veröffentlicht; `latest` ist 2026.9.4, `extended-stable` ist 2026.6.35. | `VERIFIED` |
| `evd-010` | Zwischen 2026.7.1-2 und 2026.9.4 wurden 17 Versionen veröffentlicht: 2026.8.1, 2026.8.2, 2026.9.1, 2026.9.2, 2026.9.3, neun Beta-Versionen und 2026.6.33 bis 2026.6.35. | `VERIFIED` |
| `evd-011` | Die Exportpfade `./plugin-sdk` und `./extension-api` sind in 2026.7.1-2 und 2026.7.2-beta.3 vorhanden, ab 2026.7.2-beta.4 und in 2026.9.4 nicht mehr. | `VERIFIED` |
| `evd-012` | Das Paket 2026.9.4 exportiert Unterpfade `openclaw/plugin-sdk/*`, darunter `channel-core`, `channel-contract`, `channel-entry-contract` und `plugin-entry`; `channel-core.d.ts` exportiert u. a. `ChannelPlugin` und `defineChannelPluginEntry`. | `VERIFIED` |
| `evd-013` | Laut Dokumentation braucht jedes native Plugin eine `openclaw.plugin.json`; die Felder `openclaw.compat.pluginApi` und `openclaw.install.minHostVersion` werden bei npm-Installationen zur Versionsauswahl ausgewertet. | `DOCUMENTED` |
| `evd-014` | Laut Dokumentation sind alle Plugin-APIs experimentell und können sich zwischen OpenClaw-Versionen ändern; Plugin-Autoren sollen die Version festlegen und jede als kompatibel angegebene Version testen. | `DOCUMENTED` |
| `evd-015` | Laut Dokumentation sind `openclaw/plugin-sdk`, `openclaw/plugin-sdk/compat` und `openclaw/extension-api` entfernt; Plugins, die sie importieren, laden nicht mehr. Alte Verträge laufen befristet über Kompatibilitätsadapter. | `DOCUMENTED` |
| `evd-016` | Das CHANGELOG nennt für 2026.9.3 mehrere als „Breaking“ gekennzeichnete Änderungen am Plugin-SDK und für 2026.8.1 bis 2026.9.4 Abkündigungen von SDK-Pfaden mit Entfernungsterminen 2026-09-01 und 2026-09-08. | `DOCUMENTED` |
| `evd-017` | Zwischen 2026.7.1-2 und 2026.9.4 hat sich die Plugin-Schnittstelle so geändert, dass Plugins, die die entfernten Pfade nutzen, unter 2026.9.4 laut Dokumentation nicht laden. | `INFERRED` |
| `evd-018` | Das Paket 2026.9.4 enthält unter `dist/extensions/` 60 Erweiterungen, darunter keine für XMPP; die Suche nach `xmpp`, `jabber`, `omemo`, `muc` trifft nur Fremdbibliotheken (URL-Schema, MIME-Typ). | `VERIFIED` |
| `evd-019` | Die Kanalübersicht der Dokumentation nennt mitgelieferte und offizielle Kanal-Plugins, aber kein XMPP- oder Jabber-Plugin. | `DOCUMENTED` |
| `evd-020` | Im Repository `openclaw/openclaw` enthält `extensions/` auf `main` kein XMPP-Verzeichnis; die Pull Requests #9741, #20998 und #21015 für XMPP wurden ohne Merge geschlossen; Issue #29046 „[Feature]: XMPP support“ ist mit `not_planned` geschlossen. | `VERIFIED` |
| `evd-021` | OpenClaw hieß laut Projektdokumentation zuvor Warelay, Clawdbot und Moltbot; seit dem 30. Januar 2026 heißt es OpenClaw. | `DOCUMENTED` |
| `evd-022` | ksmith211/openclaw-xmpp: Die README beschreibt ein Kanal-Plugin nur für Direktnachrichten; MUC, OMEMO und eine OpenClaw-Version werden nicht genannt. Auf npm ist `@ksmith221/openclaw-xmpp` 0.1.1 veröffentlicht. | `DOCUMENTED` |
| `evd-023` | ksmith211/openclaw-xmpp: Code für 1:1-Nachrichten ist vorhanden (`type: "chat"`); Zeichenketten zu MUC, groupchat und OMEMO kommen in `src/` nicht vor; keine Testdateien. | `VERIFIED` |
| `evd-024` | toughworm/Openclaw-XMPP-Plugin: Die README nennt Senden und Empfangen von 1:1- und Gruppenchat-Nachrichten, OMEMO nur für 1:1 im älteren Namensraum `eu.siacs.conversations.axolotl`, verschlüsselten Gruppenchat als offen und keine OpenClaw-Version. Sie beschreibt außerdem Dateipfade unter `extensions/xmpp/`, Testskripte `test-omemo-*.ts` und die Installation mit `openclaw plugins install @openclaw/xmpp`. | `DOCUMENTED` |
| `evd-025` | toughworm/Openclaw-XMPP-Plugin: OMEMO-Code im Namensraum `eu.siacs.conversations.axolotl` ist vorhanden und wird bei `groupchat` übersprungen; die Zeichenkette `http://jabber.org/protocol/muc` für einen Raumbeitritt kommt in `src/` nicht vor. | `VERIFIED` |
| `evd-026` | toughworm/Openclaw-XMPP-Plugin: Im untersuchten Repository-Stand liegen die Programmdateien unter `src/` und nicht unter `extensions/xmpp/`, die in evd-024 genannten Testskripte `test-omemo-*.ts` sind nicht vorhanden, und `@openclaw/xmpp` ist im npm-Register nicht veröffentlicht. | `VERIFIED` |
| `evd-027` | kazakhan/openclaw-xmpp: Die README nennt 1:1 und MUC; `XMPPAUDIT.md` führt OMEMO (XEP-0384) als „Not Supported“. | `DOCUMENTED` |
| `evd-028` | kazakhan/openclaw-xmpp: Code für MUC (`muc`-Namensraum, `joinRoom`) und 1:1 ist vorhanden; OMEMO-Zeichenketten kommen nicht vor. | `VERIFIED` |
| `evd-029` | kazakhan/openclaw-xmpp: Die README nennt „OpenClaw 2026.8.2+“ als Voraussetzung und begründet das mit den in 2026.8.x eingeführten Prüfungen „capability-consent“ und `contracts.tools`; `package.json` deklariert `compat.pluginApi ">=2026.6.1"` und `minGatewayVersion "2026.6.1"`. | `DOCUMENTED` |
| `evd-030` | icarito/openclaw-xmpp: Die Paketbeschreibung nennt 1:1-Chat, MUC-Räume und Ad-hoc-Befehle; die README sagt, der Produktivbetrieb lade einen separat abgeglichenen Verzeichnisbaum. | `DOCUMENTED` |
| `evd-031` | icarito/openclaw-xmpp: Code für MUC, für OMEMO im älteren Namensraum und in `urn:xmpp:omemo:2` sowie ein Python-Hilfsprogramm `src/omemo/sidecar.py` sind vorhanden. | `VERIFIED` |
| `evd-032` | icarito/openclaw-xmpp: `AGENTS.md` beschreibt das Plugin „for OpenClaw 2026.6.9 or newer“; `package.json` deklariert `compat.pluginApi ">=2026.7.1"` und als Entwicklungsabhängigkeit `openclaw ^2026.7.1`. | `DOCUMENTED` |
| `evd-033` | soilDNRA/openclaw-xmpp: Die README beschreibt nur Direktchats, nennt MUC und OMEMO ausdrücklich als nicht unterstützt und OpenClaw 2026.8.2 als Mindestversion; sie verweist auf ClawHub `openclaw-xmpp@0.1.2-beta.2` und auf die Hauptquelle https://git.sdf.org/erici/openclaw-xmpp. | `DOCUMENTED` |
| `evd-034` | soilDNRA/openclaw-xmpp: Code für 1:1 ist vorhanden; OMEMO kommt in `src/` nicht vor; MUC kommt nur in einem Hinweistext vor, nach dem Gruppenchat-Optionen bis zum Abschluss einer „MUC security gate“ nicht verfügbar sind; die Hauptquelle auf git.sdf.org hat denselben Commit. | `VERIFIED` |
| `evd-035` | elmafioso79/xmpp-channel: Die README nennt 1:1- und Gruppenchat sowie OMEMO einschließlich Gruppenchats im älteren Namensraum; `peerDependencies` verlangt `openclaw ^2026.2.2-3`. Ein offener Pull Request #4 betrifft die Anpassung an OpenClaw 2026.5.2. | `DOCUMENTED` |
| `evd-036` | elmafioso79/xmpp-channel: Code für MUC (`joinMuc`) und für OMEMO bei `groupchat` ist vorhanden; keine Testdateien. | `VERIFIED` |
| `evd-037` | watkins-matt/xmpp-channel: Fork von elmafioso79/xmpp-channel, 28 Commits voraus; die README ist identisch mit dem Ursprung; `peerDependencies` verlangt `openclaw >=2026.8.2`. | `DOCUMENTED` |
| `evd-038` | watkins-matt/xmpp-channel: Code für MUC und OMEMO ist vorhanden. | `VERIFIED` |
| `evd-039` | Programmatore-Web/openclaw-xmpp-channel: Fork von watkins-matt/xmpp-channel; die README nennt 1:1 und fest eingestellte MUC-Räume, schließt Ende-zu-Ende-Verschlüsselung aus und nennt OpenClaw 2026.8.2 oder neuer. | `DOCUMENTED` |
| `evd-040` | Programmatore-Web/openclaw-xmpp-channel: Code für MUC ist vorhanden; OMEMO-Zeichenketten kommen nicht vor; verschlüsselte Nachrichten werden verworfen. | `VERIFIED` |
| `evd-041` | Programmatore-Web/openclaw-xmpp-channel: Das CHANGELOG beschreibt OMEMO-Funktionen in den Versionen 0.3.x vom Februar 2026 und führt unter „[Unreleased]“ die Entfernung der Ende-zu-Ende-Verschlüsselung auf; die README des untersuchten Stands schließt Ende-zu-Ende-Verschlüsselung aus. | `DOCUMENTED` |
| `evd-042` | MrCPA/oc-xmpp: Die README nennt Direktnachrichten und Räume, OMEMO nur für Direktnachrichten und Live-Tests als noch offen; `peerDependencies` verlangt `openclaw "*"`. | `DOCUMENTED` |
| `evd-043` | MrCPA/oc-xmpp: Code für MUC und für OMEMO in `urn:xmpp:omemo:2` ist vorhanden. | `VERIFIED` |
| `evd-044` | chitozzz/xmpp-adapter-openclaw: Die README nennt 1:1 und MUC als Ziel und das Projekt als in Planung; `peerDependencies` verlangt `openclaw >=2026.6.9`; OMEMO wird nicht genannt. | `DOCUMENTED` |
| `evd-045` | chitozzz/xmpp-adapter-openclaw: Code für 1:1 und MUC (`joinMuc`) ist vorhanden; OMEMO-Zeichenketten kommen nicht vor. | `VERIFIED` |
| `evd-046` | weijia/xmpp-connector: Die README nennt Senden und Empfangen von Nachrichten, keine OpenClaw-Version, weder MUC noch OMEMO; auf npm ist `openclaw-xmpp-connector` 0.3.0 veröffentlicht. | `DOCUMENTED` |
| `evd-047` | weijia/xmpp-connector: Code für 1:1 ist vorhanden; MUC- und OMEMO-Zeichenketten kommen nicht vor; keine Testdateien. | `VERIFIED` |
| `evd-048` | processone/openclaw, Zweig xmpp-support: Die README der Erweiterung nennt 1:1 und MUC; OMEMO wird nicht genannt; der Zweig ist Grundlage des geschlossenen PR #9741 und hängt von `openclaw workspace:*` ab. | `DOCUMENTED` |
| `evd-049` | processone/openclaw, Zweig xmpp-support: Code für 1:1 und MUC (`joinRoom`) ist vorhanden; OMEMO-Zeichenketten kommen nicht vor. | `VERIFIED` |
| `evd-050` | rsaisankalp/clawdbotElyments: Die README beschreibt eine Anbindung von Clawdbot an die XMPP-basierte Plattform Elyments mit Direktnachrichten; `peerDependencies` verlangt `clawdbot >=2026.0.0`; auf npm ist `clawdbot-elyments` 1.0.0 veröffentlicht. | `DOCUMENTED` |
| `evd-051` | rsaisankalp/clawdbotElyments: Code verarbeitet den Nachrichtentyp `groupchat`, enthält aber keinen Raumbeitritt; OMEMO-Zeichenketten kommen nicht vor; keine Testdateien. | `VERIFIED` |
| `evd-052` | Ob eines der untersuchten Projekte Direktnachrichten, OMEMO-Verschlüsselung und Gruppenchats über MUC tatsächlich funktionsfähig bereitstellt, ist unbekannt. | `UNKNOWN` |
| `evd-053` | Ob die untersuchten Projekte unter OpenClaw 2026.7.1-2 oder 2026.9.4 laden und laufen, ist unbekannt; es liegen nur deklarierte Versionsangaben vor. | `UNKNOWN` |
| `evd-054` | Ob es XMPP-Anbindungen für OpenClaw außerhalb von GitHub und npm gibt, etwa auf ClawHub, GitLab oder Codeberg, ist unbekannt. | `UNKNOWN` |

## 5. Einzelbefunde

### evd-001

Aussage:
Zurzeit sind zwei OpenClaw-Installationen mit den Versionen 2026.9.4 und 2026.7.1-2 aktiv.

Nachweisstatus:
`USER_PROVIDED`

Begründung des Nachweisstatus:
Die Aussage stammt aus der akzeptierten `idea.md` des Ideengebers. Nach `rules/evidence.md` erhält sie `USER_PROVIDED`; skizzwerk setzt sie nicht selbstständig auf `VERIFIED`.

Quellen:

| Quellenart | Fundstelle | Version oder Commit | Prüfdatum | Beitrag zum Befund |
|---|---|---|---|---|
| `USER_STATEMENT` | `idea.md` Abschnitt 2, Zeile 31 | `idea.md` Commit 4e46961 | 2026-09-14 | Aussage des Ideengebers |

Prüfung:

Durchgeführt:
- keine; Aussage übernommen

Ergebnis: –

Nicht durchgeführt:
- nicht durchgeführt: Zuordnung der Versionen zu konkreten Rechnern (siehe evd-006)

Einschränkung der Aussagekraft: Aussage des Ideengebers, nicht durch skizzwerk bestätigt

Bezug zur Projektidee:

- Fundstelle: idea.md, Abschnitt 2, Abschnitt 6
- Bedeutung: bestimmt die Versionen, deren Bestand untersucht wird

Folgerung:
Die beiden Versionen bilden den Bezugspunkt für die Versionsuntersuchung.

### evd-002

Aussage:
Ein eigener XMPP-Server ist vorhanden.

Nachweisstatus:
`USER_PROVIDED`

Begründung des Nachweisstatus:
Die Aussage stammt aus der akzeptierten `idea.md` des Ideengebers. Nach `rules/evidence.md` erhält sie `USER_PROVIDED`; skizzwerk setzt sie nicht selbstständig auf `VERIFIED`.

Quellen:

| Quellenart | Fundstelle | Version oder Commit | Prüfdatum | Beitrag zum Befund |
|---|---|---|---|---|
| `USER_STATEMENT` | `idea.md` Abschnitt 2, Zeile 30 | `idea.md` Commit 4e46961 | 2026-09-14 | Aussage des Ideengebers |

Prüfung:

Durchgeführt:
- keine; Aussage übernommen

Ergebnis: –

Nicht durchgeführt:
- wegen fehlenden Zugriffs nicht möglich: Untersuchung des Servers (siehe evd-008)

Einschränkung der Aussagekraft: Aussage des Ideengebers, nicht durch skizzwerk bestätigt

Bezug zur Projektidee:

- Fundstelle: idea.md, Abschnitt 2, Abschnitt 6
- Bedeutung: beteiligtes System

Folgerung:
Zum Server liegen keine weiteren Angaben vor.

### evd-003

Aussage:
Bestehende Plugins konnten zum Teil nicht installiert werden oder erfüllten nicht die Anforderungen an Sicherheit (OMEMO) oder Kommunikation (Gruppenchats/MUC).

Nachweisstatus:
`USER_PROVIDED`

Begründung des Nachweisstatus:
Die Aussage stammt aus der akzeptierten `idea.md` des Ideengebers. Nach `rules/evidence.md` erhält sie `USER_PROVIDED`; skizzwerk setzt sie nicht selbstständig auf `VERIFIED`.

Quellen:

| Quellenart | Fundstelle | Version oder Commit | Prüfdatum | Beitrag zum Befund |
|---|---|---|---|---|
| `USER_STATEMENT` | `idea.md` Abschnitt 2, Zeilen 32–34 | `idea.md` Commit 4e46961 | 2026-09-14 | Aussage des Ideengebers |

Prüfung:

Durchgeführt:
- keine; Aussage übernommen

Ergebnis: –

Nicht durchgeführt:
- wegen fehlenden Zugriffs nicht möglich: Ermittlung der erprobten Plugins (siehe evd-007)

Einschränkung der Aussagekraft: Aussage des Ideengebers, nicht durch skizzwerk bestätigt

Bezug zur Projektidee:

- Fundstelle: idea.md, Abschnitt 2, Abschnitt 11
- Bedeutung: dokumentierter bisheriger Versuch

Folgerung:
Die erprobten Plugins sind nicht benannt; ein Abgleich mit den Projekten in evd-022 bis evd-051 ist nicht möglich.

### evd-004

Aussage:
Auf dem Rechner srv001 ist OpenClaw 2026.9.4 (Commit 3a9d69d) als globales npm-Paket installiert; der Dienst `openclaw.service` ist aktiv.

Nachweisstatus:
`VERIFIED`

Begründung des Nachweisstatus:
Version, Paket und Dienststatus wurden unmittelbar durch Befehlsausgaben auf srv001 bestätigt.

Quellen:

| Quellenart | Fundstelle | Version oder Commit | Prüfdatum | Beitrag zum Befund |
|---|---|---|---|---|
| `MANUAL_TEST` | `openclaw --version` auf srv001 | openclaw@2026.9.4 (3a9d69d) | 2026-09-14 | Ausgabe `OpenClaw 2026.9.4 (3a9d69d)` |
| `MANUAL_TEST` | `npm ls -g --depth=0` auf srv001 | openclaw@2026.9.4 | 2026-09-14 | Ausgabe `openclaw@2026.9.4` |
| `MANUAL_TEST` | `systemctl is-active openclaw` auf srv001 | – | 2026-09-14 | Ausgabe `active` |

Prüfung:

Durchgeführt:
- Befehlsausgaben gelesen

Ergebnis: wie in der Aussage

Nicht durchgeführt:
- wegen fehlenden Zugriffs nicht möglich: Lesen von Konfiguration und installierten Plugins

Einschränkung der Aussagekraft: belegt nur Version und Dienststatus, keine Kanal- oder Plugin-Konfiguration

Bezug zur Projektidee:

- Fundstelle: idea.md, Abschnitt 2, Abschnitt 6
- Bedeutung: vorhandene Installation einer der genannten Versionen

Folgerung:
Eine Installation der Version 2026.9.4 ist auf srv001 vorhanden.

### evd-005

Aussage:
Die lokale Installationsanleitung beschreibt OpenClaw mit dem mitgelieferten WebChat und Authelia sowie ein über ClawHub installiertes Provider-Plugin; XMPP wird dort nicht erwähnt.

Nachweisstatus:
`DOCUMENTED`

Begründung des Nachweisstatus:
Die Aussage beruht auf Projektdokumentation, die nicht mit dem Betriebsstand abgeglichen wurde; sie erhält daher höchstens `DOCUMENTED`.

Quellen:

| Quellenart | Fundstelle | Version oder Commit | Prüfdatum | Beitrag zum Befund |
|---|---|---|---|---|
| `PROJECT_DOCUMENTATION` | `/srv/aixlab/docs/anleitungen/dev-server/09-00-dev-server-install-openclaw.md` Zeilen 3, 32 | kein Git-Stand; Dateistand 2026-08-30, SHA-256-Präfix e559ec29d7d8b2aa | 2026-09-14 | Beschreibung von WebChat, Authelia und Installation über npm |
| `PROJECT_DOCUMENTATION` | `/srv/aixlab/docs/sysdoc/srv001/anleitungen/eurouter-provider-openclaw.md` Zeile 14 | kein Git-Stand; Dateistand 2026-08-12, SHA-256-Präfix 5a93f1232b7ebc32 | 2026-09-14 | Installation eines Provider-Plugins über ClawHub |
| `PROJECT_DOCUMENTATION` | Volltextsuche in `/srv/aixlab/docs` nach xmpp, jabber, prosody, ejabberd, omemo | Dateistand 2026-09-14 | 2026-09-14 | keine XMPP-Treffer außerhalb von `archiv/` |

Prüfung:

Durchgeführt:
- Dateien gelesen und durchsucht

Ergebnis: wie in der Aussage

Nicht durchgeführt:
- wegen fehlenden Zugriffs nicht möglich: Abgleich mit der tatsächlichen Konfiguration

Einschränkung der Aussagekraft: Dokumentation kann vom Betriebsstand abweichen

Bezug zur Projektidee:

- Fundstelle: idea.md, Abschnitt 2, Abschnitt 6
- Bedeutung: dokumentierter Bestand der vorhandenen Installation

Folgerung:
Die vorhandene Dokumentation enthält keine Angaben zu einer XMPP-Anbindung.

### evd-006

Aussage:
Ob srv001 eine der beiden vom Ideengeber genannten Installationen ist und wo die Installation mit Version 2026.7.1-2 läuft, ist unbekannt.

Nachweisstatus:
`UNKNOWN`

Begründung des Nachweisstatus:
Weder `idea.md` noch die lokale Dokumentation noch der Rechner srv001 enthalten eine Angabe dazu; es liegt keine ausreichende Information vor.

Quellen:

| Quellenart | Fundstelle | Version oder Commit | Prüfdatum | Beitrag zum Befund |
|---|---|---|---|---|
| `USER_STATEMENT` | `idea.md` Abschnitt 2, Zeile 31 | `idea.md` Commit 4e46961 | 2026-09-14 | nennt die Versionen, aber keine Rechner |
| `PROJECT_DOCUMENTATION` | Volltextsuche in `/srv/aixlab/docs` | Dateistand 2026-09-14 | 2026-09-14 | keine Angabe zur zweiten Installation |
| `MANUAL_TEST` | `openclaw --version` auf srv001 | openclaw@2026.9.4 (3a9d69d) | 2026-09-14 | zeigt nur die lokale Version |

Prüfung:

Durchgeführt:
- lokale Dokumentation und Rechner srv001 durchsucht

Ergebnis: keine Angabe zur zweiten Installation gefunden

Nicht durchgeführt:
- nicht durchgeführt: Suche auf weiteren Rechnern, weil keine weiteren Rechner genannt sind

Einschränkung der Aussagekraft: Angabe fehlt in allen zugänglichen Quellen

Bezug zur Projektidee:

- Fundstelle: idea.md, Abschnitt 2, Abschnitt 11
- Bedeutung: Umfang der vorhandenen Installationen

Folgerung:
Die Installation mit 2026.7.1-2 ist nicht untersucht.

### evd-007

Aussage:
Welche Plugins in den vorhandenen Installationen installiert oder erprobt wurden und woran ihre Installation scheiterte, ist unbekannt.

Nachweisstatus:
`UNKNOWN`

Begründung des Nachweisstatus:
Das Konfigurationsverzeichnis ist nicht lesbar und keine Dokumentation beschreibt die Versuche; es liegt keine ausreichende Information vor.

Quellen:

| Quellenart | Fundstelle | Version oder Commit | Prüfdatum | Beitrag zum Befund |
|---|---|---|---|---|
| `MANUAL_TEST` | `ls /var/lib/openclaw/.openclaw` auf srv001 | – | 2026-09-14 | Ausgabe `Permission denied` |
| `PROJECT_DOCUMENTATION` | Volltextsuche in `/srv/aixlab/docs` | Dateistand 2026-09-14 | 2026-09-14 | keine Aufzeichnung zu früheren Plugin-Versuchen |
| `USER_STATEMENT` | `idea.md` Abschnitt 2, Zeilen 32–34 | `idea.md` Commit 4e46961 | 2026-09-14 | nennt Versuche ohne Plugin-Namen |

Prüfung:

Durchgeführt:
- Verzeichnis zu lesen versucht; Dokumentation durchsucht

Ergebnis: Zugriff verweigert; keine Dokumentation

Nicht durchgeführt:
- wegen fehlenden Zugriffs nicht möglich: Lesen der Plugin-Liste
- nicht durchgeführt: `openclaw plugins list` auf dem produktiv verwendeten srv001

Einschränkung der Aussagekraft: keine zugängliche Quelle

Bezug zur Projektidee:

- Fundstelle: idea.md, Abschnitt 2, Abschnitt 11
- Bedeutung: dokumentierter bisheriger Versuch

Folgerung:
Die bisherigen Versuche sind nicht nachvollziehbar dokumentiert.

### evd-008

Aussage:
Software, Standort und unterstützte XMPP-Erweiterungen des eigenen XMPP-Servers sind unbekannt.

Nachweisstatus:
`UNKNOWN`

Begründung des Nachweisstatus:
Keine zugängliche Quelle enthält Angaben zum Server; das Fehlen eines Dienstes auf srv001 ist kein Nachweis über einen Server an anderer Stelle.

Quellen:

| Quellenart | Fundstelle | Version oder Commit | Prüfdatum | Beitrag zum Befund |
|---|---|---|---|---|
| `USER_STATEMENT` | `idea.md` Abschnitt 2, Zeile 30 | `idea.md` Commit 4e46961 | 2026-09-14 | nennt den Server ohne weitere Angaben |
| `PROJECT_DOCUMENTATION` | Volltextsuche in `/srv/aixlab/docs` nach xmpp, prosody, ejabberd | Dateistand 2026-09-14 | 2026-09-14 | keine Dokumentation außerhalb von `archiv/` |
| `MANUAL_TEST` | `systemctl list-units --type=service` auf srv001, gefiltert nach prosody, ejabberd, xmpp | – | 2026-09-14 | kein Dienst mit diesen Namen auf srv001 |

Prüfung:

Durchgeführt:
- Dokumentation und Dienstliste auf srv001 durchsucht

Ergebnis: keine Angaben

Nicht durchgeführt:
- wegen fehlenden Zugriffs nicht möglich: Untersuchung des Servers selbst, da Standort unbekannt

Einschränkung der Aussagekraft: keine zugängliche Quelle zum Server

Bezug zur Projektidee:

- Fundstelle: idea.md, Abschnitt 2, Abschnitt 11
- Bedeutung: beteiligtes System

Folgerung:
Der XMPP-Server ist nicht untersucht.

### evd-009

Aussage:
Die Versionen 2026.7.1-2 (veröffentlicht 2026-07-18T03:53:48Z, Tag-Commit 0790d9f593ad) und 2026.9.4 (veröffentlicht 2026-09-11T02:44:59Z, Tag-Commit 3a9d69db306c) sind im npm-Register veröffentlicht; `latest` ist 2026.9.4, `extended-stable` ist 2026.6.35.

Nachweisstatus:
`VERIFIED`

Begründung des Nachweisstatus:
Veröffentlichungsdaten und Dist-Tags stammen unmittelbar aus dem npm-Register als Primärquelle; die Tags wurden über die GitHub-API auf Commits aufgelöst.

Quellen:

| Quellenart | Fundstelle | Version oder Commit | Prüfdatum | Beitrag zum Befund |
|---|---|---|---|---|
| `PRIMARY_DOCUMENTATION` | https://registry.npmjs.org/openclaw (`time`, `dist-tags`) | Registerstand 2026-09-14 | 2026-09-14 | Veröffentlichungsdaten und Dist-Tags |
| `SOURCE_CODE` | https://github.com/openclaw/openclaw Tags `v2026.7.1-2` und `v2026.9.4` | Tag-Objekte be8b8a9e8838 und 8bec206f3c1f | 2026-09-14 | Auflösung der Tags auf die Commits 0790d9f593ad und 3a9d69db306c |

Prüfung:

Durchgeführt:
- Registerdaten mit `jq` ausgewertet; Tags über die GitHub-API aufgelöst

Ergebnis: wie in der Aussage

Nicht durchgeführt:
- nicht durchgeführt: Laden des Paketinhalts von 2026.7.1-2

Einschränkung der Aussagekraft: Register ist Primärquelle für Veröffentlichungen

Bezug zur Projektidee:

- Fundstelle: idea.md, Abschnitt 1 („aktuelle OpenClaw-Versionen“), Abschnitt 10
- Bedeutung: Einordnung der genannten Versionen

Folgerung:
Beide genannten Versionen existieren; 2026.9.4 ist die zum Untersuchungszeitpunkt neueste stabile Version.

### evd-010

Aussage:
Zwischen 2026.7.1-2 und 2026.9.4 wurden 17 Versionen veröffentlicht: 2026.8.1, 2026.8.2, 2026.9.1, 2026.9.2, 2026.9.3, neun Beta-Versionen und 2026.6.33 bis 2026.6.35.

Nachweisstatus:
`VERIFIED`

Begründung des Nachweisstatus:
Die Zählung wurde unmittelbar aus den Veröffentlichungszeiten des npm-Registers ermittelt.

Quellen:

| Quellenart | Fundstelle | Version oder Commit | Prüfdatum | Beitrag zum Befund |
|---|---|---|---|---|
| `PRIMARY_DOCUMENTATION` | https://registry.npmjs.org/openclaw (`time`) | Registerstand 2026-09-14 | 2026-09-14 | Veröffentlichungszeiten aller Versionen |

Prüfung:

Durchgeführt:
- Veröffentlichungszeiten mit `jq` gefiltert

Ergebnis: 17 Einträge

Nicht durchgeführt:
- nicht erforderlich: weitere Prüfung

Einschränkung der Aussagekraft: Zählung nach Veröffentlichungsdatum, nicht nach Versionsnummer

Bezug zur Projektidee:

- Fundstelle: idea.md, Abschnitt 1 („neue OpenClaw-Versionen“), Abschnitt 11
- Bedeutung: Häufigkeit neuer Versionen

Folgerung:
Im Zeitraum von knapp acht Wochen erschienen fünf stabile Versionen.

### evd-011

Aussage:
Die Exportpfade `./plugin-sdk` und `./extension-api` sind in 2026.7.1-2 und 2026.7.2-beta.3 vorhanden, ab 2026.7.2-beta.4 und in 2026.9.4 nicht mehr.

Nachweisstatus:
`VERIFIED`

Begründung des Nachweisstatus:
Die Exportpfade wurden unmittelbar in den Paketmetadaten des npm-Registers verglichen.

Quellen:

| Quellenart | Fundstelle | Version oder Commit | Prüfdatum | Beitrag zum Befund |
|---|---|---|---|---|
| `PRIMARY_DOCUMENTATION` | https://registry.npmjs.org/openclaw (`versions["2026.7.1-2"].exports`, `versions["2026.7.2-beta.3"].exports`, `versions["2026.7.2-beta.4"].exports`, `versions["2026.9.4"].exports`) | Registerstand 2026-09-14 | 2026-09-14 | vorhandene und fehlende Exportpfade je Version |

Prüfung:

Durchgeführt:
- `exports` der Versionen mit `jq` verglichen

Ergebnis: wie in der Aussage

Nicht durchgeführt:
- nicht durchgeführt: Vergleich der Paketinhalte

Einschränkung der Aussagekraft: belegt die Paketmetadaten, nicht das Laufzeitverhalten

Bezug zur Projektidee:

- Fundstelle: idea.md, Abschnitt 1, Abschnitt 11
- Bedeutung: Änderungen an der Plugin-Schnittstelle

Folgerung:
Die Plugin-Schnittstelle unterscheidet sich zwischen den beiden genannten Versionen in ihren Exportpfaden.

### evd-012

Aussage:
Das Paket 2026.9.4 exportiert Unterpfade `openclaw/plugin-sdk/*`, darunter `channel-core`, `channel-contract`, `channel-entry-contract` und `plugin-entry`; `channel-core.d.ts` exportiert u. a. `ChannelPlugin` und `defineChannelPluginEntry`.

Nachweisstatus:
`VERIFIED`

Begründung des Nachweisstatus:
Exporte und Typnamen wurden unmittelbar in den Dateien des installierten Pakets gelesen.

Quellen:

| Quellenart | Fundstelle | Version oder Commit | Prüfdatum | Beitrag zum Befund |
|---|---|---|---|---|
| `SOURCE_CODE` | `/usr/lib/node_modules/openclaw/package.json` Zeilen 1068, 1072, 1076, 1396 | openclaw@2026.9.4 (3a9d69d) | 2026-09-14 | Exportpfade für Kanal-Plugins |
| `SOURCE_CODE` | `/usr/lib/node_modules/openclaw/dist/plugin-sdk/channel-core.d.ts` Zeile 10 | openclaw@2026.9.4 (3a9d69d) | 2026-09-14 | exportierte Typen und Funktionen |

Prüfung:

Durchgeführt:
- Dateien im installierten Paket gelesen

Ergebnis: wie in der Aussage

Nicht durchgeführt:
- nicht durchgeführt: Bau eines Plugins gegen die Schnittstelle

Einschränkung der Aussagekraft: belegt vorhandene Exporte und Typen, nicht deren Verhalten

Bezug zur Projektidee:

- Fundstelle: idea.md, Abschnitt 1, Abschnitt 5
- Bedeutung: vorhandene Schnittstelle für Kanal-Plugins

Folgerung:
Für Kanal-Plugins ist in 2026.9.4 eine eigene SDK-Schnittstelle vorhanden.

### evd-013

Aussage:
Laut Dokumentation braucht jedes native Plugin eine `openclaw.plugin.json`; die Felder `openclaw.compat.pluginApi` und `openclaw.install.minHostVersion` werden bei npm-Installationen zur Versionsauswahl ausgewertet.

Nachweisstatus:
`DOCUMENTED`

Begründung des Nachweisstatus:
Die Aussage steht in der offiziellen Dokumentation; das Installationsverhalten wurde nicht praktisch geprüft.

Quellen:

| Quellenart | Fundstelle | Version oder Commit | Prüfdatum | Beitrag zum Befund |
|---|---|---|---|---|
| `PRIMARY_DOCUMENTATION` | `/usr/lib/node_modules/openclaw/docs/plugins/manifest.md` Zeile 20 | openclaw@2026.9.4 (3a9d69d) | 2026-09-14 | Pflicht der `openclaw.plugin.json` |
| `PRIMARY_DOCUMENTATION` | `/usr/lib/node_modules/openclaw/docs/plugins/building-plugins.md` Zeilen 79–86 | openclaw@2026.9.4 (3a9d69d) | 2026-09-14 | Kompatibilitätsfelder in `package.json` |
| `PRIMARY_DOCUMENTATION` | `/usr/lib/node_modules/openclaw/docs/tools/plugin.md` Zeilen 141–147 | openclaw@2026.9.4 (3a9d69d) | 2026-09-14 | Auswertung bei npm-Installationen |

Prüfung:

Durchgeführt:
- Dokumentation gelesen

Ergebnis: wie in der Aussage

Nicht durchgeführt:
- nicht durchgeführt: Test des Installationsverhaltens

Einschränkung der Aussagekraft: Dokumentationsaussage

Bezug zur Projektidee:

- Fundstelle: idea.md, Abschnitt 1, Abschnitt 5
- Bedeutung: dokumentierter Plugin- und Kompatibilitätsmechanismus

Folgerung:
Die Kompatibilitätsangaben eines Plugins werden laut Dokumentation bei der Installation berücksichtigt.

### evd-014

Aussage:
Laut Dokumentation sind alle Plugin-APIs experimentell und können sich zwischen OpenClaw-Versionen ändern; Plugin-Autoren sollen die Version festlegen und jede als kompatibel angegebene Version testen.

Nachweisstatus:
`DOCUMENTED`

Begründung des Nachweisstatus:
Die Aussage steht wörtlich in der offiziellen Dokumentation; sie ist eine Herstelleraussage, kein geprüftes Verhalten.

Quellen:

| Quellenart | Fundstelle | Version oder Commit | Prüfdatum | Beitrag zum Befund |
|---|---|---|---|---|
| `PRIMARY_DOCUMENTATION` | `/usr/lib/node_modules/openclaw/docs/plugins/sdk-overview.md` Zeilen 25–36 | openclaw@2026.9.4 (3a9d69d) | 2026-09-14 | wörtlich: „These contracts can change between OpenClaw releases.“ |

Prüfung:

Durchgeführt:
- Dokumentation gelesen

Ergebnis: wie in der Aussage

Nicht durchgeführt:
- nicht erforderlich: praktische Prüfung einer Herstelleraussage zur Stabilität

Einschränkung der Aussagekraft: Dokumentationsaussage

Bezug zur Projektidee:

- Fundstelle: idea.md, Abschnitt 1 (Verfahren für neue Versionen), Abschnitt 11
- Bedeutung: dokumentierte Stabilität der Schnittstelle

Folgerung:
Die Hersteller-Dokumentation sagt keine stabile Plugin-Schnittstelle zu.

### evd-015

Aussage:
Laut Dokumentation sind `openclaw/plugin-sdk`, `openclaw/plugin-sdk/compat` und `openclaw/extension-api` entfernt; Plugins, die sie importieren, laden nicht mehr. Alte Verträge laufen befristet über Kompatibilitätsadapter.

Nachweisstatus:
`DOCUMENTED`

Begründung des Nachweisstatus:
Die Aussage steht in der offiziellen Dokumentation; das Ladeverhalten wurde nicht praktisch geprüft.

Quellen:

| Quellenart | Fundstelle | Version oder Commit | Prüfdatum | Beitrag zum Befund |
|---|---|---|---|---|
| `PRIMARY_DOCUMENTATION` | `/usr/lib/node_modules/openclaw/docs/plugins/sdk-migration.md` Zeilen 19–22, 37–49 | openclaw@2026.9.4 (3a9d69d) | 2026-09-14 | entfernte Einstiegspfade und Folge für Plugins |
| `PRIMARY_DOCUMENTATION` | `/usr/lib/node_modules/openclaw/docs/plugins/compatibility.md` Zeilen 14–33 | openclaw@2026.9.4 (3a9d69d) | 2026-09-14 | Kompatibilitätsadapter mit Status und Entfernungsfristen |

Prüfung:

Durchgeführt:
- Dokumentation gelesen

Ergebnis: wie in der Aussage

Nicht durchgeführt:
- nicht durchgeführt: Lesen von `src/plugins/compat/registry.ts`
- nicht durchgeführt: Test des Ladeverhaltens

Einschränkung der Aussagekraft: Dokumentationsaussage

Bezug zur Projektidee:

- Fundstelle: idea.md, Abschnitt 1, Abschnitt 11
- Bedeutung: dokumentierte Folgen von Schnittstellenänderungen

Folgerung:
Die Dokumentation beschreibt Änderungen, die ältere Plugins am Laden hindern.

### evd-016

Aussage:
Das CHANGELOG nennt für 2026.9.3 mehrere als „Breaking“ gekennzeichnete Änderungen am Plugin-SDK und für 2026.8.1 bis 2026.9.4 Abkündigungen von SDK-Pfaden mit Entfernungsterminen 2026-09-01 und 2026-09-08.

Nachweisstatus:
`DOCUMENTED`

Begründung des Nachweisstatus:
Die Aussage beruht auf dem offiziellen CHANGELOG; Vollständigkeit und Umsetzung wurden nicht geprüft.

Quellen:

| Quellenart | Fundstelle | Version oder Commit | Prüfdatum | Beitrag zum Befund |
|---|---|---|---|---|
| `PRIMARY_DOCUMENTATION` | https://github.com/openclaw/openclaw/blob/v2026.9.4/CHANGELOG.md, Abschnitt 2026.9.3 („Breaking — SDK aliases“, „Breaking — approval SDK“) | Commit 3a9d69db306c | 2026-09-14 | Breaking Changes am Plugin-SDK |
| `PRIMARY_DOCUMENTATION` | https://github.com/openclaw/openclaw/blob/v2026.9.4/CHANGELOG.md, Abschnitte 2026.8.1 („Upcoming deprecations (2026-09-01)“), 2026.8.2 und 2026.9.2 | Commit 3a9d69db306c | 2026-09-14 | Abkündigungen mit Entfernungsterminen |

Prüfung:

Durchgeführt:
- Einträge mit Bezug zu Plugin-SDK und Kanälen durchsucht

Ergebnis: 15 zitierte Einträge, davon 4 „Breaking“ in 2026.9.3

Nicht durchgeführt:
- nicht durchgeführt: vollständiges Lesen des CHANGELOG (rund 24 000 Zeilen)

Einschränkung der Aussagekraft: Dokumentationsaussage; die Abschnitte 2026.7.1-1 und 2026.7.1-2 fehlen im CHANGELOG am Tag `v2026.9.4`

Bezug zur Projektidee:

- Fundstelle: idea.md, Abschnitt 1, Abschnitt 11
- Bedeutung: Häufigkeit von Schnittstellenänderungen

Folgerung:
Im untersuchten Zeitraum sind Schnittstellenänderungen dokumentiert.

### evd-017

Aussage:
Zwischen 2026.7.1-2 und 2026.9.4 hat sich die Plugin-Schnittstelle so geändert, dass Plugins, die die entfernten Pfade nutzen, unter 2026.9.4 laut Dokumentation nicht laden.

Nachweisstatus:
`INFERRED`

Begründung des Nachweisstatus:
Die Aussage verbindet den geprüften Wegfall der Exportpfade (evd-011) mit den dokumentierten Folgen (evd-015, evd-016). Sie ist nachvollziehbar abgeleitet, aber nicht praktisch geprüft.

Quellen:

| Quellenart | Fundstelle | Version oder Commit | Prüfdatum | Beitrag zum Befund |
|---|---|---|---|---|
| `PRIMARY_DOCUMENTATION` | https://registry.npmjs.org/openclaw (`versions[*].exports`) | Registerstand 2026-09-14 | 2026-09-14 | Wegfall der Exportpfade, siehe evd-011 |
| `PRIMARY_DOCUMENTATION` | `/usr/lib/node_modules/openclaw/docs/plugins/sdk-migration.md` Zeilen 19–22 | openclaw@2026.9.4 (3a9d69d) | 2026-09-14 | dokumentierte Folge, siehe evd-015 |
| `PRIMARY_DOCUMENTATION` | https://github.com/openclaw/openclaw/blob/v2026.9.4/CHANGELOG.md | Commit 3a9d69db306c | 2026-09-14 | dokumentierte Änderungen, siehe evd-016 |
| `ANALYSIS` | Verknüpfung von evd-011, evd-015 und evd-016 | – | 2026-09-14 | Ableitung |

Prüfung:

Durchgeführt:
- Ableitung aus den genannten Befunden

Ergebnis: –

Nicht durchgeführt:
- nicht durchgeführt: Laden eines Plugins unter beiden Versionen

Einschränkung der Aussagekraft: Ableitung aus Registerdaten und Dokumentation

Bezug zur Projektidee:

- Fundstelle: idea.md, Abschnitt 1, Abschnitt 10 („aktuelle OpenClaw-Versionen“), Abschnitt 11
- Bedeutung: Bestand zu Änderungen zwischen den genannten Versionen

Folgerung:
Die beiden genannten Versionen stellen nicht dieselbe Plugin-Schnittstelle bereit.

### evd-018

Aussage:
Das Paket 2026.9.4 enthält unter `dist/extensions/` 60 Erweiterungen, darunter keine für XMPP; die Suche nach `xmpp`, `jabber`, `omemo`, `muc` trifft nur Fremdbibliotheken (URL-Schema, MIME-Typ).

Nachweisstatus:
`VERIFIED`

Begründung des Nachweisstatus:
Verzeichnisinhalt und Suchtreffer wurden unmittelbar im installierten Paket ermittelt.

Quellen:

| Quellenart | Fundstelle | Version oder Commit | Prüfdatum | Beitrag zum Befund |
|---|---|---|---|---|
| `SOURCE_CODE` | `/usr/lib/node_modules/openclaw/dist/extensions/` | openclaw@2026.9.4 (3a9d69d) | 2026-09-14 | 60 Ordner, keiner mit xmpp im Namen |
| `SOURCE_CODE` | Volltextsuche mit Wortgrenzen in `/usr/lib/node_modules/openclaw/` ohne `node_modules`; Treffer u. a. `dist/worker/worker.mjs` Zeile 31129 | openclaw@2026.9.4 (3a9d69d) | 2026-09-14 | Treffer nur in Fremdbibliotheken |

Prüfung:

Durchgeführt:
- Verzeichnis gelistet und nachgezählt; Volltextsuche

Ergebnis: wie in der Aussage

Nicht durchgeführt:
- nicht erforderlich: weitere Prüfung

Einschränkung der Aussagekraft: gilt nur für das installierte Paket, nicht für nachinstallierbare Plugins

Bezug zur Projektidee:

- Fundstelle: idea.md, Abschnitt 1, Abschnitt 5
- Bedeutung: vorhandene XMPP-Unterstützung im Lieferumfang

Folgerung:
OpenClaw 2026.9.4 liefert keinen XMPP-Kanal mit.

### evd-019

Aussage:
Die Kanalübersicht der Dokumentation nennt mitgelieferte und offizielle Kanal-Plugins, aber kein XMPP- oder Jabber-Plugin.

Nachweisstatus:
`DOCUMENTED`

Begründung des Nachweisstatus:
Die Aussage beruht auf der offiziellen Dokumentation; sie beschreibt den dokumentierten, nicht den tatsächlich verfügbaren Bestand.

Quellen:

| Quellenart | Fundstelle | Version oder Commit | Prüfdatum | Beitrag zum Befund |
|---|---|---|---|---|
| `PRIMARY_DOCUMENTATION` | `/usr/lib/node_modules/openclaw/docs/channels/index.md` Zeilen 38–69 | openclaw@2026.9.4 (3a9d69d) | 2026-09-14 | Liste der dokumentierten Kanäle ohne XMPP |

Prüfung:

Durchgeführt:
- Datei gelesen, nach xmpp und jabber gesucht

Ergebnis: keine Treffer

Nicht durchgeführt:
- nicht durchgeführt: Vergleich mit docs.openclaw.ai

Einschränkung der Aussagekraft: Dokumentationsaussage

Bezug zur Projektidee:

- Fundstelle: idea.md, Abschnitt 1, Abschnitt 5
- Bedeutung: offiziell dokumentierte Kanäle

Folgerung:
Ein offizielles XMPP-Plugin ist nicht dokumentiert.

### evd-020

Aussage:
Im Repository `openclaw/openclaw` enthält `extensions/` auf `main` kein XMPP-Verzeichnis; die Pull Requests #9741, #20998 und #21015 für XMPP wurden ohne Merge geschlossen; Issue #29046 „[Feature]: XMPP support“ ist mit `not_planned` geschlossen.

Nachweisstatus:
`VERIFIED`

Begründung des Nachweisstatus:
Verzeichnisbaum und Status wurden unmittelbar über die GitHub-API gelesen. Bestätigt sind nur Verzeichnisinhalt und Status, nicht die Inhalte der Diskussionen.

Quellen:

| Quellenart | Fundstelle | Version oder Commit | Prüfdatum | Beitrag zum Befund |
|---|---|---|---|---|
| `SOURCE_CODE` | https://github.com/openclaw/openclaw/tree/main/extensions | Commit df663a946582 | 2026-09-14 | 167 Einträge, keiner mit xmpp oder jabber |
| `ISSUE_OR_PR` | https://github.com/openclaw/openclaw/pull/9741 | – | 2026-09-14 | geschlossen 2026-02-06, `merged=false` |
| `ISSUE_OR_PR` | https://github.com/openclaw/openclaw/pull/20998 | – | 2026-09-14 | geschlossen 2026-02-20, `merged=false` |
| `ISSUE_OR_PR` | https://github.com/openclaw/openclaw/pull/21015 | – | 2026-09-14 | geschlossen 2026-02-28, `merged=false` |
| `ISSUE_OR_PR` | https://github.com/openclaw/openclaw/issues/29046 | – | 2026-09-14 | geschlossen, `state_reason: not_planned` |

Prüfung:

Durchgeführt:
- GitHub-API: Verzeichnisbaum, Status, `merged`, `closed_at`, `state_reason`

Ergebnis: wie in der Aussage

Nicht durchgeführt:
- nicht durchgeführt: Auswertung der Diskussionen

Einschränkung der Aussagekraft: belegt nur den Status, nicht die Gründe

Bezug zur Projektidee:

- Fundstelle: idea.md, Abschnitt 1 („Vorhandene GitHub-Projekte“), Abschnitt 5
- Bedeutung: vorhandene Upstream-Arbeiten zu XMPP

Folgerung:
Es gab Beiträge für XMPP im Hauptprojekt, die nicht übernommen wurden.

### evd-021

Aussage:
OpenClaw hieß laut Projektdokumentation zuvor Warelay, Clawdbot und Moltbot; seit dem 30. Januar 2026 heißt es OpenClaw.

Nachweisstatus:
`DOCUMENTED`

Begründung des Nachweisstatus:
Die Namensfolge steht in der offiziellen Dokumentation; die Umleitung der alten Repository-Namen stützt sie, bestätigt aber nicht die Daten.

Quellen:

| Quellenart | Fundstelle | Version oder Commit | Prüfdatum | Beitrag zum Befund |
|---|---|---|---|---|
| `PRIMARY_DOCUMENTATION` | `/usr/lib/node_modules/openclaw/docs/start/lore.md` Zeilen 14–24 | openclaw@2026.9.4 (3a9d69d) | 2026-09-14 | Namensfolge und Datum |
| `PRIMARY_DOCUMENTATION` | https://github.com/openclaw/openclaw/blob/main/VISION.md Zeile 13 | Commit df663a946582 | 2026-09-14 | Namensfolge |
| `SOURCE_CODE` | GitHub-API `repos/clawdbot/clawdbot` und `repos/moltbot/moltbot` | – | 2026-09-14 | HTTP 301 auf das Repository `openclaw/openclaw` |

Prüfung:

Durchgeführt:
- Dateien gelesen; Umleitung über die GitHub-API geprüft

Ergebnis: wie in der Aussage

Nicht durchgeführt:
- nicht erforderlich: weitere Prüfung

Einschränkung der Aussagekraft: Dokumentationsaussage

Bezug zur Projektidee:

- Fundstelle: idea.md, Abschnitt 1 („Vorhandene GitHub-Projekte“)
- Bedeutung: Suchbegriffe für ältere Projekte

Folgerung:
Ältere Projekte können unter den früheren Namen geführt sein; diese Namen wurden in die Suche aufgenommen.

### evd-022

Aussage:
ksmith211/openclaw-xmpp: Die README beschreibt ein Kanal-Plugin nur für Direktnachrichten; MUC, OMEMO und eine OpenClaw-Version werden nicht genannt. Auf npm ist `@ksmith221/openclaw-xmpp` 0.1.1 veröffentlicht.

Nachweisstatus:
`DOCUMENTED`

Begründung des Nachweisstatus:
Die Aussage beruht auf Projektdokumentation und deklarierten Paketangaben. Nach `rules/evidence.md` erhalten README-Angaben höchstens `DOCUMENTED`; eine praktische Prüfung liegt nicht vor.

Quellen:

| Quellenart | Fundstelle | Version oder Commit | Prüfdatum | Beitrag zum Befund |
|---|---|---|---|---|
| `PROJECT_DOCUMENTATION` | https://github.com/ksmith211/openclaw-xmpp, `README.md` Zeilen 1–3, 14 | Commit ad1ad44777fc | 2026-09-14 | Beschreibung als DM-Plugin, keine Versionsangabe |
| `SOURCE_CODE` | https://github.com/ksmith211/openclaw-xmpp, `package.json` | Commit ad1ad44777fc | 2026-09-14 | kein `peerDependencies`- und kein `engines`-Feld |
| `PRIMARY_DOCUMENTATION` | https://registry.npmjs.org/@ksmith221/openclaw-xmpp | Registerstand 2026-09-14 | 2026-09-14 | veröffentlichte Version 0.1.1 vom 2026-02-02 |

Prüfung:

Durchgeführt:
- README und Paketmetadaten gelesen

Ergebnis: wie in der Aussage

Nicht durchgeführt:
- nicht durchgeführt: Installation und Funktionstest in einer getrennten Arbeitsumgebung

Einschränkung der Aussagekraft: Projektangaben, nicht praktisch bestätigt

Bezug zur Projektidee:

- Fundstelle: idea.md, Abschnitt 1 (Direktnachrichten, OMEMO, MUC, GitHub-Projekte), Abschnitt 7
- Bedeutung: dokumentierte Funktionen und Versionsangaben eines vorhandenen Projekts

Folgerung:
Die dokumentierten Funktionen sind nicht praktisch geprüft.

### evd-023

Aussage:
ksmith211/openclaw-xmpp: Code für 1:1-Nachrichten ist vorhanden (`type: "chat"`); Zeichenketten zu MUC, groupchat und OMEMO kommen in `src/` nicht vor; keine Testdateien.

Nachweisstatus:
`VERIFIED`

Begründung des Nachweisstatus:
Die Aussage beschränkt sich auf im gelesenen Quelltext vorhandene oder nicht gefundene Zeichenketten und Dateien. Das ist unmittelbar durch den Quelltext bestätigt. Über die Funktionsfähigkeit sagt die Aussage nichts.

Quellen:

| Quellenart | Fundstelle | Version oder Commit | Prüfdatum | Beitrag zum Befund |
|---|---|---|---|---|
| `SOURCE_CODE` | https://github.com/ksmith211/openclaw-xmpp, `src/inbound.ts` Zeile 101 | Commit ad1ad44777fc | 2026-09-14 | Verarbeitung von 1:1-Nachrichten |
| `SOURCE_CODE` | https://github.com/ksmith211/openclaw-xmpp, `src/send.ts` Zeile 16 | Commit ad1ad44777fc | 2026-09-14 | Senden von 1:1-Nachrichten |
| `SOURCE_CODE` | https://github.com/ksmith211/openclaw-xmpp, `src/` mit `grep -rniE 'muc\|omemo\|groupchat'` | Commit ad1ad44777fc | 2026-09-14 | 0 Treffer |

Prüfung:

Durchgeführt:
- Quelltext in einer getrennten Arbeitsumgebung per `git clone --depth 1` gelesen und nach Namensräumen und Bezeichnern durchsucht

Ergebnis: wie in der Aussage; Tests: keine

Nicht durchgeführt:
- nicht durchgeführt: Build, Ausführen der Tests und Funktionstest in einer getrennten Arbeitsumgebung

Einschränkung der Aussagekraft: belegt nur vorhandenen Code; 0 Treffer belegt nur das Fehlen der gesuchten Zeichenketten, nicht das Fehlen einer Funktion

Bezug zur Projektidee:

- Fundstelle: idea.md, Abschnitt 1, Abschnitt 7
- Bedeutung: im Quelltext vorhandene Implementierungsteile

Folgerung:
Vorhandener Code ist nicht als funktionsfähig nachgewiesen.

### evd-024

Aussage:
toughworm/Openclaw-XMPP-Plugin: Die README nennt Senden und Empfangen von 1:1- und Gruppenchat-Nachrichten, OMEMO nur für 1:1 im älteren Namensraum `eu.siacs.conversations.axolotl`, verschlüsselten Gruppenchat als offen und keine OpenClaw-Version. Sie beschreibt außerdem Dateipfade unter `extensions/xmpp/`, Testskripte `test-omemo-*.ts` und die Installation mit `openclaw plugins install @openclaw/xmpp`.

Nachweisstatus:
`DOCUMENTED`

Begründung des Nachweisstatus:
Die Aussage beruht auf Projektdokumentation und deklarierten Paketangaben. Nach `rules/evidence.md` erhalten README-Angaben höchstens `DOCUMENTED`; eine praktische Prüfung liegt nicht vor.

Quellen:

| Quellenart | Fundstelle | Version oder Commit | Prüfdatum | Beitrag zum Befund |
|---|---|---|---|---|
| `PROJECT_DOCUMENTATION` | https://github.com/toughworm/Openclaw-XMPP-Plugin, `README.md` Zeilen 100–102, 133, 137, 214–215 | Commit 428886a5fab2 | 2026-09-14 | Funktionsangaben |
| `PROJECT_DOCUMENTATION` | https://github.com/toughworm/Openclaw-XMPP-Plugin, `README.md` Zeilen 13–24, 54, 190–196 | Commit 428886a5fab2 | 2026-09-14 | beschriebene Pfade, Testskripte und Installationsbefehl |
| `SOURCE_CODE` | https://github.com/toughworm/Openclaw-XMPP-Plugin, `package.json` | Commit 428886a5fab2 | 2026-09-14 | kein `peerDependencies`- und kein `engines`-Feld |

Prüfung:

Durchgeführt:
- README und Paketmetadaten gelesen

Ergebnis: wie in der Aussage

Nicht durchgeführt:
- nicht durchgeführt: Installation und Funktionstest in einer getrennten Arbeitsumgebung

Einschränkung der Aussagekraft: Projektangaben, nicht praktisch bestätigt

Bezug zur Projektidee:

- Fundstelle: idea.md, Abschnitt 1 (Direktnachrichten, OMEMO, MUC, GitHub-Projekte), Abschnitt 7
- Bedeutung: dokumentierte Funktionen und Versionsangaben eines vorhandenen Projekts

Folgerung:
Die dokumentierten Funktionen sind nicht praktisch geprüft.

### evd-025

Aussage:
toughworm/Openclaw-XMPP-Plugin: OMEMO-Code im Namensraum `eu.siacs.conversations.axolotl` ist vorhanden und wird bei `groupchat` übersprungen; die Zeichenkette `http://jabber.org/protocol/muc` für einen Raumbeitritt kommt in `src/` nicht vor.

Nachweisstatus:
`VERIFIED`

Begründung des Nachweisstatus:
Die Aussage beschränkt sich auf im gelesenen Quelltext vorhandene oder nicht gefundene Zeichenketten und Dateien. Das ist unmittelbar durch den Quelltext bestätigt. Über die Funktionsfähigkeit sagt die Aussage nichts.

Quellen:

| Quellenart | Fundstelle | Version oder Commit | Prüfdatum | Beitrag zum Befund |
|---|---|---|---|---|
| `SOURCE_CODE` | https://github.com/toughworm/Openclaw-XMPP-Plugin, `src/omemo/OmemoManager.ts` Zeile 11 | Commit 428886a5fab2 | 2026-09-14 | OMEMO-Namensraum |
| `SOURCE_CODE` | https://github.com/toughworm/Openclaw-XMPP-Plugin, `src/client.ts` Zeile 187 | Commit 428886a5fab2 | 2026-09-14 | Bedingung `options?.type !== "groupchat"` für OMEMO |
| `SOURCE_CODE` | https://github.com/toughworm/Openclaw-XMPP-Plugin, `src/` mit `grep -rn 'jabber.org/protocol/muc'` | Commit 428886a5fab2 | 2026-09-14 | 0 Treffer |

Prüfung:

Durchgeführt:
- Quelltext in einer getrennten Arbeitsumgebung per `git clone --depth 1` gelesen und nach Namensräumen und Bezeichnern durchsucht

Ergebnis: wie in der Aussage; Tests: `test/jid-normalization.test.ts`, `test/omemo-lookup.test.ts`

Nicht durchgeführt:
- nicht durchgeführt: Build, Ausführen der Tests und Funktionstest in einer getrennten Arbeitsumgebung

Einschränkung der Aussagekraft: belegt nur vorhandenen Code; 0 Treffer belegt nur das Fehlen der gesuchten Zeichenketten, nicht das Fehlen einer Funktion

Bezug zur Projektidee:

- Fundstelle: idea.md, Abschnitt 1, Abschnitt 7
- Bedeutung: im Quelltext vorhandene Implementierungsteile

Folgerung:
Vorhandener Code ist nicht als funktionsfähig nachgewiesen.

### evd-026

Aussage:
toughworm/Openclaw-XMPP-Plugin: Im untersuchten Repository-Stand liegen die Programmdateien unter `src/` und nicht unter `extensions/xmpp/`, die in evd-024 genannten Testskripte `test-omemo-*.ts` sind nicht vorhanden, und `@openclaw/xmpp` ist im npm-Register nicht veröffentlicht.

Nachweisstatus:
`VERIFIED`

Begründung des Nachweisstatus:
Dateiliste und npm-Register wurden unmittelbar geprüft. Die README-Angaben, mit denen verglichen wurde, stehen als dokumentierte Aussage in evd-024. Kein `CONFLICT`: Die README beschreibt einen Verzeichnisaufbau unter `extensions/xmpp/`, also einen anderen Geltungsbereich als dieses Repository, und `openclaw plugins install` kann laut Hilfe auch andere Quellen als npm verwenden. Ebenso ist das Fehlen eines Raumbeitritts im Code allein kein Konflikt mit der Gruppenchat-Angabe (siehe evd-024, evd-025).

Quellen:

| Quellenart | Fundstelle | Version oder Commit | Prüfdatum | Beitrag zum Befund |
|---|---|---|---|---|
| `SOURCE_CODE` | https://github.com/toughworm/Openclaw-XMPP-Plugin, `git ls-files` | Commit 428886a5fab2 | 2026-09-14 | tatsächlich vorhandene Dateien unter `src/` und `test/` |
| `PRIMARY_DOCUMENTATION` | https://registry.npmjs.org/@openclaw%2fxmpp | Registerstand 2026-09-14 | 2026-09-14 | HTTP 404 |
| `MANUAL_TEST` | `openclaw plugins install --help` auf srv001 | openclaw@2026.9.4 (3a9d69d) | 2026-09-14 | Hilfe nennt Pfad, Archiv, npm, git, `clawhub:` und Marketplace als Quellen |

Prüfung:

Durchgeführt:
- Dateiliste und npm-Register mit den README-Angaben aus evd-024 abgeglichen; Hilfe des Installationsbefehls gelesen

Ergebnis: wie in der Aussage

Nicht durchgeführt:
- nicht durchgeführt: Installation nach README in einer getrennten Arbeitsumgebung

Einschränkung der Aussagekraft: Die README beschreibt vermutlich einen anderen Aufbau; welchen, ist nicht geprüft

Bezug zur Projektidee:

- Fundstelle: idea.md, Abschnitt 1 („Vorhandene GitHub-Projekte“), Abschnitt 7
- Bedeutung: Belastbarkeit der Projektangaben

Folgerung:
Die README beschreibt nicht durchgehend den untersuchten Repository-Stand.

### evd-027

Aussage:
kazakhan/openclaw-xmpp: Die README nennt 1:1 und MUC; `XMPPAUDIT.md` führt OMEMO (XEP-0384) als „Not Supported“.

Nachweisstatus:
`DOCUMENTED`

Begründung des Nachweisstatus:
Die Aussage beruht auf Projektdokumentation und deklarierten Paketangaben. Nach `rules/evidence.md` erhalten README-Angaben höchstens `DOCUMENTED`; eine praktische Prüfung liegt nicht vor.

Quellen:

| Quellenart | Fundstelle | Version oder Commit | Prüfdatum | Beitrag zum Befund |
|---|---|---|---|---|
| `PROJECT_DOCUMENTATION` | https://github.com/kazakhan/openclaw-xmpp, `README.md` Zeilen 3, 94–97 | Commit 4fb1e113150e | 2026-09-14 | Funktionsangaben 1:1 und MUC |
| `PROJECT_DOCUMENTATION` | https://github.com/kazakhan/openclaw-xmpp, `XMPPAUDIT.md` Zeile 322 | Commit 4fb1e113150e | 2026-09-14 | OMEMO als nicht unterstützt |

Prüfung:

Durchgeführt:
- README und Paketmetadaten gelesen

Ergebnis: wie in der Aussage

Nicht durchgeführt:
- nicht durchgeführt: Installation und Funktionstest in einer getrennten Arbeitsumgebung

Einschränkung der Aussagekraft: Projektangaben, nicht praktisch bestätigt

Bezug zur Projektidee:

- Fundstelle: idea.md, Abschnitt 1 (Direktnachrichten, OMEMO, MUC, GitHub-Projekte), Abschnitt 7
- Bedeutung: dokumentierte Funktionen und Versionsangaben eines vorhandenen Projekts

Folgerung:
Die dokumentierten Funktionen sind nicht praktisch geprüft.

### evd-028

Aussage:
kazakhan/openclaw-xmpp: Code für MUC (`muc`-Namensraum, `joinRoom`) und 1:1 ist vorhanden; OMEMO-Zeichenketten kommen nicht vor.

Nachweisstatus:
`VERIFIED`

Begründung des Nachweisstatus:
Die Aussage beschränkt sich auf im gelesenen Quelltext vorhandene oder nicht gefundene Zeichenketten und Dateien. Das ist unmittelbar durch den Quelltext bestätigt. Über die Funktionsfähigkeit sagt die Aussage nichts.

Quellen:

| Quellenart | Fundstelle | Version oder Commit | Prüfdatum | Beitrag zum Befund |
|---|---|---|---|---|
| `SOURCE_CODE` | https://github.com/kazakhan/openclaw-xmpp, `src/startXMPP.ts` Zeilen 513, 761 | Commit 4fb1e113150e | 2026-09-14 | MUC-Namensräume |
| `SOURCE_CODE` | https://github.com/kazakhan/openclaw-xmpp, `index.ts` Zeile 35 | Commit 4fb1e113150e | 2026-09-14 | `xmpp.joinRoom` |
| `SOURCE_CODE` | https://github.com/kazakhan/openclaw-xmpp, `src/commands.ts` Zeile 231 | Commit 4fb1e113150e | 2026-09-14 | 1:1-Nachrichten |
| `SOURCE_CODE` | https://github.com/kazakhan/openclaw-xmpp, `src/`, `index.ts` mit `grep -rniE 'omemo\|axolotl'` | Commit 4fb1e113150e | 2026-09-14 | 0 Treffer |

Prüfung:

Durchgeführt:
- Quelltext in einer getrennten Arbeitsumgebung per `git clone --depth 1` gelesen und nach Namensräumen und Bezeichnern durchsucht

Ergebnis: wie in der Aussage; Tests: `tests/` mit 33 Dateien

Nicht durchgeführt:
- nicht durchgeführt: Build, Ausführen der Tests und Funktionstest in einer getrennten Arbeitsumgebung

Einschränkung der Aussagekraft: belegt nur vorhandenen Code; 0 Treffer belegt nur das Fehlen der gesuchten Zeichenketten, nicht das Fehlen einer Funktion

Bezug zur Projektidee:

- Fundstelle: idea.md, Abschnitt 1, Abschnitt 7
- Bedeutung: im Quelltext vorhandene Implementierungsteile

Folgerung:
Vorhandener Code ist nicht als funktionsfähig nachgewiesen.

### evd-029

Aussage:
kazakhan/openclaw-xmpp: Die README nennt „OpenClaw 2026.8.2+“ als Voraussetzung und begründet das mit den in 2026.8.x eingeführten Prüfungen „capability-consent“ und `contracts.tools`; `package.json` deklariert `compat.pluginApi ">=2026.6.1"` und `minGatewayVersion "2026.6.1"`.

Nachweisstatus:
`DOCUMENTED`

Begründung des Nachweisstatus:
Beide Angaben sind dokumentierte bzw. deklarierte Projektangaben ohne praktische Prüfung. Kein `CONFLICT`: Die Angaben haben unterschiedliche Bedeutung. Die README nennt eine Voraussetzung für bestimmte Prüfungen, `compat.pluginApi` ist laut OpenClaw-Dokumentation eine Untergrenze der Plugin-API (`docs/reference/RELEASING.md` Zeile 416). Unterschiedliche Versionsangaben mit möglicherweise unterschiedlicher Bedeutung reichen nach `rules/evidence.md` nicht für `CONFLICT`.

Quellen:

| Quellenart | Fundstelle | Version oder Commit | Prüfdatum | Beitrag zum Befund |
|---|---|---|---|---|
| `PROJECT_DOCUMENTATION` | https://github.com/kazakhan/openclaw-xmpp, `README.md` Zeilen 21–23 | Commit 4fb1e113150e | 2026-09-14 | Voraussetzung OpenClaw 2026.8.2+ mit Begründung |
| `SOURCE_CODE` | https://github.com/kazakhan/openclaw-xmpp, `package.json` Zeilen 20–24 | Commit 4fb1e113150e | 2026-09-14 | deklarierte Felder `compat.pluginApi` und `minGatewayVersion` |
| `PRIMARY_DOCUMENTATION` | `/usr/lib/node_modules/openclaw/docs/reference/RELEASING.md` Zeile 416 | openclaw@2026.9.4 (3a9d69d) | 2026-09-14 | Bedeutung von `openclaw.compat.pluginApi` als Untergrenze |

Prüfung:

Durchgeführt:
- Angaben gelesen und ihre Bedeutung verglichen

Ergebnis: wie in der Aussage

Nicht durchgeführt:
- nicht durchgeführt: Laden des Plugins unter 2026.6.1, 2026.7.1-2 und 2026.9.4 in einer getrennten Arbeitsumgebung

Einschränkung der Aussagekraft: Welche Version tatsächlich mindestens nötig ist, ist offen

Bezug zur Projektidee:

- Fundstelle: idea.md, Abschnitt 1, Abschnitt 10 („aktuelle OpenClaw-Versionen“)
- Bedeutung: dokumentierte Versionsangaben eines vorhandenen Projekts

Folgerung:
Das Projekt enthält zwei Versionsangaben mit unterschiedlichem Bezug.

### evd-030

Aussage:
icarito/openclaw-xmpp: Die Paketbeschreibung nennt 1:1-Chat, MUC-Räume und Ad-hoc-Befehle; die README sagt, der Produktivbetrieb lade einen separat abgeglichenen Verzeichnisbaum.

Nachweisstatus:
`DOCUMENTED`

Begründung des Nachweisstatus:
Die Aussage beruht auf Projektdokumentation und deklarierten Paketangaben. Nach `rules/evidence.md` erhalten README-Angaben höchstens `DOCUMENTED`; eine praktische Prüfung liegt nicht vor.

Quellen:

| Quellenart | Fundstelle | Version oder Commit | Prüfdatum | Beitrag zum Befund |
|---|---|---|---|---|
| `SOURCE_CODE` | https://github.com/icarito/openclaw-xmpp, `package.json` Zeile 80 | Commit 820213a98cb1 | 2026-09-14 | Paketbeschreibung |
| `PROJECT_DOCUMENTATION` | https://github.com/icarito/openclaw-xmpp, `README.md` Zeilen 9–11 | Commit 820213a98cb1 | 2026-09-14 | Hinweis zum Produktivbetrieb |

Prüfung:

Durchgeführt:
- README und Paketmetadaten gelesen

Ergebnis: wie in der Aussage

Nicht durchgeführt:
- nicht durchgeführt: Installation und Funktionstest in einer getrennten Arbeitsumgebung

Einschränkung der Aussagekraft: Projektangaben, nicht praktisch bestätigt

Bezug zur Projektidee:

- Fundstelle: idea.md, Abschnitt 1 (Direktnachrichten, OMEMO, MUC, GitHub-Projekte), Abschnitt 7
- Bedeutung: dokumentierte Funktionen und Versionsangaben eines vorhandenen Projekts

Folgerung:
Die dokumentierten Funktionen sind nicht praktisch geprüft.

### evd-031

Aussage:
icarito/openclaw-xmpp: Code für MUC, für OMEMO im älteren Namensraum und in `urn:xmpp:omemo:2` sowie ein Python-Hilfsprogramm `src/omemo/sidecar.py` sind vorhanden.

Nachweisstatus:
`VERIFIED`

Begründung des Nachweisstatus:
Die Aussage beschränkt sich auf im gelesenen Quelltext vorhandene oder nicht gefundene Zeichenketten und Dateien. Das ist unmittelbar durch den Quelltext bestätigt. Über die Funktionsfähigkeit sagt die Aussage nichts.

Quellen:

| Quellenart | Fundstelle | Version oder Commit | Prüfdatum | Beitrag zum Befund |
|---|---|---|---|---|
| `SOURCE_CODE` | https://github.com/icarito/openclaw-xmpp, `src/client.ts` Zeilen 121, 134 | Commit 820213a98cb1 | 2026-09-14 | MUC-Namensraum und Raumbeitritt |
| `SOURCE_CODE` | https://github.com/icarito/openclaw-xmpp, `src/omemo/types.ts` Zeile 13 | Commit 820213a98cb1 | 2026-09-14 | älterer OMEMO-Namensraum |
| `SOURCE_CODE` | https://github.com/icarito/openclaw-xmpp, `src/omemo/omemo2.ts` Zeile 12 | Commit 820213a98cb1 | 2026-09-14 | `urn:xmpp:omemo:2` |
| `SOURCE_CODE` | https://github.com/icarito/openclaw-xmpp, `src/omemo/sidecar.py` | Commit 820213a98cb1 | 2026-09-14 | Python-Hilfsprogramm |
| `SOURCE_CODE` | https://github.com/icarito/openclaw-xmpp, `src/send.ts` Zeile 356 | Commit 820213a98cb1 | 2026-09-14 | 1:1-Nachrichten |

Prüfung:

Durchgeführt:
- Quelltext in einer getrennten Arbeitsumgebung per `git clone --depth 1` gelesen und nach Namensräumen und Bezeichnern durchsucht

Ergebnis: wie in der Aussage; Tests: `src/tests/` mit 6 Dateien, u. a. `omemo.test.ts`

Nicht durchgeführt:
- nicht durchgeführt: Build, Ausführen der Tests und Funktionstest in einer getrennten Arbeitsumgebung

Einschränkung der Aussagekraft: belegt nur vorhandenen Code; 0 Treffer belegt nur das Fehlen der gesuchten Zeichenketten, nicht das Fehlen einer Funktion

Bezug zur Projektidee:

- Fundstelle: idea.md, Abschnitt 1, Abschnitt 7
- Bedeutung: im Quelltext vorhandene Implementierungsteile

Folgerung:
Vorhandener Code ist nicht als funktionsfähig nachgewiesen.

### evd-032

Aussage:
icarito/openclaw-xmpp: `AGENTS.md` beschreibt das Plugin „for OpenClaw 2026.6.9 or newer“; `package.json` deklariert `compat.pluginApi ">=2026.7.1"` und als Entwicklungsabhängigkeit `openclaw ^2026.7.1`.

Nachweisstatus:
`DOCUMENTED`

Begründung des Nachweisstatus:
Beide Angaben sind dokumentierte bzw. deklarierte Projektangaben ohne praktische Prüfung. Kein `CONFLICT`: `AGENTS.md` ist eine Arbeitsanleitung für Entwickler, `compat.pluginApi` eine maschinenlesbare Untergrenze der Plugin-API; ob beide denselben Geltungsbereich und denselben Bezugszeitpunkt haben, ist nicht belegt. Unterschiedliche Versionsangaben reichen nach `rules/evidence.md` allein nicht für `CONFLICT`.

Quellen:

| Quellenart | Fundstelle | Version oder Commit | Prüfdatum | Beitrag zum Befund |
|---|---|---|---|---|
| `PROJECT_DOCUMENTATION` | https://github.com/icarito/openclaw-xmpp, `AGENTS.md` Zeile 3 | Commit 820213a98cb1 | 2026-09-14 | Versionsangabe 2026.6.9 or newer |
| `SOURCE_CODE` | https://github.com/icarito/openclaw-xmpp, `package.json` Zeilen 85, 113 | Commit 820213a98cb1 | 2026-09-14 | deklarierte Felder `compat.pluginApi` und `devDependencies.openclaw` |

Prüfung:

Durchgeführt:
- Angaben gelesen und ihre Bedeutung verglichen

Ergebnis: wie in der Aussage

Nicht durchgeführt:
- nicht durchgeführt: Laden des Plugins unter 2026.6.9, 2026.7.1-2 und 2026.9.4 in einer getrennten Arbeitsumgebung
- nicht durchgeführt: Prüfung der Git-Historie von `AGENTS.md`

Einschränkung der Aussagekraft: Welche Version tatsächlich mindestens nötig ist, ist offen

Bezug zur Projektidee:

- Fundstelle: idea.md, Abschnitt 1, Abschnitt 10 („aktuelle OpenClaw-Versionen“)
- Bedeutung: dokumentierte Versionsangaben eines vorhandenen Projekts

Folgerung:
Das Projekt enthält zwei Versionsangaben mit unterschiedlichem Bezug.

### evd-033

Aussage:
soilDNRA/openclaw-xmpp: Die README beschreibt nur Direktchats, nennt MUC und OMEMO ausdrücklich als nicht unterstützt und OpenClaw 2026.8.2 als Mindestversion; sie verweist auf ClawHub `openclaw-xmpp@0.1.2-beta.2` und auf die Hauptquelle https://git.sdf.org/erici/openclaw-xmpp.

Nachweisstatus:
`DOCUMENTED`

Begründung des Nachweisstatus:
Die Aussage beruht auf Projektdokumentation und deklarierten Paketangaben. Nach `rules/evidence.md` erhalten README-Angaben höchstens `DOCUMENTED`; eine praktische Prüfung liegt nicht vor.

Quellen:

| Quellenart | Fundstelle | Version oder Commit | Prüfdatum | Beitrag zum Befund |
|---|---|---|---|---|
| `PROJECT_DOCUMENTATION` | https://github.com/soilDNRA/openclaw-xmpp, `README.md` Zeilen 1–2, 15–18, 44–46, 72 | Commit a41df5fc1417 | 2026-09-14 | Funktionsangaben, Mindestversion, ClawHub, Hauptquelle |
| `SOURCE_CODE` | https://github.com/soilDNRA/openclaw-xmpp, `package.json` Zeile 41 | Commit a41df5fc1417 | 2026-09-14 | `peerDependencies.openclaw >=2026.8.2` |

Prüfung:

Durchgeführt:
- README und Paketmetadaten gelesen

Ergebnis: wie in der Aussage

Nicht durchgeführt:
- nicht durchgeführt: Installation und Funktionstest in einer getrennten Arbeitsumgebung
- nicht durchgeführt: Prüfung des ClawHub-Eintrags

Einschränkung der Aussagekraft: Projektangaben, nicht praktisch bestätigt

Bezug zur Projektidee:

- Fundstelle: idea.md, Abschnitt 1 (Direktnachrichten, OMEMO, MUC, GitHub-Projekte), Abschnitt 7
- Bedeutung: dokumentierte Funktionen und Versionsangaben eines vorhandenen Projekts

Folgerung:
Die dokumentierten Funktionen sind nicht praktisch geprüft.

### evd-034

Aussage:
soilDNRA/openclaw-xmpp: Code für 1:1 ist vorhanden; OMEMO kommt in `src/` nicht vor; MUC kommt nur in einem Hinweistext vor, nach dem Gruppenchat-Optionen bis zum Abschluss einer „MUC security gate“ nicht verfügbar sind; die Hauptquelle auf git.sdf.org hat denselben Commit.

Nachweisstatus:
`VERIFIED`

Begründung des Nachweisstatus:
Die Aussage beschränkt sich auf im gelesenen Quelltext vorhandene oder nicht gefundene Zeichenketten und Dateien. Das ist unmittelbar durch den Quelltext bestätigt. Über die Funktionsfähigkeit sagt die Aussage nichts.

Quellen:

| Quellenart | Fundstelle | Version oder Commit | Prüfdatum | Beitrag zum Befund |
|---|---|---|---|---|
| `SOURCE_CODE` | https://github.com/soilDNRA/openclaw-xmpp, `src/stanzas.ts` Zeile 151 | Commit a41df5fc1417 | 2026-09-14 | 1:1-Nachrichten |
| `SOURCE_CODE` | https://github.com/soilDNRA/openclaw-xmpp, `src/setup.ts` Zeile 116 | Commit a41df5fc1417 | 2026-09-14 | Hinweistext „Group-chat options remain unavailable until the MUC security gate is complete.“ |
| `SOURCE_CODE` | https://github.com/soilDNRA/openclaw-xmpp, `src/` mit `grep -rniE 'muc\|omemo'` | Commit a41df5fc1417 | 2026-09-14 | 1 Treffer (`src/setup.ts` Zeile 116), 0 Treffer zu OMEMO |
| `SOURCE_CODE` | https://git.sdf.org/erici/openclaw-xmpp, Branch `main` über Gitea-API | Commit a41df5fc1417 | 2026-09-14 | gleicher Commit wie der GitHub-Spiegel |

Prüfung:

Durchgeführt:
- Quelltext in einer getrennten Arbeitsumgebung per `git clone --depth 1` gelesen und nach Namensräumen und Bezeichnern durchsucht

Ergebnis: wie in der Aussage; Tests: `test/` mit 12 Dateien, `.github/workflows/ci.yml`

Nicht durchgeführt:
- nicht durchgeführt: Build, Ausführen der Tests und Funktionstest in einer getrennten Arbeitsumgebung

Einschränkung der Aussagekraft: belegt nur vorhandenen Code; 0 Treffer belegt nur das Fehlen der gesuchten Zeichenketten, nicht das Fehlen einer Funktion

Bezug zur Projektidee:

- Fundstelle: idea.md, Abschnitt 1, Abschnitt 7
- Bedeutung: im Quelltext vorhandene Implementierungsteile

Folgerung:
Vorhandener Code ist nicht als funktionsfähig nachgewiesen.

### evd-035

Aussage:
elmafioso79/xmpp-channel: Die README nennt 1:1- und Gruppenchat sowie OMEMO einschließlich Gruppenchats im älteren Namensraum; `peerDependencies` verlangt `openclaw ^2026.2.2-3`. Ein offener Pull Request #4 betrifft die Anpassung an OpenClaw 2026.5.2.

Nachweisstatus:
`DOCUMENTED`

Begründung des Nachweisstatus:
Die Aussage beruht auf Projektdokumentation und deklarierten Paketangaben. Nach `rules/evidence.md` erhalten README-Angaben höchstens `DOCUMENTED`; eine praktische Prüfung liegt nicht vor.

Quellen:

| Quellenart | Fundstelle | Version oder Commit | Prüfdatum | Beitrag zum Befund |
|---|---|---|---|---|
| `PROJECT_DOCUMENTATION` | https://github.com/elmafioso79/xmpp-channel, `README.md` Zeilen 9–10, 211, 223 | Commit a447455d6cb1 | 2026-09-14 | Funktionsangaben einschließlich OMEMO in Gruppenchats |
| `SOURCE_CODE` | https://github.com/elmafioso79/xmpp-channel, `package.json` Zeile 63 | Commit a447455d6cb1 | 2026-09-14 | `peerDependencies.openclaw ^2026.2.2-3` |
| `ISSUE_OR_PR` | https://github.com/elmafioso79/xmpp-channel/pull/4 | – | 2026-09-14 | offener PR „update openclaw plugin json to fit OpenClaw 2026.5.2“ vom 2026-05-03 |

Prüfung:

Durchgeführt:
- README und Paketmetadaten gelesen

Ergebnis: wie in der Aussage

Nicht durchgeführt:
- nicht durchgeführt: Installation und Funktionstest in einer getrennten Arbeitsumgebung

Einschränkung der Aussagekraft: Projektangaben, nicht praktisch bestätigt

Bezug zur Projektidee:

- Fundstelle: idea.md, Abschnitt 1 (Direktnachrichten, OMEMO, MUC, GitHub-Projekte), Abschnitt 7
- Bedeutung: dokumentierte Funktionen und Versionsangaben eines vorhandenen Projekts

Folgerung:
Die dokumentierten Funktionen sind nicht praktisch geprüft.

### evd-036

Aussage:
elmafioso79/xmpp-channel: Code für MUC (`joinMuc`) und für OMEMO bei `groupchat` ist vorhanden; keine Testdateien.

Nachweisstatus:
`VERIFIED`

Begründung des Nachweisstatus:
Die Aussage beschränkt sich auf im gelesenen Quelltext vorhandene oder nicht gefundene Zeichenketten und Dateien. Das ist unmittelbar durch den Quelltext bestätigt. Über die Funktionsfähigkeit sagt die Aussage nichts.

Quellen:

| Quellenart | Fundstelle | Version oder Commit | Prüfdatum | Beitrag zum Befund |
|---|---|---|---|---|
| `SOURCE_CODE` | https://github.com/elmafioso79/xmpp-channel, `src/monitor.ts` Zeile 255 | Commit a447455d6cb1 | 2026-09-14 | `joinMuc` |
| `SOURCE_CODE` | https://github.com/elmafioso79/xmpp-channel, `src/omemo/types.ts` Zeilen 13, 26 | Commit a447455d6cb1 | 2026-09-14 | OMEMO-Namensräume |
| `SOURCE_CODE` | https://github.com/elmafioso79/xmpp-channel, `src/inbound.ts` Zeilen 359, 386 | Commit a447455d6cb1 | 2026-09-14 | 1:1-Nachrichten und verschlüsselte Gruppenchat-Nachrichten |

Prüfung:

Durchgeführt:
- Quelltext in einer getrennten Arbeitsumgebung per `git clone --depth 1` gelesen und nach Namensräumen und Bezeichnern durchsucht

Ergebnis: wie in der Aussage; Tests: keine

Nicht durchgeführt:
- nicht durchgeführt: Build, Ausführen der Tests und Funktionstest in einer getrennten Arbeitsumgebung

Einschränkung der Aussagekraft: belegt nur vorhandenen Code; 0 Treffer belegt nur das Fehlen der gesuchten Zeichenketten, nicht das Fehlen einer Funktion

Bezug zur Projektidee:

- Fundstelle: idea.md, Abschnitt 1, Abschnitt 7
- Bedeutung: im Quelltext vorhandene Implementierungsteile

Folgerung:
Vorhandener Code ist nicht als funktionsfähig nachgewiesen.

### evd-037

Aussage:
watkins-matt/xmpp-channel: Fork von elmafioso79/xmpp-channel, 28 Commits voraus; die README ist identisch mit dem Ursprung; `peerDependencies` verlangt `openclaw >=2026.8.2`.

Nachweisstatus:
`DOCUMENTED`

Begründung des Nachweisstatus:
Die Aussage beruht auf Projektdokumentation und deklarierten Paketangaben. Nach `rules/evidence.md` erhalten README-Angaben höchstens `DOCUMENTED`; eine praktische Prüfung liegt nicht vor.

Quellen:

| Quellenart | Fundstelle | Version oder Commit | Prüfdatum | Beitrag zum Befund |
|---|---|---|---|---|
| `PROJECT_DOCUMENTATION` | https://github.com/watkins-matt/xmpp-channel, `README.md` | Commit 1a734552fe19 | 2026-09-14 | identisch mit elmafioso79/xmpp-channel (per `diff` verglichen) |
| `SOURCE_CODE` | https://github.com/watkins-matt/xmpp-channel, `package.json` Zeilen 64–65 | Commit 1a734552fe19 | 2026-09-14 | `peerDependencies.openclaw >=2026.8.2` |
| `SOURCE_CODE` | GitHub-API `repos/watkins-matt/xmpp-channel` (Fork-Vergleich) | Commit 1a734552fe19 | 2026-09-14 | 28 Commits Vorsprung vor dem Ursprung |

Prüfung:

Durchgeführt:
- README und Paketmetadaten gelesen

Ergebnis: wie in der Aussage

Nicht durchgeführt:
- nicht durchgeführt: Installation und Funktionstest in einer getrennten Arbeitsumgebung

Einschränkung der Aussagekraft: Projektangaben, nicht praktisch bestätigt

Bezug zur Projektidee:

- Fundstelle: idea.md, Abschnitt 1 (Direktnachrichten, OMEMO, MUC, GitHub-Projekte), Abschnitt 7
- Bedeutung: dokumentierte Funktionen und Versionsangaben eines vorhandenen Projekts

Folgerung:
Die dokumentierten Funktionen sind nicht praktisch geprüft.

### evd-038

Aussage:
watkins-matt/xmpp-channel: Code für MUC und OMEMO ist vorhanden.

Nachweisstatus:
`VERIFIED`

Begründung des Nachweisstatus:
Die Aussage beschränkt sich auf im gelesenen Quelltext vorhandene oder nicht gefundene Zeichenketten und Dateien. Das ist unmittelbar durch den Quelltext bestätigt. Über die Funktionsfähigkeit sagt die Aussage nichts.

Quellen:

| Quellenart | Fundstelle | Version oder Commit | Prüfdatum | Beitrag zum Befund |
|---|---|---|---|---|
| `SOURCE_CODE` | https://github.com/watkins-matt/xmpp-channel, `src/monitor.ts` Zeile 292 | Commit 1a734552fe19 | 2026-09-14 | MUC |
| `SOURCE_CODE` | https://github.com/watkins-matt/xmpp-channel, `src/omemo/types.ts` Zeilen 13, 26 | Commit 1a734552fe19 | 2026-09-14 | OMEMO-Namensräume |
| `SOURCE_CODE` | https://github.com/watkins-matt/xmpp-channel, `src/inbound.ts` Zeile 495 | Commit 1a734552fe19 | 2026-09-14 | OMEMO-Verarbeitung |

Prüfung:

Durchgeführt:
- Quelltext in einer getrennten Arbeitsumgebung per `git clone --depth 1` gelesen und nach Namensräumen und Bezeichnern durchsucht

Ergebnis: wie in der Aussage; Tests: `src/payload-filter.test.ts`, `src/sdk-contract.test.ts`

Nicht durchgeführt:
- nicht durchgeführt: Build, Ausführen der Tests und Funktionstest in einer getrennten Arbeitsumgebung

Einschränkung der Aussagekraft: belegt nur vorhandenen Code; 0 Treffer belegt nur das Fehlen der gesuchten Zeichenketten, nicht das Fehlen einer Funktion

Bezug zur Projektidee:

- Fundstelle: idea.md, Abschnitt 1, Abschnitt 7
- Bedeutung: im Quelltext vorhandene Implementierungsteile

Folgerung:
Vorhandener Code ist nicht als funktionsfähig nachgewiesen.

### evd-039

Aussage:
Programmatore-Web/openclaw-xmpp-channel: Fork von watkins-matt/xmpp-channel; die README nennt 1:1 und fest eingestellte MUC-Räume, schließt Ende-zu-Ende-Verschlüsselung aus und nennt OpenClaw 2026.8.2 oder neuer.

Nachweisstatus:
`DOCUMENTED`

Begründung des Nachweisstatus:
Die Aussage beruht auf Projektdokumentation und deklarierten Paketangaben. Nach `rules/evidence.md` erhalten README-Angaben höchstens `DOCUMENTED`; eine praktische Prüfung liegt nicht vor.

Quellen:

| Quellenart | Fundstelle | Version oder Commit | Prüfdatum | Beitrag zum Befund |
|---|---|---|---|---|
| `PROJECT_DOCUMENTATION` | https://github.com/Programmatore-Web/openclaw-xmpp-channel, `README.md` Zeilen 8, 18–19, 32 | Commit 0ba189314a14 | 2026-09-14 | Funktionsangaben und Versionsangabe |
| `SOURCE_CODE` | https://github.com/Programmatore-Web/openclaw-xmpp-channel, `package.json` Zeilen 63–64 | Commit 0ba189314a14 | 2026-09-14 | `peerDependencies.openclaw ^2026.8.2` |

Prüfung:

Durchgeführt:
- README und Paketmetadaten gelesen

Ergebnis: wie in der Aussage

Nicht durchgeführt:
- nicht durchgeführt: Installation und Funktionstest in einer getrennten Arbeitsumgebung

Einschränkung der Aussagekraft: Projektangaben, nicht praktisch bestätigt

Bezug zur Projektidee:

- Fundstelle: idea.md, Abschnitt 1 (Direktnachrichten, OMEMO, MUC, GitHub-Projekte), Abschnitt 7
- Bedeutung: dokumentierte Funktionen und Versionsangaben eines vorhandenen Projekts

Folgerung:
Die dokumentierten Funktionen sind nicht praktisch geprüft.

### evd-040

Aussage:
Programmatore-Web/openclaw-xmpp-channel: Code für MUC ist vorhanden; OMEMO-Zeichenketten kommen nicht vor; verschlüsselte Nachrichten werden verworfen.

Nachweisstatus:
`VERIFIED`

Begründung des Nachweisstatus:
Die Aussage beschränkt sich auf im gelesenen Quelltext vorhandene oder nicht gefundene Zeichenketten und Dateien. Das ist unmittelbar durch den Quelltext bestätigt. Über die Funktionsfähigkeit sagt die Aussage nichts.

Quellen:

| Quellenart | Fundstelle | Version oder Commit | Prüfdatum | Beitrag zum Befund |
|---|---|---|---|---|
| `SOURCE_CODE` | https://github.com/Programmatore-Web/openclaw-xmpp-channel, `src/monitor.ts` Zeile 772 | Commit 0ba189314a14 | 2026-09-14 | `joinMuc` |
| `SOURCE_CODE` | https://github.com/Programmatore-Web/openclaw-xmpp-channel, `src/monitor.ts` Zeilen 988–1105 | Commit 0ba189314a14 | 2026-09-14 | Behandlung verschlüsselter Nachrichten |
| `SOURCE_CODE` | https://github.com/Programmatore-Web/openclaw-xmpp-channel, `src/muc-identity.ts` | Commit 0ba189314a14 | 2026-09-14 | MUC-Identität |
| `SOURCE_CODE` | https://github.com/Programmatore-Web/openclaw-xmpp-channel, `src/` mit `grep -rniE 'omemo'` | Commit 0ba189314a14 | 2026-09-14 | 0 Treffer |

Prüfung:

Durchgeführt:
- Quelltext in einer getrennten Arbeitsumgebung per `git clone --depth 1` gelesen und nach Namensräumen und Bezeichnern durchsucht

Ergebnis: wie in der Aussage; Tests: `test/` mit 33 Dateien

Nicht durchgeführt:
- nicht durchgeführt: Build, Ausführen der Tests und Funktionstest in einer getrennten Arbeitsumgebung

Einschränkung der Aussagekraft: belegt nur vorhandenen Code; 0 Treffer belegt nur das Fehlen der gesuchten Zeichenketten, nicht das Fehlen einer Funktion

Bezug zur Projektidee:

- Fundstelle: idea.md, Abschnitt 1, Abschnitt 7
- Bedeutung: im Quelltext vorhandene Implementierungsteile

Folgerung:
Vorhandener Code ist nicht als funktionsfähig nachgewiesen.

### evd-041

Aussage:
Programmatore-Web/openclaw-xmpp-channel: Das CHANGELOG beschreibt OMEMO-Funktionen in den Versionen 0.3.x vom Februar 2026 und führt unter „[Unreleased]“ die Entfernung der Ende-zu-Ende-Verschlüsselung auf; die README des untersuchten Stands schließt Ende-zu-Ende-Verschlüsselung aus.

Nachweisstatus:
`DOCUMENTED`

Begründung des Nachweisstatus:
Die Aussage beruht auf CHANGELOG und README ohne praktische Prüfung. Kein `CONFLICT`: Die OMEMO-Einträge betreffen frühere Versionen, die README den aktuellen Stand; das CHANGELOG dokumentiert die Entfernung selbst. Eine historische Aussage und ein abweichender aktueller Stand reichen nach `rules/evidence.md` nicht für `CONFLICT`.

Quellen:

| Quellenart | Fundstelle | Version oder Commit | Prüfdatum | Beitrag zum Befund |
|---|---|---|---|---|
| `PROJECT_DOCUMENTATION` | https://github.com/Programmatore-Web/openclaw-xmpp-channel, `CHANGELOG.md` Zeilen 22–24 („### Removed“ unter „[Unreleased]“) | Commit 0ba189314a14 | 2026-09-14 | dokumentierte Entfernung der Ende-zu-Ende-Verschlüsselung |
| `PROJECT_DOCUMENTATION` | https://github.com/Programmatore-Web/openclaw-xmpp-channel, `CHANGELOG.md` Zeilen 35–107 (Versionen 0.3.1 bis 0.4.0, 2026-02-08 bis 2026-02-12) | Commit 0ba189314a14 | 2026-09-14 | frühere OMEMO-Einträge |
| `PROJECT_DOCUMENTATION` | https://github.com/Programmatore-Web/openclaw-xmpp-channel, `README.md` Zeilen 18–19 | Commit 0ba189314a14 | 2026-09-14 | aktueller Ausschluss der Ende-zu-Ende-Verschlüsselung |

Prüfung:

Durchgeführt:
- CHANGELOG-Abschnitte nach Version und Datum mit README verglichen

Ergebnis: wie in der Aussage

Nicht durchgeführt:
- nicht erforderlich: weitere Prüfung zur zeitlichen Einordnung

Einschränkung der Aussagekraft: Dokumentationsaussage

Bezug zur Projektidee:

- Fundstelle: idea.md, Abschnitt 1 (OMEMO), Abschnitt 7
- Bedeutung: dokumentierte Entwicklung eines vorhandenen Projekts

Folgerung:
Das Projekt hatte laut CHANGELOG OMEMO-Funktionen und hat sie laut eigener Dokumentation entfernt.

### evd-042

Aussage:
MrCPA/oc-xmpp: Die README nennt Direktnachrichten und Räume, OMEMO nur für Direktnachrichten und Live-Tests als noch offen; `peerDependencies` verlangt `openclaw "*"`.

Nachweisstatus:
`DOCUMENTED`

Begründung des Nachweisstatus:
Die Aussage beruht auf Projektdokumentation und deklarierten Paketangaben. Nach `rules/evidence.md` erhalten README-Angaben höchstens `DOCUMENTED`; eine praktische Prüfung liegt nicht vor.

Quellen:

| Quellenart | Fundstelle | Version oder Commit | Prüfdatum | Beitrag zum Befund |
|---|---|---|---|---|
| `PROJECT_DOCUMENTATION` | https://github.com/MrCPA/oc-xmpp, `README.md` Zeilen 5, 9, 30 | Commit 675775a49f43 | 2026-09-14 | Funktionsangaben und Teststand |
| `SOURCE_CODE` | https://github.com/MrCPA/oc-xmpp, `package.json` Zeilen 45–46 | Commit 675775a49f43 | 2026-09-14 | `peerDependencies.openclaw "*"` |

Prüfung:

Durchgeführt:
- README und Paketmetadaten gelesen

Ergebnis: wie in der Aussage

Nicht durchgeführt:
- nicht durchgeführt: Installation und Funktionstest in einer getrennten Arbeitsumgebung
- nicht durchgeführt: Prüfung der Beschränkung von OMEMO auf Direktnachrichten im Code

Einschränkung der Aussagekraft: Projektangaben, nicht praktisch bestätigt

Bezug zur Projektidee:

- Fundstelle: idea.md, Abschnitt 1 (Direktnachrichten, OMEMO, MUC, GitHub-Projekte), Abschnitt 7
- Bedeutung: dokumentierte Funktionen und Versionsangaben eines vorhandenen Projekts

Folgerung:
Die dokumentierten Funktionen sind nicht praktisch geprüft.

### evd-043

Aussage:
MrCPA/oc-xmpp: Code für MUC und für OMEMO in `urn:xmpp:omemo:2` ist vorhanden.

Nachweisstatus:
`VERIFIED`

Begründung des Nachweisstatus:
Die Aussage beschränkt sich auf im gelesenen Quelltext vorhandene oder nicht gefundene Zeichenketten und Dateien. Das ist unmittelbar durch den Quelltext bestätigt. Über die Funktionsfähigkeit sagt die Aussage nichts.

Quellen:

| Quellenart | Fundstelle | Version oder Commit | Prüfdatum | Beitrag zum Befund |
|---|---|---|---|---|
| `SOURCE_CODE` | https://github.com/MrCPA/oc-xmpp, `src/inbound.ts` Zeilen 76, 102, 461 | Commit 675775a49f43 | 2026-09-14 | MUC und 1:1-Nachrichten |
| `SOURCE_CODE` | https://github.com/MrCPA/oc-xmpp, `src/omemo.ts` Zeilen 17, 207 | Commit 675775a49f43 | 2026-09-14 | libsignal-Import und `urn:xmpp:omemo:2` |

Prüfung:

Durchgeführt:
- Quelltext in einer getrennten Arbeitsumgebung per `git clone --depth 1` gelesen und nach Namensräumen und Bezeichnern durchsucht

Ergebnis: wie in der Aussage; Tests: `tests/` mit 6 Dateien, u. a. `omemo-wire.test.ts`

Nicht durchgeführt:
- nicht durchgeführt: Build, Ausführen der Tests und Funktionstest in einer getrennten Arbeitsumgebung

Einschränkung der Aussagekraft: belegt nur vorhandenen Code; 0 Treffer belegt nur das Fehlen der gesuchten Zeichenketten, nicht das Fehlen einer Funktion

Bezug zur Projektidee:

- Fundstelle: idea.md, Abschnitt 1, Abschnitt 7
- Bedeutung: im Quelltext vorhandene Implementierungsteile

Folgerung:
Vorhandener Code ist nicht als funktionsfähig nachgewiesen.

### evd-044

Aussage:
chitozzz/xmpp-adapter-openclaw: Die README nennt 1:1 und MUC als Ziel und das Projekt als in Planung; `peerDependencies` verlangt `openclaw >=2026.6.9`; OMEMO wird nicht genannt.

Nachweisstatus:
`DOCUMENTED`

Begründung des Nachweisstatus:
Die Aussage beruht auf Projektdokumentation und deklarierten Paketangaben. Nach `rules/evidence.md` erhalten README-Angaben höchstens `DOCUMENTED`; eine praktische Prüfung liegt nicht vor.

Quellen:

| Quellenart | Fundstelle | Version oder Commit | Prüfdatum | Beitrag zum Befund |
|---|---|---|---|---|
| `PROJECT_DOCUMENTATION` | https://github.com/chitozzz/xmpp-adapter-openclaw, `README.md` Zeilen 9–12, 21–24 | Commit f280515acd43 | 2026-09-14 | Ziele und Planungsstand |
| `SOURCE_CODE` | https://github.com/chitozzz/xmpp-adapter-openclaw, `package.json` Zeilen 37–38 | Commit f280515acd43 | 2026-09-14 | `peerDependencies.openclaw >=2026.6.9` |

Prüfung:

Durchgeführt:
- README und Paketmetadaten gelesen

Ergebnis: wie in der Aussage

Nicht durchgeführt:
- nicht durchgeführt: Installation und Funktionstest in einer getrennten Arbeitsumgebung

Einschränkung der Aussagekraft: Projektangaben, nicht praktisch bestätigt

Bezug zur Projektidee:

- Fundstelle: idea.md, Abschnitt 1 (Direktnachrichten, OMEMO, MUC, GitHub-Projekte), Abschnitt 7
- Bedeutung: dokumentierte Funktionen und Versionsangaben eines vorhandenen Projekts

Folgerung:
Die dokumentierten Funktionen sind nicht praktisch geprüft.

### evd-045

Aussage:
chitozzz/xmpp-adapter-openclaw: Code für 1:1 und MUC (`joinMuc`) ist vorhanden; OMEMO-Zeichenketten kommen nicht vor.

Nachweisstatus:
`VERIFIED`

Begründung des Nachweisstatus:
Die Aussage beschränkt sich auf im gelesenen Quelltext vorhandene oder nicht gefundene Zeichenketten und Dateien. Das ist unmittelbar durch den Quelltext bestätigt. Über die Funktionsfähigkeit sagt die Aussage nichts.

Quellen:

| Quellenart | Fundstelle | Version oder Commit | Prüfdatum | Beitrag zum Befund |
|---|---|---|---|---|
| `SOURCE_CODE` | https://github.com/chitozzz/xmpp-adapter-openclaw, `src/xmpp-client.ts` Zeile 306 | Commit f280515acd43 | 2026-09-14 | 1:1-Nachrichten |
| `SOURCE_CODE` | https://github.com/chitozzz/xmpp-adapter-openclaw, `src/xmpp-client.ts` Zeilen 524–530 | Commit f280515acd43 | 2026-09-14 | `joinMuc` |
| `SOURCE_CODE` | https://github.com/chitozzz/xmpp-adapter-openclaw, `src/` mit `grep -rni 'omemo'` | Commit f280515acd43 | 2026-09-14 | 0 Treffer |

Prüfung:

Durchgeführt:
- Quelltext in einer getrennten Arbeitsumgebung per `git clone --depth 1` gelesen und nach Namensräumen und Bezeichnern durchsucht

Ergebnis: wie in der Aussage; Tests: `test/smoke.js`

Nicht durchgeführt:
- nicht durchgeführt: Build, Ausführen der Tests und Funktionstest in einer getrennten Arbeitsumgebung

Einschränkung der Aussagekraft: belegt nur vorhandenen Code; 0 Treffer belegt nur das Fehlen der gesuchten Zeichenketten, nicht das Fehlen einer Funktion

Bezug zur Projektidee:

- Fundstelle: idea.md, Abschnitt 1, Abschnitt 7
- Bedeutung: im Quelltext vorhandene Implementierungsteile

Folgerung:
Vorhandener Code ist nicht als funktionsfähig nachgewiesen.

### evd-046

Aussage:
weijia/xmpp-connector: Die README nennt Senden und Empfangen von Nachrichten, keine OpenClaw-Version, weder MUC noch OMEMO; auf npm ist `openclaw-xmpp-connector` 0.3.0 veröffentlicht.

Nachweisstatus:
`DOCUMENTED`

Begründung des Nachweisstatus:
Die Aussage beruht auf Projektdokumentation und deklarierten Paketangaben. Nach `rules/evidence.md` erhalten README-Angaben höchstens `DOCUMENTED`; eine praktische Prüfung liegt nicht vor.

Quellen:

| Quellenart | Fundstelle | Version oder Commit | Prüfdatum | Beitrag zum Befund |
|---|---|---|---|---|
| `PROJECT_DOCUMENTATION` | https://github.com/weijia/xmpp-connector, `README.md` Zeilen 7–8, 52 | Commit 3d7c72e66cd9 | 2026-09-14 | Funktionsangaben und Laufzeitangabe |
| `PRIMARY_DOCUMENTATION` | https://registry.npmjs.org/openclaw-xmpp-connector | Registerstand 2026-09-14 | 2026-09-14 | veröffentlichte Version 0.3.0 vom 2026-03-28 |

Prüfung:

Durchgeführt:
- README und Paketmetadaten gelesen

Ergebnis: wie in der Aussage

Nicht durchgeführt:
- nicht durchgeführt: Installation und Funktionstest in einer getrennten Arbeitsumgebung

Einschränkung der Aussagekraft: Projektangaben, nicht praktisch bestätigt

Bezug zur Projektidee:

- Fundstelle: idea.md, Abschnitt 1 (Direktnachrichten, OMEMO, MUC, GitHub-Projekte), Abschnitt 7
- Bedeutung: dokumentierte Funktionen und Versionsangaben eines vorhandenen Projekts

Folgerung:
Die dokumentierten Funktionen sind nicht praktisch geprüft.

### evd-047

Aussage:
weijia/xmpp-connector: Code für 1:1 ist vorhanden; MUC- und OMEMO-Zeichenketten kommen nicht vor; keine Testdateien.

Nachweisstatus:
`VERIFIED`

Begründung des Nachweisstatus:
Die Aussage beschränkt sich auf im gelesenen Quelltext vorhandene oder nicht gefundene Zeichenketten und Dateien. Das ist unmittelbar durch den Quelltext bestätigt. Über die Funktionsfähigkeit sagt die Aussage nichts.

Quellen:

| Quellenart | Fundstelle | Version oder Commit | Prüfdatum | Beitrag zum Befund |
|---|---|---|---|---|
| `SOURCE_CODE` | https://github.com/weijia/xmpp-connector, `plugin.ts` Zeile 507 | Commit 3d7c72e66cd9 | 2026-09-14 | 1:1-Nachrichten |
| `SOURCE_CODE` | https://github.com/weijia/xmpp-connector, `plugin.ts` mit `grep -niE 'muc\|omemo'` | Commit 3d7c72e66cd9 | 2026-09-14 | 0 Treffer |

Prüfung:

Durchgeführt:
- Quelltext in einer getrennten Arbeitsumgebung per `git clone --depth 1` gelesen und nach Namensräumen und Bezeichnern durchsucht

Ergebnis: wie in der Aussage; Tests: keine

Nicht durchgeführt:
- nicht durchgeführt: Build, Ausführen der Tests und Funktionstest in einer getrennten Arbeitsumgebung

Einschränkung der Aussagekraft: belegt nur vorhandenen Code; 0 Treffer belegt nur das Fehlen der gesuchten Zeichenketten, nicht das Fehlen einer Funktion

Bezug zur Projektidee:

- Fundstelle: idea.md, Abschnitt 1, Abschnitt 7
- Bedeutung: im Quelltext vorhandene Implementierungsteile

Folgerung:
Vorhandener Code ist nicht als funktionsfähig nachgewiesen.

### evd-048

Aussage:
processone/openclaw, Zweig xmpp-support: Die README der Erweiterung nennt 1:1 und MUC; OMEMO wird nicht genannt; der Zweig ist Grundlage des geschlossenen PR #9741 und hängt von `openclaw workspace:*` ab.

Nachweisstatus:
`DOCUMENTED`

Begründung des Nachweisstatus:
Die Aussage beruht auf Projektdokumentation und deklarierten Paketangaben. Nach `rules/evidence.md` erhalten README-Angaben höchstens `DOCUMENTED`; eine praktische Prüfung liegt nicht vor.

Quellen:

| Quellenart | Fundstelle | Version oder Commit | Prüfdatum | Beitrag zum Befund |
|---|---|---|---|---|
| `PROJECT_DOCUMENTATION` | https://github.com/processone/openclaw/tree/xmpp-support/extensions/xmpp, `extensions/xmpp/README.md` Zeilen 10–11 | Commit a6adb95b35c1 | 2026-09-14 | Funktionsangaben |
| `SOURCE_CODE` | https://github.com/processone/openclaw/tree/xmpp-support/extensions/xmpp, `extensions/xmpp/package.json` | Commit a6adb95b35c1 | 2026-09-14 | `devDependencies.openclaw workspace:*` |
| `ISSUE_OR_PR` | https://github.com/openclaw/openclaw/pull/9741 | Kopf-Commit 8a4bc43 | 2026-09-14 | Bezug des Zweigs zum geschlossenen PR |

Prüfung:

Durchgeführt:
- README und Paketmetadaten gelesen

Ergebnis: wie in der Aussage

Nicht durchgeführt:
- nicht durchgeführt: Installation und Funktionstest in einer getrennten Arbeitsumgebung

Einschränkung der Aussagekraft: Projektangaben, nicht praktisch bestätigt; Dateien über die GitHub-API geladen, nicht geklont

Bezug zur Projektidee:

- Fundstelle: idea.md, Abschnitt 1 (Direktnachrichten, OMEMO, MUC, GitHub-Projekte), Abschnitt 7
- Bedeutung: dokumentierte Funktionen und Versionsangaben eines vorhandenen Projekts

Folgerung:
Die dokumentierten Funktionen sind nicht praktisch geprüft.

### evd-049

Aussage:
processone/openclaw, Zweig xmpp-support: Code für 1:1 und MUC (`joinRoom`) ist vorhanden; OMEMO-Zeichenketten kommen nicht vor.

Nachweisstatus:
`VERIFIED`

Begründung des Nachweisstatus:
Die Aussage beschränkt sich auf im gelesenen Quelltext vorhandene oder nicht gefundene Zeichenketten und Dateien. Das ist unmittelbar durch den Quelltext bestätigt. Über die Funktionsfähigkeit sagt die Aussage nichts.

Quellen:

| Quellenart | Fundstelle | Version oder Commit | Prüfdatum | Beitrag zum Befund |
|---|---|---|---|---|
| `SOURCE_CODE` | https://github.com/processone/openclaw/tree/xmpp-support/extensions/xmpp, `extensions/xmpp/src/channel.ts` Zeilen 150, 290 | Commit a6adb95b35c1 | 2026-09-14 | `joinRoom` |
| `SOURCE_CODE` | https://github.com/processone/openclaw/tree/xmpp-support/extensions/xmpp, `extensions/xmpp/src/client.ts` Zeile 353 | Commit a6adb95b35c1 | 2026-09-14 | 1:1-Nachrichten |
| `SOURCE_CODE` | https://github.com/processone/openclaw/tree/xmpp-support/extensions/xmpp, `extensions/xmpp/src/` mit Suche nach `omemo` | Commit a6adb95b35c1 | 2026-09-14 | 0 Treffer |

Prüfung:

Durchgeführt:
- Quelltext in einer getrennten Arbeitsumgebung per `git clone --depth 1` gelesen und nach Namensräumen und Bezeichnern durchsucht

Ergebnis: wie in der Aussage; Tests: `src/client.test.ts`, `src/actions.test.ts`

Nicht durchgeführt:
- nicht durchgeführt: Build, Ausführen der Tests und Funktionstest in einer getrennten Arbeitsumgebung

Einschränkung der Aussagekraft: belegt nur vorhandenen Code; 0 Treffer belegt nur das Fehlen der gesuchten Zeichenketten, nicht das Fehlen einer Funktion

Bezug zur Projektidee:

- Fundstelle: idea.md, Abschnitt 1, Abschnitt 7
- Bedeutung: im Quelltext vorhandene Implementierungsteile

Folgerung:
Vorhandener Code ist nicht als funktionsfähig nachgewiesen.

### evd-050

Aussage:
rsaisankalp/clawdbotElyments: Die README beschreibt eine Anbindung von Clawdbot an die XMPP-basierte Plattform Elyments mit Direktnachrichten; `peerDependencies` verlangt `clawdbot >=2026.0.0`; auf npm ist `clawdbot-elyments` 1.0.0 veröffentlicht.

Nachweisstatus:
`DOCUMENTED`

Begründung des Nachweisstatus:
Die Aussage beruht auf Projektdokumentation und deklarierten Paketangaben. Nach `rules/evidence.md` erhalten README-Angaben höchstens `DOCUMENTED`; eine praktische Prüfung liegt nicht vor.

Quellen:

| Quellenart | Fundstelle | Version oder Commit | Prüfdatum | Beitrag zum Befund |
|---|---|---|---|---|
| `PROJECT_DOCUMENTATION` | https://github.com/rsaisankalp/clawdbotElyments, `README.md` Zeilen 79–96 | Commit f2e1dde49780 | 2026-09-14 | Funktionsangaben |
| `SOURCE_CODE` | https://github.com/rsaisankalp/clawdbotElyments, `package.json` | Commit f2e1dde49780 | 2026-09-14 | `peerDependencies.clawdbot >=2026.0.0` |
| `PRIMARY_DOCUMENTATION` | https://registry.npmjs.org/clawdbot-elyments | Registerstand 2026-09-14 | 2026-09-14 | veröffentlichte Version 1.0.0 vom 2026-01-17 |

Prüfung:

Durchgeführt:
- README und Paketmetadaten gelesen

Ergebnis: wie in der Aussage

Nicht durchgeführt:
- nicht durchgeführt: Installation und Funktionstest in einer getrennten Arbeitsumgebung

Einschränkung der Aussagekraft: Projektangaben, nicht praktisch bestätigt

Bezug zur Projektidee:

- Fundstelle: idea.md, Abschnitt 1 (Direktnachrichten, OMEMO, MUC, GitHub-Projekte), Abschnitt 7
- Bedeutung: dokumentierte Funktionen und Versionsangaben eines vorhandenen Projekts

Folgerung:
Die dokumentierten Funktionen sind nicht praktisch geprüft.

### evd-051

Aussage:
rsaisankalp/clawdbotElyments: Code verarbeitet den Nachrichtentyp `groupchat`, enthält aber keinen Raumbeitritt; OMEMO-Zeichenketten kommen nicht vor; keine Testdateien.

Nachweisstatus:
`VERIFIED`

Begründung des Nachweisstatus:
Die Aussage beschränkt sich auf im gelesenen Quelltext vorhandene oder nicht gefundene Zeichenketten und Dateien. Das ist unmittelbar durch den Quelltext bestätigt. Über die Funktionsfähigkeit sagt die Aussage nichts.

Quellen:

| Quellenart | Fundstelle | Version oder Commit | Prüfdatum | Beitrag zum Befund |
|---|---|---|---|---|
| `SOURCE_CODE` | https://github.com/rsaisankalp/clawdbotElyments, `src/elyments/xmpp.ts` Zeile 320 | Commit f2e1dde49780 | 2026-09-14 | Nachrichtentyp `groupchat` |
| `SOURCE_CODE` | https://github.com/rsaisankalp/clawdbotElyments, `src/` mit `grep -rniE 'joinRoom\|jabber.org/protocol/muc\|omemo'` | Commit f2e1dde49780 | 2026-09-14 | 0 Treffer |

Prüfung:

Durchgeführt:
- Quelltext in einer getrennten Arbeitsumgebung per `git clone --depth 1` gelesen und nach Namensräumen und Bezeichnern durchsucht

Ergebnis: wie in der Aussage; Tests: keine

Nicht durchgeführt:
- nicht durchgeführt: Build, Ausführen der Tests und Funktionstest in einer getrennten Arbeitsumgebung

Einschränkung der Aussagekraft: belegt nur vorhandenen Code; 0 Treffer belegt nur das Fehlen der gesuchten Zeichenketten, nicht das Fehlen einer Funktion

Bezug zur Projektidee:

- Fundstelle: idea.md, Abschnitt 1, Abschnitt 7
- Bedeutung: im Quelltext vorhandene Implementierungsteile

Folgerung:
Vorhandener Code ist nicht als funktionsfähig nachgewiesen.

### evd-052

Aussage:
Ob eines der untersuchten Projekte Direktnachrichten, OMEMO-Verschlüsselung und Gruppenchats über MUC tatsächlich funktionsfähig bereitstellt, ist unbekannt.

Nachweisstatus:
`UNKNOWN`

Begründung des Nachweisstatus:
Für die Funktionsfähigkeit liegen nur Dokumentationsangaben (`DOCUMENTED`) und vorhandener Quelltext (`VERIFIED` nur für das Vorhandensein) vor. Eine Funktionsprüfung wurde nicht durchgeführt; damit fehlt eine ausreichende Information.

Quellen:

| Quellenart | Fundstelle | Version oder Commit | Prüfdatum | Beitrag zum Befund |
|---|---|---|---|---|
| `PROJECT_DOCUMENTATION` | README-Angaben der Projekte, siehe evd-022 bis evd-051 | Commits wie dort angegeben | 2026-09-14 | dokumentierte Funktionen |
| `SOURCE_CODE` | Quelltext der Projekte, siehe evd-022 bis evd-051 | Commits wie dort angegeben | 2026-09-14 | vorhandener Code ohne Funktionsnachweis |

Prüfung:

Durchgeführt:
- keine Funktionsprüfung

Ergebnis: –

Nicht durchgeführt:
- nicht durchgeführt: Build, Tests und Funktionstest der Projekte in einer getrennten, entbehrlichen Arbeitsumgebung mit eigener OpenClaw-Instanz und Test-XMPP-Server. Nach `phases/swk-02-inventory.md` wäre das zulässig, wenn es kein produktives System verändert und keine produktiven Zugangsdaten nutzt. Wegen fehlenden Zugriffs nicht möglich: Test gegen den eigenen XMPP-Server, da dieser nicht bekannt ist (siehe evd-008).

Einschränkung der Aussagekraft: Aussagen zu Funktionen reichen höchstens bis `DOCUMENTED` oder bis zum Vorhandensein von Code

Bezug zur Projektidee:

- Fundstelle: idea.md, Abschnitt 11 (erster unbekannter Sachverhalt)
- Bedeutung: offener Sachverhalt aus `idea.md`

Folgerung:
Der in `idea.md` genannte unbekannte Sachverhalt bleibt unbekannt.

### evd-053

Aussage:
Ob die untersuchten Projekte unter OpenClaw 2026.7.1-2 oder 2026.9.4 laden und laufen, ist unbekannt; es liegen nur deklarierte Versionsangaben vor.

Nachweisstatus:
`UNKNOWN`

Begründung des Nachweisstatus:
Deklarierte Versionsbereiche sind nach der OpenClaw-Dokumentation keine Kompatibilitätsnachweise (evd-014); ein Laden wurde nicht geprüft. Es liegt keine ausreichende Information vor.

Quellen:

| Quellenart | Fundstelle | Version oder Commit | Prüfdatum | Beitrag zum Befund |
|---|---|---|---|---|
| `SOURCE_CODE` | `package.json` der Projekte, siehe evd-022 bis evd-051 | Commits wie dort angegeben | 2026-09-14 | deklarierte Versionsangaben |
| `PRIMARY_DOCUMENTATION` | `/usr/lib/node_modules/openclaw/docs/plugins/sdk-overview.md` Zeilen 25–36 | openclaw@2026.9.4 (3a9d69d) | 2026-09-14 | Hinweis, jede Host-Version zu testen |

Prüfung:

Durchgeführt:
- keine Installationsprüfung

Ergebnis: –

Nicht durchgeführt:
- nicht durchgeführt: Laden der Projekte in einer getrennten OpenClaw-Instanz der Versionen 2026.7.1-2 und 2026.9.4

Einschränkung der Aussagekraft: deklarierte Versionsbereiche sind keine Kompatibilitätsnachweise

Bezug zur Projektidee:

- Fundstelle: idea.md, Abschnitt 1, Abschnitt 10 („aktuelle OpenClaw-Versionen“)
- Bedeutung: Kompatibilität des vorhandenen Bestands

Folgerung:
Die Kompatibilität der Projekte mit den genannten Versionen ist nicht belegt.

### evd-054

Aussage:
Ob es XMPP-Anbindungen für OpenClaw außerhalb von GitHub und npm gibt, etwa auf ClawHub, GitLab oder Codeberg, ist unbekannt.

Nachweisstatus:
`UNKNOWN`

Begründung des Nachweisstatus:
Die Suche umfasste nur GitHub und npm; für andere Plattformen liegt keine Information vor.

Quellen:

| Quellenart | Fundstelle | Version oder Commit | Prüfdatum | Beitrag zum Befund |
|---|---|---|---|---|
| `ANALYSIS` | Suchanfragen auf GitHub (siehe Abschnitt 4, Quelle „GitHub-Suche“) | Trefferzahlen am 2026-09-14 | 2026-09-14 | abgedeckter Suchraum GitHub |
| `PRIMARY_DOCUMENTATION` | Suchanfragen im npm-Register (siehe Abschnitt 4, Quelle „npm-Register, Suche“) | Registerstand 2026-09-14 | 2026-09-14 | abgedeckter Suchraum npm |

Prüfung:

Durchgeführt:
- GitHub- und npm-Suche durchgeführt

Ergebnis: –

Nicht durchgeführt:
- nicht durchgeführt: Suche auf ClawHub, GitLab, Codeberg und allgemeine Websuche

Einschränkung der Aussagekraft: Suche auf zwei Plattformen beschränkt

Bezug zur Projektidee:

- Fundstelle: idea.md, Abschnitt 1 („Vorhandene GitHub-Projekte“)
- Bedeutung: Vollständigkeit der Projektliste

Folgerung:
Die Projektliste ist auf GitHub und npm beschränkt.

## 6. Grenzen der Bestandsuntersuchung

- Nicht in den Untersuchungsumfang aufgenommen: Werkzeuge und Verfahren zur automatischen Aktualisierung, auch mit KI-Agenten. `idea.md` Abschnitt 1 nennt ein solches Verfahren als Bedarf, nicht als vorhandenen Bestand; eine Suche danach wäre Lösungsrecherche. Die Änderungen an OpenClaw selbst sind im Bereich Versionen erfasst.
- Nicht in den Untersuchungsumfang aufgenommen: Nutzer des Plugins und Chatpartner. `idea.md` Abschnitt 11 führt dies als unbekannt; es gibt dazu keinen untersuchbaren Bestand.
- Nicht in den Untersuchungsumfang aufgenommen: XMPP-Clients und deren Verschlüsselungsverfahren, weil `idea.md` sie nicht nennt.
- Zeitliche Grenze: Stand 2026-09-14; alle Registerdaten, Commits und Trefferzahlen gelten für diesen Tag. Die Übertragung in das strukturierte Format am 2026-09-15 enthielt keine neue Recherche.
- Technische Grenze: Quelltext nur gelesen und durchsucht; Builds, Tests und das Laden von Plugins in einer getrennten OpenClaw-Instanz wurden nicht durchgeführt.
- Nicht verfügbare Quellen: Konfigurationsverzeichnis `/var/lib/openclaw/.openclaw` auf srv001; Installation mit 2026.7.1-2; eigener XMPP-Server; Aufzeichnungen zu bisherigen Versuchen.
- Nicht mögliche Prüfungen: Prüfungen am eigenen XMPP-Server und an der Konfiguration von srv001 (fehlender Zugriff). Funktions- und Kompatibilitätsprüfungen der Projekte wären in einer getrennten Arbeitsumgebung möglich, wurden aber nicht durchgeführt.
- Sonstige Einschränkung: Suche und Erstauswertung der Projekte und der OpenClaw-Schnittstelle erfolgten in zwei Hilfsaufträgen. Metadaten aller Projekte, Commits, Versionsdaten, Exportpfade, Stabilitätsaussage, Kanalliste, PR-Status und ausgewählte README- und Codestellen wurden von skizzwerk stichprobenartig nachgeprüft, nicht jede Zeilenangabe.
- Kein externes System, keine Installation und kein Repository wurde durch die Bestandsuntersuchung verändert.

## 7. Prüfergebnis swk-02

- Vorprüfung bestanden: `true`
- Qualitätsgrenze bestanden: `true`
- geprüft am: 2026-09-15
- geprüft durch: skizzwerk

Nicht erfüllte Kriterien:
- keine

- Begründung einer möglichen Blockade: keine

## 8. Freigabestatus

- Dokumentstatus: `review`
- angenommen am: –
- angenommen durch: –
- Anmerkungen: –
