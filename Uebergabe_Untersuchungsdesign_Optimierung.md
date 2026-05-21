# Übergabedokument: Kapitel 3 Untersuchungsdesign — Kürzen + Qualität maximieren

## Zweck

Arbeitsanweisung für einen neuen Chat. Der aktuelle Text (`Kapitel_3_Untersuchungsdesign.md`) ist **zu lang** und muss gleichzeitig **kürzer UND besser** werden. Nicht: kürzen und dann separat verbessern. Sondern: beim Kürzen die Qualität steigern.

**Aktueller Text:** `Kapitel_3_Untersuchungsdesign.md` (Projektroot)
**Alle Regeln:** `CLAUDE.md` (Projektroot)

---

## DIE ZWEI KERNPROBLEME (BEIDE GLEICHZEITIG LÖSEN)

### Problem 1: Zu lang
2.124 Wörter aktuell → Ziel ~1.400 Wörter. Ca. 700 Wörter kürzen (33%).

### Problem 2: Zu viele oberflächliche Definitionen
~20 von ~45 Döring-Belegen sind reine Lehrbuch-Definitionen: „X ist laut Döring Y (vgl. Döring, S. Z)." Das zeigt einem Prof nur, dass der Student Döring GELESEN hat — nicht, dass er sie VERSTANDEN hat. Nur ~6 Belege transferieren Döring argumentativ auf das eigene Thema. Der Prof will sehen: „Döring sagt X — und im Kontext von KI-gestützten Unit-Economics-Entscheidungen in B2C-E-Commerce-Startups bedeutet das konkret Y." Diesen Transfer macht der Text zu selten.

### Die Lösung: Beim Kürzen gleichzeitig die Qualität steigern
Statt „Definition (1 Satz) → Entscheidung (1 Satz) → Begründung (1 Satz)" = ~60 Wörter wird jede Stelle umgebaut zu „Entscheidung + Transfer + Döring-Beleg in einem Satz" = ~25 Wörter. Das kürzt UND verbessert gleichzeitig. Jeder Beleg, der aktuell Stufe 1 ist (siehe Liste in Abschnitt L), muss beim Umschreiben mindestens auf Stufe 2 gehoben werden. Die 6 Stufe-3-Belege (siehe Abschnitt E.2) sind sakrosankt — niemals kürzen oder entfernen.

---

## A. DAS ZAHLENPROBLEM IM DETAIL

| Kennzahl | Wert |
|----------|------|
| Aktueller Wortumfang | **2.124 Wörter** |
| Verfügbare Seiten | **5,3 Seiten** (Gesamtexposé max. 11 Seiten, Einleitung + Lit-Review bereits geschrieben) |
| Wörter pro Seite | **250–280** (12pt Times New Roman, 1,5 Zeilenabstand, 5cm rechts, 2cm links) |
| **Ziel-Wortumfang** | **1.325–1.484 Wörter** |
| **Zu kürzen** | **~640–800 Wörter (ca. 30–37%)** |

---

## B. ZENTRALE STRATEGIE: KOMPRIMIEREN, NICHT STREICHEN

**Falsch:** Ganze Abschnitte entfernen → Punkte verlieren.
**Richtig:** Jede Aussage in weniger Wörtern machen und dabei Transfers einbauen.

### Das Muster, das überall im Text vorkommt und Platz frisst:

```
AKTUELL (3 Sätze, ~60 Wörter):
1. „Döring definiert X als Y." (Definition)
2. „Die Forschungsfrage zielt auf Z." (Entscheidung)
3. „Deshalb wird X gewählt." (Begründung)

BESSER (1-2 Sätze, ~30 Wörter):
1. „Da die Forschungsfrage auf Z zielt, wird X gewählt — X dient laut Döring
   genau dazu, Y zu erreichen (vgl. Döring, 2023, S. N)."
```

**Prinzip:** Definition und Transfer in EINEN Satz verschmelzen. Nicht erst definieren, dann anwenden — beides gleichzeitig. Das spart ~50% der Wörter UND zeigt dem Prof, dass du Döring nicht nur zitierst, sondern *denkst*.

---

## C. BEREITS ERLEDIGTE FIXES (7 Stück, schon im Text)

