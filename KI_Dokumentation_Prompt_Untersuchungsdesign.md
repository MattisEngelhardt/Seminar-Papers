# KI-Dokumentation: Erstellung Kapitel 3 — Untersuchungsdesign

## Gesamtprompt zur Dokumentation des KI-gestützten Arbeitsprozesses

**KI-Tool:** Claude Code (Claude Opus 4)
**Einsatzzweck:** Inhaltsgenerierung — Kapitel 3 des Exposés (Untersuchungsdesign, ca. 5 Seiten, 30/70 Punkte)
**Forschungsfrage:** *„Welche Rolle spielt KI in der Gründungsphase von B2C-E-Commerce-Startups zur Stärkung des Unit-Profitability-First-Gedankens?"*

---

## Überblick: 7 Phasen von der Quelle zum fertigen DOCX

| Phase | Beschreibung | Ergebnis |
|-------|-------------|----------|
| 1 | 5 KI-Agenten durchforsten Döring (~1.100 Buchseiten) parallel | 89 Direktzitate (FUNDS) |
| 2 | Selektion der 50 besten FUNDS nach Abdeckung und Redundanz | Kuratierte FUND-Sammlung |
| 3 | Erstfassung des Fließtexts auf Basis der 50 FUNDS | ~2.124 Wörter |
| 4 | Manuelle Seitenzahlen-Verifizierung (42 Belege per PDF-Suche) | Alle Seitenangaben bestätigt |
| 5 | Kritische Review: Zitatqualität (Stufe 1/2/3), Wortbudgets, Fixes | Übergabedokument mit Arbeitsanweisungen |
| 6 | Simultane Kompression (~30%) UND Qualitätssteigerung | ~1.468 Wörter, Transfers statt Definitionen |
| 7 | DOCX-Produktion: XML-Insertion in bestehendes Exposé | Fertiges Word-Dokument |

---

## PHASE 1: Systematische Quellenextraktion — 5 parallele Agenten

### Aufgabenstellung

Die Döring-Quelle (*Forschungsmethoden und Evaluation in den Sozial- und Humanwissenschaften*, 2023) umfasst ~1.100 Buchseiten (~40.254 Zeilen als Markdown). Um die gesamte Quelle systematisch zu durchforsten, wurden 5 spezialisierte KI-Agenten parallel eingesetzt, die jeweils unterschiedliche Kapitel abdeckten.

### Agenten-Zuteilung

| Agent | Kapitelbereich | Döring-Seiten | Zuständig für | Extrahierte FUNDS |
|-------|---------------|---------------|---------------|-------------------|
| **R1** (agent4) | Kap. 6.3 + Kap. 7 | S. 169–221 | Alle 7 Design-Aspekte: Erkenntnisziel, -interesse, Gegenstand, Datengrundlage, Ansatz, Mixed-Method, Untersuchungsobjekte | 23 |
| **R2** (agent1) | Kap. 8 + Kap. 9 | S. 224–320 | Grundgesamtheit, Stichproben, Gruppenstudie, Theoretische Sättigung | 14 |
| **R3** (agent5) | Kap. 10.1–10.2 | S. 323–392 | Beobachtung (verworfene Alternative), Interview (gewähltes Instrument) | 25 |
| **R4** (agent3) | Kap. 10.3–10.6, 11, 12.1 | S. 393–600 | Fragebogen (Kontrast), Dokumentenanalyse (Kontrast), Transkription, Qualitative Analyse, Software | 19 |
| **Scout** (agent2) | Kap. 1–6.2, 12.2–19 | S. 3–168, 601–1059 | Paradigma, Gütekriterien, Grundlagenforschung, Forschungsethik, KI-Bezug | 8 |

**Kernprinzip:** Inhalt vor Seitenzahlen. Jeder Agent extrahierte 2–3 vollständige Sätze pro FUND als Direktzitat — spezifisch genug für spätere PDF-Volltextsuche zur Seitenverifikation. Jeder FUND enthielt zusätzlich einen Transfer auf die eigene Forschungsfrage.

### FUND-Format (einheitlich für alle Agenten)

```
**FUND #[N] — [DESIGN-ASPEKT]**
Kapitel:         Döring Kap. [X.Y]
MD-Zeilen:       ~[XXXX]–[YYYY]
Buchseite:       S. [XX] (falls sichtbar)
Direktzitat:     "[Mind. 2–3 vollständige Sätze]"
Kontext:         [Worum geht es im Abschnitt?]
Transfer auf FF: [Konkret: Wie passt das auf KI + B2C-E-Commerce-Startups + Unit Profitability?]
Verwendung für:  [Design-Aspekt]
```

### Suchstrategie pro Agent

Jeder Agent verwendete mindestens 7 Grep-Suchbegriffe pro Design-Aspekt. Beispiele:

- **Erkenntnisziel:** `Grundlagenforschung`, `Anwendungsforschung`, `Erkenntnisziel`, `Theorieentwicklung`, `wissenschaftliche Erkenntnis`, `grundlagenwissenschaftlich`, `anwendungswissenschaftlich`
- **Erkenntnisinteresse:** `explorativ`, `Erkenntnisinteresse`, `Theoriebildung`, `offene Forschungsfragen`, `deskriptiv`, `explanativ`, `wenig untersuchte Zusammenhänge`
- **Erhebungsinstrument:** `Experteninterview`, `leitfadengestützt`, `halbstrukturiert`, `Informationsdichte`, `subjektives Erleben`, `Interviewereinfluss`, `soziale Erwünschtheit`, `Pilotinterview`, `Transkription`, `Mayring`, `Kodierung`

