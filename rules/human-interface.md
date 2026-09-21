# Mensch-KI-Schnittstelle

## Zweck

Diese Regel trennt die interne Prozessführung von skizzwerk von der
Interaktion mit dem Ideengeber.

Interne Artefakte, Kennungen, Nachweisstatus, Validierungen und Quality Gates
dienen der zuverlässigen Arbeit von skizzwerk. Sie sind nicht die
Benutzerschnittstelle des Prozesses.

## Grundregel

Der Ideengeber arbeitet grundsätzlich mit fachlichen Aussagen, Fragen,
Bestätigungen und Entscheidungen.

skizzwerk verwaltet die dafür erforderliche Prozessmechanik selbstständig.
Der Ideengeber muss insbesondere keine JSON-Dateien, Kennungslisten,
Quality-Gate-Checklisten, Git-Historien oder vollständigen Phasendokumente
durcharbeiten, sofern er dies nicht ausdrücklich verlangt.

## Verbindliche Arbeitsansicht

Immer wenn skizzwerk eine Eingabe, Bestätigung oder Entscheidung des
Ideengebers benötigt, wird zuerst eine kurze menschenlesbare Arbeitsansicht
ausgegeben. Sie enthält ausschließlich:

- **Stand:** Wo befindet sich die fachliche Arbeit?
- **Ergebnis:** Was wurde seit der letzten notwendigen Interaktion fachlich erreicht?
- **Offen:** Was ist für den nächsten fachlichen Fortschritt noch offen?
- **Von dir benötigt:** Die konkrete Frage, Bestätigung oder Entscheidung. Ist
  nichts erforderlich, steht hier ausdrücklich `nichts`.
- **Danach:** Welchen fachlichen Schritt führt skizzwerk anschließend aus?

Die Arbeitsansicht verwendet fachliche Sprache. Interne Kennungen wie
`evd-nnn`, `clr-nnn`, `dnd-nnn` oder Dateinamen werden nur genannt, wenn
sie für die konkrete menschliche Handlung erforderlich sind oder der
Ideengeber sie ausdrücklich verlangt.

## Interaktionsminimierung

skizzwerk unterbricht den Ideengeber nur, wenn dessen Eingabe für den weiteren
fachlichen Fortschritt erforderlich ist oder eine vorgeschriebene menschliche
Bestätigung beziehungsweise Entscheidung benötigt wird.

Mehrere gleichzeitig beantwortbare Fragen werden soweit fachlich sinnvoll
gebündelt. Interne Statuswechsel, Validierungen, Dokumenterzeugung,
Rückverweise und Aktualisierungen werden ohne zusätzliche Benutzerinteraktion
durchgeführt, soweit keine menschliche Aussage oder Freigabe erforderlich ist.

## Menschliche Freigabe

Eine Freigabe wird als fachliche Bestätigung formuliert. skizzwerk legt die
für die Bestätigung relevanten Aussagen kompakt und verständlich vor.

Die Freigabe darf nicht davon abhängen, dass der Ideengeber interne
Prozessartefakte selbst prüft. Vollständige Artefakte und Nachweise bleiben im
Repository verfügbar und können auf Wunsch eingesehen werden.

Bei Änderungen eines bereits akzeptierten Ergebnisses wird nur das
freigaberelevante fachliche Delta vorgelegt. Die detaillierte
Änderungsübersicht und die Prozessnachweise bleiben intern dokumentiert.

## Fortschritt

Fortschritt wird gegenüber dem Ideengeber als fachlicher Fortschritt
dargestellt, nicht als Anzahl erzeugter Dokumente, Befunde, Commits oder
bestandener interner Prüfungen.

Rücksprünge zwischen swk-Phasen werden intern ausgeführt. Gegenüber dem
Ideengeber werden sie nur erläutert, wenn daraus eine notwendige menschliche
Eingabe entsteht oder der Rücksprung den erwarteten fachlichen Ablauf
wesentlich verändert.

## Ausnahme

Wenn eine Unstimmigkeit ohne Einsicht in ein internes Artefakt nicht
verlässlich geklärt werden kann, darf skizzwerk den relevanten Ausschnitt
vorlegen. Es muss erklären, welche konkrete Aussage geprüft werden soll.
