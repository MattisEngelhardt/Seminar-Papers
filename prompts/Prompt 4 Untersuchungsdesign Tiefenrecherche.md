PROMPT 4 — UNTERSUCHUNGSDESIGN

1. OBERSTE REGEL — ABSOLUT GÜLTIG, KEINE AUSNAHME

Der Output dieses Prompts ist ausschließlich die Datei Synthese_Plan_Untersuchungsdesign.md — kein fertiger Untersuchungsdesign-Text. Das Ausformulieren des Textes erfolgt in Prompt 4.5. Diese Trennung ist zwingend und absolut verbindlich.

Ausschließlich Döring (2023) als Quelle. Keine der 10 inhaltlichen Quellen wird in diesem Schritt verwendet. Die Verwendung einer inhaltlichen Quelle im Untersuchungsdesign ist ein Fehler.

Keine halluzierten Seitenangaben — niemals. Dies ist die kritischste Einzelregel dieses Prompts. Das vollständige Protokoll steht in Sektion 3.

Döring nie vollständig in einem Zug laden. Immer gezielt per Grep navigieren. Die Tiefe der Recherche — nicht die Breite des Ladens — entscheidet über die Qualität der Synthese-Datei.

2. SEITENANGABEN-PROTOKOLL — KRITISCHSTE EINZELREGEL

Die Döring-Quelle liegt als PDF-zu-Markdown-Konvertierung vor (ca 40.000 Zeilen). Buchseitenzahlen und MD-Zeilennummern sind zwei völlig verschiedene Systeme. Aus einer MD-Zeilennummer kann niemals zuverlässig eine Buchseitenzahl abgeleitet werden: Layoutelemente, Abbildungen, Fußnoten und Kapitelköpfe verzerren jede rechnerische Hochrechnung. Eine erfundene Seitenzahl ist nicht nur wertlos, sondern schadet aktiv: Mattis öffnet im PDF die falsche Seite und verliert Zeit.

Die drei verbindlichen Szenarien — für jeden einzelnen Fund:

– SZENARIO 1 — Seitenzahl im MD explizit sichtbar: Im Markdown-Text ist eine Zahl als eigenständige Zeile oder Seitenkopf sichtbar und eindeutig als Buchseitenzahl identifizierbar (z.B. eine isolierte Zahl wie '183' oder ein Seitentrennzeichen mit Zahl). In diesem Fall: Seitenzahl übernehmen und mit dem Tag [SICHTBAR IM MD] versehen.

– SZENARIO 2 — Seitenzahl nicht ableitbar: Die MD-Zeile enthält keine sichtbare Buchseitenzahl im Umgebungstext. In diesem Fall: Seitenzahl vollständig weglassen, Status [NICHT ABLEITBAR] setzen, und stattdessen ein vollständiges Direktzitat von mindestens 2–3 aufeinanderfolgenden vollständigen Sätzen aus dem Döring-Text angeben. Mattis findet die Seite in Sekunden per PDF-Volltextsuche.

– SZENARIO 3 — Absolut verboten: Seitenzahl aus MD-Zeilennummer hochrechnen, schätzen, interpolieren, aus dem Gedächtnis erinnern oder mit 'ca.' versehen. Niemals. Auch ein gut gemeinter Schätzwert ist schlimmer als kein Wert, weil er Mattis auf die falsche Seite führt.

Direktzitat als Suchanker — Mindestanforderungen:

Jedes Direktzitat muss so gewählt sein, dass es per PDF-Volltextsuche eindeutig auffindbar ist. Das bedeutet konkret:

– Mindestens 2 vollständige, aufeinanderfolgende Sätze aus dem Döring-Text

– Keine generischen Passagen wie 'Die qualitative Forschung ist...' — diese kommen im gesamten Buch viele Male vor

– Spezifische, charakteristische Formulierungen bevorzugen — je einzigartiger die Wortwahl, desto treffgenauer die PDF-Suche

– Bei sehr kurzen Definitionen: den vollständigen definierenden Satz plus mindestens einen Kontextsatz zitieren

3. KONTEXT UND AUSGANGSLAGE

Forschungsfrage: „Welche Rolle spielt KI in der Gründungsphase von B2C-E-Commerce-Startups zur Stärkung des Unit-Profitability-First-Gedankens?“

Projektstand: Einleitung (Prompt 1), Synthese-Plan Literature Review (Prompt 3) und Literature Review (Prompt 3.5) sind abgeschlossen. Prompt 4 startet Phase 3 des Exposé-Projekts: die Vorbereitung des Untersuchungsdesigns (Kapitel 3, ca. 5 Seiten, 30/70 Punkte). Das Untersuchungsdesign ist der methodisch anspruchsvollste Teil des Exposés. Es wird ausschließlich mit Döring (2023) belegt. Jede Entscheidung muss (a) nachvollziehbar aus der Forschungsfrage abgeleitet und (b) mit Döring fundiert sein.