Lesetiefe: 100–150 Zeilen Kontext pro Treffer. Prof-Kernkapitel (6.3, 7, 10) komplett durchgelesen, nicht nur Grep-Treffer.

---

## PHASE 2: Selektion — 50 FUNDS aus 89

### Selektionskriterien

1. **Maximale Abdeckung** aller 7 Blöcke des Untersuchungsdesigns + Erhebungsinstrument-Dreischritt
2. **Keine Redundanz** — jedes Zitat trägt eindeutig neuen Inhalt bei
3. **Direkte Anwendbarkeit** auf die Forschungsfrage
4. **Belegkraft** — Zitat muss eine methodische Entscheidung stützen oder definieren

### Verteilung der 50 selektierten FUNDS

| Block | Thema | Punkte | Anz. FUNDS | Quell-Agenten |
|-------|-------|--------|------------|---------------|
| 0 | Rahmung (Sensibilisierende Konzepte, Paradigma) | — | 4 | R1 + Scout |
| 1 | Erkenntnisziel: Grundlagenforschung | 1 | 3 | R1 + Scout |
| 2 | Erkenntnisinteresse: Explorativ | 2 | 3 | R1 |
| 3 | Gegenstand: Empirische Studie | 1 | 2 | R1 |
| 4 | Datengrundlage: Primäranalyse | 1 | 2 | R1 |
| 5 | Ansatz: Qualitativ + Mixed-Method | 2+2 | 5 | R1 |
| 6 | Untersuchungsobjekte | 3+3 | 9 | R1 + R2 |
| 7 | **Erhebungsinstrument** | **15** | **19** | R3 + R4 |
| 8 | Scout-Findings (Gütekriterien, Ethik) | — | 3 | Scout |
| **Gesamt** | | **30** | **50** | |

### Selektierte FUNDS nach Block — Vollständige Liste

**BLOCK 0 — Rahmung:**
| # | Quelle | Thema | Seite |
|---|--------|-------|-------|
| 1 | R1 #22 | Untersuchungsdesign als Gesamtbegriff, 9 Klassifikationskriterien | S. 185 |
| 2 | R1 #21 | Sensibilisierende Konzepte in explorativer Forschung | S. 169 |
| 3 | Scout #1 | Qualitatives Paradigma: Theorieentdeckung, induktive Logik | S. 64–67 |
| 4 | Scout #2 | Zirkularität und Flexibilität des qualitativen Forschungsprozesses | S. 68 |

**BLOCK 1 — Erkenntnisziel: Grundlagenforschung:**
| # | Quelle | Thema | Seite |
|---|--------|-------|-------|
| 5 | R1 #1 | Definition Grundlagenforschung | S. 187 |
| 6 | R1 #3 | Entscheidungskriterium: wann Grundlagenforschung wählen | S. 188 |
| 7 | Scout #6 | Dreigliedrige Abgrenzung Grundlagen-/Interventions-/Evaluationsforschung | S. 953–954 |

**BLOCK 2 — Erkenntnisinteresse: Explorativ:**
| # | Quelle | Thema | Seite |
|---|--------|-------|-------|
| 8 | R1 #4 | Definition Explorative Studie | S. 192 |
| 9 | R1 #5 | Explorative Studie als qualitatives Design, Offenheit für unerwartete Befunde | S. 192/193 |
| 10 | R1 #7 | Abgrenzung Explorativ von Deskriptiv und Explanativ | S. 192/193 |

**BLOCK 3 — Gegenstand: Empirische Studie:**
| # | Quelle | Thema | Seite |
|---|--------|-------|-------|
| 11 | R1 #8 | Definition Empirische Studie | S. 188 |
| 12 | R1 #9 | Entscheidungskriterium: Originalstudie bei Qualifikationsarbeiten | S. 193 |

**BLOCK 4 — Datengrundlage: Primäranalyse:**
| # | Quelle | Thema | Seite |
|---|--------|-------|-------|
| 13 | R1 #10 | Definition Primäranalyse als typischer Fall | S. 193 |
| 14 | R1 #11 | Entscheidungskriterien Primäranalyse vs. Metaanalyse | S. 194 |

**BLOCK 5 — Ansatz: Qualitativ + Mixed-Method: Vorstudienmodell:**
| # | Quelle | Thema | Seite |
|---|--------|-------|-------|
| 15 | R1 #12 | Definition Qualitativer Forschungsansatz | S. 185 |
| 16 | R1 #13 | Entscheidungskriterium: wann qualitatives Design wählen | S. 187 |
| 17 | R1 #15 | Vorstudienmodell: qual → quant | S. 187 |
| 18 | R1 #16 | Vertiefungsmodell: quant → qual (Kontrast) | S. 187 |
| 19 | R1 #17 | Entscheidungskriterien Mixed-Methods (Ressourcen, Vorkenntnisse) | S. 187 |

