---
document: inventory
process_phase: swk-02
project: "openclaw-xmpp"
status: review
created: 2026-09-14
last_updated: 2026-09-14
basis: idea.md
---

# Bestandsuntersuchung

## 1. Grundlage und Untersuchungsauftrag

- zugrunde liegende `idea.md`: `pilots/openclaw-xmpp/idea.md`, Commit 4e46961
- Status der `idea.md`: `accepted`
- bestätigte Fassung vom: 2026-09-14
- Beginn der Untersuchung: 2026-09-14
- Stand der Untersuchung: 2026-09-14

Untersucht wird der vorhandene Bestand zu einer XMPP-Anbindung an OpenClaw:
die vorhandenen OpenClaw-Installationen, die Plugin-Schnittstelle der
genannten OpenClaw-Versionen und ihre Änderungen, XMPP im Lieferumfang und im
Hauptprojekt von OpenClaw, vorhandene öffentliche Projekte sowie die Angaben
zum eigenen XMPP-Server und zu bisherigen Versuchen.

Kennzeichnung nach `rules/evidence.md`: `USER_PROVIDED` (Aussage des
Ideengebers), `VERIFIED` (unmittelbar durch Code, Befehlsausgabe oder
Primärquelle bestätigt), `DOCUMENTED` (dokumentierte Behauptung), `INFERRED`
(Ableitung), `ASSUMED` (Annahme), `UNKNOWN` (unbekannt), `CONFLICT`
(widersprüchlich), `DISPROVED` (widerlegt). In dieser Untersuchung wurden keine
Annahmen gesetzt und keine Aussage widerlegt.

## 2. Untersuchungsumfang

Die Untersuchungsbereiche müssen aus der akzeptierten `idea.md` abgeleitet
werden.

| Untersuchungsbereich | Bezug zur `idea.md` | Begründung der Relevanz | Untersuchung vorgesehen |
|---|---|---|---|
| Vorhandene OpenClaw-Installationen | Abschnitt 2 („2 OpenClaw Installationen … aktiv“), Abschnitt 6, Abschnitt 11 | vorhandene Systeme, für die das Plugin bestimmt ist | ja |
| Plugin- und Kanalschnittstelle von OpenClaw | Abschnitt 1 („Ein XMPP-Plugin für aktuelle OpenClaw-Versionen“), Abschnitt 5 | vorhandene Grundlage, an die ein Plugin anschließt | ja |
| Versionen und Schnittstellenänderungen zwischen 2026.7.1-2 und 2026.9.4 | Abschnitt 1 („Für neue OpenClaw-Versionen …“), Abschnitt 10 („aktuelle OpenClaw-Versionen“), Abschnitt 11 („Ob und wie oft neue OpenClaw-Versionen Änderungen bringen“) | Bestand zu Häufigkeit und Art von Änderungen | ja |
| XMPP im Lieferumfang und im Hauptprojekt von OpenClaw | Abschnitt 1, Abschnitt 5 | vorhandene XMPP-Unterstützung durch den Hersteller | ja |
| Vorhandene öffentliche XMPP-Projekte für OpenClaw | Abschnitt 1 („Vorhandene GitHub-Projekte sollen als mögliche Grundlage untersucht werden“), Abschnitt 7, Abschnitt 11 | ausdrücklich zu untersuchende mögliche Grundlagen | ja |
| Eigener XMPP-Server | Abschnitt 2 („Ein eigener XMPP-Server ist vorhanden“), Abschnitt 6, Abschnitt 11 | genanntes vorhandenes System | ja |
| Bisherige Versuche mit bestehenden Plugins | Abschnitt 2 („bestehende Plugins konnten z. T. nicht installiert werden …“), Abschnitt 11 | dokumentierter bisheriger Versuch | ja |

Nicht in den Untersuchungsumfang aufgenommene Bereiche:

| Bereich | Begründung |
|---|---|
| Werkzeuge und Verfahren zur automatischen Aktualisierung, auch mit KI-Agenten | `idea.md` Abschnitt 1 nennt ein solches Verfahren als Bedarf, nicht als vorhandenen Bestand; eine Suche danach wäre Lösungsrecherche. Die Änderungen an OpenClaw selbst sind im Bereich Versionen erfasst. |
| Nutzer des Plugins und Chatpartner | `idea.md` Abschnitt 11 führt dies als unbekannt; es gibt dazu keinen untersuchbaren Bestand. |
| XMPP-Clients und deren Verschlüsselungsverfahren | in `idea.md` nicht genannt |
| Funktionsprüfung vorhandener Projekte durch Installation und Test | nach `phases/swk-02-inventory.md` keine Installation oder Veränderung zur Bestandsaufnahme; als nicht durchgeführte Prüfung in Abschnitt 9 dokumentiert |

## 3. Durchgeführte Untersuchung

| Untersuchungsbereich | Tatsächlich untersucht | Nicht untersucht | Einschränkungen |
|---|---|---|---|
| Vorhandene OpenClaw-Installationen | Version und Dienststatus auf srv001; lokale Installationsdokumentation | Konfiguration und Plugins auf srv001; Installation mit 2026.7.1-2 | Konfigurationsverzeichnis nicht lesbar; zweite Installation nicht auffindbar |
| Plugin- und Kanalschnittstelle | `package.json`, Typdefinitionen und `docs/plugins/` im Paket 2026.9.4 | Paketinhalt 2026.7.1-2; `src/plugins/compat/registry.ts`; Website docs.openclaw.ai | Beschreibung aus Dateien, kein Plugin gebaut |
| Versionen und Schnittstellenänderungen | npm-Registerdaten; Tags; CHANGELOG am Tag `v2026.9.4` (Einträge zu Plugin-SDK und Kanälen) | CHANGELOG nicht vollständig gelesen | CHANGELOG enthält keine Abschnitte 2026.7.1-1 und 2026.7.1-2 |
| XMPP im Lieferumfang und Hauptprojekt | `dist/extensions/` und Volltextsuche im Paket; `extensions/` auf `main`; PRs #9741, #20998, #21015; Issue #29046 | Diskussionsinhalte der PRs und Issues | nur Status ausgewertet |
| Vorhandene öffentliche XMPP-Projekte | 12 Projekte und 1 Grenzfall auf GitHub; npm-Register | ClawHub, GitLab, Codeberg; Forks cronus42, kitschmensch, zhgzhg, jerry-harm, indorri; geschlossene Issues; Funktionsfähigkeit | Quelltext nur auf Vorhandensein geprüft |
| Eigener XMPP-Server | Suche in lokaler Dokumentation und Dienstliste auf srv001 | Server selbst | keine Angaben zu Standort und Software |
| Bisherige Versuche | Suche in lokaler Dokumentation; Versuch, das Konfigurationsverzeichnis auf srv001 zu lesen | Plugin-Liste der Installationen | Zugriff verweigert; keine Dokumentation vorhanden |

## 4. Quellen

Für die Quellenarten gilt `rules/evidence.md`.

### Quelle: idea.md

- Quellenart: USER_STATEMENT
- Herausgeber oder Verantwortlicher: Martin Henkel (Ideengeber)
- Titel oder Bezeichnung: Projektidee openclaw-xmpp
- Fundstelle: `pilots/openclaw-xmpp/idea.md`
- Version, Commit oder Veröffentlichungsstand: Commit 4e46961, Status `accepted`
- Abruf- oder Prüfdatum: 2026-09-14
- tatsächlich untersuchter Teil: vollständig
- Zugänglichkeit: Repository skizzwerk
- erkannte Einschränkungen: –

### Quelle: Rechner srv001

- Quellenart: MANUAL_TEST
- Herausgeber oder Verantwortlicher: Betreiber srv001
- Titel oder Bezeichnung: OpenClaw-Installation auf srv001.martinhenkel.net
- Fundstelle: Befehle `openclaw --version`, `npm ls -g --depth=0`, `systemctl is-active openclaw`, `systemctl list-units --type=service`, `ls /var/lib/openclaw/.openclaw`
- Version, Commit oder Veröffentlichungsstand: openclaw@2026.9.4 (3a9d69d)
- Abruf- oder Prüfdatum: 2026-09-14
- tatsächlich untersuchter Teil: Version, Dienststatus, Dienstliste
- Zugänglichkeit: lesend; `/var/lib/openclaw/.openclaw` nicht lesbar
- erkannte Einschränkungen: keine Befehle, die Konfiguration schreiben

### Quelle: lokale Dokumentation

- Quellenart: PROJECT_DOCUMENTATION
- Herausgeber oder Verantwortlicher: Betreiber srv001
- Titel oder Bezeichnung: Installationsanleitung OpenClaw und Anleitung eurouter-Provider
- Fundstelle: `/srv/aixlab/docs/anleitungen/dev-server/09-00-dev-server-install-openclaw.md`; `/srv/aixlab/docs/sysdoc/srv001/anleitungen/eurouter-provider-openclaw.md`; Volltextsuche in `/srv/aixlab/docs`
- Version, Commit oder Veröffentlichungsstand: kein Git-Stand; Dateistand 2026-08-30 bzw. 2026-08-12
- Abruf- oder Prüfdatum: 2026-09-14
- tatsächlich untersuchter Teil: beide Dateien; Suche nach xmpp, jabber, prosody, ejabberd, omemo im ganzen Verzeichnis
- Zugänglichkeit: lesend
- erkannte Einschränkungen: Treffer nur im Ordner `archiv/` mit allgemeinen Erwähnungen von XMPP

### Quelle: OpenClaw-Paket 2026.9.4

- Quellenart: SOURCE_CODE und PRIMARY_DOCUMENTATION
- Herausgeber oder Verantwortlicher: OpenClaw-Projekt
- Titel oder Bezeichnung: npm-Paket `openclaw`
- Fundstelle: `/usr/lib/node_modules/openclaw` (`package.json`, `dist/plugin-sdk/`, `dist/extensions/`, `docs/`)
- Version, Commit oder Veröffentlichungsstand: 2026.9.4, Commit 3a9d69db306c
- Abruf- oder Prüfdatum: 2026-09-14
- tatsächlich untersuchter Teil: `package.json` Exporte, Kanal-Typdefinitionen, Erweiterungsverzeichnis, `docs/plugins/`, `docs/channels/index.md`, `docs/start/lore.md`; Volltextsuche nach xmpp, jabber, omemo, muc
- Zugänglichkeit: lesend
- erkannte Einschränkungen: Übereinstimmung mit docs.openclaw.ai nicht geprüft

### Quelle: npm-Register

- Quellenart: PRIMARY_DOCUMENTATION
- Herausgeber oder Verantwortlicher: npm, Inc.
- Titel oder Bezeichnung: Registerdaten `openclaw` und Suche
- Fundstelle: https://registry.npmjs.org/openclaw; https://registry.npmjs.org/-/v1/search mit `text=openclaw xmpp`, `openclaw jabber`, `openclaw omemo`, `openclaw prosody`, `clawdbot xmpp`, `moltbot xmpp`, `keywords:openclaw` (seitenweise), `keywords:clawdbot`, `keywords:moltbot`, `keywords:openclaw-plugin`, `keywords:openclaw-channel`, `text=xmpp`, `text=omemo`, `text=jabber`; Direktabfragen `@openclaw/xmpp`, `openclaw-xmpp`, `openclaw-channel-xmpp`, `@openclaw/channel-xmpp`, `clawdbot-xmpp`, `moltbot-xmpp`
- Version, Commit oder Veröffentlichungsstand: Registerstand am Abrufdatum
- Abruf- oder Prüfdatum: 2026-09-14
- tatsächlich untersuchter Teil: `time`, `dist-tags`, `versions[*].exports`; Suchtreffer
- Zugänglichkeit: öffentlich
- erkannte Einschränkungen: `keywords:openclaw`: 134 von 5134 Einträgen nicht abrufbar (Suchgrenze 5000)

### Quelle: OpenClaw-Repository

- Quellenart: PROJECT_DOCUMENTATION und ISSUE_OR_PR
- Herausgeber oder Verantwortlicher: OpenClaw-Projekt
- Titel oder Bezeichnung: github.com/openclaw/openclaw
- Fundstelle: https://github.com/openclaw/openclaw (`CHANGELOG.md` am Tag `v2026.9.4`, `VISION.md`, Baum `extensions/`, PRs #9741, #20998, #21015, Issue #29046)
- Version, Commit oder Veröffentlichungsstand: Tag `v2026.9.4` → 3a9d69db306c; Tag `v2026.7.1-2` → 0790d9f593ad; `main` df663a946582
- Abruf- oder Prüfdatum: 2026-09-14
- tatsächlich untersuchter Teil: Einträge zu Plugin-SDK und Kanälen im CHANGELOG; Verzeichnisbaum `extensions/`; Status der PRs und des Issues
- Zugänglichkeit: öffentlich
- erkannte Einschränkungen: CHANGELOG nicht vollständig gelesen; Diskussionen nicht ausgewertet

### Quelle: GitHub-Suche

- Quellenart: ANALYSIS
- Herausgeber oder Verantwortlicher: skizzwerk
- Titel oder Bezeichnung: Suchanfragen auf GitHub
- Fundstelle: `gh search repos` mit „openclaw xmpp“ (6), „openclaw jabber“ (0), „openclaw prosody“ (0), „openclaw omemo“ (0), „clawdbot xmpp“ (0), „moltbot xmpp“ (0), „openclaw-channel xmpp“ (0), „xmpp openclaw plugin“ (0), „openclaw ejabberd“ (0); `gh api search/repositories` mit `xmpp in:name,description,readme openclaw` (176), `xmpp clawdbot in:readme` (10), `xmpp moltbot in:readme` (7), `topic:openclaw topic:xmpp` (4), `omemo openclaw in:readme` (12), `jabber openclaw in:readme` (24), `openclaw xmpp fork:true` (21), `xmpp in:name claw` (5); `gh api search/code` mit `openclaw @xmpp/client filename:package.json` (5), `openclaw xmpp filename:openclaw.plugin.json` (2), `openclaw urn:xmpp:omemo` (2), `openclaw muc groupchat xmpp` (19), `"channels.xmpp" openclaw` (18); `gh search prs/issues --repo openclaw/openclaw xmpp` (je 7)
- Version, Commit oder Veröffentlichungsstand: Trefferzahlen am Abrufdatum
- Abruf- oder Prüfdatum: 2026-09-14
- tatsächlich untersuchter Teil: Trefferlisten gesichtet
- Zugänglichkeit: öffentlich, angemeldet als macodix (nur lesend)
- erkannte Einschränkungen: Codesuche nur auf Standard-Branches; Nicht-Standard-Zweige von Forks nicht erfasst

### Quelle: https://github.com/ksmith211/openclaw-xmpp

- Quellenart: PROJECT_DOCUMENTATION, SOURCE_CODE und ISSUE_OR_PR
- Herausgeber oder Verantwortlicher: ksmith211
- Titel oder Bezeichnung: ksmith211/openclaw-xmpp
- Fundstelle: https://github.com/ksmith211/openclaw-xmpp
- Version, Commit oder Veröffentlichungsstand: ad1ad44777fce6471b68e9f661bbe90413c789fa, letzter Commit 2026-02-02; npm `@ksmith221/openclaw-xmpp` 0.1.1
- Abruf- oder Prüfdatum: 2026-09-14
- tatsächlich untersuchter Teil: README, package.json, `src/`; Lizenz: MIT
- Zugänglichkeit: öffentlich; Klon mit `--depth 1`, nur gelesen
- erkannte Einschränkungen: kein Code und kein Test ausgeführt

### Quelle: https://github.com/toughworm/Openclaw-XMPP-Plugin

