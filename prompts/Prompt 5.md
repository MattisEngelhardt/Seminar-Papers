# Plan: Synthese-Blueprint für das Untersuchungsdesign

## Context

Das Untersuchungsdesign (Kapitel 3 des Exposés, ca. 5 Seiten, 30/70 Punkte) muss auf Basis von 89 Döring-Direktzitaten (FUNDS) aus fünf Agent-Dateien zu einem ausformulierungsfertigen Blueprint verdichtet werden. Die methodischen Entscheidungen stehen bereits fest (aus Mattis' Notizen + Whisper-Plan):

| Aspekt | Entscheidung |

|---|---|

| Erkenntnisziel | Grundlagenforschung |

| Erkenntnisinteresse | Explorativ |

| Gegenstand | Empirische Studie |

| Datengrundlage | Primäranalyse |

| Ansatz | Qualitativ |

| Mixed-Method | Vorstudienmodell (qual → quant) |

| Untersuchungsobjekte | Gruppenstudie, 6–10 Interviews |

| Erhebungsinstrument A (verworfen) | Qualitative Beobachtung |

| Erhebungsinstrument B (gewählt) | Leitfadengestütztes Experteninterview |

| Auswertung | Qualitative Inhaltsanalyse nach Mayring + MAXQDA/NVivo |

## Vorgehen in 3 Schritten

### Schritt 1: Kontextabsicherung (Lesen)

Alle 5 FUND-Dateien vollständig lesen + scribe_agent_prompt.md + plan_fizzy_whisper.md. Bereits erledigt durch Explore-Agents — Zusammenfassungen liegen vor:

- **agent4_funds.md** (R1, Kap. 6.3+7): 23 FUNDS — alle 7 Design-Aspekte

- **agent1_funds.md** (R2, Kap. 8+9): 14 FUNDS — Grundgesamtheit, Stichprobe, Sättigung

- **agent5_funds.md** (R3, Kap. 10.1–10.2): 25 FUNDS — Beobachtung vs. Experteninterview

- **agent3_funds.md** (R4, Kap. 10.3–10.6, 11, 12.1): 19 FUNDS — Fragebogen, Dokumentenanalyse, Auswertung

- **agent2_funds.md** (Scout, Kap. 1–6.2, 12.2–19): 8 FUNDS — Paradigma, Gütekriterien, KI, Ethik

### Schritt 2: Selektion der ~50 besten FUNDS

Kriterien:

1. **Maximale Abdeckung** aller 7 Blöcke des Untersuchungsdesigns + Erhebungsinstrument-Dreischritt

2. **Keine Redundanz** — jedes Zitat trägt eindeutig neuen Inhalt bei

3. **Direkte Anwendbarkeit** auf die Forschungsfrage (KI + B2C-E-Commerce-Startups + Unit Profitability)

4. **Belegkraft** — Zitat muss eine methodische Entscheidung stützen oder definieren

Erwartete Verteilung der ~50 FUNDS:

| Block | Aus Datei(en) | ~Anzahl |

|---|---|---|

| 3.1 Erkenntnisziel (1P) | agent4 + agent2 | 3–4 |

| 3.1 Erkenntnisinteresse (2P) | agent4 | 3–4 |

| 3.2 Gegenstand (1P) | agent4 | 2 |

| 3.2 Datengrundlage (1P) | agent4 | 2 |

| 3.3 Ansatz (2P) + Mixed-Method (2P) | agent4 + agent2 | 4–5 |

| 3.4 Untersuchungsobjekte (6P) | agent4 + agent1 | 6–8 |

| 3.5 Erhebungsinstrument (15P) | agent5 + agent3 | 20–25 |

| Scout-Ergänzungen | agent2 | 3–5 |

### Schritt 3: Synthese-Markdown aufbauen

Zielstruktur der Datei `Synthese_Plan_Untersuchungsdesign.md`:

```

# META

# FUND-KATALOG (alle selektierten FUNDS, durchnummeriert #1–~50)

# BLOCK 0: RAHMUNG (Forschungsfrage, Paradigma, Gütekriterien)

# BLOCK 1: ERKENNTNISZIEL — Grundlagenforschung

# BLOCK 2: ERKENNTNISINTERESSE — Explorativ

# BLOCK 3: GEGENSTAND — Empirische Studie

# BLOCK 4: DATENGRUNDLAGE — Primäranalyse

# BLOCK 5: ANSATZ — Qualitativ + Mixed-Method-Reflexion

# BLOCK 6: UNTERSUCHUNGSOBJEKTE — Gruppenstudie, Grundgesamtheit, Stichprobe

# BLOCK 7: ERHEBUNGSINSTRUMENT (größter Block)

  7a: Instrument A — Beobachtung (Definition + Begründung Eignung)

  7b: Instrument B — Leitfadengestütztes Experteninterview (Definition + Begründung Eignung)

  7c: Begründete Auswahl von B über A

  7d: Hinweise zum weiteren Vorgehen (Leitfaden, Transkription, Mayring, Software)

# BLOCK 8: SCOUT-FINDINGS (Paradigma, Gütekriterien, KI-Definition, Ethik)

# BLOCK 9: ZITATIONSMATRIX

# BLOCK 10: SATZ-FÜR-SATZ-SCHREIBPLAN (Gliederung 3.1–3.5)

```

Jeder Block enthält:

- **Entscheidung** (was wird gewählt)

- **Begründungstyp** (Typ A: aus FF abgeleitet / Typ B: aus Forschungsstand)

- **Selektierte FUNDS** mit vollem Zitattext und Seitenangabe

- **Transfer auf die eigene Forschungsfrage** (vorformuliert)

- **Argumentationslinie** für die Ausformulierung

## Umsetzung: Parallelisierte Agenten

Da die 5 FUND-Dateien unabhängig voneinander lesbar sind und die Synthese-Datei ein einzelnes Ausgabedokument ist, wird folgendermaßen parallelisiert:

1. **3 Lese-Agenten parallel** lesen die 5 FUND-Dateien vollständig (Agent A: agent4+agent2, Agent B: agent1, Agent C: agent5+agent3) und extrahieren die besten FUNDS mit vollständigem Zitattext

2. **1 Synthese-Agent** baut daraus die finale Markdown-Datei auf Basis der oben definierten Struktur

## Kritische Dateien

| Datei | Pfad | Rolle |

|---|---|---|

| FUND-Dateien (5×) | `funds_backup/agent{1-5}_funds.md` | Input: 89 Direktzitate |

| Whisper-Plan | `funds_backup/plan_fizzy_whisper.md` | Orchestrierungslogik, FUND-Format, Begründungstypen |

| Scribe-Prompt | `funds_backup/scribe_agent_prompt.md` | Zielstruktur, Design-Entscheidungen, Sektionsaufbau |

| Vorlesungsskript | `output_marker/Vorlesungsskript.../...md` | Punkteverteilung, Anforderungen, Vor-/Nachteile |

| Beispiel-Exposé | `output_marker/Beispiel für ein gutes Expose/...md` | Strukturvorlage Kapitel 3 |

| CLAUDE.md | Projektroot | Verbindliche Regeln, Zitierregeln, Gliederung |

## Verifikation

- [ ] ~50 FUNDS selektiert, keine Redundanzen

- [ ] Alle 7 Design-Aspekte + Erhebungsinstrument-Dreischritt abgedeckt

- [ ] Block 7 (Erhebungsinstrument) ist der umfangreichste Block

- [ ] Jeder FUND hat: Kapitel, Zeilenbereich, Buchseite (wenn vorhanden), Direktzitat, Transfer

- [ ] Begründungstyp (A/B) bei jedem Block korrekt zugeordnet

- [ ] Zitationsmatrix vollständig

- [ ] Satz-für-Satz-Schreibplan deckt Gliederung 3.1–3.5 ab

- [ ] Datei ist sofort ausformulierungsbereit