Diese 7 Fixes wurden in der vorherigen Session implementiert. NICHT nochmal machen, aber beim Kürzen NICHT wieder entfernen — sie schließen Lücken, die Punkte kosten:

1. **Vertiefungsmodell** (3.3) — Definition + Abgrenzung zum Vorstudienmodell (S. 27)
2. **Quantitativer Ausschluss** (3.3) — „Ein quantitatives Design scheidet aus..."
3. **Anwendungsforschung** (3.1) — Namentlich ausgeschlossen (S. 187)
4. **Theorie-/Methodenstudie** (3.2) — Namentlich ausgeschlossen
5. **Interview-Nachteile** (3.5) — Zeitaufwand, soziale Erwünschtheit, Reaktivität (S. 354)
6. **Design-Rückbezug** (3.5) — „Unter Beachtung des bislang definierten Designs..."
7. **Meinungen/Einstellungen/Trends** (3.5) — Wording aus Vorlesungsskript bei Kodierung

---

## D. ABSCHNITT-FÜR-ABSCHNITT: WO KÜRZEN, WO VERDICHTEN

### D.1 Einleitungsparagraph (aktuell ~55 Wörter → Ziel: ~40)

**Aktuell:** Zwei Sätze Definition von „Untersuchungsdesign" + ein Satz mit verbatim zitierter Forschungsfrage.

**Kürzungspotenzial:** Die Forschungsfrage wurde bereits in 2.6 abgeleitet — sie hier nochmal vollständig zu zitieren frisst ~25 Wörter. Das Beispiel-Exposé paraphrasiert hier stattdessen. → Forschungsfrage paraphrasieren oder auf einen Rückverweis kürzen.

---

### D.2 Abschnitt 3.1 — Erkenntnisziel + Erkenntnisinteresse (aktuell ~365 Wörter → Ziel: ~250)

**Kürzungspotenzial: ~115 Wörter**

**Erkenntnisziel — was bleibt:**
- Entscheidung: Grundlagenforschung ✓
- Begründung aus FF ✓
- Abgrenzung: Interventions-/Evaluationsforschung (S. 953) ✓ — BEHALTEN, ist Stufe-3-Beleg
- Abgrenzung: Anwendungsforschung (S. 187) ✓ — BEHALTEN (Fix 3)

**Erkenntnisziel — was kürzen:**
- Die Definition von Grundlagenforschung ist zu lang (~45 Wörter). Kann auf ~20 komprimiert werden, indem Definition und Transfer verschmolzen werden.
- „Die Einordnung als Grundlagenforschung leitet sich logisch aus der Forschungsfrage ab: Es geht um die Weiterentwicklung des theoretischen Rahmens, konkret die Erweiterung des Unit-Profitability-First-Gedankens um eine KI-Dimension." → Der erste Halbsatz ist redundant (das sagt der vorherige Satz schon). Kürzen auf: „Konkret geht es um die Erweiterung des Unit-Profitability-First-Gedankens um eine KI-Dimension."

**Erkenntnisinteresse — was bleibt:**
- Entscheidung: Explorativ ✓
- Begründung aus Forschungsstand ✓
- „Schnittmenge stellt wissenschaftliches Neuland dar" ✓
- Abgrenzung: deskriptiv + explanativ ✓
- Brücke: „qualitative Studien" ✓

**Erkenntnisinteresse — was kürzen:**
- Drei separate Belege auf S. 194. Alle drei Sätze zitieren dieselbe Seite. → Zu zwei Sätzen komprimieren.
- „Die Forschungsfrage ist als offene W-Frage formuliert und zielt auf Theoriebildung, nicht auf Theorieprüfung." → Redundant zum vorherigen Satz. Streichen.

---

### D.3 Abschnitt 3.2 — Gegenstand + Datengrundlage (aktuell ~250 Wörter → Ziel: ~180)

**Kürzungspotenzial: ~70 Wörter**

**Was bleibt:**
- Empirische Studie + Begründung ✓
- Theorie-/Methodenstudie ausgeschlossen (Fix 4) ✓
- Originalstudie vs. Replikation ✓
- Primäranalyse + Abgrenzung Sekundär/Meta ✓
- Direktzitat Metaanalyse (S. 194) ✓ — UNBEDINGT BEHALTEN, ist Stufe-3-Beleg