- Quellenart: PROJECT_DOCUMENTATION, SOURCE_CODE und ISSUE_OR_PR
- Herausgeber oder Verantwortlicher: toughworm
- Titel oder Bezeichnung: toughworm/Openclaw-XMPP-Plugin
- Fundstelle: https://github.com/toughworm/Openclaw-XMPP-Plugin
- Version, Commit oder Veröffentlichungsstand: 428886a5fab2371a61edbe80037d453006f3869b, letzter Commit 2026-02-21
- Abruf- oder Prüfdatum: 2026-09-14
- tatsächlich untersuchter Teil: README, package.json, `src/`, `test/`, `git ls-files`; Lizenz: keine laut API
- Zugänglichkeit: öffentlich; Klon mit `--depth 1`, nur gelesen
- erkannte Einschränkungen: kein Code und kein Test ausgeführt

### Quelle: https://github.com/kazakhan/openclaw-xmpp

- Quellenart: PROJECT_DOCUMENTATION, SOURCE_CODE und ISSUE_OR_PR
- Herausgeber oder Verantwortlicher: kazakhan
- Titel oder Bezeichnung: kazakhan/openclaw-xmpp
- Fundstelle: https://github.com/kazakhan/openclaw-xmpp
- Version, Commit oder Veröffentlichungsstand: 4fb1e113150e33a8a67a0f7a4428eb249f511a66, letzter Commit 2026-09-14T10:39:31Z
- Abruf- oder Prüfdatum: 2026-09-14
- tatsächlich untersuchter Teil: README, XMPPAUDIT.md, package.json, `src/`, `index.ts`, `tests/`; Lizenz: MIT laut API
- Zugänglichkeit: öffentlich; Klon mit `--depth 1`, nur gelesen
- erkannte Einschränkungen: kein Code und kein Test ausgeführt

### Quelle: https://github.com/icarito/openclaw-xmpp

- Quellenart: PROJECT_DOCUMENTATION, SOURCE_CODE und ISSUE_OR_PR
- Herausgeber oder Verantwortlicher: icarito
- Titel oder Bezeichnung: icarito/openclaw-xmpp
- Fundstelle: https://github.com/icarito/openclaw-xmpp
- Version, Commit oder Veröffentlichungsstand: 820213a98cb151c3aadbb68014f9c3b2d0ae76f5, letzter Commit 2026-07-26
- Abruf- oder Prüfdatum: 2026-09-14
- tatsächlich untersuchter Teil: README, AGENTS.md, package.json, `src/`; Lizenz: keine laut API
- Zugänglichkeit: öffentlich; Klon mit `--depth 1`, nur gelesen
- erkannte Einschränkungen: kein Code und kein Test ausgeführt

### Quelle: https://github.com/soilDNRA/openclaw-xmpp

- Quellenart: PROJECT_DOCUMENTATION, SOURCE_CODE und ISSUE_OR_PR
- Herausgeber oder Verantwortlicher: soilDNRA; Hauptquelle git.sdf.org/erici/openclaw-xmpp
- Titel oder Bezeichnung: soilDNRA/openclaw-xmpp
- Fundstelle: https://github.com/soilDNRA/openclaw-xmpp
- Version, Commit oder Veröffentlichungsstand: a41df5fc141735216d09fb17ca635dad6bef4d31, letzter Commit 2026-09-09
- Abruf- oder Prüfdatum: 2026-09-14
- tatsächlich untersuchter Teil: README, PROJECT.md, package.json, `src/`, `test/`; Lizenz: GPL-3.0
- Zugänglichkeit: öffentlich; Klon mit `--depth 1`, nur gelesen
- erkannte Einschränkungen: kein Code und kein Test ausgeführt

### Quelle: https://github.com/elmafioso79/xmpp-channel

- Quellenart: PROJECT_DOCUMENTATION, SOURCE_CODE und ISSUE_OR_PR
- Herausgeber oder Verantwortlicher: elmafioso79
- Titel oder Bezeichnung: elmafioso79/xmpp-channel
- Fundstelle: https://github.com/elmafioso79/xmpp-channel
- Version, Commit oder Veröffentlichungsstand: a447455d6cb13bf2be00e10c3600fe5d72178863, letzter Commit 2026-02-18
- Abruf- oder Prüfdatum: 2026-09-14
- tatsächlich untersuchter Teil: README, package.json, `src/`, offene Issues und PRs; Lizenz: MIT
- Zugänglichkeit: öffentlich; Klon mit `--depth 1`, nur gelesen
- erkannte Einschränkungen: kein Code und kein Test ausgeführt

### Quelle: https://github.com/watkins-matt/xmpp-channel

- Quellenart: PROJECT_DOCUMENTATION, SOURCE_CODE und ISSUE_OR_PR
- Herausgeber oder Verantwortlicher: watkins-matt
- Titel oder Bezeichnung: watkins-matt/xmpp-channel
- Fundstelle: https://github.com/watkins-matt/xmpp-channel
- Version, Commit oder Veröffentlichungsstand: 1a734552fe19bc4cdb29ba31a398845237282e09, letzter Commit 2026-09-11
- Abruf- oder Prüfdatum: 2026-09-14
- tatsächlich untersuchter Teil: README (Vergleich mit Ursprung), package.json, `src/`; Lizenz: MIT
- Zugänglichkeit: öffentlich; Klon mit `--depth 1`, nur gelesen
- erkannte Einschränkungen: kein Code und kein Test ausgeführt

### Quelle: https://github.com/Programmatore-Web/openclaw-xmpp-channel

- Quellenart: PROJECT_DOCUMENTATION, SOURCE_CODE und ISSUE_OR_PR
- Herausgeber oder Verantwortlicher: Programmatore-Web
- Titel oder Bezeichnung: Programmatore-Web/openclaw-xmpp-channel
- Fundstelle: https://github.com/Programmatore-Web/openclaw-xmpp-channel
- Version, Commit oder Veröffentlichungsstand: 0ba189314a14b15a3a50c9e47c0b64035fc19e8a, letzter Commit 2026-09-10
- Abruf- oder Prüfdatum: 2026-09-14
- tatsächlich untersuchter Teil: README, CHANGELOG.md, package.json, `src/`, `test/`; Lizenz: MIT
- Zugänglichkeit: öffentlich; Klon mit `--depth 1`, nur gelesen
- erkannte Einschränkungen: kein Code und kein Test ausgeführt

### Quelle: https://github.com/MrCPA/oc-xmpp

- Quellenart: PROJECT_DOCUMENTATION, SOURCE_CODE und ISSUE_OR_PR
- Herausgeber oder Verantwortlicher: MrCPA
- Titel oder Bezeichnung: MrCPA/oc-xmpp
- Fundstelle: https://github.com/MrCPA/oc-xmpp
- Version, Commit oder Veröffentlichungsstand: 675775a49f430f912e56ea43777c1fa32cf0cfef, letzter Commit 2026-04-11
- Abruf- oder Prüfdatum: 2026-09-14
- tatsächlich untersuchter Teil: README, package.json, `src/`, `tests/`; Lizenz: GPL-3.0
- Zugänglichkeit: öffentlich; Klon mit `--depth 1`, nur gelesen
- erkannte Einschränkungen: kein Code und kein Test ausgeführt

### Quelle: https://github.com/chitozzz/xmpp-adapter-openclaw

- Quellenart: PROJECT_DOCUMENTATION, SOURCE_CODE und ISSUE_OR_PR
- Herausgeber oder Verantwortlicher: chitozzz
- Titel oder Bezeichnung: chitozzz/xmpp-adapter-openclaw
- Fundstelle: https://github.com/chitozzz/xmpp-adapter-openclaw
- Version, Commit oder Veröffentlichungsstand: f280515acd43681d0a6cb89945eafecd6d7b6729, letzter Commit 2026-09-12
- Abruf- oder Prüfdatum: 2026-09-14
- tatsächlich untersuchter Teil: README, package.json, `src/`, `test/`; Lizenz: keine laut API
- Zugänglichkeit: öffentlich; Klon mit `--depth 1`, nur gelesen
- erkannte Einschränkungen: kein Code und kein Test ausgeführt

### Quelle: https://github.com/weijia/xmpp-connector

- Quellenart: PROJECT_DOCUMENTATION, SOURCE_CODE und ISSUE_OR_PR
- Herausgeber oder Verantwortlicher: weijia
- Titel oder Bezeichnung: weijia/xmpp-connector
- Fundstelle: https://github.com/weijia/xmpp-connector
- Version, Commit oder Veröffentlichungsstand: 3d7c72e66cd95da5cf1b01e56d85040e211fc775 (Branch `master`), letzter Commit 2026-03-29; npm `openclaw-xmpp-connector` 0.3.0
- Abruf- oder Prüfdatum: 2026-09-14
- tatsächlich untersuchter Teil: README, package.json, `plugin.ts`; Lizenz: keine laut API
- Zugänglichkeit: öffentlich; Klon mit `--depth 1`, nur gelesen
- erkannte Einschränkungen: kein Code und kein Test ausgeführt

### Quelle: https://github.com/processone/openclaw/tree/xmpp-support/extensions/xmpp

- Quellenart: PROJECT_DOCUMENTATION, SOURCE_CODE und ISSUE_OR_PR
- Herausgeber oder Verantwortlicher: ProcessOne
- Titel oder Bezeichnung: processone/openclaw/tree/xmpp-support/extensions/xmpp
- Fundstelle: https://github.com/processone/openclaw/tree/xmpp-support/extensions/xmpp
- Version, Commit oder Veröffentlichungsstand: a6adb95b35c183a81eef3afcef17071e9b647673 (Branch `xmpp-support`), letzter Commit 2026-02-07
- Abruf- oder Prüfdatum: 2026-09-14
- tatsächlich untersuchter Teil: `extensions/xmpp/` über GitHub-API geladen, nicht geklont; Lizenz: MIT
- Zugänglichkeit: öffentlich; Klon mit `--depth 1`, nur gelesen
- erkannte Einschränkungen: kein Code und kein Test ausgeführt

### Quelle: https://github.com/rsaisankalp/clawdbotElyments

- Quellenart: PROJECT_DOCUMENTATION, SOURCE_CODE und ISSUE_OR_PR
- Herausgeber oder Verantwortlicher: rsaisankalp
- Titel oder Bezeichnung: rsaisankalp/clawdbotElyments
- Fundstelle: https://github.com/rsaisankalp/clawdbotElyments
- Version, Commit oder Veröffentlichungsstand: f2e1dde4978053ed7212cbd5168f1c8be3c2e52a, letzter Commit 2026-01-17; npm `clawdbot-elyments` 1.0.0
- Abruf- oder Prüfdatum: 2026-09-14
- tatsächlich untersuchter Teil: README, package.json, `src/elyments/`; Lizenz: keine laut API
- Zugänglichkeit: öffentlich; Klon mit `--depth 1`, nur gelesen
- erkannte Einschränkungen: kein Code und kein Test ausgeführt

## 5. Befundübersicht