**BLOCK 6 — Untersuchungsobjekte:**
| # | Quelle | Thema | Seite |
|---|--------|-------|-------|
| 20 | R1 #18 | Gruppenstudie vs. Einzelfallstudie Definition | S. 216 |
| 21 | R1 #19 | Entscheidungskriterien Gruppenstudie | S. 218 |
| 22 | R2 #1 | Grundgesamtheit/Population: Definition Zielpopulation | S. 294 |
| 23 | R2 #2 | Pragmatische Eingrenzung: manifeste, operationalisierbare Merkmale | S. 294 |
| 24 | R2 #7 | Qualitative Stichproben: absichtsvolle Auswahl (purposive sampling) | S. 303 |
| 25 | R2 #8 | Theoretische Stichprobe: schrittweise Fallauswahl | S. 303–304 |
| 26 | R2 #9 | Theoretische Sättigung als Abbruchkriterium | S. 304–305 |
| 27 | R2 #11 | Homogene gezielte Stichprobe für spezielle Zielgruppen | S. 306 |
| 28 | R2 #14 | Schneeballverfahren für schwer erreichbare Populationen | S. 310–311 |

**BLOCK 7 — Erhebungsinstrument (15/70 Punkte, größter Block):**

*7a — Instrument A: Beobachtung (verworfen):*
| # | Quelle | Thema | Seite |
|---|--------|-------|-------|
| 29 | R3 #1 | Beobachtung Definition + Außenperspektive | S. 324 |
| 30 | R3 #2 | Grenzen der Beobachtbarkeit: subjektive Phänomene nicht zugänglich | S. 325 |

*7b — Instrument B: Leitfadengestütztes Experteninterview (gewählt):*
| # | Quelle | Thema | Seite |
|---|--------|-------|-------|
| 31 | R3 #5 | Interview Definition: wichtigste qualitative Datenerhebungstechnik | S. 353 |
| 32 | R3 #6 | Vorteile: Zugang zu subjektivem Erleben, Flexibilität | S. 353–354 |
| 33 | R3 #7 | Nachteile: Zeitaufwand, soziale Erwünschtheit, Reaktivität | S. 354 |
| 34 | R3 #9 | Informationsdichte: Interview bei komplexen Sachverhalten überlegen | S. 354 |
| 35 | R3 #11 | Leitfaden-Interview: Vergleichbarkeit + Flexibilität | S. 368 |
| 36 | R3 #12 | Leitfaden Umfang: 1–2 Seiten, 8–15 offene Fragen | S. 368–369 |
| 37 | R3 #16 | Experteninterview: Definition, Spezialwissen, Rollengestaltung | S. 372 |
| 38 | R3 #17 | Praxis-/Handlungswissen: schwer verbalisierbar, nur im Interview zugänglich | S. 371 |

*7c — Begründete Auswahl + Kontrast zu Fragebogen/Dokumentenanalyse:*
| # | Quelle | Thema | Seite |
|---|--------|-------|-------|
| 39 | R4 #1 | Fragebogen: fehlende Tiefe, keine längeren Erzählungen | S. 393–394 |
| 40 | R4 #2 | Fragebogen: erfordert Vorwissen, ungeeignet für explorative FF | — |
| 41 | R4 #4 | Dokumentenanalyse: Definition + Nonreaktivität | S. 525–526 |
| 42 | R4 #7 | Dokumentenanalyse: fehlende Kontextinformationen | S. 530–531 |

*7d — Hinweise zum weiteren Vorgehen:*
| # | Quelle | Thema | Seite |
|---|--------|-------|-------|
| 43 | R3 #25 | 10-Schritte-Ablauf qualitativer Interviewstudie | S. 362–365 |
| 44 | R3 #21 | Transkription: verbatim, 5–8h pro Stunde | S. 362–363 |
| 45 | R4 #15 | Mayring: induktiv-deduktive Qualitative Inhaltsanalyse | S. 533–534 |
| 46 | R4 #16 | Kodierung: fallbezogen + fallübergreifend | S. 592–593 |
| 47 | R4 #18 | MAXQDA/NVivo: QDA-Software | S. 597–599 |

**BLOCK 8 — Scout-Findings:**
| # | Quelle | Thema | Seite |
|---|--------|-------|-------|
| 48 | Scout #3 | Lincoln & Guba: 4 Gütekriterien (Trustworthiness) | S. 109–110 |
| 49 | Scout #4 | Steinke: 7 Kernkriterien, intersubjektive Nachvollziehbarkeit | S. 111–114 |
| 50 | Scout #8 | Forschungsethik: informierte Einwilligung, Anonymisierung | S. 121–123 |

### Redundanz-Logik — Warum 39 FUNDS verworfen wurden

Beispiele der Verwerfungsgründe:
- R1 #2 (Boxdefinition Grundlagenforschung): Überlappt mit #1, gleicher Inhalt kompakter
- R1 #14 (Qualitativ Theoriebildung): Überlappt mit #12, gleiche Argumentation
- R2 #5, #6 (Gruppenstudie): Überlappt mit R1 #18/#19
- R3 #3, #4 (Qualitative Beobachtung Details): #1 und #2 decken Verwerfung ab
- R3 #13, #14 (Probe-Interview, Fragen-Reihenfolge): Details für Durchführung, nicht für Blueprint
- R4 #3 (Fragebogen Reaktivität): Überlappt mit #1
- R4 #5, #6, #8, #9, #10 (Dokumentenanalyse Details): #4 und #7 decken Definition + Verwerfung ab

---

## PHASE 3: Erstfassung des Fließtexts

### Design-Entscheidungen (feststehend vor dem Schreiben)