Das Erhebungsinstrument (Abschnitt 3.5) trägt 15 von 70 Punkten — die höchste Einzelwertung der gesamten Prüfungsleistung. Dies bestimmt die Schwerpunktsetzung der Recherche.

Mattis’ vorläufige methodische Einordnungen (aus CLAUDE.md Sektion 9):

– Erkenntnisziel → Grundlagenforschung: weil die FF auf Verständnis und Theorieweiterentwicklung abzielt (Unit-Profitability-First-Theorie wird auf KI/Gründungsphase ausgeweitet), nicht auf Lösung eines Praxisproblems im Auftrag

– Erkenntnisinteresse → Explorativ: weil 'WELCHE ROLLE SPIELT...' eine offene FF ist, wenig Wissenschaft dazu existiert, Theoriebildung das Ziel ist

– Ansatz → Qualitativ mit Mixed-Method-Reflexion: explorative FF verlangt qualitatives Design; Mixed-Method als Vorstudienmodell (qual → quant) reflektieren

Diese Einordnungen sind vorläufig. Aufgabe der Reader-Agents R1 und R2: Döring-fundiert bestätigen, präzisieren oder begründet korrigieren.

4. VERFÜGBARE DATEIEN FÜR DIESEN PROMPT

– CLAUDE.md — Absoluter Vorrang vor allem anderen. Besonders genau: Sektionen 3.3 (Untersuchungsdesign-Bewertungsraster mit allen 7 Aspekten und Punkten), 5.5 (Döring-Navigationstabelle mit Zeilenanfängen — Ausgangspunkt für Reader-Agents, aber kein abschließendes Bild), 6.4 (Pflichtlektüre Phase Untersuchungsdesign), 9 (Mattis' vorläufige Einordnungen), 10.Phase 3 (Arbeitsplan).

– Vorlesungsskript_zur_Aufgabenleistung_.md — Alle Anforderungen des Professors: alle 7 Aspekte mit Punkteverteilung, alle 4 Erhebungsinstrumente mit Vor-/Nachteilen, Hinweise zum weiteren Vorgehen je Instrument, Döring-Seitenverweise des Profs (6.3 S. 169–182; Kap. 7 S. 183–221; Kap. 10 S. 321–424 und S. 525–570). Den gesamten Untersuchungsdesign-Part sehr genau lesen.

– Beispiel_fuer_ein_gutes_Expose.md — Blueprint für Kapitel 3. Analytisch lesen: Wie werden die 7 Aspekte formuliert? Wie werden Döring-Stellen in die Argumentation eingebunden? Welcher Abschnitt ist der umfangreichste (Antwort: 3.5 Erhebungsinstrument)? Welche Zitiertiefe ist Standard?

– output_pymupdf/[Döring-MD-Datei] — ~15.000 Zeilen. Niemals vollständig laden. Zugriff ausschließlich über Reader- und Scout-Agents mit gezielten Grep-Kommandos und eingegrenzten Zeilenbereichen.

5. DEINE AUFGABE UND DIE STRUKTUR DER OUTPUT-DATEI

Erstelle: Synthese_Plan_Untersuchungsdesign.md. Diese Datei ist das vollständig recherchierte, Döring-fundierte Fundament für Prompt 4.5. Sie muss so vollständig sein, dass Prompt 4.5 keinerlei eigenständige Döring-Recherche mehr benötigt.

Verbindliche Struktur der Synthese-Datei (10 Abschnitte):

# Synthese_Plan_Untersuchungsdesign.md

## META

   Forschungsfrage | Projektstand | Agent-Protokoll

   (welcher Agent hat welche Zeilen gelesen, wie viele Funds je Agent)

   Doring-Coverage: welche Zeilenbereiche abgedeckt

   Scout-Zusammenfassung: Kategorien durchsucht, relevante Funds gefunden

## ALLE FUNDS (numeriert, chronologisch)

   FUND #1 ... FUND #N

   Jeder Fund im vollstandigen FUND-Format (siehe Sektion 6)

## 0. Ubergreifende Designkohärenz und Querverbindungen

   Logik aller 7 Aspekte im Zusammenhang

   Querverbindungen aus Doring (z.B. Erkenntnisinteresse <-> Ansatz <-> Instrument)

   Begründungskette: warum passen alle Entscheidungen zusammen?

## 1. Erkenntnisziel [1 Punkt]

   Entscheidung: Grundlagenforschung

   Doring-Fundierung [FUND #X, #Y]

   Begrundungskette (3-5 Satze): warum Grundlagenforschung fur unsere FF?

   Mattis' Einordnung: bestatigt / prazisiert durch [Doring-Stelle]

   Satz-fur-Satz Schreibplan fur 3.1 (erster Teil)

## 2. Erkenntnisinteresse [2 Punkte]

   Entscheidung: Explorativ

   Abgrenzung: warum nicht deskriptiv, warum nicht explanativ?

   Doring-Fundierung inkl. Tabelle [FUND #X]

   Begrundungskette aus aktuellem Forschungsstand

   Mattis' Einordnung: bestatigt / prazisiert

   Satz-fur-Satz Schreibplan fur 3.1 (zweiter Teil)

## 3. Gegenstand [1 Punkt]

   Entscheidung: Empirische Studie

   Doring-Definition + Abgrenzung [FUND #X]

   Begrundungskette

   Schreibplan fur 3.2

## 4. Datengrundlage [1 Punkt]

   Entscheidung: Primäranalyse

   Doring-Definition [FUND #X]

   Begrundungskette: kein geeigneter Sekundardatensatz vorhanden

   Integration in Schreibplan 3.2

## 5. Ansatz [4 Punkte]

   Entscheidung: Qualitativ

   Doring zur qualitativen Forschung [FUND #X]

   Begrundung warum qualitativ bei explorativer FF

   Mixed-Method-Potenzial: Vorstudienmodell qual -> quant

   Doring S. 186 zur Mixed-Method-Definition [FUND #X]

   Mattis' Einordnung: bestatigt / prazisiert

   Satz-fur-Satz Schreibplan fur 3.3

## 6. Untersuchungsobjekte [6 Punkte]

   6.1 Grundgesamtheit

       Definition: Grunder/Entscheidungstrager von B2C-E-Commerce-Startups

       in Grundungsphase mit Kompetenz uber KI-Einsatz

       Doring-Fundierung [FUND #X]

       Begrundungskette

   6.2 Gruppen- vs. Einzelfallentscheidung

       Entscheidung: Gruppenstudie

       Doring-Definitionen beider Typen [FUND #X, #Y]

       Kriterien fur die Entscheidung

   6.3 Stichprobenumfang

       Theoretische Sattigung als Abbruchkriterium

       Doring S. 295-297 [FUND #X]

       Konkrete Schatzung: z.B. 6-10 leitfadengestutzte Experteninterviews

   Satz-fur-Satz Schreibplan fur 3.4

## 7. Erhebungsinstrument [15 Punkte] -- LANGSTER ABSCHNITT

   7.1 Instrument A: Leitfadengestutztes Experteninterview

       Doring-Definition [FUND #X]

       Charakteristika (Strukturiertheit, Befragte, Kontaktart)

       Vorteile fur unsere FF [Doring-Beleg]

       Nachteile [Doring-Beleg]

       Eignung fur explorative, qualitative FF zu KI in B2C-Startups

   7.2 Instrument B: [z.B. Dokumentenanalyse oder Fragebogen]

       Gleiche Struktur wie 7.1

   7.3 Auswahlentscheidung

       Drei klare Auswahlkriterien (kriteriengesteuert)

       Doring zur Auswahllogik [FUND #X]

       Begrundung: warum Instrument A besser als Instrument B?

   7.4 Hinweise zum weiteren Vorgehen

       Vorgehensmodell: Leitfaden erstellen -> Pilotinterview ->

         Aufzeichnung/Transkription -> Kodierung -> Auswertung

       Qualitative Inhaltsanalyse nach Mayring [Doring FUND #X]

       Kodierungslogik: deduktiv + induktiv [Doring FUND #X]

       Softwaregestutzte Auswertung (z.B. NVivo/MAXQDA) [Doring FUND #X]

   Satz-fur-Satz Schreibplan fur 3.5

## 8. SCOUT-FINDINGS: Hidden Gems ausserhalb Prof-Kapitel

   Alle relevanten Doring-Stellen ausserhalb Kap. 6.3, 7, 9, 10

   Jeden Fund im FUND-Format mit Relevanz-Tag SCOUT-FUND

## 9. ZITATIONSMATRIX

   | Fund # | Aspekt | Kap. | MD-Zeile | Buchseite | Status | Direktzitat-Anfang |

## 10. SATZ-FUR-SATZ SCHREIBPLAN KOMPLETT

   3.1 Erkenntnis ziel + Erkenntnisinteresse

   3.2 Gegenstand + Datengrundlage

   3.3 Ansatz (inkl. Mixed-Method)

   3.4 Untersuchungsobjekte

   3.5 Auswahl Erhebungsinstrumente

6. DAS FUND-FORMAT — VERBINDLICHE NOTATION FÜR JEDEN EINZELNEN FUND

Jeder Döring-Fund — ob von R1–R4 oder vom Scout — wird ausnahmslos in diesem Format dokumentiert. Der Scribe-Agent übernimmt das Format unverändert in die Synthese-Datei. Ohne vollständiges FUND-Format ist ein Fund nicht verwendbar.

**FUND #[N] -- [DESIGN-ASPEKT]**

Kapitel:         [z.B. Doring Kap. 7.1 / Kap. 10.2 / Kap. 9]

MD-Zeilen:       ~[XXXX]-[YYYY]   (direkt aus Grep-Output)

Buchseite:       S. [XX]  [SICHTBAR IM MD]

                 ODER:  [NICHT ABLEITBAR -- Direktzitat fur PDF-Suche nutzen]

Seitenstatus:    VERIFIZIERT  /  NICHT ABLEITBAR

Direktzitat:     "[Mindestens 2-3 vollstandige Satze aus dem Doring-Text,

                   spezifisch und charakteristisch genug fur PDF-Volltextsuche]"

Kontext:         [Was steht im umgebenden Abschnitt? Worum geht es insgesamt?]

Transfer auf FF: [Wie passt diese Stelle auf 'Welche Rolle spielt KI

                  in der Grundungsphase von B2C-E-Commerce-Startups...?']

Verwendung fur:  [Erkenntnisziel / Erkenntnisinteresse / Gegenstand /

                  Datengrundlage / Ansatz / Mixed-Method /

                  Untersuchungsobjekte / Erhebungsinstrument / Scout-Fund]

Relevanz:        HOCH / MITTEL / SCOUT-FUND

Pflicht-Erinnerung: Das Direktzitat-Feld ist immer auszufüllen — unabhängig davon, ob die Seitenzahl bekannt ist. Das Direktzitat ist der Suchanker für Mattis im PDF. Ein Fund ohne Direktzitat ist für die Arbeit nicht verwendbar.

7. PFLICHTANFORDERUNGEN AN DIE SYNTHESE-DATEI

A — Inhaltliche Vollständigkeit

– Alle 7 Design-Aspekte plus Erhebungsinstrument in der Datei vollständig abgedeckt

– Erkenntnisziel, Gegenstand, Datengrundlage: mind. 1 Döring-Fund je Aspekt

– Erkenntnisinteresse, Ansatz: mind. 2 Funds je Aspekt (inkl. Abgrenzung)

– Untersuchungsobjekte: mind. 3 Funds (Grundgesamtheit, Gruppen-/Einzelfall, Stichprobenumfang)

– Erhebungsinstrument: mind. 5 Funds (je 2 pro Instrument + Auswahllogik + Auswertungsverfahren)

– Mattis' vorläufige Einordnungen für alle 3 Aspekte Döring-fundiert bestätigt oder präzisiert

– Satz-für-Satz Schreibplan für alle 5 Unterabschnitte (3.1–3.5) vorhanden

– Zitationsmatrix vollständig befüllt

B — Döring-Recherche-Tiefe (Mindeststandards)

– Mindestens 5 verschiedene Grep-Suchbegriffe pro Design-Aspekt — nie nur den naheliegendsten

– Mindestens 100 Zeilen Kontext nach jedem Grep-Treffer lesen (50 vor, 50 nach der Trefferzeile)

– Kapitelübergreifende Querverbindungen aktiv suchen: Döring verknüpft Erkenntnisinteresse mit Ansatz, Ansatz mit Instrument, Instrument mit Auswertung

– Scout-Agent deckt den gesamten Döring-Text ab — alle Kapitel außerhalb der Prof-Navigationstabelle

C — Bewertungsprioritäten

– 15 Punkte: Erhebungsinstrument → größte Recherchetiefe (R3 + R4), längster Abschnitt in der Synthese-Datei

– 6 Punkte: Untersuchungsobjekte → alle drei Teilaspekte ausführlich

– 4 Punkte: Ansatz inkl. Mixed-Method → Begründung nachvollziehbar aus Forschungsstand

– 2 Punkte: Erkenntnisinteresse → klare Abgrenzung zu deskriptiv und explanativ

8. MULTI-AGENT WORKFLOW — DIE SUPERPOWER

8.0 Architektur-Übersicht

Dieser Prompt implementiert einen echten Multi-Agent-Workflow über das Claude Code Task-Tool. Sechs spezialisierte Agents übernehmen klar abgegrenzte Aufgaben. Kein Agent macht mehr als seine definierte Aufgabe.

COORDINATOR (Agent 0)

  |-- liest: CLAUDE.md, Vorlesungsskript, Beispiel-Expose (Kap. 3)

  |-- erstellt: Master Briefing fur alle Agents

  |-- dispatcht PARALLEL via Task-Tool:

  |     |-- Task -> R1  [Doring Kap. 6.3 + 7.1-7.5 | ~Zeile 5892-7200]

  |     |-- Task -> R2  [Doring Kap. 7.6-7.9 + Kap. 9 | ~Zeile 7200-11000]

  |     |-- Task -> R3  [Doring Kap. 10.1-10.2 | ~Zeile 11530-13500]

  |     |-- Task -> R4  [Doring Kap. 10.3+ | ~Zeile 13500-14500+]

  |     +-- Task -> S   [Scout: gesamter Doring-Text, alle Kapitel]

  |

  |-- sammelt alle FUND-Reports -> dispatcht:

  |     +-- Task -> W   [Scribe: schreibt Synthese_Plan_Untersuchungsdesign.md]

  |

  +-- dispatcht abschliessend:

        +-- Task -> Q   [Quality: 10-Punkte-Checkliste, Nachrecherche-Trigger]

8.1 Agent 0: Coordinator

Der Coordinator ist der einzige Agent, der die Rahmendokumente liest. Er liest Döring selbst nicht. Seine Aufgaben:

– Liest vollständig: CLAUDE.md (Sektionen 3.3, 5.5, 6.4, 9, 10.Phase 3), Vorlesungsskript (Untersuchungsdesign-Part komplett), Beispiel-Exposé Kapitel 3 (analytisch)

– Erstellt ein Master Briefing, das ALLE anderen Agents als erste Information erhalten. Inhalt: Forschungsfrage, Mattis' vorläufige Einordnungen, alle 7 Design-Aspekte mit Punkteverteilung, Döring-Navigationstabelle mit Zeilenanfängen, Bewertungsprioritäten, FUND-Format (Sektion 6 dieses Prompts), Seitenangaben-Protokoll (Sektion 2 dieses Prompts)

– Dispatcht alle fünf parallelen Tasks (R1–R4 + Scout) gleichzeitig via Task-Tool

– Sammelt alle zurückgegebenen FUND-Reports vollständig und leitet sie gesammelt an Agent W weiter

– Startet nach Scribe-Abschluss den Quality-Agent Q

– Bei Q-Checkliste mit NEIN-Punkten: dispatcht gezielte Nachrecherche-Tasks und startet W und Q erneut

8.2 Agent R1: Döring Kap. 6.3 + 7.1–7.5 (Zeilen ~5892–7200)

Zuständig für: Theoretischer Hintergrund + Erkenntnisziel + Erkenntnisinteresse + Gegenstand + Datengrundlage + Ansatz (Grundlagen). Erhält Master Briefing vom Coordinator.

– Erkenntnisziel: Grep-Runden mit 'Grundlagenforschung', 'Anwendungsforschung', 'Erkenntnisziel', 'wissenschaftliche Erkenntnis', 'Theorieentwicklung', 'Zweck der Forschung', 'Weiterentwicklung von Theorien'

– Erkenntnisinteresse: Grep-Runden mit 'explorativ', 'Erkenntnisinteresse', 'Theoriebildung als Ziel', 'offene Forschungsfragen', 'wenig untersuchte Zusammenhänge', 'deskriptiv', 'explanativ', 'Entdecken'

– Gegenstand: Grep-Runden mit 'empirische Studie', 'Theoriestudie', 'Methodenstudie', 'Gegenstand der Studie', 'systematische eigene Datenerhebung', 'inhaltliche Forschungsprobleme'

– Datengrundlage: Grep-Runden mit 'Primäranalyse', 'Sekundäranalyse', 'Metaanalyse', 'selbst erhobener Datensatz', 'Primärstudie', 'Datengrundlage'

– Ansatz Grundlagen: Grep-Runden mit 'qualitativ', 'quantitativ', 'Forschungsparadigma', 'Hermeneutik', 'Gegenstandsbeschreibung', 'Theoriebildung qualitativ'

– Querverbindungen aktiv suchen: Verbindet Döring Erkenntnisziel explizit mit Erkenntnisinteresse? Verbindet Döring exploratives Erkenntnisinteresse mit qualitativem Ansatz?

– Liest: mind. 100 Zeilen Kontext pro Treffer. Mind. 5 Suchbegriffe pro Aspekt. Dokumentiert alle relevanten Findings im FUND-Format. Gibt FUND-Reports an Coordinator zurück.

8.3 Agent R2: Döring Kap. 7.6–7.9 + Kap. 9 (Zeilen ~7200–11000)

Zuständig für: Mixed-Methods + Untersuchungsobjekte (Grundgesamtheit, Gruppen-/Einzelfall) + Stichprobenumfang. Erhält Master Briefing vom Coordinator.

– Mixed-Methods: Grep-Runden mit 'Mixed-Methods', 'Vorstudienmodell', 'Vertiefungsmodell', 'Integrationsstrategien', 'qualitativ quantitativ kombinieren', 'Sequenzmodell'. Besonders: Döring S. 186 (vom Prof explizit genannt) — Zeilenbereich um ~6533 systematisch nach Mixed-Method-Definition absuchen.

– Untersuchungsobjekte: Grep-Runden mit 'Grundgesamtheit', 'Einzelfallstudie', 'Fallstudie', 'case study', 'Gruppenstudie', 'Untersuchungseinheiten', 'Population'

– Stichprobenumfang: Grep-Runden mit 'theoretische Sättigung', 'theoretical sampling', 'Stichprobenumfang', 'qualitative Forschung Stichprobengröße', 'Sättigung', 'Fallauswahl'

– Seitenbereich S. 295–297 (vom Prof genannt): Zeilenbereich ~10610 gezielt aufsuchen und vollständig lesen

– Querverbindungen aktiv suchen: Verbindet Döring Stichprobenlogik explizit mit qualitativer Forschung? Verbindet Döring Mixed-Method mit Erkenntnisinteresse?

– Liest: mind. 100 Zeilen Kontext pro Treffer. Mind. 5 Suchbegriffe pro Aspekt. FUND-Format. Rückgabe an Coordinator.

8.4 Agent R3: Döring Kap. 10.1–10.2 (Zeilen ~11530–13500)

Zuständig für: Beobachtung (vollständig) + Interview (vollständig, inkl. aller Durchführungsdetails und Auswertungsverfahren). R3 liest am tiefsten: Das Interview-Kapitel trägt direkt zu den 15 Punkten des Erhebungsinstruments bei. Seitenbereich S. 321–424 (vom Prof genannt). Erhält Master Briefing vom Coordinator.

– Beobachtung: Grep-Runden mit 'Beobachtung', 'Beobachtungsprotokoll', 'verdeckt', 'teilnehmend', 'strukturiert Beobachtung', 'Beobachtungseffekt'

– Interview Definition: Grep-Runden mit 'Experteninterview', 'leitfadengestützt', 'halbstrukturiert', 'Leitfaden', 'niedrigschwellig', 'Informationsdichte', 'subjektives Erleben'

– Interview Durchführung: Grep-Runden mit 'Interviewleitfaden erstellen', 'Pilotinterview', 'Pretest', 'Aufzeichnung', 'Transkription', 'Interviewerfühler', 'soziale Erwünschtheit'

– Interview Auswertung: Grep-Runden mit 'Qualitative Inhaltsanalyse', 'Mayring', 'thematische Kodierung', 'deduktiv', 'induktiv', 'Auswertungsverfahren Interview', 'NVivo', 'MAXQDA'

– Mindestens 150 Zeilen Kontext pro relevantem Treffer (höhere Tiefe wegen 15-Punkte-Gewichtung)

– FUND-Format. Rückgabe an Coordinator.

8.5 Agent R4: Döring Kap. 10.3+ (Zeilen ~13500—14500+)

Zuständig für: Fragebogen (vollständig) + Dokumentenanalyse + alle weiteren Erhebungsinstrumente + Auswertungsverfahren + Auswahllogik Instrument. Seitenbereich S. 525–570 (vom Prof genannt). Erhält Master Briefing vom Coordinator.

– Fragebogen: Grep-Runden mit 'Fragebogen', 'schriftliche Befragung', 'survey', 'Fragebogenkonstruktion', 'Skalierung', 'Rücklaufquote', 'Online-Befragung', 'Anonymität'

– Dokumentenanalyse: Grep-Runden mit 'Dokumentenanalyse', 'Textanalyse', 'Diskursanalyse', 'Kodierung Dokument', 'Inhaltsanalyse Dokument', 'Art des Materials'

– Seitenbereich S. 525–570: Zeilenbereich ~13500+ gezielt aufsuchen und vollständig lesen

– Auswahllogik Instrument: Grep-Runden mit 'Auswahl Erhebungsmethode', 'Eignung Instrument', 'Forschungsgegenstand Methode', 'Kriterien Methodenwahl', 'Passung Methode'

– Auswertungsverfahren: Grep-Runden mit 'Grounded Theory', 'Kategorien', 'Mustererkennung', 'Diskursanalyse Auswertung', 'Kodierungslogik'

– Mindestens 150 Zeilen Kontext pro relevantem Treffer. FUND-Format. Rückgabe an Coordinator.

8.6 Agent S: Scout — Hidden Gems außerhalb der Prof-Kapitel

Der Scout durchsucht den gesamten Döring-Text (~15.000 Zeilen) nach relevantem Inhalt AUSSERHALB der vom Prof genannten Kapitel (6.3, 7, 9, 10). Die Prof-Navigationstabelle ist ein hilfreicher Ausgangspunkt — aber kein vollständiges Bild aller relevanten Döring-Inhalte. Es können relevante Definitionen, Gütekriterien, Methodendetails oder Ethik-Hinweise in anderen Kapiteln stehen, die das Untersuchungsdesign qualitativ erheblich verbessern. Diese zu finden ist die einzige Aufgabe des Scouts.

Der Scout verwendet mindestens 35 Suchbegriffe aus 8 Kategorien. Pro relevantem Treffer: mindestens 150 Zeilen Kontext lesen. Irrelevante Treffer verwerfen. Relevante Treffer im FUND-Format mit Relevanz-Tag SCOUT-FUND dokumentieren. Erhält Master Briefing vom Coordinator.

Suchbegriff-Katalog des Scout (mindestens diese 35 Begriffe):

Kategorie 1 — Gütekriterien qualitativer Forschung:

– 'Gütekriterien', 'Validität qualitativ', 'Reliabilität qualitativ', 'kommunikative Validierung', 'Reflexivität', 'member checking', 'Glaubwürdigkeit', 'Übertragbarkeit'

Kategorie 2 — Sampling-Strategien (Details außerhalb Kap. 9):

– 'purposive sampling', 'Schlüsselinformant', 'Expertenauswahl', 'Gate-Keeper', 'Feldzugang', 'Snowball-Sampling', 'Zugang zur Stichprobe'

Kategorie 3 — Interview-Details (außerhalb Kap. 10):

– 'Forschungstagebuch', 'Interviewereinfluss', 'Anonymisierung Interview', 'Interviewbereitschaft', 'virtuelles Interview', 'Online-Interview'

Kategorie 4 — Analyse- und Auswertungsmethoden:

– 'Inhaltsanalyse', 'Mayring', 'Grounded Theory', 'Kodierung', 'Interrater', 'Konsensmethode', 'Kategorien bilden', 'Musteranalyse'

Kategorie 5 — Mixed-Methods Details:

– 'Konvergenzmodell', 'Einbettungsmodell', 'Integration qualitativ quantitativ', 'Paradigmenstreit', 'Sequenzmodell Mixed'

Kategorie 6 — Forschungsethik:

– 'Forschungsethik', 'Datenschutz Studie', 'Einwilligung', 'informierte Zustimmung', 'Vertraulichkeit', 'Anonymisierung'

Kategorie 7 — Digitaler und Innovationskontext:

– 'Innovation Forschung', 'digitale Methode', 'Technologie Studie', 'Online-Erhebung', 'virtuelle Datenerhebung'

Kategorie 8 — Forschungsdesign Kohärenz:

– 'Kohärenz Forschungsdesign', 'Stringenz', 'externe Validität', 'Transparenz Forschung', 'Nachvollziehbarkeit', 'Forschungsprozess Qualität'

Alle Scout-Treffer: Seitenstatus nach Protokoll Sektion 2 prüfen. Direktzitat zwingend. Transfer auf Forschungsfrage prüfen. Als SCOUT-FUND dokumentieren und an Coordinator zurückgeben.

8.7 Agent W: Scribe

Der Scribe hat genau eine Aufgabe: Alle gesammelten FUND-Reports der Agents R1–R4 und Scout in die Synthese_Plan_Untersuchungsdesign.md giessen. Er trifft keine eigenen Forschungsentscheidungen, liest Döring nicht eigenständig und interpretiert nicht. Er ist ausschließlich Dokumentations-Agent.

– Empfängt: alle FUND-Reports, gesammelt vom Coordinator

– Schreibt: META-Abschnitt (Agent-Protokoll: wer hat was gelesen, wie viele Funds)

– Schreibt: alle Funds chronologisch und nummeriert in Abschnitt 'ALLE FUNDS'

– Befüllt: alle Design-Aspekt-Abschnitte (1–7) mit Entscheidungen, Begründungsketten und Verweisen auf FUND #N — kein Duplizieren des Direktzitats, nur Verweis

– Befüllt: Abschnitt 8 SCOUT-FINDINGS mit allen Scout-Funds

– Befüllt: Zitationsmatrix (Abschnitt 9) vollständig für jeden Fund

– Schreibt: vollständigen Satz-für-Satz Schreibplan (Abschnitt 10) für alle fünf Unterabschnitte 3.1–3.5

– Prüft: Ist Abschnitt 7 Erhebungsinstrument der längste Abschnitt der Datei? Falls nicht: Signal an Coordinator für Nachrecherche durch R3/R4

8.8 Agent Q: Quality

Der Quality-Agent liest die fertige Synthese-Datei vollständig durch und führt die folgende Checkliste mit explizitem JA oder NEIN je Punkt durch. Bei einem oder mehreren NEIN: Coordinator dispatcht gezielte Nachrecherche-Tasks und der Scribe ergänzt die Datei.

– (1) Alle 7 Design-Aspekte + Erhebungsinstrument vollständig in der Datei? (JA/NEIN)

– (2) Mindest-Fund-Anzahl je Aspekt erfüllt (Erhebungsinstrument mind. 5 Funds)? (JA/NEIN)

– (3) Jeder einzelne Fund enthält ein vollständiges Direktzitat (mind. 2 Sätze)? (JA/NEIN)

– (4) Kein Fund mit geschätzter, hochgerechneter oder errechneter Seitenzahl? (JA/NEIN)

– (5) Alle Funds im vollständigen 9-Felder-FUND-Format? (JA/NEIN)

– (6) Mattis’ drei vorläufige Einordnungen Döring-fundiert bestätigt oder präzisiert? (JA/NEIN)

– (7) Scout-Sektion vorhanden mit mind. 5 SCOUT-FUNDS? (JA/NEIN)

– (8) Satz-für-Satz Schreibplan für 3.1–3.5 vollständig? (JA/NEIN)

– (9) Zitationsmatrix vollständig befüllt (alle Funds eingetragen)? (JA/NEIN)

– (10) Erhebungsinstrument-Abschnitt (7) längster Abschnitt der Datei? (JA/NEIN)

10 von 10 JA → Synthese-Datei wird gespeichert. Ein oder mehrere NEIN → Coordinator dispatcht Nachrecherche, Scribe ergänzt, Quality wiederholt Prüfung.

9. RECHERCHE-TIEFE-PROTOKOLL — FÜR ALLE READER-AGENTS VERBINDLICH

Dieses Protokoll gilt für jeden einzelnen Grep-Lauf jedes Reader-Agents sowie für den Scout. Es ist nicht verhandelbar.

– Regel 1 — Kontext ist Pflicht: Nach jedem Grep-Treffer mindestens 100 Zeilen lesen (50 vor dem Treffer, 50 nach dem Treffer). Ausnahme Scout: 150 Zeilen. Döring erklärt Begriffe oft über mehrere Absätze; eine isolierte Trefferzeile reicht nie.

– Regel 2 — Mehrere Runden: Pro Design-Aspekt mindestens 5 verschiedene Suchbegriffe in separaten Grep-Läufen. Synonyme, Unterbegriffe, verwandte Konzepte aktiv einsetzen. Erst nach 5+ Runden gilt ein Aspekt als ausreichend recherchiert.

– Regel 3 — Kapitelübergreifend: Erkenntnisinteresse und Ansatz sind bei Döring verknüpft. Ansatz und Erhebungsinstrument hängen zusammen. Stichprobenlogik und qualitative Forschung sind verbunden. Diese Verknüpfungen aktiv suchen und in den Begründungsketten verwenden.

– Regel 4 — Transfer sofort: Bei jedem Treffer sofort prüfen und im FUND festhalten: Wie genau passt diese Döring-Stelle auf unsere Forschungsfrage „Welche Rolle spielt KI in der Gründungsphase von B2C-E-Commerce-Startups zur Stärkung des Unit-Profitability-First-Gedankens?“

– Regel 5 — Seitenstatus vor jedem Fund: Bevor ein Fund dokumentiert wird, den Seitenstatus bestimmen (VERIFIZIERT / NICHT ABLEITBAR). Niemals schätzen. Immer Direktzitat. Keine Ausnahme.

10. QUALITÄTSKONTROLLE — DURCH AGENT Q

Die 10-Punkte-Checkliste von Agent Q ist in Sektion 8.8 vollständig spezifiziert. Hier nochmals die zwei kritischsten Punkte, die besondere Aufmerksamkeit verdienen:

– Kein Fund ohne Direktzitat: Dieser Punkt ist nicht verhandelbar. Ohne Direktzitat kann Mattis die Stelle im PDF nicht finden. Ein Fund ohne Direktzitat wird vom Scribe als unvollständig markiert und triggert sofort eine Nachrecherche.

– Kein Fund mit geschätzter Seitenzahl: Dieser Punkt ist nicht verhandelbar. Eine falsche Seitenzahl führt Mattis auf die falsche PDF-Seite. Lieber [NICHT ABLEITBAR] mit perfektem Direktzitat als eine schätzungsbasierte Seitenzahl.

11. ÜBERGREIFENDE ARBEITSWEISE

– Kein Schritt überspringen — die Agents laufen in der definierten Reihenfolge (Coordinator -> parallel R1-R4 + Scout -> Scribe -> Quality).

– Der Scout ist keine optionale Erweiterung, sondern Pflicht. Die Prof-Navigationstabelle deckt nicht alle relevanten Döring-Inhalte ab.

– Das Seitenangaben-Protokoll (Sektion 2) gilt für jeden einzelnen Fund ohne Ausnahme.

– Das FUND-Format (Sektion 6) gilt für jeden einzelnen Fund ohne Ausnahme.

– R3 und R4 zusammen erhalten die größte Recherchetiefe, weil das Erhebungsinstrument 15/70 Punkten trägt.

– CLAUDE.md hat Vorrang vor diesem Prompt und vor allen anderen Dokumenten.

– Der Output ist ausschließlich Synthese_Plan_Untersuchungsdesign.md — kein fertiger Untersuchungsdesign-Text.

– Die Synthese-Datei muss so vollständig sein, dass Prompt 4.5 (Schreiben des Untersuchungsdesigns) keinerlei eigenständige Döring-Recherche mehr benötigt.