| Kennung | Aussage | Nachweisstatus | wichtigste Quelle |
|---|---|---|---|
| `evd-001` | Zurzeit sind zwei OpenClaw-Installationen mit den Versionen 2026.9.4 und 2026.7.1-2 aktiv. | `USER_PROVIDED` | idea.md |
| `evd-002` | Ein eigener XMPP-Server ist vorhanden. | `USER_PROVIDED` | idea.md |
| `evd-003` | Bestehende Plugins konnten zum Teil nicht installiert werden oder erfüllten nicht die Anforderungen an Sicherheit (OMEMO) oder Kommunikation (Gruppenchats/MUC). | `USER_PROVIDED` | idea.md |
| `evd-004` | Auf dem Rechner srv001 ist OpenClaw 2026.9.4 (Commit 3a9d69d) als globales npm-Paket installiert; der Dienst `openclaw.service` ist aktiv. | `VERIFIED` | srv001 |
| `evd-005` | Die lokale Installationsanleitung beschreibt OpenClaw mit dem mitgelieferten WebChat und Authelia sowie ein über ClawHub installiertes Provider-Plugin; XMPP wird dort nicht erwähnt. | `DOCUMENTED` | lokale Dokumentation |
| `evd-006` | Ob srv001 eine der beiden vom Ideengeber genannten Installationen ist und wo die Installation mit Version 2026.7.1-2 läuft, ist unbekannt. | `UNKNOWN` | – |
| `evd-007` | Welche Plugins in den vorhandenen Installationen installiert oder erprobt wurden und woran ihre Installation scheiterte, ist unbekannt. | `UNKNOWN` | srv001 |
| `evd-008` | Software, Standort und unterstützte XMPP-Erweiterungen des eigenen XMPP-Servers sind unbekannt. | `UNKNOWN` | lokale Dokumentation, srv001 |
| `evd-009` | Die Versionen 2026.7.1-2 (veröffentlicht 2026-07-18T03:53:48Z, Tag-Commit 0790d9f593ad) und 2026.9.4 (veröffentlicht 2026-09-11T02:44:59Z, Tag-Commit 3a9d69db306c) sind im npm-Register veröffentlicht; `latest` ist 2026.9.4, `extended-stable` ist 2026.6.35. | `VERIFIED` | npm-Register |
| `evd-010` | Zwischen 2026.7.1-2 und 2026.9.4 wurden 17 Versionen veröffentlicht: 2026.8.1, 2026.8.2, 2026.9.1, 2026.9.2, 2026.9.3, neun Beta-Versionen und 2026.6.33 bis 2026.6.35. | `VERIFIED` | npm-Register |
| `evd-011` | Die Exportpfade `./plugin-sdk` und `./extension-api` sind in 2026.7.1-2 und 2026.7.2-beta.3 vorhanden, ab 2026.7.2-beta.4 und in 2026.9.4 nicht mehr. | `VERIFIED` | npm-Register |
| `evd-012` | Das Paket 2026.9.4 exportiert Unterpfade `openclaw/plugin-sdk/*`, darunter `channel-core`, `channel-contract`, `channel-entry-contract` und `plugin-entry`; `channel-core.d.ts` exportiert u. a. `ChannelPlugin` und `defineChannelPluginEntry`. | `VERIFIED` | OpenClaw-Paket 2026.9.4 |
| `evd-013` | Laut Dokumentation braucht jedes native Plugin eine `openclaw.plugin.json`; die Felder `openclaw.compat.pluginApi` und `openclaw.install.minHostVersion` werden bei npm-Installationen zur Versionsauswahl ausgewertet. | `DOCUMENTED` | OpenClaw-Paket 2026.9.4 |
| `evd-014` | Laut Dokumentation sind alle Plugin-APIs experimentell und können sich zwischen OpenClaw-Versionen ändern; Plugin-Autoren sollen die Version festlegen und jede als kompatibel angegebene Version testen. | `DOCUMENTED` | OpenClaw-Paket 2026.9.4 |
| `evd-015` | Laut Dokumentation sind `openclaw/plugin-sdk`, `openclaw/plugin-sdk/compat` und `openclaw/extension-api` entfernt; Plugins, die sie importieren, laden nicht mehr. Alte Verträge laufen befristet über Kompatibilitätsadapter. | `DOCUMENTED` | OpenClaw-Paket 2026.9.4 |
| `evd-016` | Das CHANGELOG nennt für 2026.9.3 mehrere als „Breaking“ gekennzeichnete Änderungen am Plugin-SDK und für 2026.8.1 bis 2026.9.4 Abkündigungen von SDK-Pfaden mit Entfernungsterminen 2026-09-01 und 2026-09-08. | `DOCUMENTED` | OpenClaw-Repository |
| `evd-017` | Zwischen 2026.7.1-2 und 2026.9.4 hat sich die Plugin-Schnittstelle so geändert, dass Plugins, die die entfernten Pfade nutzen, unter 2026.9.4 laut Dokumentation nicht laden. | `INFERRED` | evd-011, evd-015, evd-016 |
| `evd-018` | Das Paket 2026.9.4 enthält unter `dist/extensions/` 60 Erweiterungen, darunter keine für XMPP; die Suche nach `xmpp`, `jabber`, `omemo`, `muc` trifft nur Fremdbibliotheken (URL-Schema, MIME-Typ). | `VERIFIED` | OpenClaw-Paket 2026.9.4 |
| `evd-019` | Die Kanalübersicht der Dokumentation nennt mitgelieferte und offizielle Kanal-Plugins, aber kein XMPP- oder Jabber-Plugin. | `DOCUMENTED` | OpenClaw-Paket 2026.9.4 |
| `evd-020` | Im Repository `openclaw/openclaw` enthält `extensions/` auf `main` kein XMPP-Verzeichnis; die Pull Requests #9741, #20998 und #21015 für XMPP wurden ohne Merge geschlossen; Issue #29046 „[Feature]: XMPP support“ ist mit `not_planned` geschlossen. | `VERIFIED` | OpenClaw-Repository |
| `evd-021` | OpenClaw hieß laut Projektdokumentation zuvor Warelay, Clawdbot und Moltbot; seit dem 30. Januar 2026 heißt es OpenClaw. | `DOCUMENTED` | OpenClaw-Paket 2026.9.4 |
| `evd-022` | ksmith211/openclaw-xmpp: Die README beschreibt ein Kanal-Plugin nur für Direktnachrichten; MUC, OMEMO und eine OpenClaw-Version werden nicht genannt. Auf npm ist `@ksmith221/openclaw-xmpp` 0.1.1 veröffentlicht. | `DOCUMENTED` | https://github.com/ksmith211/openclaw-xmpp |
| `evd-023` | ksmith211/openclaw-xmpp: Code für 1:1-Nachrichten ist vorhanden (`type: "chat"`); Zeichenketten zu MUC, groupchat und OMEMO kommen in `src/` nicht vor; keine Testdateien. | `VERIFIED` | https://github.com/ksmith211/openclaw-xmpp |
| `evd-024` | toughworm/Openclaw-XMPP-Plugin: Die README nennt 1:1- und Gruppenchat, OMEMO nur für 1:1 im älteren Namensraum `eu.siacs.conversations.axolotl`, verschlüsselten Gruppenchat als offen und keine OpenClaw-Version. | `DOCUMENTED` | https://github.com/toughworm/Openclaw-XMPP-Plugin |
| `evd-025` | toughworm/Openclaw-XMPP-Plugin: OMEMO-Code im Namensraum `eu.siacs.conversations.axolotl` ist vorhanden und wird bei `groupchat` übersprungen; Code für einen MUC-Raumbeitritt (`http://jabber.org/protocol/muc`) kommt nicht vor. | `VERIFIED` | https://github.com/toughworm/Openclaw-XMPP-Plugin |
| `evd-026` | toughworm/Openclaw-XMPP-Plugin: Die README nennt Gruppenchat und die Installation über `@openclaw/xmpp`; im Code fehlt ein Raumbeitritt, das Paket `@openclaw/xmpp` gibt es auf npm nicht (HTTP 404), und die in der README genannten Testskripte fehlen im Repository. | `CONFLICT` | https://github.com/toughworm/Openclaw-XMPP-Plugin |
| `evd-027` | kazakhan/openclaw-xmpp: Die README nennt 1:1 und MUC und „OpenClaw 2026.8.2+“; `XMPPAUDIT.md` führt OMEMO (XEP-0384) als „Not Supported“. | `DOCUMENTED` | https://github.com/kazakhan/openclaw-xmpp |
| `evd-028` | kazakhan/openclaw-xmpp: Code für MUC (`muc`-Namensraum, `joinRoom`) und 1:1 ist vorhanden; OMEMO-Zeichenketten kommen nicht vor. | `VERIFIED` | https://github.com/kazakhan/openclaw-xmpp |
| `evd-029` | kazakhan/openclaw-xmpp: Die README nennt als Mindestversion OpenClaw 2026.8.2, `package.json` gibt `compat.pluginApi ">=2026.6.1"` und `minGatewayVersion "2026.6.1"` an. | `CONFLICT` | https://github.com/kazakhan/openclaw-xmpp |
| `evd-030` | icarito/openclaw-xmpp: Die Paketbeschreibung nennt 1:1-Chat, MUC-Räume und Ad-hoc-Befehle; `compat.pluginApi` ist `>=2026.7.1`; die README sagt, der Produktivbetrieb lade einen separat abgeglichenen Verzeichnisbaum. | `DOCUMENTED` | https://github.com/icarito/openclaw-xmpp |
| `evd-031` | icarito/openclaw-xmpp: Code für MUC, für OMEMO im älteren Namensraum und in `urn:xmpp:omemo:2` sowie ein Python-Hilfsprogramm `src/omemo/sidecar.py` sind vorhanden. | `VERIFIED` | https://github.com/icarito/openclaw-xmpp |
| `evd-032` | icarito/openclaw-xmpp: `AGENTS.md` nennt OpenClaw 2026.6.9, `package.json` gibt `compat.pluginApi ">=2026.7.1"` an. | `CONFLICT` | https://github.com/icarito/openclaw-xmpp |
| `evd-033` | soilDNRA/openclaw-xmpp: Die README beschreibt nur Direktchats, nennt MUC und OMEMO ausdrücklich als nicht unterstützt und OpenClaw 2026.8.2 als Mindestversion; sie verweist auf ClawHub `openclaw-xmpp@0.1.2-beta.2` und auf die Hauptquelle https://git.sdf.org/erici/openclaw-xmpp. | `DOCUMENTED` | https://github.com/soilDNRA/openclaw-xmpp |
| `evd-034` | soilDNRA/openclaw-xmpp: Code für 1:1 ist vorhanden; MUC- und OMEMO-Zeichenketten kommen nicht vor; die Hauptquelle auf git.sdf.org hat denselben Commit. | `VERIFIED` | https://github.com/soilDNRA/openclaw-xmpp |
| `evd-035` | elmafioso79/xmpp-channel: Die README nennt 1:1- und Gruppenchat sowie OMEMO einschließlich Gruppenchats im älteren Namensraum; `peerDependencies` verlangt `openclaw ^2026.2.2-3`. Offener PR #4 zur Anpassung an OpenClaw 2026.5.2. | `DOCUMENTED` | https://github.com/elmafioso79/xmpp-channel |
| `evd-036` | elmafioso79/xmpp-channel: Code für MUC (`joinMuc`) und für OMEMO bei `groupchat` ist vorhanden; keine Testdateien. | `VERIFIED` | https://github.com/elmafioso79/xmpp-channel |
| `evd-037` | watkins-matt/xmpp-channel: Fork von elmafioso79/xmpp-channel, 28 Commits voraus; die README ist identisch mit dem Ursprung; `peerDependencies` verlangt `openclaw >=2026.8.2`. | `DOCUMENTED` | https://github.com/watkins-matt/xmpp-channel |
| `evd-038` | watkins-matt/xmpp-channel: Code für MUC und OMEMO ist vorhanden. | `VERIFIED` | https://github.com/watkins-matt/xmpp-channel |
| `evd-039` | Programmatore-Web/openclaw-xmpp-channel: Fork von watkins-matt/xmpp-channel; die README nennt 1:1 und fest eingestellte MUC-Räume, schließt Ende-zu-Ende-Verschlüsselung aus und nennt OpenClaw 2026.8.2 oder neuer. | `DOCUMENTED` | https://github.com/Programmatore-Web/openclaw-xmpp-channel |
| `evd-040` | Programmatore-Web/openclaw-xmpp-channel: Code für MUC ist vorhanden; OMEMO-Zeichenketten kommen nicht vor; verschlüsselte Nachrichten werden verworfen. | `VERIFIED` | https://github.com/Programmatore-Web/openclaw-xmpp-channel |
| `evd-041` | Programmatore-Web/openclaw-xmpp-channel: Das übernommene CHANGELOG beschreibt OMEMO-Funktionen, die im Code und in der README nicht mehr vorkommen. | `CONFLICT` | https://github.com/Programmatore-Web/openclaw-xmpp-channel |
| `evd-042` | MrCPA/oc-xmpp: Die README nennt Direktnachrichten und Räume, OMEMO nur für Direktnachrichten und Live-Tests als noch offen; `peerDependencies` verlangt `openclaw "*"`. | `DOCUMENTED` | https://github.com/MrCPA/oc-xmpp |
| `evd-043` | MrCPA/oc-xmpp: Code für MUC und für OMEMO in `urn:xmpp:omemo:2` ist vorhanden. | `VERIFIED` | https://github.com/MrCPA/oc-xmpp |
| `evd-044` | chitozzz/xmpp-adapter-openclaw: Die README nennt 1:1 und MUC als Ziel und das Projekt als in Planung; `peerDependencies` verlangt `openclaw >=2026.6.9`; OMEMO wird nicht genannt. | `DOCUMENTED` | https://github.com/chitozzz/xmpp-adapter-openclaw |
| `evd-045` | chitozzz/xmpp-adapter-openclaw: Code für 1:1 und MUC (`joinMuc`) ist vorhanden; OMEMO-Zeichenketten kommen nicht vor. | `VERIFIED` | https://github.com/chitozzz/xmpp-adapter-openclaw |
| `evd-046` | weijia/xmpp-connector: Die README nennt Senden und Empfangen von Nachrichten, keine OpenClaw-Version, weder MUC noch OMEMO; auf npm ist `openclaw-xmpp-connector` 0.3.0 veröffentlicht. | `DOCUMENTED` | https://github.com/weijia/xmpp-connector |
| `evd-047` | weijia/xmpp-connector: Code für 1:1 ist vorhanden; MUC- und OMEMO-Zeichenketten kommen nicht vor; keine Testdateien. | `VERIFIED` | https://github.com/weijia/xmpp-connector |
| `evd-048` | processone/openclaw, Zweig xmpp-support: Die README der Erweiterung nennt 1:1 und MUC; OMEMO wird nicht genannt; der Zweig ist Grundlage des geschlossenen PR #9741 und hängt von `openclaw workspace:*` ab. | `DOCUMENTED` | https://github.com/processone/openclaw/tree/xmpp-support/extensions/xmpp |
| `evd-049` | processone/openclaw, Zweig xmpp-support: Code für 1:1 und MUC (`joinRoom`) ist vorhanden; OMEMO-Zeichenketten kommen nicht vor. | `VERIFIED` | https://github.com/processone/openclaw/tree/xmpp-support/extensions/xmpp |
| `evd-050` | rsaisankalp/clawdbotElyments: Die README beschreibt eine Anbindung von Clawdbot an die XMPP-basierte Plattform Elyments mit Direktnachrichten; `peerDependencies` verlangt `clawdbot >=2026.0.0`; auf npm ist `clawdbot-elyments` 1.0.0 veröffentlicht. | `DOCUMENTED` | https://github.com/rsaisankalp/clawdbotElyments |
| `evd-051` | rsaisankalp/clawdbotElyments: Code verarbeitet den Nachrichtentyp `groupchat`, enthält aber keinen Raumbeitritt; OMEMO-Zeichenketten kommen nicht vor; keine Testdateien. | `VERIFIED` | https://github.com/rsaisankalp/clawdbotElyments |
| `evd-052` | Ob eines der untersuchten Projekte Direktnachrichten, OMEMO-Verschlüsselung und Gruppenchats über MUC tatsächlich funktionsfähig bereitstellt, ist unbekannt. | `UNKNOWN` | – |
| `evd-053` | Ob die untersuchten Projekte unter OpenClaw 2026.7.1-2 oder 2026.9.4 laden und laufen, ist unbekannt; es liegen nur deklarierte Versionsangaben vor. | `UNKNOWN` | – |
| `evd-054` | Ob es XMPP-Anbindungen für OpenClaw außerhalb von GitHub und npm gibt, etwa auf ClawHub, GitLab oder Codeberg, ist unbekannt. | `UNKNOWN` | – |

## 6. Einzelbefunde

Für jeden relevanten Befund ist ein eigener Abschnitt anzulegen.

### evd-001

Aussage:
Zurzeit sind zwei OpenClaw-Installationen mit den Versionen 2026.9.4 und 2026.7.1-2 aktiv.

Nachweisstatus:
`USER_PROVIDED`

Quelle:

- Typ: `USER_STATEMENT`
- Fundstelle: `idea.md` Abschnitt 2, Zeile 31
- Version oder Commit: `idea.md` Commit 4e46961
- Abruf- oder Prüfdatum: 2026-09-14

Prüfung:

- durchgeführte Prüfung: keine; Aussage übernommen
- Ergebnis: –
- nicht durchgeführte Prüfung: Zuordnung zu konkreten Rechnern nicht geprüft (siehe evd-006)
- Einschränkung der Aussagekraft: Aussage des Ideengebers, nicht durch skizzwerk bestätigt

Bezug zur Projektidee:

- Abschnitt oder Originalaussage: `idea.md` Abschnitt 2, Abschnitt 6
- Bedeutung für die Bestandsuntersuchung: bestimmt die Versionen, deren Bestand untersucht wird

Folgerung:
Die beiden Versionen bilden den Bezugspunkt für die Versionsuntersuchung.

### evd-002

Aussage:
Ein eigener XMPP-Server ist vorhanden.

Nachweisstatus:
`USER_PROVIDED`

Quelle:

- Typ: `USER_STATEMENT`
- Fundstelle: `idea.md` Abschnitt 2, Zeile 30
- Version oder Commit: `idea.md` Commit 4e46961
- Abruf- oder Prüfdatum: 2026-09-14

Prüfung:

- durchgeführte Prüfung: keine; Aussage übernommen
- Ergebnis: –
- nicht durchgeführte Prüfung: Server nicht untersucht (siehe evd-008)
- Einschränkung der Aussagekraft: Aussage des Ideengebers, nicht durch skizzwerk bestätigt

Bezug zur Projektidee:

- Abschnitt oder Originalaussage: `idea.md` Abschnitt 2, Abschnitt 6
- Bedeutung für die Bestandsuntersuchung: beteiligtes System

Folgerung:
Zum Server liegen keine weiteren Angaben vor.

### evd-003

Aussage:
Bestehende Plugins konnten zum Teil nicht installiert werden oder erfüllten nicht die Anforderungen an Sicherheit (OMEMO) oder Kommunikation (Gruppenchats/MUC).

Nachweisstatus:
`USER_PROVIDED`

Quelle:

- Typ: `USER_STATEMENT`
- Fundstelle: `idea.md` Abschnitt 2, Zeilen 32–34
- Version oder Commit: `idea.md` Commit 4e46961
- Abruf- oder Prüfdatum: 2026-09-14

Prüfung:

- durchgeführte Prüfung: keine; Aussage übernommen
- Ergebnis: –
- nicht durchgeführte Prüfung: Welche Plugins gemeint sind, nicht ermittelbar (siehe evd-007)
- Einschränkung der Aussagekraft: Aussage des Ideengebers, nicht durch skizzwerk bestätigt

Bezug zur Projektidee:

- Abschnitt oder Originalaussage: `idea.md` Abschnitt 2, Abschnitt 11
- Bedeutung für die Bestandsuntersuchung: dokumentierter bisheriger Versuch

Folgerung:
Die erprobten Plugins sind nicht benannt; ein Abgleich mit den Projekten in evd-022 bis evd-051 ist nicht möglich.

### evd-004

Aussage:
Auf dem Rechner srv001 ist OpenClaw 2026.9.4 (Commit 3a9d69d) als globales npm-Paket installiert; der Dienst `openclaw.service` ist aktiv.

Nachweisstatus:
`VERIFIED`

Quelle:

- Typ: `MANUAL_TEST`
- Fundstelle: Befehle `openclaw --version`, `npm ls -g --depth=0`, `systemctl is-active openclaw` auf srv001
- Version oder Commit: openclaw@2026.9.4
- Abruf- oder Prüfdatum: 2026-09-14

Prüfung:

- durchgeführte Prüfung: Befehlsausgaben gelesen
- Ergebnis: `OpenClaw 2026.9.4 (3a9d69d)`, `openclaw@2026.9.4`, `active`
- nicht durchgeführte Prüfung: Konfiguration und installierte Plugins nicht gelesen (Zugriff verweigert)
- Einschränkung der Aussagekraft: belegt nur Version und Dienststatus, keine Kanal- oder Plugin-Konfiguration