| Aspekt | Entscheidung | Begründungstyp | Döring-Kapitel |
|--------|-------------|---------------|----------------|
| Erkenntnisziel | Grundlagenforschung | **Typ A** (aus FF) | Kap. 7.2 |
| Erkenntnisinteresse | Explorativ | **Typ B** (aus Forschungsstand) | Kap. 7.5 |
| Gegenstand | Empirische Studie (Originalstudie) | **Typ A** (aus FF) | Kap. 7.3 |
| Datengrundlage | Primäranalyse | **Typ B** (aus Forschungsstand) | Kap. 7.4 |
| Ansatz | Qualitativ | **Typ B** (aus Forschungsstand) | Kap. 7.1 |
| Mixed-Method | Vorstudienmodell (qual → quant) | **Typ A** (aus FF) | Kap. 7.1 |
| Untersuchungsobjekte (GG) | B2C-E-Commerce-Gründer, 0–3 Jahre, KI-Einsatz | **Typ A** (aus FF + Wissensstand) | Kap. 9.1 |
| Untersuchungsobjekte (Typ) | Gruppenstudie | **Typ A** (aus FF) | Kap. 7.9 |
| Stichprobe | 6–10 Interviews, theoretische Sättigung, Schneeballverfahren | — | Kap. 9.2 |
| Instrument A (verworfen) | Wissenschaftliche Beobachtung | — | Kap. 10.1 |
| Instrument B (gewählt) | Leitfadengestütztes Experteninterview | — | Kap. 10.2 |
| Auswertung | Qualitative Inhaltsanalyse nach Mayring, deduktiv-induktiv | — | Kap. 12.1 |
| Software | MAXQDA | — | Kap. 12.1.3 |

### Zwei Begründungstypen (aus der Bewertungsrubrik des Professors)

- **Typ A — „leitet sich logisch aus der Forschungsfrage ab":** Erkenntnisziel (1P), Gegenstand (1P), Mixed-Method (2P), Grundgesamtheit (3P)
- **Typ B — „ergibt sich nachvollziehbar aus dem aktuellen Forschungsstand":** Erkenntnisinteresse (2P), Datengrundlage (1P), Ansatz (2P)

### Dreischritt beim Erhebungsinstrument (15/70 Punkte — höchste Einzelwertung)

1. Zwei Instrumente definieren und Eignung begründen (Beobachtung + Experteninterview)
2. Begründete Auswahl eines der beiden (Experteninterview), unter Beachtung des bislang definierten Designs
3. Hinweise zum weiteren Vorgehen (Vorgehensmodell, Leitfadenerstellung, Transkription, Auswertung nach Mayring)

### Schreibregeln