**Was kürzen:**
- „Werden anhand von neu erhobenen Daten inhaltliche Forschungsfragen bearbeitet, so handelt es sich um eine empirische Studie, die der Lösung von inhaltlichen Forschungsproblemen auf der Basis systematischer eigener Datenerhebung dient" → Dopplung (erst Paraphrase, dann nochmal Definition). Einen der beiden streichen.
- „Die Forschungsfrage nach der Rolle von KI in der Gründungsphase von B2C-E-Commerce-Startups kann nicht durch eine reine Literaturarbeit beantwortet werden" → Die FF nochmal ausgeschrieben. Kürzen auf: „Die Forschungsfrage kann nicht durch eine reine Literaturarbeit beantwortet werden"

---

### D.4 Abschnitt 3.3 — Ansatz + Mixed-Method (aktuell ~365 Wörter → Ziel: ~270)

**Kürzungspotenzial: ~95 Wörter**

**Ansatz — VORSICHT: bester Abschnitt im Text!**
- S. 25 (theorieentdeckende Logik), S. 169 (sensibilisierende Konzepte) → UNBEDINGT BEHALTEN
- Aber: Die Definition des qualitativen Ansatzes (S. 186) ist zu ausführlich paraphrasiert. Komprimieren.
- Der Satz „Die Wahl ergibt sich nachvollziehbar aus dem aktuellen Forschungsstand: Das Themenfeld ist wenig erforscht, die Forschungsfrage ist als offene W-Frage formuliert, und das Ziel liegt in der Theoriebildung." wiederholt, was schon in 3.1 steht. Stark kürzen.

**Mixed-Method:**
- Vorstudienmodell (S. 186) + Vertiefungsmodell (S. 27) + Begründete Auswahl + Ressourcen (S. 187) → Alles inhaltlich nötig, aber kann dichter formuliert werden.
- „Die vorliegende qualitative Primärstudie könnte Hypothesen über die spezifischen KI-Rollen für Unit Profitability generieren, die in einer Anschlussstudie quantitativ geprüft werden." → Guter Transfer, behalten.
- „Ein vollständiges Mixed-Methods-Design wird im Rahmen dieser Qualifikationsarbeit nicht realisiert, da dies solide Vorkenntnisse in beiden Forschungsparadigmen sowie ausreichende zeitliche, finanzielle und personelle Ressourcen voraussetzt" → Kann auf „...nicht realisiert, da die erforderlichen Ressourcen und Vorkenntnisse in beiden Paradigmen dies nicht zulassen" gekürzt werden.

---

### D.5 Abschnitt 3.4 — Untersuchungsobjekte (aktuell ~310 Wörter → Ziel: ~220)

**Kürzungspotenzial: ~90 Wörter**

**GRÖSSTES KÜRZUNGSPOTENZIAL im ganzen Text.** Hier reihen sich 7 Definitionen aneinander (Grundgesamtheit, Gruppenstudie, Einzelfall, Purposive Sampling, Theoretical Sampling, Sättigung, Schneeball) mit fast keinem Transfer.

**Strategie:**
- Grundgesamtheit + Operationalisierung: Zusammenfassen statt getrennte Sätze. Definition und Merkmale in einem Satz.
- Gruppenstudie + Einzelfallausschluss: In einem Satz abhandeln statt in zweien.
- Sampling-Kette (Purposive → Theoretical → Sättigung): Drei Definitionen zu einer Argumentationskette verschmelzen, die auf das Thema transferiert. Statt drei einzelne Definitionen: „Die Fallauswahl folgt dem Prinzip des Theoretical Sampling, bei dem anhand bisheriger Ergebnisse schrittweise weitere Fälle aufgenommen werden, bis die theoretische Sättigung erreicht ist — also KI-Rollen und Unit-Economics-Muster keine neuen Kategorien mehr hervorbringen (vgl. Döring, 2023, S. 303–304)."
- Schneeballverfahren: Definition + Transfer in einem Satz (warum Gründerszene = schwer erreichbar aber gut vernetzt).
- „Führungskräfte" kurz begründen (1 Halbsatz).

---

### D.6 Abschnitt 3.5 — Erhebungsinstrumente (aktuell ~780 Wörter → Ziel: ~530)