Bezug zur Projektidee:

- Abschnitt oder Originalaussage: `idea.md` Abschnitt 2, Abschnitt 6
- Bedeutung für die Bestandsuntersuchung: vorhandene Installation einer der genannten Versionen

Folgerung:
Eine Installation der Version 2026.9.4 ist auf srv001 vorhanden.

### evd-005

Aussage:
Die lokale Installationsanleitung beschreibt OpenClaw mit dem mitgelieferten WebChat und Authelia sowie ein über ClawHub installiertes Provider-Plugin; XMPP wird dort nicht erwähnt.

Nachweisstatus:
`DOCUMENTED`

Quelle:

- Typ: `PROJECT_DOCUMENTATION`
- Fundstelle: `/srv/aixlab/docs/anleitungen/dev-server/09-00-dev-server-install-openclaw.md` Zeilen 3, 32; `/srv/aixlab/docs/sysdoc/srv001/anleitungen/eurouter-provider-openclaw.md` Zeile 14
- Version oder Commit: kein Git-Stand; Dateistand 2026-08-30 bzw. 2026-08-12, SHA-256-Präfix e559ec29d7d8b2aa bzw. 5a93f1232b7ebc32
- Abruf- oder Prüfdatum: 2026-09-14

Prüfung:

- durchgeführte Prüfung: Dateien gelesen, Suche nach xmpp, jabber, prosody, ejabberd, omemo
- Ergebnis: keine XMPP-Treffer außerhalb von `archiv/`
- nicht durchgeführte Prüfung: Abgleich mit der tatsächlichen Konfiguration nicht möglich
- Einschränkung der Aussagekraft: Dokumentation kann vom Betriebsstand abweichen

Bezug zur Projektidee:

- Abschnitt oder Originalaussage: `idea.md` Abschnitt 2, Abschnitt 6
- Bedeutung für die Bestandsuntersuchung: dokumentierter Bestand der vorhandenen Installation

Folgerung:
Die vorhandene Dokumentation enthält keine Angaben zu einer XMPP-Anbindung.

### evd-006

Aussage:
Ob srv001 eine der beiden vom Ideengeber genannten Installationen ist und wo die Installation mit Version 2026.7.1-2 läuft, ist unbekannt.

Nachweisstatus:
`UNKNOWN`

Quelle:

- Typ: `NONE`
- Fundstelle: –
- Version oder Commit: –
- Abruf- oder Prüfdatum: 2026-09-14

Prüfung:

- durchgeführte Prüfung: lokale Dokumentation und Rechner srv001 durchsucht
- Ergebnis: keine Angabe zur zweiten Installation gefunden
- nicht durchgeführte Prüfung: keine Prüfung weiterer Rechner
- Einschränkung der Aussagekraft: Angabe fehlt in allen zugänglichen Quellen

Bezug zur Projektidee:

- Abschnitt oder Originalaussage: `idea.md` Abschnitt 2, Abschnitt 11
- Bedeutung für die Bestandsuntersuchung: Umfang der vorhandenen Installationen

Folgerung:
Die Installation mit 2026.7.1-2 ist nicht untersucht.

### evd-007

Aussage:
Welche Plugins in den vorhandenen Installationen installiert oder erprobt wurden und woran ihre Installation scheiterte, ist unbekannt.

Nachweisstatus:
`UNKNOWN`

Quelle:

- Typ: `NONE`
- Fundstelle: `/var/lib/openclaw/.openclaw` auf srv001: Zugriff verweigert
- Version oder Commit: –
- Abruf- oder Prüfdatum: 2026-09-14

Prüfung:

- durchgeführte Prüfung: `ls /var/lib/openclaw/.openclaw`
- Ergebnis: `Permission denied`
- nicht durchgeführte Prüfung: `openclaw plugins list` nicht ausgeführt, um nichts zu verändern
- Einschränkung der Aussagekraft: keine zugängliche Quelle

Bezug zur Projektidee:

- Abschnitt oder Originalaussage: `idea.md` Abschnitt 2, Abschnitt 11
- Bedeutung für die Bestandsuntersuchung: dokumentierter bisheriger Versuch

Folgerung:
Die bisherigen Versuche sind nicht nachvollziehbar dokumentiert.

### evd-008

Aussage:
Software, Standort und unterstützte XMPP-Erweiterungen des eigenen XMPP-Servers sind unbekannt.

Nachweisstatus:
`UNKNOWN`

Quelle:

- Typ: `NONE`
- Fundstelle: –
- Version oder Commit: –
- Abruf- oder Prüfdatum: 2026-09-14

Prüfung:

- durchgeführte Prüfung: lokale Dokumentation durchsucht; auf srv001 `systemctl list-units --type=service` nach prosody, ejabberd, xmpp gefiltert
- Ergebnis: keine Dokumentation, kein Dienst mit diesen Namen auf srv001
- nicht durchgeführte Prüfung: kein Zugriff auf andere Rechner; Server nicht angefragt
- Einschränkung der Aussagekraft: Das Fehlen eines Dienstes auf srv001 sagt nichts über den Server an anderer Stelle

Bezug zur Projektidee:

- Abschnitt oder Originalaussage: `idea.md` Abschnitt 2, Abschnitt 11
- Bedeutung für die Bestandsuntersuchung: beteiligtes System

Folgerung:
Der XMPP-Server ist nicht untersucht.

### evd-009

Aussage:
Die Versionen 2026.7.1-2 (veröffentlicht 2026-07-18T03:53:48Z, Tag-Commit 0790d9f593ad) und 2026.9.4 (veröffentlicht 2026-09-11T02:44:59Z, Tag-Commit 3a9d69db306c) sind im npm-Register veröffentlicht; `latest` ist 2026.9.4, `extended-stable` ist 2026.6.35.

Nachweisstatus:
`VERIFIED`

Quelle:

- Typ: `PRIMARY_DOCUMENTATION`
- Fundstelle: https://registry.npmjs.org/openclaw (`time`, `dist-tags`); GitHub-Tags `v2026.7.1-2`, `v2026.9.4` in `openclaw/openclaw`
- Version oder Commit: Registerstand 2026-09-14
- Abruf- oder Prüfdatum: 2026-09-14

Prüfung:

- durchgeführte Prüfung: Registerdaten mit `jq` ausgewertet; Tags über GitHub-API auf Commits aufgelöst
- Ergebnis: wie in der Aussage
- nicht durchgeführte Prüfung: Paketinhalt von 2026.7.1-2 nicht geladen
- Einschränkung der Aussagekraft: Register ist Primärquelle für Veröffentlichungen

Bezug zur Projektidee:

- Abschnitt oder Originalaussage: `idea.md` Abschnitt 1 („aktuelle OpenClaw-Versionen“), Abschnitt 10
- Bedeutung für die Bestandsuntersuchung: Einordnung der genannten Versionen

Folgerung:
Beide genannten Versionen existieren; 2026.9.4 ist die zum Untersuchungszeitpunkt neueste stabile Version.

### evd-010

Aussage:
Zwischen 2026.7.1-2 und 2026.9.4 wurden 17 Versionen veröffentlicht: 2026.8.1, 2026.8.2, 2026.9.1, 2026.9.2, 2026.9.3, neun Beta-Versionen und 2026.6.33 bis 2026.6.35.

Nachweisstatus:
`VERIFIED`

Quelle:

- Typ: `PRIMARY_DOCUMENTATION`
- Fundstelle: https://registry.npmjs.org/openclaw (`time`)
- Version oder Commit: Registerstand 2026-09-14
- Abruf- oder Prüfdatum: 2026-09-14

Prüfung:

- durchgeführte Prüfung: Veröffentlichungszeiten mit `jq` gefiltert
- Ergebnis: 17 Einträge
- nicht durchgeführte Prüfung: –
- Einschränkung der Aussagekraft: Zählung nach Veröffentlichungsdatum, nicht nach Versionsnummer

Bezug zur Projektidee:

- Abschnitt oder Originalaussage: `idea.md` Abschnitt 1 („neue OpenClaw-Versionen“), Abschnitt 11
- Bedeutung für die Bestandsuntersuchung: Häufigkeit neuer Versionen

Folgerung:
Im Zeitraum von knapp acht Wochen erschienen fünf stabile Versionen.

### evd-011

Aussage:
Die Exportpfade `./plugin-sdk` und `./extension-api` sind in 2026.7.1-2 und 2026.7.2-beta.3 vorhanden, ab 2026.7.2-beta.4 und in 2026.9.4 nicht mehr.

Nachweisstatus:
`VERIFIED`

Quelle:

- Typ: `PRIMARY_DOCUMENTATION`
- Fundstelle: https://registry.npmjs.org/openclaw (`versions[*].exports`)
- Version oder Commit: Registerstand 2026-09-14
- Abruf- oder Prüfdatum: 2026-09-14

Prüfung:

- durchgeführte Prüfung: `exports` der Versionen mit `jq` verglichen
- Ergebnis: wie in der Aussage
- nicht durchgeführte Prüfung: Paketinhalte nicht verglichen
- Einschränkung der Aussagekraft: belegt die Paketmetadaten, nicht das Laufzeitverhalten

Bezug zur Projektidee:

- Abschnitt oder Originalaussage: `idea.md` Abschnitt 1, Abschnitt 11
- Bedeutung für die Bestandsuntersuchung: Änderungen an der Plugin-Schnittstelle

Folgerung:
Die Plugin-Schnittstelle unterscheidet sich zwischen den beiden genannten Versionen in ihren Exportpfaden.

### evd-012

Aussage:
Das Paket 2026.9.4 exportiert Unterpfade `openclaw/plugin-sdk/*`, darunter `channel-core`, `channel-contract`, `channel-entry-contract` und `plugin-entry`; `channel-core.d.ts` exportiert u. a. `ChannelPlugin` und `defineChannelPluginEntry`.

Nachweisstatus:
`VERIFIED`

Quelle:

- Typ: `SOURCE_CODE`
- Fundstelle: `/usr/lib/node_modules/openclaw/package.json` Zeilen 1068, 1072, 1076, 1396; `dist/plugin-sdk/channel-core.d.ts` Zeile 10
- Version oder Commit: openclaw@2026.9.4 (3a9d69d)
- Abruf- oder Prüfdatum: 2026-09-14

Prüfung:

- durchgeführte Prüfung: Dateien im installierten Paket gelesen
- Ergebnis: wie in der Aussage
- nicht durchgeführte Prüfung: Schnittstelle nicht benutzt, kein Plugin gebaut
- Einschränkung der Aussagekraft: belegt vorhandene Exporte und Typen, nicht deren Verhalten

Bezug zur Projektidee:

- Abschnitt oder Originalaussage: `idea.md` Abschnitt 1, Abschnitt 5
- Bedeutung für die Bestandsuntersuchung: vorhandene Schnittstelle für Kanal-Plugins

Folgerung:
Für Kanal-Plugins ist in 2026.9.4 eine eigene SDK-Schnittstelle vorhanden.

### evd-013

Aussage:
Laut Dokumentation braucht jedes native Plugin eine `openclaw.plugin.json`; die Felder `openclaw.compat.pluginApi` und `openclaw.install.minHostVersion` werden bei npm-Installationen zur Versionsauswahl ausgewertet.

Nachweisstatus:
`DOCUMENTED`

Quelle:

- Typ: `PRIMARY_DOCUMENTATION`
- Fundstelle: `docs/plugins/manifest.md` Zeile 20; `docs/plugins/building-plugins.md` Zeilen 79–86; `docs/tools/plugin.md` Zeilen 141–147
- Version oder Commit: openclaw@2026.9.4
- Abruf- oder Prüfdatum: 2026-09-14

Prüfung:

- durchgeführte Prüfung: Dokumentation gelesen
- Ergebnis: wie in der Aussage
- nicht durchgeführte Prüfung: Installationsverhalten nicht getestet
- Einschränkung der Aussagekraft: Dokumentationsaussage

Bezug zur Projektidee:

- Abschnitt oder Originalaussage: `idea.md` Abschnitt 1, Abschnitt 5
- Bedeutung für die Bestandsuntersuchung: dokumentierter Plugin- und Kompatibilitätsmechanismus

Folgerung:
Die Kompatibilitätsangaben eines Plugins werden laut Dokumentation bei der Installation berücksichtigt.

### evd-014

Aussage:
Laut Dokumentation sind alle Plugin-APIs experimentell und können sich zwischen OpenClaw-Versionen ändern; Plugin-Autoren sollen die Version festlegen und jede als kompatibel angegebene Version testen.

Nachweisstatus:
`DOCUMENTED`

Quelle:

- Typ: `PRIMARY_DOCUMENTATION`
- Fundstelle: `docs/plugins/sdk-overview.md` Zeilen 25–36
- Version oder Commit: openclaw@2026.9.4
- Abruf- oder Prüfdatum: 2026-09-14

Prüfung:

- durchgeführte Prüfung: Dokumentation gelesen (durch skizzwerk nachgelesen)
- Ergebnis: wörtlich: „These contracts can change between OpenClaw releases.“
- nicht durchgeführte Prüfung: –
- Einschränkung der Aussagekraft: Dokumentationsaussage

Bezug zur Projektidee:

- Abschnitt oder Originalaussage: `idea.md` Abschnitt 1 (Verfahren für neue Versionen), Abschnitt 11
- Bedeutung für die Bestandsuntersuchung: dokumentierte Stabilität der Schnittstelle

Folgerung:
Die Hersteller-Dokumentation sagt keine stabile Plugin-Schnittstelle zu.

### evd-015

Aussage:
Laut Dokumentation sind `openclaw/plugin-sdk`, `openclaw/plugin-sdk/compat` und `openclaw/extension-api` entfernt; Plugins, die sie importieren, laden nicht mehr. Alte Verträge laufen befristet über Kompatibilitätsadapter.

Nachweisstatus:
`DOCUMENTED`

Quelle:

- Typ: `PRIMARY_DOCUMENTATION`
- Fundstelle: `docs/plugins/sdk-migration.md` Zeilen 19–22, 37–49; `docs/plugins/compatibility.md` Zeilen 14–33
- Version oder Commit: openclaw@2026.9.4
- Abruf- oder Prüfdatum: 2026-09-14

Prüfung:

- durchgeführte Prüfung: Dokumentation gelesen
- Ergebnis: wie in der Aussage
- nicht durchgeführte Prüfung: `src/plugins/compat/registry.ts` nicht gelesen; Ladeverhalten nicht getestet
- Einschränkung der Aussagekraft: Dokumentationsaussage

Bezug zur Projektidee:

- Abschnitt oder Originalaussage: `idea.md` Abschnitt 1, Abschnitt 11
- Bedeutung für die Bestandsuntersuchung: dokumentierte Folgen von Schnittstellenänderungen

Folgerung:
Die Dokumentation beschreibt Änderungen, die ältere Plugins am Laden hindern.

### evd-016

Aussage:
Das CHANGELOG nennt für 2026.9.3 mehrere als „Breaking“ gekennzeichnete Änderungen am Plugin-SDK und für 2026.8.1 bis 2026.9.4 Abkündigungen von SDK-Pfaden mit Entfernungsterminen 2026-09-01 und 2026-09-08.

Nachweisstatus:
`DOCUMENTED`

Quelle:

- Typ: `PROJECT_DOCUMENTATION`
- Fundstelle: `CHANGELOG.md` am Tag `v2026.9.4` in `openclaw/openclaw`, Abschnitte 2026.9.3 (u. a. „Breaking — SDK aliases“), 2026.8.2 und 2026.8.1 („Upcoming deprecations (2026-09-01)“)
- Version oder Commit: Commit 3a9d69db306c
- Abruf- oder Prüfdatum: 2026-09-14

Prüfung:

- durchgeführte Prüfung: Einträge mit Bezug zu Plugin-SDK und Kanälen durchsucht
- Ergebnis: 15 zitierte Einträge, davon 4 „Breaking“ in 2026.9.3
- nicht durchgeführte Prüfung: CHANGELOG (rund 24 000 Zeilen) nicht vollständig gelesen; Abschnitte 2026.7.1-1 und 2026.7.1-2 fehlen dort
- Einschränkung der Aussagekraft: Dokumentationsaussage; Vollständigkeit nicht geprüft

Bezug zur Projektidee:

- Abschnitt oder Originalaussage: `idea.md` Abschnitt 1, Abschnitt 11
- Bedeutung für die Bestandsuntersuchung: Häufigkeit von Schnittstellenänderungen

Folgerung:
Im untersuchten Zeitraum sind Schnittstellenänderungen dokumentiert.

### evd-017

Aussage:
Zwischen 2026.7.1-2 und 2026.9.4 hat sich die Plugin-Schnittstelle so geändert, dass Plugins, die die entfernten Pfade nutzen, unter 2026.9.4 laut Dokumentation nicht laden.

Nachweisstatus:
`INFERRED`

Quelle:

- Typ: `ANALYSIS`
- Fundstelle: abgeleitet aus evd-011, evd-015, evd-016
- Version oder Commit: –
- Abruf- oder Prüfdatum: 2026-09-14

Prüfung:

- durchgeführte Prüfung: Ableitung aus den genannten Befunden
- Ergebnis: –
- nicht durchgeführte Prüfung: nicht mit einem Plugin praktisch geprüft
- Einschränkung der Aussagekraft: Ableitung aus Registerdaten und Dokumentation

Bezug zur Projektidee:

- Abschnitt oder Originalaussage: `idea.md` Abschnitt 1, Abschnitt 10 („aktuelle OpenClaw-Versionen“), Abschnitt 11
- Bedeutung für die Bestandsuntersuchung: Bestand zu Änderungen zwischen den genannten Versionen

Folgerung:
Die beiden genannten Versionen stellen nicht dieselbe Plugin-Schnittstelle bereit.

### evd-018

Aussage:
Das Paket 2026.9.4 enthält unter `dist/extensions/` 60 Erweiterungen, darunter keine für XMPP; die Suche nach `xmpp`, `jabber`, `omemo`, `muc` trifft nur Fremdbibliotheken (URL-Schema, MIME-Typ).

Nachweisstatus:
`VERIFIED`

Quelle:

- Typ: `SOURCE_CODE`
- Fundstelle: `/usr/lib/node_modules/openclaw/dist/extensions/`; Treffer u. a. `dist/worker/worker.mjs` Zeile 31129
- Version oder Commit: openclaw@2026.9.4
- Abruf- oder Prüfdatum: 2026-09-14

Prüfung:

- durchgeführte Prüfung: Verzeichnis gelistet (durch skizzwerk nachgezählt), Volltextsuche mit Wortgrenzen
- Ergebnis: 60 Ordner, 0 mit xmpp im Namen
- nicht durchgeführte Prüfung: –
- Einschränkung der Aussagekraft: gilt nur für das installierte Paket, nicht für nachinstallierbare Plugins

Bezug zur Projektidee:

- Abschnitt oder Originalaussage: `idea.md` Abschnitt 1, Abschnitt 5
- Bedeutung für die Bestandsuntersuchung: vorhandene XMPP-Unterstützung im Lieferumfang

Folgerung:
OpenClaw 2026.9.4 liefert keinen XMPP-Kanal mit.

### evd-019

Aussage:
Die Kanalübersicht der Dokumentation nennt mitgelieferte und offizielle Kanal-Plugins, aber kein XMPP- oder Jabber-Plugin.

Nachweisstatus:
`DOCUMENTED`

Quelle:

- Typ: `PRIMARY_DOCUMENTATION`
- Fundstelle: `docs/channels/index.md` Zeilen 38–69
- Version oder Commit: openclaw@2026.9.4
- Abruf- oder Prüfdatum: 2026-09-14

Prüfung:

- durchgeführte Prüfung: Datei gelesen, nach xmpp und jabber gesucht
- Ergebnis: keine Treffer
- nicht durchgeführte Prüfung: Website docs.openclaw.ai nicht verglichen
- Einschränkung der Aussagekraft: Dokumentationsaussage

Bezug zur Projektidee:

- Abschnitt oder Originalaussage: `idea.md` Abschnitt 1, Abschnitt 5
- Bedeutung für die Bestandsuntersuchung: offiziell dokumentierte Kanäle

Folgerung:
Ein offizielles XMPP-Plugin ist nicht dokumentiert.

### evd-020

Aussage:
Im Repository `openclaw/openclaw` enthält `extensions/` auf `main` kein XMPP-Verzeichnis; die Pull Requests #9741, #20998 und #21015 für XMPP wurden ohne Merge geschlossen; Issue #29046 „[Feature]: XMPP support“ ist mit `not_planned` geschlossen.

Nachweisstatus:
`VERIFIED`

Quelle:

- Typ: `ISSUE_OR_PR`
- Fundstelle: https://github.com/openclaw/openclaw/pull/9741, /pull/20998, /pull/21015, /issues/29046; Baum `extensions/` auf `main`
- Version oder Commit: `main` Commit df663a946582
- Abruf- oder Prüfdatum: 2026-09-14

Prüfung:

- durchgeführte Prüfung: GitHub-API: Status, `merged`, `closed_at`, `state_reason`; Verzeichnisbaum gelistet (durch skizzwerk nachgeprüft)
- Ergebnis: 167 Einträge, 0 mit xmpp/jabber; PRs geschlossen am 2026-02-06, 2026-02-20, 2026-02-28, jeweils `merged=false`
- nicht durchgeführte Prüfung: Begründungen in den Diskussionen nicht ausgewertet
- Einschränkung der Aussagekraft: belegt nur den Status, nicht die Gründe

Bezug zur Projektidee:

- Abschnitt oder Originalaussage: `idea.md` Abschnitt 1 („Vorhandene GitHub-Projekte“), Abschnitt 5
- Bedeutung für die Bestandsuntersuchung: vorhandene Upstream-Arbeiten zu XMPP

Folgerung:
Es gab Beiträge für XMPP im Hauptprojekt, die nicht übernommen wurden.

### evd-021

Aussage:
OpenClaw hieß laut Projektdokumentation zuvor Warelay, Clawdbot und Moltbot; seit dem 30. Januar 2026 heißt es OpenClaw.

Nachweisstatus:
`DOCUMENTED`

Quelle:

- Typ: `PROJECT_DOCUMENTATION`
- Fundstelle: `docs/start/lore.md` Zeilen 14–24; `VISION.md` Zeile 13 in `openclaw/openclaw`
- Version oder Commit: openclaw@2026.9.4
- Abruf- oder Prüfdatum: 2026-09-14

Prüfung:

- durchgeführte Prüfung: Datei gelesen (durch skizzwerk nachgelesen); GitHub leitet `clawdbot/clawdbot` und `moltbot/moltbot` auf dasselbe Repository um
- Ergebnis: wie in der Aussage
- nicht durchgeführte Prüfung: –
- Einschränkung der Aussagekraft: Dokumentationsaussage

Bezug zur Projektidee:

- Abschnitt oder Originalaussage: `idea.md` Abschnitt 1 („Vorhandene GitHub-Projekte“)
- Bedeutung für die Bestandsuntersuchung: Suchbegriffe für ältere Projekte

Folgerung:
Ältere Projekte können unter den früheren Namen geführt sein; diese Namen wurden in die Suche aufgenommen.

### evd-022

Aussage:
ksmith211/openclaw-xmpp: Die README beschreibt ein Kanal-Plugin nur für Direktnachrichten; MUC, OMEMO und eine OpenClaw-Version werden nicht genannt. Auf npm ist `@ksmith221/openclaw-xmpp` 0.1.1 veröffentlicht.

Nachweisstatus:
`DOCUMENTED`

Quelle:

- Typ: `PROJECT_DOCUMENTATION`
- Fundstelle: `README.md` Zeilen 1–3, 14; `package.json`; npm `@ksmith221/openclaw-xmpp`
- Version oder Commit: Commit ad1ad44777fc, 2026-02-02
- Abruf- oder Prüfdatum: 2026-09-14

Prüfung:

- durchgeführte Prüfung: README und Paketmetadaten gelesen
- Ergebnis: wie in der Aussage
- nicht durchgeführte Prüfung: keine Installation, kein Funktionstest
- Einschränkung der Aussagekraft: Projektangaben, nicht praktisch bestätigt

Bezug zur Projektidee:

- Abschnitt oder Originalaussage: `idea.md` Abschnitt 1 (Direktnachrichten, OMEMO, MUC, GitHub-Projekte), Abschnitt 7
- Bedeutung für die Bestandsuntersuchung: dokumentierte Funktionen und Versionsangaben eines vorhandenen Projekts

Folgerung:
Die dokumentierten Funktionen sind nicht praktisch geprüft.

### evd-023

Aussage:
ksmith211/openclaw-xmpp: Code für 1:1-Nachrichten ist vorhanden (`type: "chat"`); Zeichenketten zu MUC, groupchat und OMEMO kommen in `src/` nicht vor; keine Testdateien.

Nachweisstatus:
`VERIFIED`

Quelle:

- Typ: `SOURCE_CODE`
- Fundstelle: `src/inbound.ts` Zeile 101, `src/send.ts` Zeile 16; `grep -rniE 'muc|omemo|groupchat' src` = 0 Treffer
- Version oder Commit: Commit ad1ad44777fc
- Abruf- oder Prüfdatum: 2026-09-14

Prüfung:

- durchgeführte Prüfung: Quelltext per `git clone --depth 1` gelesen und nach Namensräumen und Bezeichnern durchsucht
- Ergebnis: wie in der Aussage; Tests: keine
- nicht durchgeführte Prüfung: Code nicht ausgeführt, Tests nicht ausgeführt, kein Build
- Einschränkung der Aussagekraft: belegt nur vorhandenen Code, nicht dessen Funktionsfähigkeit; 0 Treffer belegt nur das Fehlen der gesuchten Zeichenketten

Bezug zur Projektidee:

- Abschnitt oder Originalaussage: `idea.md` Abschnitt 1, Abschnitt 7
- Bedeutung für die Bestandsuntersuchung: im Quelltext vorhandene Implementierungsteile

Folgerung:
Vorhandener Code ist nicht als funktionsfähig nachgewiesen.

### evd-024

Aussage:
toughworm/Openclaw-XMPP-Plugin: Die README nennt 1:1- und Gruppenchat, OMEMO nur für 1:1 im älteren Namensraum `eu.siacs.conversations.axolotl`, verschlüsselten Gruppenchat als offen und keine OpenClaw-Version.

Nachweisstatus:
`DOCUMENTED`

Quelle:

- Typ: `PROJECT_DOCUMENTATION`
- Fundstelle: `README.md` Zeilen 100–102, 133, 137, 214–215
- Version oder Commit: Commit 428886a5fab2, 2026-02-21
- Abruf- oder Prüfdatum: 2026-09-14

Prüfung:

- durchgeführte Prüfung: README und Paketmetadaten gelesen
- Ergebnis: wie in der Aussage
- nicht durchgeführte Prüfung: keine Installation, kein Funktionstest
- Einschränkung der Aussagekraft: Projektangaben, nicht praktisch bestätigt

Bezug zur Projektidee:

- Abschnitt oder Originalaussage: `idea.md` Abschnitt 1 (Direktnachrichten, OMEMO, MUC, GitHub-Projekte), Abschnitt 7
- Bedeutung für die Bestandsuntersuchung: dokumentierte Funktionen und Versionsangaben eines vorhandenen Projekts

Folgerung:
Die dokumentierten Funktionen sind nicht praktisch geprüft.

### evd-025

Aussage:
toughworm/Openclaw-XMPP-Plugin: OMEMO-Code im Namensraum `eu.siacs.conversations.axolotl` ist vorhanden und wird bei `groupchat` übersprungen; Code für einen MUC-Raumbeitritt (`http://jabber.org/protocol/muc`) kommt nicht vor.

Nachweisstatus:
`VERIFIED`

Quelle:

- Typ: `SOURCE_CODE`
- Fundstelle: `src/omemo/OmemoManager.ts` Zeile 11, `src/client.ts` Zeile 187; `grep -rn 'jabber.org/protocol/muc' src` = 0 Treffer
- Version oder Commit: Commit 428886a5fab2
- Abruf- oder Prüfdatum: 2026-09-14

Prüfung:

- durchgeführte Prüfung: Quelltext per `git clone --depth 1` gelesen und nach Namensräumen und Bezeichnern durchsucht
- Ergebnis: wie in der Aussage; Tests: `test/jid-normalization.test.ts`, `test/omemo-lookup.test.ts`
- nicht durchgeführte Prüfung: Code nicht ausgeführt, Tests nicht ausgeführt, kein Build
- Einschränkung der Aussagekraft: belegt nur vorhandenen Code, nicht dessen Funktionsfähigkeit; 0 Treffer belegt nur das Fehlen der gesuchten Zeichenketten

Bezug zur Projektidee:

- Abschnitt oder Originalaussage: `idea.md` Abschnitt 1, Abschnitt 7
- Bedeutung für die Bestandsuntersuchung: im Quelltext vorhandene Implementierungsteile

Folgerung:
Vorhandener Code ist nicht als funktionsfähig nachgewiesen.

### evd-026

Aussage:
toughworm/Openclaw-XMPP-Plugin: Die README nennt Gruppenchat und die Installation über `@openclaw/xmpp`; im Code fehlt ein Raumbeitritt, das Paket `@openclaw/xmpp` gibt es auf npm nicht (HTTP 404), und die in der README genannten Testskripte fehlen im Repository.

Nachweisstatus:
`CONFLICT`

Quelle:

- Typ: `PROJECT_DOCUMENTATION`
- Fundstelle: `README.md` Zeilen 24, 54, 133, 193–196 gegen `src/` und `git ls-files`; https://registry.npmjs.org/@openclaw%2fxmpp
- Version oder Commit: Commit 428886a5fab2
- Abruf- oder Prüfdatum: 2026-09-14

Prüfung:

- durchgeführte Prüfung: Angaben verschiedener Dateien gegenübergestellt
- Ergebnis: widersprechende Angaben
- nicht durchgeführte Prüfung: nicht durch Installation oder Test aufgelöst
- Einschränkung der Aussagekraft: Welche Angabe zutrifft, ist offen

Bezug zur Projektidee:

- Abschnitt oder Originalaussage: `idea.md` Abschnitt 1, Abschnitt 7, Abschnitt 10
- Bedeutung für die Bestandsuntersuchung: Belastbarkeit der Projektangaben

Folgerung:
Die widersprechenden Angaben stehen nebeneinander; keine davon ist bestätigt.

### evd-027

Aussage:
kazakhan/openclaw-xmpp: Die README nennt 1:1 und MUC und „OpenClaw 2026.8.2+“; `XMPPAUDIT.md` führt OMEMO (XEP-0384) als „Not Supported“.

Nachweisstatus:
`DOCUMENTED`

Quelle:

- Typ: `PROJECT_DOCUMENTATION`
- Fundstelle: `README.md` Zeilen 3, 22, 94–97; `XMPPAUDIT.md` Zeile 322
- Version oder Commit: Commit 4fb1e113150e, 2026-09-14
- Abruf- oder Prüfdatum: 2026-09-14

Prüfung:

- durchgeführte Prüfung: README und Paketmetadaten gelesen
- Ergebnis: wie in der Aussage
- nicht durchgeführte Prüfung: keine Installation, kein Funktionstest
- Einschränkung der Aussagekraft: Projektangaben, nicht praktisch bestätigt

Bezug zur Projektidee:

- Abschnitt oder Originalaussage: `idea.md` Abschnitt 1 (Direktnachrichten, OMEMO, MUC, GitHub-Projekte), Abschnitt 7
- Bedeutung für die Bestandsuntersuchung: dokumentierte Funktionen und Versionsangaben eines vorhandenen Projekts

Folgerung:
Die dokumentierten Funktionen sind nicht praktisch geprüft.

### evd-028

Aussage:
kazakhan/openclaw-xmpp: Code für MUC (`muc`-Namensraum, `joinRoom`) und 1:1 ist vorhanden; OMEMO-Zeichenketten kommen nicht vor.

Nachweisstatus:
`VERIFIED`

Quelle:

- Typ: `SOURCE_CODE`
- Fundstelle: `src/startXMPP.ts` Zeilen 513, 761; `index.ts` Zeile 35; `src/commands.ts` Zeile 231
- Version oder Commit: Commit 4fb1e113150e
- Abruf- oder Prüfdatum: 2026-09-14

Prüfung:

- durchgeführte Prüfung: Quelltext per `git clone --depth 1` gelesen und nach Namensräumen und Bezeichnern durchsucht
- Ergebnis: wie in der Aussage; Tests: `tests/` mit 33 Dateien
- nicht durchgeführte Prüfung: Code nicht ausgeführt, Tests nicht ausgeführt, kein Build
- Einschränkung der Aussagekraft: belegt nur vorhandenen Code, nicht dessen Funktionsfähigkeit; 0 Treffer belegt nur das Fehlen der gesuchten Zeichenketten

Bezug zur Projektidee:

- Abschnitt oder Originalaussage: `idea.md` Abschnitt 1, Abschnitt 7
- Bedeutung für die Bestandsuntersuchung: im Quelltext vorhandene Implementierungsteile

Folgerung:
Vorhandener Code ist nicht als funktionsfähig nachgewiesen.

### evd-029

Aussage:
kazakhan/openclaw-xmpp: Die README nennt als Mindestversion OpenClaw 2026.8.2, `package.json` gibt `compat.pluginApi ">=2026.6.1"` und `minGatewayVersion "2026.6.1"` an.

Nachweisstatus:
`CONFLICT`

Quelle:

- Typ: `PROJECT_DOCUMENTATION`
- Fundstelle: `README.md` Zeile 22 gegen `package.json` Zeilen 20–24
- Version oder Commit: Commit 4fb1e113150e
- Abruf- oder Prüfdatum: 2026-09-14

Prüfung:

- durchgeführte Prüfung: Angaben verschiedener Dateien gegenübergestellt
- Ergebnis: widersprechende Angaben
- nicht durchgeführte Prüfung: nicht durch Installation oder Test aufgelöst
- Einschränkung der Aussagekraft: Welche Angabe zutrifft, ist offen

Bezug zur Projektidee:

- Abschnitt oder Originalaussage: `idea.md` Abschnitt 1, Abschnitt 7, Abschnitt 10
- Bedeutung für die Bestandsuntersuchung: Belastbarkeit der Projektangaben

Folgerung:
Die widersprechenden Angaben stehen nebeneinander; keine davon ist bestätigt.

### evd-030

Aussage:
icarito/openclaw-xmpp: Die Paketbeschreibung nennt 1:1-Chat, MUC-Räume und Ad-hoc-Befehle; `compat.pluginApi` ist `>=2026.7.1`; die README sagt, der Produktivbetrieb lade einen separat abgeglichenen Verzeichnisbaum.

Nachweisstatus:
`DOCUMENTED`

Quelle:

- Typ: `PROJECT_DOCUMENTATION`
- Fundstelle: `package.json` Zeilen 80, 85; `README.md` Zeilen 9–11
- Version oder Commit: Commit 820213a98cb1, 2026-07-26
- Abruf- oder Prüfdatum: 2026-09-14

Prüfung:

- durchgeführte Prüfung: README und Paketmetadaten gelesen
- Ergebnis: wie in der Aussage
- nicht durchgeführte Prüfung: keine Installation, kein Funktionstest
- Einschränkung der Aussagekraft: Projektangaben, nicht praktisch bestätigt

Bezug zur Projektidee:

- Abschnitt oder Originalaussage: `idea.md` Abschnitt 1 (Direktnachrichten, OMEMO, MUC, GitHub-Projekte), Abschnitt 7
- Bedeutung für die Bestandsuntersuchung: dokumentierte Funktionen und Versionsangaben eines vorhandenen Projekts

Folgerung:
Die dokumentierten Funktionen sind nicht praktisch geprüft.

### evd-031

Aussage:
icarito/openclaw-xmpp: Code für MUC, für OMEMO im älteren Namensraum und in `urn:xmpp:omemo:2` sowie ein Python-Hilfsprogramm `src/omemo/sidecar.py` sind vorhanden.

Nachweisstatus:
`VERIFIED`

Quelle:

- Typ: `SOURCE_CODE`
- Fundstelle: `src/client.ts` Zeilen 121, 134; `src/omemo/types.ts` Zeile 13; `src/omemo/omemo2.ts` Zeile 12; `src/send.ts` Zeile 356
- Version oder Commit: Commit 820213a98cb1
- Abruf- oder Prüfdatum: 2026-09-14

Prüfung:

- durchgeführte Prüfung: Quelltext per `git clone --depth 1` gelesen und nach Namensräumen und Bezeichnern durchsucht
- Ergebnis: wie in der Aussage; Tests: `src/tests/` mit 6 Dateien, u. a. `omemo.test.ts`
- nicht durchgeführte Prüfung: Code nicht ausgeführt, Tests nicht ausgeführt, kein Build
- Einschränkung der Aussagekraft: belegt nur vorhandenen Code, nicht dessen Funktionsfähigkeit; 0 Treffer belegt nur das Fehlen der gesuchten Zeichenketten

Bezug zur Projektidee:

- Abschnitt oder Originalaussage: `idea.md` Abschnitt 1, Abschnitt 7
- Bedeutung für die Bestandsuntersuchung: im Quelltext vorhandene Implementierungsteile

Folgerung:
Vorhandener Code ist nicht als funktionsfähig nachgewiesen.

### evd-032

Aussage:
icarito/openclaw-xmpp: `AGENTS.md` nennt OpenClaw 2026.6.9, `package.json` gibt `compat.pluginApi ">=2026.7.1"` an.

Nachweisstatus:
`CONFLICT`

Quelle:

- Typ: `PROJECT_DOCUMENTATION`
- Fundstelle: `AGENTS.md` Zeile 3 gegen `package.json` Zeile 85
- Version oder Commit: Commit 820213a98cb1
- Abruf- oder Prüfdatum: 2026-09-14

Prüfung:

- durchgeführte Prüfung: Angaben verschiedener Dateien gegenübergestellt
- Ergebnis: widersprechende Angaben
- nicht durchgeführte Prüfung: nicht durch Installation oder Test aufgelöst
- Einschränkung der Aussagekraft: Welche Angabe zutrifft, ist offen

Bezug zur Projektidee:

- Abschnitt oder Originalaussage: `idea.md` Abschnitt 1, Abschnitt 7, Abschnitt 10
- Bedeutung für die Bestandsuntersuchung: Belastbarkeit der Projektangaben

Folgerung:
Die widersprechenden Angaben stehen nebeneinander; keine davon ist bestätigt.

### evd-033

Aussage:
soilDNRA/openclaw-xmpp: Die README beschreibt nur Direktchats, nennt MUC und OMEMO ausdrücklich als nicht unterstützt und OpenClaw 2026.8.2 als Mindestversion; sie verweist auf ClawHub `openclaw-xmpp@0.1.2-beta.2` und auf die Hauptquelle https://git.sdf.org/erici/openclaw-xmpp.

Nachweisstatus:
`DOCUMENTED`

Quelle:

- Typ: `PROJECT_DOCUMENTATION`
- Fundstelle: `README.md` Zeilen 1–2, 15–18, 44–46, 72; `package.json` Zeile 41 (`openclaw >=2026.8.2`)
- Version oder Commit: Commit a41df5fc1417, 2026-09-09
- Abruf- oder Prüfdatum: 2026-09-14

Prüfung:

- durchgeführte Prüfung: README und Paketmetadaten gelesen
- Ergebnis: wie in der Aussage
- nicht durchgeführte Prüfung: keine Installation, kein Funktionstest; ClawHub-Eintrag nicht geprüft
- Einschränkung der Aussagekraft: Projektangaben, nicht praktisch bestätigt

Bezug zur Projektidee:

- Abschnitt oder Originalaussage: `idea.md` Abschnitt 1 (Direktnachrichten, OMEMO, MUC, GitHub-Projekte), Abschnitt 7
- Bedeutung für die Bestandsuntersuchung: dokumentierte Funktionen und Versionsangaben eines vorhandenen Projekts

Folgerung:
Die dokumentierten Funktionen sind nicht praktisch geprüft.

### evd-034

Aussage:
soilDNRA/openclaw-xmpp: Code für 1:1 ist vorhanden; MUC- und OMEMO-Zeichenketten kommen nicht vor; die Hauptquelle auf git.sdf.org hat denselben Commit.

Nachweisstatus:
`VERIFIED`

Quelle:

- Typ: `SOURCE_CODE`
- Fundstelle: `src/stanzas.ts` Zeile 151; Gitea-API git.sdf.org `main`
- Version oder Commit: Commit a41df5fc1417
- Abruf- oder Prüfdatum: 2026-09-14

Prüfung:

- durchgeführte Prüfung: Quelltext per `git clone --depth 1` gelesen und nach Namensräumen und Bezeichnern durchsucht
- Ergebnis: wie in der Aussage; Tests: `test/` mit 12 Dateien, `.github/workflows/ci.yml`
- nicht durchgeführte Prüfung: Code nicht ausgeführt, Tests nicht ausgeführt, kein Build
- Einschränkung der Aussagekraft: belegt nur vorhandenen Code, nicht dessen Funktionsfähigkeit; 0 Treffer belegt nur das Fehlen der gesuchten Zeichenketten

Bezug zur Projektidee:

- Abschnitt oder Originalaussage: `idea.md` Abschnitt 1, Abschnitt 7
- Bedeutung für die Bestandsuntersuchung: im Quelltext vorhandene Implementierungsteile

Folgerung:
Vorhandener Code ist nicht als funktionsfähig nachgewiesen.

### evd-035

Aussage:
elmafioso79/xmpp-channel: Die README nennt 1:1- und Gruppenchat sowie OMEMO einschließlich Gruppenchats im älteren Namensraum; `peerDependencies` verlangt `openclaw ^2026.2.2-3`. Offener PR #4 zur Anpassung an OpenClaw 2026.5.2.

Nachweisstatus:
`DOCUMENTED`

Quelle:

- Typ: `PROJECT_DOCUMENTATION`
- Fundstelle: `README.md` Zeilen 9–10, 211, 223; `package.json` Zeile 63; https://github.com/elmafioso79/xmpp-channel/pull/4
- Version oder Commit: Commit a447455d6cb1, 2026-02-18
- Abruf- oder Prüfdatum: 2026-09-14

Prüfung:

- durchgeführte Prüfung: README und Paketmetadaten gelesen
- Ergebnis: wie in der Aussage
- nicht durchgeführte Prüfung: keine Installation, kein Funktionstest
- Einschränkung der Aussagekraft: Projektangaben, nicht praktisch bestätigt

Bezug zur Projektidee:

- Abschnitt oder Originalaussage: `idea.md` Abschnitt 1 (Direktnachrichten, OMEMO, MUC, GitHub-Projekte), Abschnitt 7
- Bedeutung für die Bestandsuntersuchung: dokumentierte Funktionen und Versionsangaben eines vorhandenen Projekts

Folgerung:
Die dokumentierten Funktionen sind nicht praktisch geprüft.

### evd-036

Aussage:
elmafioso79/xmpp-channel: Code für MUC (`joinMuc`) und für OMEMO bei `groupchat` ist vorhanden; keine Testdateien.

Nachweisstatus:
`VERIFIED`

Quelle:

- Typ: `SOURCE_CODE`
- Fundstelle: `src/monitor.ts` Zeile 255; `src/omemo/types.ts` Zeilen 13, 26; `src/inbound.ts` Zeilen 359, 386
- Version oder Commit: Commit a447455d6cb1
- Abruf- oder Prüfdatum: 2026-09-14

Prüfung:

- durchgeführte Prüfung: Quelltext per `git clone --depth 1` gelesen und nach Namensräumen und Bezeichnern durchsucht
- Ergebnis: wie in der Aussage; Tests: keine
- nicht durchgeführte Prüfung: Code nicht ausgeführt, Tests nicht ausgeführt, kein Build
- Einschränkung der Aussagekraft: belegt nur vorhandenen Code, nicht dessen Funktionsfähigkeit; 0 Treffer belegt nur das Fehlen der gesuchten Zeichenketten

Bezug zur Projektidee:

- Abschnitt oder Originalaussage: `idea.md` Abschnitt 1, Abschnitt 7
- Bedeutung für die Bestandsuntersuchung: im Quelltext vorhandene Implementierungsteile

Folgerung:
Vorhandener Code ist nicht als funktionsfähig nachgewiesen.

### evd-037

Aussage:
watkins-matt/xmpp-channel: Fork von elmafioso79/xmpp-channel, 28 Commits voraus; die README ist identisch mit dem Ursprung; `peerDependencies` verlangt `openclaw >=2026.8.2`.

Nachweisstatus:
`DOCUMENTED`

Quelle:

- Typ: `PROJECT_DOCUMENTATION`
- Fundstelle: `README.md` (per `diff` mit dem Ursprung verglichen); `package.json` Zeilen 64–65
- Version oder Commit: Commit 1a734552fe19, 2026-09-11
- Abruf- oder Prüfdatum: 2026-09-14

Prüfung:

- durchgeführte Prüfung: README und Paketmetadaten gelesen
- Ergebnis: wie in der Aussage
- nicht durchgeführte Prüfung: keine Installation, kein Funktionstest
- Einschränkung der Aussagekraft: Projektangaben, nicht praktisch bestätigt

Bezug zur Projektidee:

- Abschnitt oder Originalaussage: `idea.md` Abschnitt 1 (Direktnachrichten, OMEMO, MUC, GitHub-Projekte), Abschnitt 7
- Bedeutung für die Bestandsuntersuchung: dokumentierte Funktionen und Versionsangaben eines vorhandenen Projekts

Folgerung:
Die dokumentierten Funktionen sind nicht praktisch geprüft.

### evd-038

Aussage:
watkins-matt/xmpp-channel: Code für MUC und OMEMO ist vorhanden.

Nachweisstatus:
`VERIFIED`

Quelle:

- Typ: `SOURCE_CODE`
- Fundstelle: `src/monitor.ts` Zeile 292; `src/omemo/types.ts` Zeilen 13, 26; `src/inbound.ts` Zeile 495
- Version oder Commit: Commit 1a734552fe19
- Abruf- oder Prüfdatum: 2026-09-14

Prüfung:

- durchgeführte Prüfung: Quelltext per `git clone --depth 1` gelesen und nach Namensräumen und Bezeichnern durchsucht
- Ergebnis: wie in der Aussage; Tests: `src/payload-filter.test.ts`, `src/sdk-contract.test.ts`
- nicht durchgeführte Prüfung: Code nicht ausgeführt, Tests nicht ausgeführt, kein Build
- Einschränkung der Aussagekraft: belegt nur vorhandenen Code, nicht dessen Funktionsfähigkeit; 0 Treffer belegt nur das Fehlen der gesuchten Zeichenketten

Bezug zur Projektidee:

- Abschnitt oder Originalaussage: `idea.md` Abschnitt 1, Abschnitt 7
- Bedeutung für die Bestandsuntersuchung: im Quelltext vorhandene Implementierungsteile

Folgerung:
Vorhandener Code ist nicht als funktionsfähig nachgewiesen.

### evd-039