- Ausschließlich Döring (2023) zitieren, Format: (vgl. Döring, 2023, S. XX)
- Keine inhaltlichen Quellen (die 10 englischen) im Untersuchungsdesign verwenden
- Jede Entscheidung definieren, auf die eigene Forschungsfrage übertragen und mit Döring belegen
- Die Forschungsfrage nicht inhaltlich beantworten — nur das methodische Vorgehen beschreiben
- Präzise Seitenangaben (nicht „f.", „ff." oder Bereiche wie „S. 3–6")
- Sensibilisierende Konzepte (Döring, S. 169) als Brücke zwischen Literature Review und Untersuchungsdesign einbauen

### Ergebnis der Erstfassung

~2.124 Wörter mit ~45 Döring-Belegen, Gliederung 3.1–3.5.

---

## PHASE 4: Seitenzahlen-Verifizierung

### Methode

Für jeden der 42 Döring-Belege im Text wurde ein eindeutiger Suchbegriff (Döring-Direktzitat) identifiziert. Diese Suchbegriffe wurden dann per Strg+F im Döring-PDF gesucht und die korrekte Buchseitenzahl notiert.

### Verifizierungstabelle (42 Belege)

| Nr. | Abschnitt | Suchbegriff im PDF | Aktuelle S. | Korrekte S. |
|-----|-----------|-------------------|-------------|-------------|
| 1 | Einl. Kap. 3 | „Das Untersuchungsdesign [...] charakterisiert ganz allgemein die methodische Vorgehensweise einer Studie" | 185 | **184** |
| 2 | 3.1 | „Eine Untersuchung kann darauf abzielen, wissenschaftliche Probleme zu lösen [...] eine solche Grundlagenforschung" | 187 | **187** |
| 3 | 3.1 | „Während die Grundlagenforschung Theorien entwickelt und überprüft, die dazu dienen, Sachverhalte zu beschreiben, zu erklären und vorherzusagen" | 953–954 | **953** |
| 4 | 3.1 | „Die explorative Studie [...] dient der genauen Erkundung und Beschreibung eines Sachverhaltes mit dem Ziel, wissenschaftliche Forschungsfragen, Hypothesen und Theorien zu entwickeln" | 192 | **194** |
| 5 | 3.1 | „Die explanative Studie [...] dient der Überprüfung vorher aufgestellter Hypothesen" | 192–193 | **194** |
| 6 | 3.1 | „Explorative Studien werden oft als nicht oder wenig strukturierte qualitative Studien durchgeführt [...] da dieses Vorgehen offen ist für unerwartete Befunde" | 192 | **194** |
| 7 | 3.2 | „Die empirische Studie [...] dient der Lösung von inhaltlichen Forschungsproblemen auf der Basis systematischer eigener Datenerhebung" | 188 | **188** |
| 8 | 3.2 | „In den Human- und Sozialwissenschaften fällt bei Qualifikationsarbeiten die Wahl meist auf [...] eine Originalstudie" | 193 | **193** |
| 9 | 3.2 | „Bei der Primärstudie [...] werden die empirischen Daten selbst erhoben und anschließend analysiert" | 193 | **193** |
| 10 | 3.2 | „Avisieren Sie eine Metaanalyse, wenn zum interessierenden Forschungsproblem bereits eine Reihe hochwertiger [...] Studien durchgeführt wurden" | 194 | **194** |
| 11 | 3.3 | „Im qualitativen Forschungsansatz [...] werden offene Forschungsfragen an wenigen Untersuchungseinheiten sehr detailliert [...] untersucht. Ziel ist eine Gegenstandsbeschreibung samt Theoriebildung" | 185 | **186** |
| 12 | 3.3 | „Wählen Sie ein qualitatives Untersuchungsdesign, wenn Sie [...] einen neuen Gegenstand erkunden und eine Hypothese oder Theorie entwickeln wollen" | 187 | **187** |
| 13 | 3.3 | „Der qualitative Forschungsansatz folgt primär einer theorieentdeckenden Forschungslogik, wobei das induktive, datengestützte Vorgehen besonders wichtig ist" | 64–67 | **25** |
| 14 | 3.3 | „In der qualitativen Forschung spricht man [...] von 'sensibilisierenden Konzepten'" | 169 | **169** |
| 15 | 3.3 | „Beim Vorstudienmodell [...] dient eine qualitative Studie als Vorstudie dazu, Hypothesen zu generieren" | 187 | **186** |
| 16 | 3.3 | „Wählen Sie bevorzugt ein Mixed-Methods-Design, wenn Sie [...] über solide Vorkenntnisse sowohl in qualitativer als auch quantitativer [Forschung verfügen]" | 187 | **187** |
| 17 | 3.4 | „Die Gesamtheit aller Fälle, über die in einer Studie wissenschaftlich etwas ausgesagt werden soll, heißt [...] Population" | 294 | **294** |
| 18 | 3.4 | „Bei den meisten [...] empirischen Untersuchungen handelt es sich um Gruppenstudien" | 216 | **216** |
| 19 | 3.4 | „Entscheiden Sie sich für eine Einzelfallstudie, wenn Sie [...] Forschungsfragen untersuchen möchten, die sich speziell auf einen individuellen Einzelfall beziehen" | 218 | **218** |
| 20 | 3.4 | „bewusste bzw. absichtsvolle Auswahl von Fällen" | 303 | **303** |
| 21 | 3.4 | „Das Verfahren der Theoretischen Stichprobenbildung ('theoretical sampling')" | 303–304 | **303** |
| 22 | 3.4 | „Die Stichprobenziehung wird im Idealfall erst dann abgeschlossen, wenn [...] weitere Fälle keinen neuen Informationsgehalt für die Theoriebildung versprechen (theoretische Sättigung)" | 304–305 | **304** |
| 23 | 3.4 | „Die Stichprobenziehung nach dem Schneeballverfahren ('snowball sampling') ist geeignet für Populationen, die für die Forschenden schwer erreichbar, deren Mitglieder untereinander jedoch gut vernetzt sind" | 310–311 | **310** |
| 24 | 3.5 | „Unter einer wissenschaftlichen Beobachtung [...] versteht man die zielgerichtete, systematische und regelgeleitete Erfassung [...] von Merkmalen, Ereignissen oder Verhaltensweisen" | 324 | **323** |
| 25 | 3.5 | „Bei der sozialwissenschaftlichen Beobachtung [...] wird von den Forschenden eine Außenperspektive eingenommen" | 324 | **324** |
| 26 | 3.5 | „Viele subjektive Erlebensphänomene sind einer Fremdbeobachtung nicht zugänglich [...] und müssen erfragt werden" | 325 | **325** |
| 27 | 3.5 | „Die Befragung ist [...] die am häufigsten eingesetzte Datenerhebungsmethode. Im qualitativen Forschungsansatz stellt das [...] Interview die wichtigste Datenerhebungstechnik dar" | 353 | **353** |
| 28 | 3.5 | „Die Interviewtechnik [...] hat gegenüber der Beobachtung den Vorteil, dass [...] Aspekte des subjektiven Erlebens zugänglich werden" | 353–354 | **353** |
| 29 | 3.5 | „Dem teilstrukturierten [...] Interview liegt ein Interview-Leitfaden ('interview guide') als Liste offener Fragen [zugrunde]" | 368 | **367** |
| 30 | 3.5 | „Das Experten-Interview [...] ist eine Variante des Leitfaden-Interviews, bei der die Befragungspersonen als fachliche Expertinnen und Experten [...] befragt werden" | 372 | **371** |
| 31 | 3.5 | „Das [...] Expertenwissen bezieht sich einerseits auf [...] strukturelles Fachwissen, andererseits aber auch auf Praxis- und Handlungswissen. Letzteres ist oft stark verinnerlicht" | 372 | **371** |
| 32 | 3.5 | „Insbesondere ausführliche Schilderungen komplexer Zusammenhänge oder zeitlich lang ausgedehnter Prozesse erhält man [...] nur mündlich im Zuge qualitativer Interviews" | 354 | **354** |
| 33 | 3.5 | „Im Vergleich zur Interviewtechnik ist die Fragebogenmethode [...] effizienter [...] Sehr umfangreiche und komplexe Antworten sind schriftlich nicht zu erwarten" | 393–394 | **393** |
| 34 | 3.5 | „Bei einer genuinen Dokumentenanalyse wird auf bereits vorhandene [...] Dokumente [...] zurückgegriffen" | 525–526 | **525** |
| 35 | 3.5 | „Je nach Art und Ursprung der Dokumente stehen mehr oder weniger Kontextinformationen zur Verfügung, die Auskunft darüber geben, wer unter welchen Umständen [...] die Dokumente [...] erstellt hat" | 530–531 | **529** |
| 36 | 3.5 | „Bevor wir auf einzelne Interviewtechniken eingehen [...] in zehn Arbeitsschritte einteilen" | 362–365 | **361** |
| 37 | 3.5 | „Üblicherweise umfasst ein Interview-Leitfaden 1–2 Seiten mit 8–15 Fragen" | 368–369 | **368** |
| 38 | 3.5 | „Freiwilligkeit und informierte Einwilligung [...] freiwillig an wissenschaftlichen Studien beteiligen, nachdem sie über Zielsetzung und Ablauf [...] aufgeklärt wurden" | 121–123 | **121** |
| 39 | 3.5 | „Die Audioaufzeichnungen müssen [...] vollständig oder auszugsweise wortwörtlich verschriftet werden ('verbatim transcription')" | 362–363 | **362** |
| 40 | 3.5 | „Im deutschsprachigen Raum hat sich die von [...] Mayring [...] entwickelte Form der qualitativen Inhaltsanalyse am stärksten etabliert" | 533–534 | **533** |
| 41 | 3.5 | „Generell lassen sich bei den meisten Varianten der qualitativen Datenanalyse zwei Auswertungsebenen differenzieren: Die fallbezogene [...] sowie die fallübergreifende Auswertung" | 592–593 | **592** |
| 42 | 3.5 | „Dass durch QDA-Software die Datenanalyse effizienter erfolgt, größere und heterogenere Datenmengen verarbeitet werden können" | 597–599 | **598** |

**Ergebnis:** Alle 42 Seitenangaben wurden verifiziert und korrigiert. Zusätzlich 3 neue Belege aus Fixes bestätigt: Vertiefungsmodell **S. 27**, Anwendungsforschung **S. 187**, Interview-Nachteile **S. 354**.

---

## PHASE 5: Kritische Review und Übergabedokument

### Identifizierte Probleme

**Problem 1 — Zu lang:** 2.124 Wörter für verfügbare 5,3 Seiten (Ziel: 1.325–1.484 Wörter)

**Problem 2 — Zu viele oberflächliche Definitionen:** ~20 von ~45 Belegen waren reine Lehrbuch-Definitionen (Stufe 1: „X ist laut Döring Y"). Nur ~6 Belege transferierten Döring argumentativ auf das eigene Thema.

### Qualitätsstufen der Döring-Belege

| Stufe | Beschreibung | Beispiel | Anzahl im Text |
|-------|-------------|---------|----------------|
| **1** (Definition) | Reine Döring-Definition ohne Transfer | „Unter einer wissenschaftlichen Beobachtung versteht man..." | ~20 |
| **2** (Vergleich/Kriterium) | Abgrenzung oder Kriterienanwendung | „Ein deskriptives Erkenntnisinteresse scheidet aus, da..." | ~19 |
| **3** (Transfer/Stark) | Döring-Argument konkret auf eigenes Thema bezogen | „Gründer verfügen über beide Wissenstypen: strukturelles Fachwissen zu KI-Tools und Unit Economics sowie Praxis- und Handlungswissen..." | **6** |

### Die 6 sakrosankten Stufe-3-Belege (niemals kürzen oder entfernen)

1. **S. 953** (Kap. 18) — Dreigliedrige Abgrenzung Grundlagen-/Interventions-/Evaluationsforschung → Querverweis über Kapitelgrenzen hinweg
2. **S. 194 DIREKTZITAT** — Metaanalyse „methodisch aufwendig und komplex, d. h. als Einstiegsstudie für Neulinge eher ungeeignet" → Döring spricht, auf eigene Situation angewendet
3. **S. 169** (Kap. 6) — Sensibilisierende Konzepte → Brücke zwischen Literature Review und Untersuchungsdesign
4. **S. 25** (Kap. 2) — Theorieentdeckende Forschungslogik → zeigt Gesamtverständnis der qualitativen Methodologie
5. **S. 371 + Transfer** — Praxis-/Handlungswissen → „Gründer von B2C-E-Commerce-Startups verfügen über beide Wissenstypen"
6. **S. 354 + Transfer** — Informationsdichte → „Die Gründungsphase eines E-Commerce-Startups ist ein solcher vielschichtiger Prozess"

### 7 bereits implementierte Fixes (in der Erstfassung ergänzt)

1. **Vertiefungsmodell** (3.3) — Definition + Abgrenzung zum Vorstudienmodell (S. 27)
2. **Quantitativer Ausschluss** (3.3) — „Ein quantitatives Design scheidet aus..."
3. **Anwendungsforschung** (3.1) — Namentlich ausgeschlossen (S. 187)
4. **Theorie-/Methodenstudie** (3.2) — Namentlich ausgeschlossen
5. **Interview-Nachteile** (3.5) — Zeitaufwand, soziale Erwünschtheit, Reaktivität (S. 354)
6. **Design-Rückbezug** (3.5) — „Unter Beachtung des bislang definierten explorativen, qualitativen Designs..."
7. **Meinungen/Einstellungen/Trends** (3.5) — Wording aus Vorlesungsskript bei Kodierung (S. 592)

### Vollständige Zitatqualitätsliste (45 Belege mit Qualitätsstufe)

| Seitenzahl | Abschnitt | Inhalt | Stufe |
|-----------|-----------|--------|-------|
| 184 | Einl. | Untersuchungsdesign = methodische Vorgehensweise | 1 |
| 187 | 3.1 | Grundlagenforschung | 1 |
| 953 | 3.1 | Dreigliedrige Abgrenzung | **3** |
| 187 | 3.1 | Anwendungsforschung (Abgrenzung) | 2 |
| 194 | 3.1 | Explorative Studien | 1 |
| 194 | 3.1 | Deskriptiv/explanativ ausschließen | 2 |
| 194 | 3.1 | Explorativ = qualitativ (Brücke) | 2 |
| 188 | 3.2 | Empirische Studie | 1 |
| 193 | 3.2 | Originalstudie bei Qualifikationsarbeiten | 2 |
| 193 | 3.2 | Primäranalyse | 1 |
| 194 | 3.2 | Metaanalyse DIREKTZITAT | **3** |
| 186 | 3.3 | Qualitativer Forschungsansatz | 1 |
| 187 | 3.3 | Entscheidungskriterium qualitativ | 2 |
| 25 | 3.3 | Theorieentdeckende Forschungslogik | **3** |
| 169 | 3.3 | Sensibilisierende Konzepte | **3** |
| 186 | 3.3 | Vorstudienmodell | 1 |
| 27 | 3.3 | Vertiefungsmodell | 1 |
| 187 | 3.3 | Mixed-Methods Ressourcen | 2 |
| 294 | 3.4 | Zielpopulation | 1 |
| 216 | 3.4 | Gruppenstudie | 1 |
| 218 | 3.4 | Einzelfallstudie ausschließen | 2 |
| 303 | 3.4 | Bewusste Auswahl / Theoretical Sampling | 1 |
| 304 | 3.4 | Theoretische Sättigung | 1 |
| 310 | 3.4 | Schneeballverfahren | 1 |
| 323 | 3.5 | Beobachtung Definition | 1 |
| 324 | 3.5 | Beobachtung = Außenperspektive | 2 |
| 325 | 3.5 | Subjektive Phänomene unzugänglich | 2 |
| 353 | 3.5 | Interview = wichtigste Methode | 1 |
| 353 | 3.5 | Interview-Vorteil ggü. Beobachtung | 2 |
| 367 | 3.5 | Leitfaden-Interview | 1 |
| 371 | 3.5 | Experteninterview: Spezialwissen | 1 |
| 371 | 3.5 | Praxis-/Handlungswissen + Transfer | **3** |
| 354 | 3.5 | Interview-Nachteile | 2 |
| 354 | 3.5 | Informationsdichte + Transfer | **3** |
| 393 | 3.5 | Fragebogen ungeeignet | 2 |
| 525 | 3.5 | Dokumentenanalyse nonreaktiv | 2 |
| 529 | 3.5 | Dokumentenanalyse fehlender Kontext | 2 |
| 361 | 3.5 | 10-Schritte-Modell | 1 |
| 368 | 3.5 | Leitfaden 8–15 Fragen | 1 |
| 121 | 3.5 | Informierte Einwilligung | 1 |
| 362 | 3.5 | Wortwörtliche Transkription | 1 |
| 533 | 3.5 | Mayring Inhaltsanalyse | 1 |
| 592 | 3.5 | Fallbezogen + fallübergreifend | 1 |
| 598 | 3.5 | QDA-Software | 1 |

---

## PHASE 6: Simultane Kompression + Qualitätssteigerung

### Kompressionsstrategie

**Kernmuster — überall im Text angewendet:**

```
VORHER (3 Sätze, ~60 Wörter):
1. „Döring definiert X als Y." (Definition)
2. „Die Forschungsfrage zielt auf Z." (Entscheidung)
3. „Deshalb wird X gewählt." (Begründung)

NACHHER (1-2 Sätze, ~25-30 Wörter):
1. „Da die Forschungsfrage auf Z zielt, wird X gewählt — X dient laut Döring
   genau dazu, Y zu erreichen (vgl. Döring, 2023, S. N)."
```

### Wort-Budget nach Abschnitt

| Abschnitt | Vorher | Nachher | Kürzung |
|-----------|--------|---------|---------|
| Einleitung Kap. 3 | ~55 | ~40 | -15 |
| 3.1 Erkenntnisziel + -interesse | ~365 | ~250 | -115 |
| 3.2 Gegenstand + Datengrundlage | ~250 | ~180 | -70 |
| 3.3 Ansatz + Mixed-Method | ~365 | ~270 | -95 |
| 3.4 Untersuchungsobjekte | ~310 | ~220 | -90 |
| 3.5 Erhebungsinstrumente | ~780 | ~530 | -250 |
| **Gesamt** | **~2.124** | **~1.468** | **~-656 (31%)** |

### Neue Transfers (ersetzen bestehende Definitionen, kosten keine Extra-Wörter)

Beim Komprimieren wurden 3 neue thematische Transfers eingebaut, die Stufe-1-Definitionen zu Stufe-2/3-Transfers umwandelten:

1. **Schneeballverfahren** (S. 310): Statt nur Definition → „...da die B2C-E-Commerce-Gründerszene für akademische Forschung schwer zugänglich, intern aber über Accelerator-Kohorten und Investorenkreise eng vernetzt ist"
2. **Theoretische Sättigung** (S. 304): Statt nur Definition → „...bis KI-Rollen und Unit-Economics-Muster keine neuen Kategorien mehr hervorbringen"
3. **Deduktiv-induktiv** (S. 533): Statt nur Methodenrezept → „Die deduktiven Ausgangskategorien leiten sich aus den Konzepten des Literature Reviews ab — Dynamic Capabilities, Unit-Economics-Kennzahlen, KI-Anwendungsfelder —, während induktive Kategorien bislang unbekannte KI-Rollen abbilden"

### 4 finale Mikro-Kürzungen (~22 Wörter) für Seitenpassung

Nach der Hauptkompression (2.124 → ~1.490 Wörter) war der Text 2 Zeilen zu lang für das DOCX-Layout. Vier gezielte Kürzungen ohne Inhaltsverlust:

1. **3.4:** „als leicht operationalisierbare Kriterien" entfernt + „in der Gründungsphase" (redundant, da Kontext klar) + „einzelne" → -8 Wörter
2. **3.2:** Redundanter Satz „Diese Einordnung leitet sich logisch aus der Forschungsfrage ab." gestrichen (Typ-A-Begründung steht bereits im vorherigen Satz) → -8 Wörter
3. **3.1:** „zu diesem spezifischen Zusammenhang" → „hierzu" → -3 Wörter
4. **3.3:** „zu diesem Schnittmengenthema" gestrichen → -3 Wörter

### Einzige entfernte Referenz

S. 369 (Transkriptionszeit 5–8 Stunden pro Interviewstunde) — ist Handwerksdetail, kein Punkteargument.

---

## PHASE 7: DOCX-Produktion

### Technischer Ablauf

1. **Unpack:** Original-DOCX (`Expose.docx`, enthält Kap. 1 + Kap. 2) mittels Python-Script in XML-Struktur entpackt
2. **XML-Generierung:** Python-Script (`insert_chapter3.py`) erzeugt Word-Open-XML-Paragraphen mit korrektem Styling:
   - Überschrift 1: `<w:pStyle w:val="berschrift1"/>`, Times New Roman
   - Überschrift 2: `<w:pStyle w:val="berschrift2"/>`, Times New Roman, 12pt, spacing before/after
   - Fließtext: Standard-Body-Paragraphen
   - Fettdruck-Absätze: `<w:b/>` für Instrumenten-Labels (Instrument A, Instrument B, Begründete Auswahl, Hinweise)
   - XML-Escaping für deutsche Anführungszeichen: `&#x201E;` (öffnend), `&#x201C;` (schließend)
3. **Insertion:** XML-Paragraphen vor `<w:sectPr` in `document.xml` eingefügt (Kapitel 3 direkt nach Kapitel 2, ohne Seitenumbruch)
4. **Repack:** Modifizierte XML-Dateien zurück in DOCX verpackt mit Validierung

### Layout-Parameter (aus dem bestehenden Dokument übernommen)

- Seitenformat: US Letter (12240 × 15840 DXA)
- Ränder: oben 2cm, rechts 5cm, unten 2cm, links 2cm (`w:top="1134" w:right="2835" w:bottom="1134" w:left="1134"`)
- Schrift: Times New Roman 12pt
- Zeilenabstand: 1,5

---

## Qualitätssicherung — Checkliste am Ende

- [x] Alle 7 Design-Aspekte abgedeckt (Erkenntnisziel, -interesse, Gegenstand, Datengrundlage, Ansatz, Mixed-Method, Untersuchungsobjekte)
- [x] Abschnitt 3.5 ist der längste Abschnitt und enthält den vollständigen Dreischritt
- [x] Jede Entscheidung mit Döring belegt (45 Belege, alle Seitenangaben verifiziert)
- [x] Begründungstyp (A/B) pro Aspekt korrekt zugeordnet
- [x] Keine inhaltlichen Quellen im Untersuchungsdesign
- [x] Alle 6 Stufe-3-Belege erhalten und unverändert
- [x] Alle 7 Fixes erhalten
- [x] 3 neue thematische Transfers eingebaut (Schneeballverfahren, Sättigung, deduktiv-induktiv)
- [x] Alle Alternativen namentlich ausgeschlossen (Anwendungsforschung, deskriptiv, explanativ, quantitativ, Einzelfall, Theoriestudie, Methodenstudie, Replikation, Sekundäranalyse, Metaanalyse, Fragebogen, Dokumentenanalyse)
- [x] Wortumfang im Zielbereich (~1.468 Wörter)
- [x] DOCX-Layout korrekt und seitenpassend
- [x] Sensibilisierende Konzepte als Brücke Lit-Review ↔ Untersuchungsdesign eingebaut
- [x] Meinungen/Einstellungen/Trends-Wording bei Kodierung (aus Vorlesungsskript)