**Kürzungspotenzial: ~250 Wörter** (größter Block!)

**ACHTUNG:** 15/70 Punkte. Hier darf inhaltlich NICHTS fehlen. Aber die Formulierungen sind oft zu breit.

#### Instrument A — Beobachtung (aktuell ~115 Wörter → Ziel: ~90)
- Definition (S. 323): Komprimieren. „Unter einer wissenschaftlichen Beobachtung versteht man die zielgerichtete, systematische und regelgeleitete Erfassung, Dokumentation und Interpretation von Merkmalen, Ereignissen oder Verhaltensweisen zum Zeitpunkt ihres Auftretens" → Kürzen auf Kernidee.
- Eignung 1-2 Sätze ausbauen (potenzielle Eignung für KI-Nutzungsroutinen), dann Grenzen.
- Die drei Döring-Belege (S. 323, 324, 325) können zu zweien komprimiert werden (324 + 325 sagen beide „nicht beobachtbar").

#### Instrument B — Interview (aktuell ~215 Wörter → Ziel: ~150)
- Fünf Döring-Belege in Serie (S. 353, 353, 367, 371, 371, 354). Zu viele einzelne Definitionen.
- „Die Befragung ist die in den empirischen Sozialwissenschaften am häufigsten eingesetzte Datenerhebungsmethode" → Autoritätsaussage, kein Argument. Streichen oder mit Begründung versehen.
- Das Leitfaden-Interview (S. 367) und das Experteninterview (S. 371) können in einem Satz zusammengefasst werden: „Als Format wird das leitfadengestützte Experteninterview gewählt, das durch sein Grundgerüst Vergleichbarkeit sichert (vgl. Döring, 2023, S. 367), während es das Spezialwissen der Befragten — strukturelles Fachwissen ebenso wie schwer verbalisierbares Praxis- und Handlungswissen — systematisch erschließt (vgl. Döring, 2023, S. 371)."
- S. 371 Transfer (Gründer = beide Wissenstypen): BEHALTEN — Stufe-3-Beleg.

#### Begründete Auswahl (aktuell ~215 Wörter → Ziel: ~160)
- Drei Argumente (Innenperspektive, Informationsdichte, Balance) → Können dichter formuliert werden.
- Fragebogen-Verwerfung (S. 393): Komprimieren auf einen Satz.
- Dokumentenanalyse-Verwerfung (S. 525, 529): Komprimieren auf einen Satz.
- „Die subjektiven Entscheidungslogiken der Gründerinnen und Gründer sind aus vorgefundenen Dokumenten nicht rekonstruierbar." → Guter Transfer, behalten.

#### Hinweise zum weiteren Vorgehen (aktuell ~235 Wörter → Ziel: ~130)
- GRÖSSTES KÜRZUNGSPOTENZIAL innerhalb von 3.5.
- 10-Schritte-Modell (S. 361) + Leitfaden (S. 368) + Probe-Interview: In einem Satz.
- Thematische Kontextualisierung: Behalten — ist Transfer.
- Audioaufzeichnung + Einwilligung (S. 121) + Postskriptum: In einem Satz.
- Transkription (S. 362) + Zeitaufwand (S. 369): Zusammenfassen. Zeitaufwand-Detail (5-8 Stunden) kann gestrichen werden — das ist Handwerksdetail, keine Punkteargument.
- Mayring (S. 533) + Kodierung (S. 592): Zusammenfassen, aber Transfer einbauen (deduktive Kategorien = Dynamic Capabilities, Unit Economics; induktive = unbekannte KI-Rollen).
- MAXQDA/NVivo (S. 598): Kann in den Kodierungs-Satz integriert werden.

---

## E. ZITATQUALITÄT — BEIM KÜRZEN GLEICHZEITIG VERBESSERN

### E.1 Das Kernproblem

~20 von ~45 Belegen sind reine Definitionen (Stufe 1). Nur ~6 sind echte Transfers (Stufe 3). Beim Kürzen bietet sich die Chance, die Stufe-1-Definitionen gleichzeitig zu Stufe-2/3-Transfers umzubauen.

### E.2 Die 6 starken Stellen (NIEMALS kürzen oder entfernen!)

1. **S. 953** (Kap. 18) — Dreigliedrige Abgrenzung → Querverweist über Kapitelgrenzen
2. **S. 194 DIREKTZITAT** — Metaanalyse „für Neulinge ungeeignet" → Döring spricht, auf eigene Situation angewendet
3. **S. 169** (Kap. 6) — Sensibilisierende Konzepte → Brücke LitReview ↔ Design
4. **S. 25** (Kap. 2) — Theorieentdeckende Forschungslogik → zeigt Gesamtverständnis
5. **S. 371 + Transfer** — Praxis-/Handlungswissen → „Gründer verfügen über beide Wissenstypen"
6. **S. 354 + Transfer** — Informationsdichte → „Gründungsphase ist zeitlich ausgedehnt"

### E.3 Transfers die beim Kürzen NEU eingebaut werden sollten

Diese kosten keine zusätzlichen Wörter, weil sie BESTEHENDE Definitionen ersetzen:

1. **Schneeballverfahren** (S. 310): Statt nur Definition → „...über das Schneeballverfahren, da die B2C-E-Commerce-Gründerszene für akademische Forschung schwer zugänglich, intern aber über Accelerator-Kohorten und Investorenkreise eng vernetzt ist (vgl. Döring, 2023, S. 310)."

2. **Theoretische Sättigung** (S. 304): Statt nur Definition → „...bis die identifizierten KI-Rollen und deren Wirkung auf Unit-Economics-Entscheidungen keine neuen Kategorien mehr hervorbringen."

3. **Deduktiv-induktiv** (S. 533): Statt nur Methodenrezept → „Die deduktiven Ausgangskategorien leiten sich aus den Konzepten des Literature Reviews ab — Dynamic Capabilities, Unit-Economics-Kennzahlen, KI-Anwendungsfelder —, während induktive Kategorien bislang unbekannte KI-Rollen abbilden."

4. **Quantitativer Ausschluss** (3.3): Döring-Beleg S. 187 ergänzen (bereits verifiziert, kostet 4 Wörter).

---

## F. SEITENZAHLEN-STATUS

### Alle verifizierten Belege
- 42 Belege aus `Seitenzahlen_Verifizierung.md` → Alle korrekt im aktuellen Text
- 3 neue Belege aus Fixes → Alle von Mattis bestätigt:
  - Vertiefungsmodell: **S. 27** ✅
  - Anwendungsforschung: **S. 187** ✅
  - Interview-Nachteile: **S. 354** ✅

### Regel für den neuen Chat
**Keine neuen Döring-Seitenzahlen einfügen.** Alle Transfers nutzen bestehende, verifizierte Belege. Wenn doch eine neue Stelle nötig wäre: Originalzitat (1-3 Sätze) angeben, damit Mattis die Seite im PDF nachschlagen kann.

---

## G. WORT-BUDGET NACH ABSCHNITT

| Abschnitt | Aktuell | Ziel | Kürzung |
|-----------|---------|------|---------|
| Einleitung Kap. 3 | ~55 | ~40 | -15 |
| 3.1 Erkenntnisziel + -interesse | ~365 | ~250 | -115 |
| 3.2 Gegenstand + Datengrundlage | ~250 | ~180 | -70 |
| 3.3 Ansatz + Mixed-Method | ~365 | ~270 | -95 |
| 3.4 Untersuchungsobjekte | ~310 | ~220 | -90 |
| 3.5 Erhebungsinstrumente | ~780 | ~530 | -250 |
| **Gesamt** | **~2.124** | **~1.490** | **~-634** |

---

## H. CHECKLISTE FÜR DEN NEUEN CHAT

### Pflichtlektüre vor dem Arbeiten
- [ ] `CLAUDE.md` lesen (alle Regeln)
- [ ] `Kapitel_3_Untersuchungsdesign.md` lesen (aktueller Text)
- [ ] Dieses Dokument als Arbeitsanweisung verwenden
- [ ] `Seitenzahlen_Verifizierung.md` lesen (verifizierte Seitenzahlen)

### Beim Kürzen prüfen
- [ ] Ziel-Wortumfang ~1.325–1.484 Wörter erreicht?
- [ ] Alle 6 Stufe-3-Belege (S. 953, 194 Direktzitat, 169, 25, 371+Transfer, 354+Transfer) erhalten?
- [ ] Alle 7 Fixes erhalten (Vertiefungsmodell, quantitativer Ausschluss, Anwendungsforschung, Theorie-/Methodenstudie, Interview-Nachteile, Design-Rückbezug, Meinungen/Einstellungen/Trends)?
- [ ] Neue Transfers eingebaut (Schneeballverfahren, Sättigung, deduktiv-induktiv)?
- [ ] Keine inhaltlichen Quellen im Untersuchungsdesign?
- [ ] Keine neuen unverifizierten Döring-Seitenzahlen?
- [ ] Jede Döring-Stelle hat einen Transfer auf das eigene Thema (nicht nur Definition)?
- [ ] Muster „Definition → Beleg → Entscheidung" durch „Transfer + Beleg in einem Satz" ersetzt?

### Qualitätsprüfung am Ende
- [ ] Liest sich der Text wie ein Student, der Döring VERSTANDEN hat (nicht nur gelesen)?
- [ ] Ist das Erhebungsinstrument (15/70 Punkte) trotz Kürzung vollständig (2 Instrumente → Auswahl → Hinweise)?
- [ ] Sind alle Alternativen namentlich ausgeschlossen (Anwendungsforschung, deskriptiv, explanativ, quantitativ, Einzelfall, Theoriestudie, Methodenstudie, Replikation, Sekundär, Meta)?
- [ ] Stimmt der Dreischritt beim Erhebungsinstrument?

---

## I. FORMULIERUNGSMUSTER AUS DEM BEISPIEL-EXPOSÉ (STILVORLAGE)

Das Beispiel-Exposé (Datei: `output_marker/Beispiel für ein gutes Expose/Beispiel für ein gutes Expose.md`, ab Zeile 108) zeigt, wie Kap. 3 auf ~1.460 Wörter mit nur ~12 Döring-Zitaten funktioniert. Es ist der Qualitätsmaßstab. Entscheidende Muster:

### I.1 Satzstruktur: „Entscheidung + da + Döring"

Das Beispiel-Exposé definiert NICHT erst und entscheidet dann. Es verschmilzt beides:

```
BEISPIEL-EXPOSÉ (1 Satz):
„Methodologisch ist sie der anwendungsorientierten Forschung zuzuordnen,
 da sie auf die Ableitung konkreter Handlungsempfehlungen zur Lösung
 eines praxisrelevanten Problems abzielt (vgl. Döring, 2023, S. 187)."

→ Entscheidung + Begründung + Beleg = 1 Satz, ~30 Wörter.

MATTIS AKTUELL (3 Sätze):
„Eine Untersuchung kann darauf abzielen... eine solche Grundlagenforschung
 trägt zum Erkenntnisgewinn bei (vgl. Döring, 2023, S. 187).
 Die Forschungsfrage fragt nach der ‚Rolle' von KI...
 Die Einordnung als Grundlagenforschung leitet sich logisch ab..."

→ Definition + Entscheidung + Begründung = 3 Sätze, ~75 Wörter.
```

**Takeaway:** Das Beispiel-Exposé nutzt „da" als Konjunktion, die Entscheidung und Döring-Argument in einem Satz verbindet. Mattis' Text trennt beides und braucht dadurch doppelt so viele Wörter.

### I.2 Abschnitte fließen ineinander

Das Beispiel-Exposé hat in 3.3 (Ansatz) ALLES in einem einzigen Absatz: qualitativ + warum + Erhebungsmethode (Experteninterview!) + Auswertung (Mayring!) + Mixed-Method. Mattis hat das auf 3.3 + 3.5 verteilt, was zu Wiederholungen führt (z.B. „Experteninterview" wird in 3.3 UND 3.5 eingeführt).

### I.3 Döring-Seitenangaben: „S. 185f." statt „S. 185"

Das Beispiel-Exposé nutzt „f." und „ff." bei Döring. ACHTUNG: Laut Bewertungskriterien in `CLAUDE.md` sind „ff." und Seitenbereiche wie „S. 3-6" NICHT erlaubt — es werden präzise Seitenangaben verlangt. Also: „S. 187" statt „S. 187f.". Mattis macht das bereits richtig.

### I.4 Kompaktheit bei Untersuchungsobjekten

Das Beispiel-Exposé handelt Grundgesamtheit, Stichprobe, Sampling und Sättigung in EINEM Absatz ab (~130 Wörter). Mattis hat dafür DREI Absätze (~310 Wörter). Größtes Einsparpotenzial.

### I.5 Inhaltliche Unterschiede zum Beachten

Das Beispiel-Exposé wählt Anwendungsforschung + explorativ + qualitativ + Experteninterview vs. Dokumentenanalyse. Mattis wählt Grundlagenforschung + explorativ + qualitativ + Experteninterview vs. Beobachtung. Die Grundstruktur ist identisch, aber Mattis muss MEHR abgrenzen (Grundlagenforschung braucht die Abgrenzung zur Anwendungsforschung UND die dreigliedrige Abgrenzung, das Beispiel-Exposé braucht das nicht).

---

## J. BEGRÜNDUNGSTYPEN — WO WELCHER GILT

Aus dem Vorlesungsskript und der Bewertungstabelle ergeben sich zwei Begründungstypen. Jeder Aspekt hat EINEN zugewiesenen Typ. Den falschen Typ zu verwenden kostet Punkte.

| Begründungstyp | Formulierung im Text | Gilt für |
|----------------|---------------------|----------|
| **Typ A** — aus der Forschungsfrage | „leitet sich logisch aus der Forschungsfrage ab" | Erkenntnisziel, Gegenstand, Mixed-Method, Untersuchungsobjekte (GG) |
| **Typ B** — aus dem Forschungsstand | „ergibt sich nachvollziehbar aus dem aktuellen Forschungsstand" | Erkenntnisinteresse, Datengrundlage, Ansatz |

**Status im aktuellen Text:** Alle korrekt zugeordnet. Beim Kürzen darauf achten, dass die Formulierungen „logisch aus der Forschungsfrage" bzw. „aus dem aktuellen Forschungsstand" erhalten bleiben — der Prof sucht genau danach.

---

## K. BEWERTUNGSRASTER — EXAKTE PUNKTEVERTEILUNG

Aus `CLAUDE.md` und dem Vorlesungsskript (`output_marker/Vorlesungsskript zur Aufgabenleistung/Vorlesungsskript zur Aufgabenleistung..md`):

| Aspekt | Punkte | Begründungstyp | Entscheidung (Mattis) |
|--------|--------|---------------|----------------------|
| Erkenntnisziel | 1 | A (aus FF) | Grundlagenforschung |
| Erkenntnisinteresse | 2 | B (aus Forschungsstand) | Explorativ |
| Gegenstand | 1 | A (aus FF) | Empirische Studie |
| Datengrundlage | 1 | B (aus Forschungsstand) | Primäranalyse |
| Ansatz | 2 | B (aus Forschungsstand) | Qualitativ |
| Mixed-Method | 2 | A (aus FF) | Vorstudienmodell |
| Untersuchungsobjekte (GG) | 3 | A (aus FF + Wissensstand) | B2C-E-Commerce-Gründer |
| Untersuchungsobjekte (Gruppe/Einzelfall) | 3 | — | Gruppenstudie |
| Erhebungsinstrument | **15** | Dreischritt | Experteninterview |
| **Gesamt** | **30** | | |

**Gewichtung beachten:** Das Erhebungsinstrument allein ist 15/30 = 50% der Untersuchungsdesign-Note. Hier darf beim Kürzen NICHTS Inhaltliches verloren gehen. Die Kürzung muss vor allem bei 3.1–3.4 stattfinden (zusammen nur 15 Punkte, aber aktuell ~980 Wörter = fast die Hälfte des Textes).

---

## L. VOLLSTÄNDIGE LISTE ALLER DÖRING-SEITENZAHLEN IM TEXT

Alle diese Seitenzahlen sind verifiziert. Beim Kürzen KEINE davon ändern oder neue hinzufügen.

| Seitenzahl | Abschnitt | Inhalt | Qualitätsstufe |
|-----------|-----------|--------|---------------|
| 184 | Einl. | Untersuchungsdesign = methodische Vorgehensweise | 1 (Definition) |
| 187 | 3.1 | Grundlagenforschung | 1 (Definition) |
| 953 | 3.1 | Dreigliedrige Abgrenzung | **3 (STARK)** |
| 187 | 3.1 | Anwendungsforschung (Abgrenzung) | 2 (Abgrenzung) |
| 194 | 3.1 | Explorative Studien | 1 (Definition) |
| 194 | 3.1 | Deskriptiv/explanativ ausschließen | 2 (Abgrenzung) |
| 194 | 3.1 | Explorativ = qualitativ (Brücke) | 2 (Brücke) |
| 188 | 3.2 | Empirische Studie | 1 (Definition) |
| 193 | 3.2 | Originalstudie bei Qualifikationsarbeiten | 2 (Empfehlung) |
| 193 | 3.2 | Primäranalyse | 1 (Definition) |
| 194 | 3.2 | Metaanalyse DIREKTZITAT | **3 (STARK)** |
| 186 | 3.3 | Qualitativer Forschungsansatz | 1 (Definition) |
| 187 | 3.3 | Entscheidungskriterium qualitativ | 2 (Kriterium) |
| 25 | 3.3 | Theorieentdeckende Forschungslogik | **3 (STARK)** |
| 169 | 3.3 | Sensibilisierende Konzepte | **3 (STARK)** |
| 186 | 3.3 | Vorstudienmodell | 1 (Definition) |
| 27 | 3.3 | Vertiefungsmodell | 1 (Definition) |
| 187 | 3.3 | Mixed-Methods Ressourcen | 2 (Abgrenzung) |
| 294 | 3.4 | Zielpopulation | 1 (Definition) |
| 216 | 3.4 | Gruppenstudie | 1 (Definition) |
| 218 | 3.4 | Einzelfallstudie ausschließen | 2 (Abgrenzung) |
| 303 | 3.4 | Bewusste Auswahl | 1 (Definition) |
| 303 | 3.4 | Theoretical Sampling | 1 (Definition) |
| 304 | 3.4 | Theoretische Sättigung | 1 (Definition) |
| 310 | 3.4 | Schneeballverfahren | 1 (Definition) |
| 323 | 3.5 | Beobachtung Definition | 1 (Definition) |
| 324 | 3.5 | Beobachtung = Außenperspektive | 2 (Argument) |
| 325 | 3.5 | Subjektive Phänomene unzugänglich | 2 (Argument) |
| 353 | 3.5 | Interview = häufigste Methode | 1 (Definition) |
| 353 | 3.5 | Interview-Vorteil ggü. Beobachtung | 2 (Vergleich) |
| 367 | 3.5 | Leitfaden-Interview | 1 (Definition) |
| 371 | 3.5 | Experteninterview: Spezialwissen | 1 (Definition) |
| 371 | 3.5 | Praxis-/Handlungswissen + Transfer | **3 (STARK)** |
| 354 | 3.5 | Interview-Nachteile | 2 (Reflexion) |
| 354 | 3.5 | Informationsdichte + Transfer | **3 (STARK)** |
| 393 | 3.5 | Fragebogen ungeeignet | 2 (Abgrenzung) |
| 525 | 3.5 | Dokumentenanalyse nonreaktiv | 2 (Argument) |
| 529 | 3.5 | Dokumentenanalyse fehlender Kontext | 2 (Argument) |
| 361 | 3.5 | 10-Schritte-Modell | 1 (Referenz) |
| 368 | 3.5 | Leitfaden 8-15 Fragen | 1 (Spezifikation) |
| 121 | 3.5 | Informierte Einwilligung | 1 (Ethik) |
| 362 | 3.5 | Wortwörtliche Transkription | 1 (Spezifikation) |
| 369 | 3.5 | 5-8 Stunden Transkriptionszeit | 1 (Detail) |
| 533 | 3.5 | Mayring Inhaltsanalyse | 1 (Referenz) |
| 592 | 3.5 | Fallbezogen + fallübergreifend | 1 (Spezifikation) |
| 598 | 3.5 | QDA-Software | 1 (Referenz) |

**Beim Kürzen:** Stufe-1-Belege sind die Kandidaten zum Komprimieren/Verschmelzen. Die 6 Stufe-3-Belege (fett markiert) sind sakrosankt.