Aussage:
Programmatore-Web/openclaw-xmpp-channel: Fork von watkins-matt/xmpp-channel; die README nennt 1:1 und fest eingestellte MUC-Räume, schließt Ende-zu-Ende-Verschlüsselung aus und nennt OpenClaw 2026.8.2 oder neuer.

Nachweisstatus:
`DOCUMENTED`

Quelle:

- Typ: `PROJECT_DOCUMENTATION`
- Fundstelle: `README.md` Zeilen 8, 18–19, 32; `package.json` Zeilen 63–64
- Version oder Commit: Commit 0ba189314a14, 2026-09-10
- Abruf- oder Prüfdatum: 2026-09-14

Prüfung:

- durchgeführte Prüfung: README und Paketmetadaten gelesen
- Ergebnis: wie in der Aussage
- nicht durchgeführte Prüfung: keine Installation, kein Funktionstest
- Einschränkung der Aussagekraft: Projektangaben, nicht praktisch bestätigt

Bezug zur Projektidee:

- Abschnitt oder Originalaussage: `idea.md` Abschnitt 1 (Direktnachrichten, OMEMO, MUC, GitHub-Projekte), Abschnitt 7
- Bedeutung für die Bestandsuntersuchung: dokumentierte Funktionen und Versionsangaben eines vorhandenen Projekts

Folgerung:
Die dokumentierten Funktionen sind nicht praktisch geprüft.

### evd-040

Aussage:
Programmatore-Web/openclaw-xmpp-channel: Code für MUC ist vorhanden; OMEMO-Zeichenketten kommen nicht vor; verschlüsselte Nachrichten werden verworfen.

Nachweisstatus:
`VERIFIED`

Quelle:

- Typ: `SOURCE_CODE`
- Fundstelle: `src/monitor.ts` Zeilen 772, 988–1105; `src/muc-identity.ts`
- Version oder Commit: Commit 0ba189314a14
- Abruf- oder Prüfdatum: 2026-09-14

Prüfung:

- durchgeführte Prüfung: Quelltext per `git clone --depth 1` gelesen und nach Namensräumen und Bezeichnern durchsucht
- Ergebnis: wie in der Aussage; Tests: `test/` mit 33 Dateien
- nicht durchgeführte Prüfung: Code nicht ausgeführt, Tests nicht ausgeführt, kein Build
- Einschränkung der Aussagekraft: belegt nur vorhandenen Code, nicht dessen Funktionsfähigkeit; 0 Treffer belegt nur das Fehlen der gesuchten Zeichenketten

Bezug zur Projektidee:

- Abschnitt oder Originalaussage: `idea.md` Abschnitt 1, Abschnitt 7
- Bedeutung für die Bestandsuntersuchung: im Quelltext vorhandene Implementierungsteile

Folgerung:
Vorhandener Code ist nicht als funktionsfähig nachgewiesen.

### evd-041

Aussage:
Programmatore-Web/openclaw-xmpp-channel: Das übernommene CHANGELOG beschreibt OMEMO-Funktionen, die im Code und in der README nicht mehr vorkommen.

Nachweisstatus:
`CONFLICT`

Quelle:

- Typ: `PROJECT_DOCUMENTATION`
- Fundstelle: `CHANGELOG.md` Zeilen 39–92 gegen `README.md` Zeilen 18–19 und `src/`
- Version oder Commit: Commit 0ba189314a14
- Abruf- oder Prüfdatum: 2026-09-14

Prüfung:

- durchgeführte Prüfung: Angaben verschiedener Dateien gegenübergestellt
- Ergebnis: widersprechende Angaben
- nicht durchgeführte Prüfung: nicht durch Installation oder Test aufgelöst
- Einschränkung der Aussagekraft: Welche Angabe zutrifft, ist offen

Bezug zur Projektidee:

- Abschnitt oder Originalaussage: `idea.md` Abschnitt 1, Abschnitt 7, Abschnitt 10
- Bedeutung für die Bestandsuntersuchung: Belastbarkeit der Projektangaben

Folgerung:
Die widersprechenden Angaben stehen nebeneinander; keine davon ist bestätigt.

### evd-042

Aussage:
MrCPA/oc-xmpp: Die README nennt Direktnachrichten und Räume, OMEMO nur für Direktnachrichten und Live-Tests als noch offen; `peerDependencies` verlangt `openclaw "*"`.

Nachweisstatus:
`DOCUMENTED`

Quelle:

- Typ: `PROJECT_DOCUMENTATION`
- Fundstelle: `README.md` Zeilen 5, 9, 30; `package.json` Zeilen 45–46
- Version oder Commit: Commit 675775a49f43, 2026-04-11
- Abruf- oder Prüfdatum: 2026-09-14

Prüfung:

- durchgeführte Prüfung: README und Paketmetadaten gelesen
- Ergebnis: wie in der Aussage
- nicht durchgeführte Prüfung: keine Installation, kein Funktionstest; Beschränkung von OMEMO auf Direktnachrichten im Code nicht geprüft
- Einschränkung der Aussagekraft: Projektangaben, nicht praktisch bestätigt

Bezug zur Projektidee:

- Abschnitt oder Originalaussage: `idea.md` Abschnitt 1 (Direktnachrichten, OMEMO, MUC, GitHub-Projekte), Abschnitt 7
- Bedeutung für die Bestandsuntersuchung: dokumentierte Funktionen und Versionsangaben eines vorhandenen Projekts

Folgerung:
Die dokumentierten Funktionen sind nicht praktisch geprüft.

### evd-043

Aussage:
MrCPA/oc-xmpp: Code für MUC und für OMEMO in `urn:xmpp:omemo:2` ist vorhanden.

Nachweisstatus:
`VERIFIED`

Quelle:

- Typ: `SOURCE_CODE`
- Fundstelle: `src/inbound.ts` Zeilen 76, 102, 461; `src/omemo.ts` Zeilen 17, 207
- Version oder Commit: Commit 675775a49f43
- Abruf- oder Prüfdatum: 2026-09-14

Prüfung:

- durchgeführte Prüfung: Quelltext per `git clone --depth 1` gelesen und nach Namensräumen und Bezeichnern durchsucht
- Ergebnis: wie in der Aussage; Tests: `tests/` mit 6 Dateien, u. a. `omemo-wire.test.ts`
- nicht durchgeführte Prüfung: Code nicht ausgeführt, Tests nicht ausgeführt, kein Build
- Einschränkung der Aussagekraft: belegt nur vorhandenen Code, nicht dessen Funktionsfähigkeit; 0 Treffer belegt nur das Fehlen der gesuchten Zeichenketten

Bezug zur Projektidee:

- Abschnitt oder Originalaussage: `idea.md` Abschnitt 1, Abschnitt 7
- Bedeutung für die Bestandsuntersuchung: im Quelltext vorhandene Implementierungsteile

Folgerung:
Vorhandener Code ist nicht als funktionsfähig nachgewiesen.

### evd-044

Aussage:
chitozzz/xmpp-adapter-openclaw: Die README nennt 1:1 und MUC als Ziel und das Projekt als in Planung; `peerDependencies` verlangt `openclaw >=2026.6.9`; OMEMO wird nicht genannt.

Nachweisstatus:
`DOCUMENTED`

Quelle:

- Typ: `PROJECT_DOCUMENTATION`
- Fundstelle: `README.md` Zeilen 9–12, 21–24; `package.json` Zeilen 37–38
- Version oder Commit: Commit f280515acd43, 2026-09-12
- Abruf- oder Prüfdatum: 2026-09-14

Prüfung:

- durchgeführte Prüfung: README und Paketmetadaten gelesen
- Ergebnis: wie in der Aussage
- nicht durchgeführte Prüfung: keine Installation, kein Funktionstest
- Einschränkung der Aussagekraft: Projektangaben, nicht praktisch bestätigt

Bezug zur Projektidee:

- Abschnitt oder Originalaussage: `idea.md` Abschnitt 1 (Direktnachrichten, OMEMO, MUC, GitHub-Projekte), Abschnitt 7
- Bedeutung für die Bestandsuntersuchung: dokumentierte Funktionen und Versionsangaben eines vorhandenen Projekts

Folgerung:
Die dokumentierten Funktionen sind nicht praktisch geprüft.

### evd-045

Aussage:
chitozzz/xmpp-adapter-openclaw: Code für 1:1 und MUC (`joinMuc`) ist vorhanden; OMEMO-Zeichenketten kommen nicht vor.

Nachweisstatus:
`VERIFIED`

Quelle:

- Typ: `SOURCE_CODE`
- Fundstelle: `src/xmpp-client.ts` Zeilen 306, 524–530
- Version oder Commit: Commit f280515acd43
- Abruf- oder Prüfdatum: 2026-09-14

Prüfung:

- durchgeführte Prüfung: Quelltext per `git clone --depth 1` gelesen und nach Namensräumen und Bezeichnern durchsucht
- Ergebnis: wie in der Aussage; Tests: `test/smoke.js`
- nicht durchgeführte Prüfung: Code nicht ausgeführt, Tests nicht ausgeführt, kein Build
- Einschränkung der Aussagekraft: belegt nur vorhandenen Code, nicht dessen Funktionsfähigkeit; 0 Treffer belegt nur das Fehlen der gesuchten Zeichenketten

Bezug zur Projektidee:

- Abschnitt oder Originalaussage: `idea.md` Abschnitt 1, Abschnitt 7
- Bedeutung für die Bestandsuntersuchung: im Quelltext vorhandene Implementierungsteile

Folgerung:
Vorhandener Code ist nicht als funktionsfähig nachgewiesen.

### evd-046

Aussage:
weijia/xmpp-connector: Die README nennt Senden und Empfangen von Nachrichten, keine OpenClaw-Version, weder MUC noch OMEMO; auf npm ist `openclaw-xmpp-connector` 0.3.0 veröffentlicht.

Nachweisstatus:
`DOCUMENTED`

Quelle:

- Typ: `PROJECT_DOCUMENTATION`
- Fundstelle: `README.md` Zeilen 7–8, 52; npm `openclaw-xmpp-connector`
- Version oder Commit: Commit 3d7c72e66cd9, 2026-03-29
- Abruf- oder Prüfdatum: 2026-09-14

Prüfung:

- durchgeführte Prüfung: README und Paketmetadaten gelesen
- Ergebnis: wie in der Aussage
- nicht durchgeführte Prüfung: keine Installation, kein Funktionstest
- Einschränkung der Aussagekraft: Projektangaben, nicht praktisch bestätigt

Bezug zur Projektidee:

- Abschnitt oder Originalaussage: `idea.md` Abschnitt 1 (Direktnachrichten, OMEMO, MUC, GitHub-Projekte), Abschnitt 7
- Bedeutung für die Bestandsuntersuchung: dokumentierte Funktionen und Versionsangaben eines vorhandenen Projekts

Folgerung:
Die dokumentierten Funktionen sind nicht praktisch geprüft.

### evd-047

Aussage:
weijia/xmpp-connector: Code für 1:1 ist vorhanden; MUC- und OMEMO-Zeichenketten kommen nicht vor; keine Testdateien.

Nachweisstatus:
`VERIFIED`

Quelle:

- Typ: `SOURCE_CODE`
- Fundstelle: `plugin.ts` Zeile 507
- Version oder Commit: Commit 3d7c72e66cd9
- Abruf- oder Prüfdatum: 2026-09-14

Prüfung:

- durchgeführte Prüfung: Quelltext per `git clone --depth 1` gelesen und nach Namensräumen und Bezeichnern durchsucht
- Ergebnis: wie in der Aussage; Tests: keine
- nicht durchgeführte Prüfung: Code nicht ausgeführt, Tests nicht ausgeführt, kein Build
- Einschränkung der Aussagekraft: belegt nur vorhandenen Code, nicht dessen Funktionsfähigkeit; 0 Treffer belegt nur das Fehlen der gesuchten Zeichenketten

Bezug zur Projektidee:

- Abschnitt oder Originalaussage: `idea.md` Abschnitt 1, Abschnitt 7
- Bedeutung für die Bestandsuntersuchung: im Quelltext vorhandene Implementierungsteile

Folgerung:
Vorhandener Code ist nicht als funktionsfähig nachgewiesen.

### evd-048

Aussage:
processone/openclaw, Zweig xmpp-support: Die README der Erweiterung nennt 1:1 und MUC; OMEMO wird nicht genannt; der Zweig ist Grundlage des geschlossenen PR #9741 und hängt von `openclaw workspace:*` ab.

Nachweisstatus:
`DOCUMENTED`

Quelle:

- Typ: `PROJECT_DOCUMENTATION`
- Fundstelle: `extensions/xmpp/README.md` Zeilen 10–11; `extensions/xmpp/package.json`
- Version oder Commit: Commit a6adb95b35c1, 2026-02-07
- Abruf- oder Prüfdatum: 2026-09-14

Prüfung:

- durchgeführte Prüfung: README und Paketmetadaten gelesen
- Ergebnis: wie in der Aussage
- nicht durchgeführte Prüfung: keine Installation, kein Funktionstest
- Einschränkung der Aussagekraft: Projektangaben, nicht praktisch bestätigt

Bezug zur Projektidee:

- Abschnitt oder Originalaussage: `idea.md` Abschnitt 1 (Direktnachrichten, OMEMO, MUC, GitHub-Projekte), Abschnitt 7
- Bedeutung für die Bestandsuntersuchung: dokumentierte Funktionen und Versionsangaben eines vorhandenen Projekts

Folgerung:
Die dokumentierten Funktionen sind nicht praktisch geprüft.

### evd-049

Aussage:
processone/openclaw, Zweig xmpp-support: Code für 1:1 und MUC (`joinRoom`) ist vorhanden; OMEMO-Zeichenketten kommen nicht vor.

Nachweisstatus:
`VERIFIED`

Quelle:

- Typ: `SOURCE_CODE`
- Fundstelle: `extensions/xmpp/src/channel.ts` Zeilen 150, 290; `src/client.ts` Zeile 353
- Version oder Commit: Commit a6adb95b35c1
- Abruf- oder Prüfdatum: 2026-09-14

Prüfung:

- durchgeführte Prüfung: Quelltext per `git clone --depth 1` gelesen und nach Namensräumen und Bezeichnern durchsucht
- Ergebnis: wie in der Aussage; Tests: `src/client.test.ts`, `src/actions.test.ts`
- nicht durchgeführte Prüfung: Code nicht ausgeführt, Tests nicht ausgeführt, kein Build
- Einschränkung der Aussagekraft: belegt nur vorhandenen Code, nicht dessen Funktionsfähigkeit; 0 Treffer belegt nur das Fehlen der gesuchten Zeichenketten

Bezug zur Projektidee:

- Abschnitt oder Originalaussage: `idea.md` Abschnitt 1, Abschnitt 7
- Bedeutung für die Bestandsuntersuchung: im Quelltext vorhandene Implementierungsteile

Folgerung:
Vorhandener Code ist nicht als funktionsfähig nachgewiesen.

### evd-050

Aussage:
rsaisankalp/clawdbotElyments: Die README beschreibt eine Anbindung von Clawdbot an die XMPP-basierte Plattform Elyments mit Direktnachrichten; `peerDependencies` verlangt `clawdbot >=2026.0.0`; auf npm ist `clawdbot-elyments` 1.0.0 veröffentlicht.

Nachweisstatus:
`DOCUMENTED`

Quelle:

- Typ: `PROJECT_DOCUMENTATION`
- Fundstelle: `README.md` Zeilen 79–96; `package.json`
- Version oder Commit: Commit f2e1dde49780, 2026-01-17
- Abruf- oder Prüfdatum: 2026-09-14

Prüfung:

- durchgeführte Prüfung: README und Paketmetadaten gelesen
- Ergebnis: wie in der Aussage
- nicht durchgeführte Prüfung: keine Installation, kein Funktionstest
- Einschränkung der Aussagekraft: Projektangaben, nicht praktisch bestätigt

Bezug zur Projektidee:

- Abschnitt oder Originalaussage: `idea.md` Abschnitt 1 (Direktnachrichten, OMEMO, MUC, GitHub-Projekte), Abschnitt 7
- Bedeutung für die Bestandsuntersuchung: dokumentierte Funktionen und Versionsangaben eines vorhandenen Projekts

Folgerung:
Die dokumentierten Funktionen sind nicht praktisch geprüft.

### evd-051

Aussage:
rsaisankalp/clawdbotElyments: Code verarbeitet den Nachrichtentyp `groupchat`, enthält aber keinen Raumbeitritt; OMEMO-Zeichenketten kommen nicht vor; keine Testdateien.

Nachweisstatus:
`VERIFIED`

Quelle:

- Typ: `SOURCE_CODE`
- Fundstelle: `src/elyments/xmpp.ts` Zeile 320
- Version oder Commit: Commit f2e1dde49780
- Abruf- oder Prüfdatum: 2026-09-14

Prüfung:

- durchgeführte Prüfung: Quelltext per `git clone --depth 1` gelesen und nach Namensräumen und Bezeichnern durchsucht
- Ergebnis: wie in der Aussage; Tests: keine
- nicht durchgeführte Prüfung: Code nicht ausgeführt, Tests nicht ausgeführt, kein Build
- Einschränkung der Aussagekraft: belegt nur vorhandenen Code, nicht dessen Funktionsfähigkeit; 0 Treffer belegt nur das Fehlen der gesuchten Zeichenketten

Bezug zur Projektidee:

- Abschnitt oder Originalaussage: `idea.md` Abschnitt 1, Abschnitt 7
- Bedeutung für die Bestandsuntersuchung: im Quelltext vorhandene Implementierungsteile

Folgerung:
Vorhandener Code ist nicht als funktionsfähig nachgewiesen.

### evd-052

Aussage:
Ob eines der untersuchten Projekte Direktnachrichten, OMEMO-Verschlüsselung und Gruppenchats über MUC tatsächlich funktionsfähig bereitstellt, ist unbekannt.

Nachweisstatus:
`UNKNOWN`

Quelle:

- Typ: `NONE`
- Fundstelle: evd-022 bis evd-051
- Version oder Commit: –
- Abruf- oder Prüfdatum: 2026-09-14

Prüfung:

- durchgeführte Prüfung: keine Funktionsprüfung
- Ergebnis: –
- nicht durchgeführte Prüfung: Installation, Tests und Verbindung zu einem XMPP-Server nicht durchgeführt
- Einschränkung der Aussagekraft: Funktionsprüfung außerhalb der erlaubten Bestandsaufnahme

Bezug zur Projektidee:

- Abschnitt oder Originalaussage: `idea.md` Abschnitt 11 (erster unbekannter Sachverhalt)
- Bedeutung für die Bestandsuntersuchung: offener Sachverhalt aus `idea.md`

Folgerung:
Der in `idea.md` genannte unbekannte Sachverhalt bleibt unbekannt.

### evd-053

Aussage:
Ob die untersuchten Projekte unter OpenClaw 2026.7.1-2 oder 2026.9.4 laden und laufen, ist unbekannt; es liegen nur deklarierte Versionsangaben vor.

Nachweisstatus:
`UNKNOWN`

Quelle:

- Typ: `NONE`
- Fundstelle: Versionsangaben in evd-022 bis evd-051
- Version oder Commit: –
- Abruf- oder Prüfdatum: 2026-09-14

Prüfung:

- durchgeführte Prüfung: keine Installationsprüfung
- Ergebnis: –
- nicht durchgeführte Prüfung: kein Laden in einer OpenClaw-Installation
- Einschränkung der Aussagekraft: deklarierte Versionsbereiche sind keine Kompatibilitätsnachweise (vgl. evd-014)

Bezug zur Projektidee:

- Abschnitt oder Originalaussage: `idea.md` Abschnitt 1, Abschnitt 10 („aktuelle OpenClaw-Versionen“)
- Bedeutung für die Bestandsuntersuchung: Kompatibilität des vorhandenen Bestands

Folgerung:
Die Kompatibilität der Projekte mit den genannten Versionen ist nicht belegt.

### evd-054

Aussage:
Ob es XMPP-Anbindungen für OpenClaw außerhalb von GitHub und npm gibt, etwa auf ClawHub, GitLab oder Codeberg, ist unbekannt.

Nachweisstatus:
`UNKNOWN`

Quelle:

- Typ: `NONE`
- Fundstelle: –
- Version oder Commit: –
- Abruf- oder Prüfdatum: 2026-09-14

Prüfung:

- durchgeführte Prüfung: GitHub- und npm-Suche durchgeführt (Suchanfragen siehe Abschnitt 4)
- Ergebnis: –
- nicht durchgeführte Prüfung: ClawHub, GitLab, Codeberg und allgemeine Websuche nicht durchsucht
- Einschränkung der Aussagekraft: Suche auf zwei Plattformen beschränkt

Bezug zur Projektidee:

- Abschnitt oder Originalaussage: `idea.md` Abschnitt 1 („Vorhandene GitHub-Projekte“)
- Bedeutung für die Bestandsuntersuchung: Vollständigkeit der Projektliste

Folgerung:
Die Projektliste ist auf GitHub und npm beschränkt.

## 7. Widersprüche

In diesem Abschnitt werden Befunde mit dem Nachweisstatus `CONFLICT`
zusammengeführt.

| Betroffene Befunde | Gegenstand des Widerspruchs | Widersprechende Quellen | Notwendige weitere Prüfung |
|---|---|---|---|
| `evd-026` | toughworm/Openclaw-XMPP-Plugin: Die README nennt Gruppenchat und die Installation über `@openclaw/xmpp`; im Code fehlt ein Raumbeitritt, das Paket `@openclaw/xmpp` gibt es auf npm nicht (HTTP 404), und die in der README genannten Testskripte fehlen im Repository. | `README.md` Zeilen 24, 54, 133, 193–196 gegen `src/` und `git ls-files`; https://registry.npmjs.org/@openclaw%2fxmpp | Klärung, welche Angabe zutrifft, durch Prüfung von Code oder Laufzeitverhalten |
| `evd-029` | kazakhan/openclaw-xmpp: Die README nennt als Mindestversion OpenClaw 2026.8.2, `package.json` gibt `compat.pluginApi ">=2026.6.1"` und `minGatewayVersion "2026.6.1"` an. | `README.md` Zeile 22 gegen `package.json` Zeilen 20–24 | Klärung, welche Angabe zutrifft, durch Prüfung von Code oder Laufzeitverhalten |
| `evd-032` | icarito/openclaw-xmpp: `AGENTS.md` nennt OpenClaw 2026.6.9, `package.json` gibt `compat.pluginApi ">=2026.7.1"` an. | `AGENTS.md` Zeile 3 gegen `package.json` Zeile 85 | Klärung, welche Angabe zutrifft, durch Prüfung von Code oder Laufzeitverhalten |
| `evd-041` | Programmatore-Web/openclaw-xmpp-channel: Das übernommene CHANGELOG beschreibt OMEMO-Funktionen, die im Code und in der README nicht mehr vorkommen. | `CHANGELOG.md` Zeilen 39–92 gegen `README.md` Zeilen 18–19 und `src/` | Klärung, welche Angabe zutrifft, durch Prüfung von Code oder Laufzeitverhalten |

## 8. Unbekannte Sachverhalte

Hier werden Befunde mit dem Nachweisstatus `UNKNOWN` zusammengeführt.

| Befund | Unbekannter Sachverhalt | Grund | Bedeutung für den weiteren Prozess |
|---|---|---|---|
| `evd-006` | Ob srv001 eine der beiden vom Ideengeber genannten Installationen ist und wo die Installation mit Version 2026.7.1-2 läuft, ist unbekannt. | Angabe fehlt in allen zugänglichen Quellen | Umfang der vorhandenen Installationen |
| `evd-007` | Welche Plugins in den vorhandenen Installationen installiert oder erprobt wurden und woran ihre Installation scheiterte, ist unbekannt. | keine zugängliche Quelle | dokumentierter bisheriger Versuch |
| `evd-008` | Software, Standort und unterstützte XMPP-Erweiterungen des eigenen XMPP-Servers sind unbekannt. | Das Fehlen eines Dienstes auf srv001 sagt nichts über den Server an anderer Stelle | beteiligtes System |
| `evd-052` | Ob eines der untersuchten Projekte Direktnachrichten, OMEMO-Verschlüsselung und Gruppenchats über MUC tatsächlich funktionsfähig bereitstellt, ist unbekannt. | Funktionsprüfung außerhalb der erlaubten Bestandsaufnahme | offener Sachverhalt aus `idea.md` |
| `evd-053` | Ob die untersuchten Projekte unter OpenClaw 2026.7.1-2 oder 2026.9.4 laden und laufen, ist unbekannt; es liegen nur deklarierte Versionsangaben vor. | deklarierte Versionsbereiche sind keine Kompatibilitätsnachweise (vgl. evd-014) | Kompatibilität des vorhandenen Bestands |
| `evd-054` | Ob es XMPP-Anbindungen für OpenClaw außerhalb von GitHub und npm gibt, etwa auf ClawHub, GitLab oder Codeberg, ist unbekannt. | Suche auf zwei Plattformen beschränkt | Vollständigkeit der Projektliste |

## 9. Nicht oder nur teilweise untersuchte Bereiche

| Bereich | Nicht untersuchter Teil | Grund | Auswirkung auf die Aussagekraft |
|---|---|---|---|
| Vorhandene OpenClaw-Installationen | Konfiguration und Plugins auf srv001; Installation mit 2026.7.1-2 | Zugriff verweigert; Standort unbekannt | Bisherige Versuche und die zweite Installation sind nicht belegt (evd-006, evd-007). |
| Plugin- und Kanalschnittstelle | Paketinhalt 2026.7.1-2; `src/plugins/compat/registry.ts`; Website | nicht geladen bzw. nicht gelesen | Der Vergleich der Versionen beruht auf Registermetadaten und Dokumentation (evd-011, evd-017). |
| Versionen und Schnittstellenänderungen | vollständiges CHANGELOG | Umfang von rund 24 000 Zeilen | Weitere Schnittstellenänderungen sind möglich, aber nicht erfasst (evd-016). |
| XMPP im Hauptprojekt | Inhalte der PR- und Issue-Diskussionen | nur Status ausgewertet | Gründe für die Nichtübernahme sind unbekannt (evd-020). |
| Vorhandene öffentliche XMPP-Projekte | Funktionsfähigkeit; Kompatibilität mit den genannten Versionen; ClawHub, GitLab, Codeberg; Forks cronus42, kitschmensch, zhgzhg, jerry-harm, indorri; geschlossene Issues; OMEMO-Beschränkung im Code von MrCPA/oc-xmpp | keine Installation und kein Test zulässig; Suche auf GitHub und npm beschränkt | Aussagen zu Funktionen sind höchstens dokumentiert oder als vorhandener Code belegt (evd-052 bis evd-054). |
| Eigener XMPP-Server | gesamter Server | keine Quelle zugänglich | Keine Angaben zu Server-Software und Erweiterungen (evd-008). |
| Bisherige Versuche | gesamter Bereich | keine Dokumentation, Konfiguration nicht lesbar | Die vom Ideengeber erprobten Plugins sind nicht identifizierbar (evd-003, evd-007). |

## 10. Grenzen der Bestandsuntersuchung

- zeitliche Grenze: Stand 2026-09-14; alle Registerdaten, Commits und Trefferzahlen gelten für diesen Tag.
- technische Grenze: Quelltext nur gelesen und durchsucht; kein Code, kein Test und kein Build ausgeführt; kein Plugin in eine OpenClaw-Installation geladen.
- nicht verfügbare Quellen: Konfigurationsverzeichnis `/var/lib/openclaw/.openclaw` auf srv001; Installation mit 2026.7.1-2; eigener XMPP-Server; Aufzeichnungen zu bisherigen Versuchen.
- nicht mögliche Prüfungen: Funktionsprüfung von Direktnachrichten, OMEMO und MUC; Kompatibilitätsprüfung mit den genannten OpenClaw-Versionen.
- sonstige Einschränkungen: Suche und Erstauswertung der Projekte und der OpenClaw-Schnittstelle erfolgten in zwei Hilfsaufträgen; Metadaten aller Projekte, Commits, Versionsdaten, Exportpfade, Stabilitätsaussage, Kanalliste, PR-Status und ausgewählte README- und Codestellen wurden von skizzwerk stichprobenartig nachgeprüft, nicht jede Zeilenangabe.

## 11. Abgrenzung zu späteren Phasen

Diese Bestandsuntersuchung dokumentiert vorhandene Bestandteile, Aussagen,
Nachweise, Konflikte und unbekannte Sachverhalte.

Sie enthält keine:

- neuen Anforderungen,
- Rangfolge möglicher Lösungen,
- Auswahl eines Projekts oder einer Komponente,
- Architekturentscheidung,
- Technologieentscheidung,
- Umsetzungsplanung.

## 12. Prüfergebnis swk-02

### Vorprüfung

- [x] Die projektspezifische `idea.md` existiert.
- [x] Die `idea.md` besitzt den Status `accepted`.
- [x] Alle von `phases/swk-02-inventory.md` referenzierten Dateien existieren.
- [x] Keine benötigte Regel oder Vorlage ist leer oder unvollständig.
- [x] Die Qualitätsgrenze für `swk-02` ist definiert.
- [x] Verwendete Kennungen entsprechen `rules/identifiers.md`.

Ergebnis der Vorprüfung:

- Ergebnis: `bestanden`
- geprüft am: 2026-09-14
- geprüft durch: skizzwerk
- festgestellte Mängel: keine

### Prüfung der Bestandsaufnahme

- [x] Der Untersuchungsumfang wurde aus der akzeptierten `idea.md` abgeleitet.
- [x] Jeder Untersuchungsbereich besitzt eine nachvollziehbare Begründung.
- [x] Tatsächlich und nicht untersuchte Bereiche sind getrennt dokumentiert.
- [x] Alle verwendeten Quellen besitzen reproduzierbare Fundstellen.
- [x] Jeder relevante Befund besitzt eine gültige `evd-nnn`-Kennung.
- [x] Jeder Befund besitzt einen Nachweisstatus gemäß `rules/evidence.md`.
- [x] Aussagen des Ideengebers und externe Befunde sind getrennt.
- [x] Dokumentierte Behauptungen werden nicht als nachgewiesene Tatsachen dargestellt.
- [x] Widersprüche sind mit `CONFLICT` gekennzeichnet.
- [x] Unbekannte Sachverhalte sind mit `UNKNOWN` gekennzeichnet.
- [x] Fehlende Informationen wurden nicht durch Annahmen ersetzt.
- [x] Nicht durchgeführte Prüfungen sind sichtbar.
- [x] Grenzen der Untersuchung sind dokumentiert.
- [x] Es wurden keine neuen Anforderungen formuliert.
- [x] Es wurde keine Lösung ausgewählt oder bewertet.
- [x] Es wurde keine Architekturentscheidung getroffen.
- [x] Die Qualitätsgrenze für `swk-02` wurde vollständig geprüft.

Ergebnis der Prüfung:

- Ergebnis: `bestanden`
- geprüft am: 2026-09-14
- geprüft durch: skizzwerk
- nicht erfüllte Kriterien: keine
- Begründung einer möglichen Blockade: keine Blockade; nicht zugängliche Quellen sind in Abschnitt 9 und 10 dokumentiert und verhindern den Abschluss der Bestandsaufnahme nicht.

Die Befundübersicht und die Einzelbefunde enthalten dieselben 54 Befunde
`evd-001` bis `evd-054`. Kein externes System und kein Repository wurde
verändert.

## 13. Freigabestatus

- Ergebnis: `offen`
- Dokumentstatus: `review`
- geprüft am:
- geprüft durch:
- Anmerkungen:
