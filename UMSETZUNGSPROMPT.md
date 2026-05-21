# UMSETZUNGSPROMPT: Formale Rahmendokumente für MG3-Exposé

---

## AUFGABE IN EINEM SATZ

Ergänze das bestehende Word-Dokument `----Expose-----/Expose Mattis Engelhardt.docx` um alle formalen Rahmenelemente (Deckblatt, Inhaltsverzeichnis, Abkürzungsverzeichnis, Abbildungsverzeichnis, Gender-Disclaimer, Literaturverzeichnis, Anhangsverzeichnis, Anhang mit KI-Dokumentation und 8 Prompts, Ehrenwörtliche Erklärung) — ohne den bestehenden Fließtext in irgendeiner Weise zu verändern. Das Endergebnis ist ein fertig formatiertes `.docx`.

---

## KRITISCHE REGEL

**Den bestehenden Fließtext (Kapitel 1–3) UNTER KEINEN UMSTÄNDEN verändern.** Kein Wort, kein Zeichen, keine Formatierung. Die 41 bestehenden Paragraphen bleiben byte-identisch.

---

## TECHNISCHER ANSATZ: Unpack → Edit XML → Repack

### Warum dieser Ansatz?
Der Fließtext enthält komplexe Formatierungen (deutsche Heading-Styles `berschrift1`/`berschrift2`, kursive Forschungsfrage, zentriertes Bild mit Relationship-Referenz, spezifische Absatzabstände). Eine Neuerstellung mit docx-js würde diese brechen. Das XML-Editing erhält alles exakt.

### Ablauf:
1. Bestehende docx entpacken
2. `document.xml` programmatisch um Rahmenelemente erweitern (XML-Fragmente VOR und NACH dem Fließtext einfügen)
3. Logo-Bild hinzufügen, Relationships und Content_Types aktualisieren
4. Header/Footer XML für Seitenzahlen erstellen
5. Zurückpacken und validieren

### Tools und Pfade:
```
Unpack-Script:  python "c:/Users/engel/.claude/skills/docx/scripts/office/unpack.py"
Pack-Script:    python "c:/Users/engel/.claude/skills/docx/scripts/office/pack.py"
Validate:       python "c:/Users/engel/.claude/skills/docx/scripts/office/validate.py"
npm docx:       Installiert global (docx@9.6.1) — nur als Fallback, primär XML-Editing
```

---

## BESTEHENDES DOKUMENT — TECHNISCHE DETAILS

### Datei
```
c:/Users/engel/OneDrive/000000000000000000000000000 mg3/----Expose-----/Expose Mattis Engelhardt.docx
```

### Entpacken
```bash
python "c:/Users/engel/.claude/skills/docx/scripts/office/unpack.py" \
  "c:/Users/engel/OneDrive/000000000000000000000000000 mg3/----Expose-----/Expose Mattis Engelhardt.docx" \
  /tmp/expose_work/
```

### Paragraphen-Struktur (41 Paragraphen total)
```
Para 0:  style=berschrift1 → "1 Einleitung"
Para 1:  [Fließtext Einleitung — langer Absatz]
Para 2:  [PAGE BREAK]
Para 3:  style=berschrift1 → "2 Literature Review"
Para 4:  style=berschrift2 → "2.1 Literaturinhalte"
Para 5:  [Fließtext]
Para 6:  [IMAGE: Literaturlandkarte.jpg, zentriert]
Para 7:  [Bildunterschrift: "Abbildung 1: Literaturlandkarte", kursiv, linksbündig]
Para 8:  [Fließtext]
Para 9:  style=berschrift2 → "2.2 Theorien & Modelle"
Para 10: [Fließtext]
Para 11: style=berschrift2 → "2.3 Empirische Methoden"
Para 12: [Fließtext]
Para 13: style=berschrift2 → "2.4 Erkenntnisse der Autoren"
Para 14: [Fließtext]
Para 15: style=berschrift2 → "2.5 Welche Fragen bleiben offen und für wen sind sie relevant?"
Para 16: [Fließtext]
Para 17: style=berschrift2 → "2.6 Forschungslücken & Forschungsfrage"
Para 18: [Fließtext]
Para 19: [Fließtext mit Forschungsfrage kursiv]
Para 20: style=berschrift1 → "3 Untersuchungsdesign"
Para 21: [Fließtext]
Para 22: style=berschrift2 → "3.1 Erkenntnisziel und Erkenntnisinteresse"
Para 23-24: [Fließtext]
Para 25: style=berschrift2 → "3.2 Gegenstand"
Para 26-27: [Fließtext]
Para 28: style=berschrift2 → "3.3 Ansatz"
Para 29-30: [Fließtext]
Para 31: style=berschrift2 → "3.4 Untersuchungsobjekte"
Para 32-34: [Fließtext]
Para 35: style=berschrift2 → "3.5 Auswahl Erhebungsinstrumente"
Para 36-40: [Fließtext]
```

### Seitenformat (aus bestehender sectPr)
```xml
<w:pgSz w:w="12240" w:h="15840"/>  <!-- US Letter -->
<w:pgMar w:top="1134" w:right="2835" w:bottom="1134" w:left="1134"
         w:header="720" w:footer="720" w:gutter="0"/>
```
- **1134 DXA = 2 cm**, **2835 DXA = 5 cm**
- Entspricht: 2cm oben, 2cm links, 2cm unten, 5cm rechts

### Bestehende Relationships (document.xml.rels)
```xml
<Relationship Id="rId1" Type="...customXml" Target="../customXml/item1.xml"/>
<Relationship Id="rId2" Type="...numbering" Target="numbering.xml"/>
<Relationship Id="rId3" Type="...styles" Target="styles.xml"/>
<Relationship Id="rId4" Type="...settings" Target="settings.xml"/>
<Relationship Id="rId5" Type="...webSettings" Target="webSettings.xml"/>
<Relationship Id="rId6" Type="...image" Target="media/image1.jpg"/>  <!-- Literaturlandkarte -->
<Relationship Id="rId7" Type="...fontTable" Target="fontTable.xml"/>
<Relationship Id="rId8" Type="...theme" Target="theme/theme1.xml"/>
```

### Bestehende Content_Types
```xml
<Default Extension="jpg" ContentType="image/jpeg"/>
<Default Extension="rels" ContentType="...relationships+xml"/>
<Default Extension="xml" ContentType="application/xml"/>
<!-- Plus Override-Einträge für document.xml, numbering, styles, settings, etc. -->
```

### Heading-Styles (deutsch!)
Die Styles heißen `berschrift1`, `berschrift2` (nicht `Heading1`/`Heading2`). Das ist die deutsche Word-Lokalisierung. Neue Überschriften in den Rahmenelementen MÜSSEN dieselben Style-IDs verwenden.

### Schriftformatierung (Standard-Absatz)
```xml
<!-- Kein explizites rPr im Standard — erbt von styles.xml -->
<!-- Heading-Runs setzen explizit: -->
<w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:cs="Times New Roman"/>
```

---

## HFWU-LOGO

Das Logo wurde aus der Referenz-PDF (`MG2-Engelhardt-Mattis-Hausarbeit.pdf`) extrahiert:
```bash
python -c "
import fitz
doc = fitz.open('c:/Users/engel/OneDrive/000000000000000000000000000 mg3/MG2-Engelhardt-Mattis-Hausarbeit.pdf')
page = doc[0]
images = page.get_images()
xref = images[0][0]
pix = fitz.Pixmap(doc, xref)
if pix.n > 4:
    pix = fitz.Pixmap(fitz.csRGB, pix)
pix.save('/tmp/hfwu_logo.png')
"
```
- Datei: `/tmp/hfwu_logo.png`
- Größe: **346 × 173 Pixel**
- Ziel im docx: `word/media/image2.png` (image1.jpg ist bereits die Literaturlandkarte)

---

## ZU ERSTELLENDE ELEMENTE — EXAKTE INHALTE

### ELEMENT 1: Deckblatt (Seite 1 — KEINE Seitenzahl)

Layout zentriert, Times New Roman. Struktur von oben nach unten:

1. **HFWU-Logo** — zentriert, ca. 4cm breit (≈ 2268 EMU Breite, Höhe proportional)
2. Leerraum
3. **„Handel, Vertrieb und E-Commerce"** — fett, zentriert, 14pt
4. Leerzeile
5. „Schriftliche Arbeit" — zentriert, 12pt
6. „im Modul" — zentriert, 12pt
7. **„Methodische Grundlagen 3"** — fett, zentriert, 14pt
8. Leerzeile
9. „Sommersemester 2026" — zentriert, 12pt
10. Leerraum
11. „vorgelegt von" — zentriert, 12pt
12. „Mattis Engelhardt (Matr. Nr. 4110790)" — zentriert, 12pt
13. Leerzeile
14. „vorgelegt bei" — zentriert, 12pt
15. „Herrn Prof. Dr. Dirk Funck" — zentriert, 12pt
16. Leerzeile
17. „HfWU Nürtingen-Geislingen" — zentriert, 12pt
18. Leerraum
19. „Abgabedatum: 18.05.2026" — zentriert, 12pt

**Danach: Page Break** (kein Section Break — Forschungsfrage-Seite gehört noch zur selben Section)

### ELEMENT 2: Forschungsfrage-Seite (Seite 2 — KEINE Seitenzahl)

1. Vertikaler Leerraum (ca. 1/3 der Seite)
2. **„Übergeordnete Forschungsfrage"** — zentriert, fett, 14pt
3. Leerzeile
4. *„Welche Rolle spielt KI in der Gründungsphase von B2C-E-Commerce-Startups zur Stärkung des Unit-Profitability-First-Gedankens?"* — zentriert, kursiv, 12pt

**Danach: Section Break (nächste Seite)** → neue Section für Vorspann mit römischen Seitenzahlen

### ELEMENT 3: Inhaltsverzeichnis (römische Seitenzahlen beginnen)

Überschrift: **„Inhaltsverzeichnis"** — als `berschrift1`-Style, aber OHNE Nummerierung (kein „1" davor)

Inhalte des TOC (manuell ODER als TOC-Feld):

**Empfehlung: TOC-Feld einfügen**, das beim Öffnen in Word automatisch aktualisiert wird:
```xml
<w:p>
  <w:r>
    <w:fldChar w:fldCharType="begin"/>
  </w:r>
  <w:r>
    <w:instrText xml:space="preserve"> TOC \o "1-2" \h \z \u </w:instrText>
  </w:r>
  <w:r>
    <w:fldChar w:fldCharType="separate"/>
  </w:r>
  <w:r>
    <w:t>Bitte Inhaltsverzeichnis aktualisieren (Rechtsklick → Felder aktualisieren)</w:t>
  </w:r>
  <w:r>
    <w:fldChar w:fldCharType="end"/>
  </w:r>
</w:p>
```

Die erwartete TOC-Struktur nach Aktualisierung:
```
Abkürzungsverzeichnis ........................... I
Abbildungsverzeichnis .......................... II
1   Einleitung .................................. 1
2   Literature Review ........................... 2
    2.1  Literaturinhalte ....................... 2
    2.2  Theorien & Modelle ..................... 3
    2.3  Empirische Methoden .................... 4
    2.4  Erkenntnisse der Autoren ............... 4
    2.5  Welche Fragen bleiben offen ... ........ 5
    2.6  Forschungslücken & Forschungsfrage ..... 6
3   Untersuchungsdesign ......................... 7
    3.1  Erkenntnisziel und Erkenntnisinteresse . 7
    3.2  Gegenstand ............................. 8
    3.3  Ansatz ................................. 8
    3.4  Untersuchungsobjekte ................... 9
    3.5  Auswahl Erhebungsinstrumente ........... 9
Literatur- und Quellenverzeichnis .............. 11
Anhangsverzeichnis ............................. 12
Ehrenwörtliche Erklärung ....................... XX
```

**Danach: Page Break**

### ELEMENT 4: Abkürzungsverzeichnis

Überschrift: **„Abkürzungsverzeichnis"** — als `berschrift1`-Style, OHNE Nummerierung

Tabelle mit 2 Spalten (Abkürzung | Bedeutung), OHNE Rahmenlinien (analog Referenz-PDF — dort ist es eine einfache tabulatorgetrennte Liste, kein Rahmen):

```
AI          Artificial Intelligence
B2C         Business-to-Consumer
CEO         Chief Executive Officer
DTC         Direct-to-Consumer
ERM         Emotional-Rational-Motivational Model
IT          Information Technology
KECCT       Knowledge-Experience-Competence-Characteristics-Team
KI          Künstliche Intelligenz
MAXQDA      Software für qualitative Datenanalyse
QDA         Qualitative Datenanalyse
S.          Seite
vgl.        vergleiche
z. B.       zum Beispiel
u. a.       unter anderem
```

**Danach: Page Break**

### ELEMENT 5: Abbildungsverzeichnis

Überschrift: **„Abbildungsverzeichnis"** — als `berschrift1`-Style, OHNE Nummerierung

Ein Eintrag:
```
Abb. 1: Literaturlandkarte ..................... S. X
```

(Seitenzahl X wird nach TOC-Aktualisierung in Word korrekt — alternativ als Feld)

**Danach: Page Break**

### ELEMENT 6: Gender-Disclaimer

**Kein Heading-Style** — einfacher Absatz, kursiv:

*„Aus Gründen der besseren Lesbarkeit wird in dieser Arbeit die maskuline Sprachform verwendet. Sämtliche Personenbezeichnungen gelten gleichermaßen für alle Geschlechter."*

**Danach: Section Break (nächste Seite)** → neue Section für Body mit arabischen Seitenzahlen ab 1

---

### ═══ HIER BEGINNT DER BESTEHENDE FLIESSTEXT (Para 0–40) — NICHT ANFASSEN ═══

---

### ═══ HIER ENDET DER BESTEHENDE FLIESSTEXT ═══

**Danach: Page Break** (innerhalb derselben Section — arabische Seitenzahlen laufen weiter)

---

### ELEMENT 7: Literatur- und Quellenverzeichnis

Überschrift: **„Literatur- und Quellenverzeichnis"** — als `berschrift1`-Style, OHNE Nummerierung

Die folgenden 11 Einträge **exakt so wie hier angegeben** (Quelle: `output_marker/Notwendiges zu meiner Hausarbeit (Forschungsfrage etc)/Notwendiges zu meiner Hausarbeit (Forschungsfrage etc).md`, Zeilen 57-67). Formatierung: Hängender Einzug (erste Zeile bündig, Folgezeilen 1,25cm eingerückt), 12pt Times New Roman.

```
Aryadita, H., Sukoco, B. M., & Lyver, M. (2023). Founders and the success of start-ups: An integrative review. Cogent Business & Management, 10(3), 2284451. https://doi.org/10.1080/23311975.2023.2284451

Byun, K. J., & Yoo, S. (2025). Does overconfidence of CEOs increase startup performance? The role of marketing capability. European Journal of Marketing, 59(5), 1400–1425. https://doi.org/10.1108/EJM-01-2024-0085

Cutolo, D., & Kenney, M. (2021). Platform-Dependent Entrepreneurs: Power Asymmetries, Risks, and Strategies in the Platform Economy. Academy of Management Perspectives, 35(4), 584–605. https://doi.org/10.5465/amp.2019.0103

Döring, N. (2023). Forschungsmethoden und Evaluation in den Sozial- und Humanwissenschaften. Springer Berlin Heidelberg. https://doi.org/10.1007/978-3-662-64762-2

Guo, H., Guo, A., & Ma, H. (2022). Inside the black box: How business model innovation contributes to digital start-up performance. Journal of Innovation & Knowledge, 7(2), 100188. https://doi.org/10.1016/j.jik.2022.100188

Helfat, C. E. (2022). Strategic organization, dynamic capabilities, and the external environment. Strategic Organization, 20(4), 734–742. https://doi.org/10.1177/14761270221115377

Helfat, C. E., & Peteraf, M. A. (2015). Managerial cognitive capabilities and the microfoundations of dynamic capabilities. Strategic Management Journal, 36(6), 831–850. https://doi.org/10.1002/smj.2247

McKee, S., Sands, S., Pallant, J. I., & Cohen, J. (2023). The evolving direct-to-consumer retail model: A review and research agenda. International Journal of Consumer Studies, 47(6), 2816–2842. https://doi.org/10.1111/ijcs.12972

Tidhar, R., Hallen, B. L., & Eisenhardt, K. M. (2025). Measure Twice, Cut Once: Unit Profitability, Scalability, and the Exceptional Growth of New Firms. Organization Science, 36(1), 88–120. https://doi.org/10.1287/orsc.2021.15970

Weng, Q., Wang, D., De Lurgio Ii, S., & Schuetz, S. (2025). How do small-to-medium-sized e-commerce businesses stay competitive? Evidence on the critical roles of IT capability, innovation and multihoming. Internet Research, 35(1), 126–151. https://doi.org/10.1108/INTR-01-2023-0061

Yang, H., Zhang, Y., Chen, K., & Li, J. (2023). The double-edged sword of delivery guarantee in E-commerce. Decision Support Systems, 175, 114042. https://doi.org/10.1016/j.dss.2023.114042
```

**Hinweis zur Formatierung:** Zeitschriftentitel kursiv. DOI als aktiver Hyperlink (optional — wenn zu komplex, einfach als Text).

**Danach: Page Break**

### ELEMENT 8: Anhangsverzeichnis

Überschrift: **„Anhangsverzeichnis"** — als `berschrift1`-Style, OHNE Nummerierung

Einträge mit Tabulatoren und Seitenzahlen (Seitenzahlen als Platzhalter, da erst nach Finalisierung korrekt):

```
Literaturlandkarte                                              S. XX
Anhang 0: Anmerkung und Dokumentation zur Arbeit mit KI         S. XX
Anhang 1: Prompt 1                                              S. XX
Anhang 1.5: Prompt 1.5                                          S. XX
Anhang 2: Prompt 2                                              S. XX
Anhang 3: Prompt 3                                              S. XX
Anhang 3.5: Prompt 3.5                                          S. XX
Anhang 4: Prompt 4                                              S. XX
Anhang 5: Prompt 5                                              S. XX
Anhang 6: Prompt 6                                              S. XX
```

**Danach: Page Break**

### ELEMENT 9: Literaturlandkarte (eigene Seite)

Überschrift: **„Literaturlandkarte"** — als `berschrift1`-Style, OHNE Nummerierung

Die Literaturlandkarte existiert bereits als Bild im Body (Abbildung 1). Hier dieselbe Grafik erneut einfügen — ganzseitig/groß. Die Bilddatei ist `word/media/image1.jpg` (= `Literaturlandkarte.jpg` im Projektroot).

Alternativ einfach einen Verweis-Text setzen: *„Siehe Abbildung 1 im Literature Review"* — falls das Einfügen des gleichen Bildes technisch Probleme macht.

**Danach: Page Break**

### ELEMENT 10: Anhang 0 — Anmerkung und KI-Dokumentation

Überschrift: **„Anhang 0: Anmerkung und Dokumentation zur Arbeit mit KI"** — als `berschrift1`-Style, OHNE Nummerierung

#### Teil 1: Anmerkung

Folgenden Text als normalen Absatz setzen (Ton und Struktur analog zur Referenz-PDF, aber inhaltlich auf den tatsächlichen MG3-Workflow angepasst):

```
Anmerkung:

Alle Kapitel dieser Arbeit wurden mithilfe eines generativen KI-Tools formuliert (Fall 2: Textgenerierung). Als KI-Tool wurde Claude Code (Claude Opus 4.6, Anthropic) eingesetzt. Die Literaturrecherche und Quellenauswahl erfolgten durch den Verfasser. Relevante Textstellen wurden vom Verfasser aus den Quellen entnommen, mit Seitenangaben dokumentiert und als Inputs in den jeweiligen Prompts verortet. Die KI wurde angewiesen, diese vorgegebenen Quellenstellen ausschließlich als Evidenzbasis zu verwenden und keine eigenständige Quellenrecherche oder Quellenentnahme aus dem Internet vorzunehmen. Der zugrunde gelegte Quellen- und Zitatpool wurde vollständig vom Verfasser definiert. Die methodische Quelle (Döring, 2023) wurde als Markdown-Datei bereitgestellt und gezielt per Keyword-Suche durchforstet.
```

#### Teil 2: Tabellarische Dokumentation

Tabelle mit 4 Spalten. Formatierung: 10pt, Rahmenlinien, Kopfzeile fett/grau hinterlegt.

| KI | Einsatzzweck | Ausführliche Beschreibung | Prompt |
|---|---|---|---|
| Claude Code 01 | Workflow-Planung und Erstellung der Markdown-Arbeitsgrundlage | Der Prompt dient dazu, eine strukturierte Planung für das Exposé-Projekt zu erstellen, einschließlich der Analyse aller Quelldateien und der Erstellung einer konsolidierten Markdown-Datei als Arbeitsgrundlage für alle weiteren Schritte. | Prompt zu lang — siehe Anhang 1 |
| Claude Code 01.5 | Vorarbeit Einleitung: Zitat-Recherche | Der Prompt dient dazu, systematisch zitierfähige Stellen aus den 10 inhaltlichen Quellen zu identifizieren und für die Einleitung aufzubereiten, wobei ausschließlich aus dem Kernpart (nicht Abstract/Introduction) zitiert werden darf. | Prompt zu lang — siehe Anhang 1.5 |
| Claude Code 02 | Einleitung schreiben | Der Prompt dient dazu, die wissenschaftliche Einleitung (ca. 1 Seite) zu generieren, die vom Makroproblem zur Forschungsfrage führt, alle Stakeholder benennt und einen Ausblick auf die Methodik gibt. | Prompt zu lang — siehe Anhang 2 |
| Claude Code 03 | Synthese-Plan für den Literature Review | Der Prompt dient dazu, einen detaillierten Synthese-Plan als Vorarbeit für den Literature Review zu erstellen, in dem die 10 Quellen systematisch verglichen und Forschungslücken identifiziert werden. | Prompt zu lang — siehe Anhang 3 |
| Claude Code 03.5 | Literature Review schreiben | Der Prompt dient dazu, den Literature Review (ca. 4 Seiten) als wissenschaftlichen Fließtext zu verfassen, basierend auf dem Synthese-Plan, mit vergleichender Gegenüberstellung der Quellen und Ableitung der Forschungsfrage. | Prompt zu lang — siehe Anhang 3.5 |
| Claude Code 04 | Tiefenrecherche Untersuchungsdesign | Der Prompt dient dazu, die Döring-Quelle systematisch zu durchforsten und einen Synthese-Plan mit exakten Zitaten als Grundlage für das Untersuchungsdesign zu erstellen. | Prompt zu lang — siehe Anhang 4 |
| Claude Code 05 | Synthese-Blueprint Untersuchungsdesign | Der Prompt dient dazu, aus den Döring-Rechercheergebnissen einen konkreten Blueprint für die Struktur und Argumentation des Untersuchungsdesigns zu entwickeln. | Prompt zu lang — siehe Anhang 5 |
| Claude Code 06 | Untersuchungsdesign schreiben | Der Prompt dient dazu, das Untersuchungsdesign (ca. 5 Seiten) als wissenschaftlichen Fließtext zu generieren, mit allen 7 Aspekten und dem Erhebungsinstrument, belegt ausschließlich mit Döring (2023). | Prompt zu lang — siehe Anhang 6 |

**Danach: Page Break**

### ELEMENT 11–18: Anhang 1 bis Anhang 6 (die 8 Prompts)

Für jeden der 8 Prompts eine eigene Seite (bzw. mehrere Seiten bei langen Prompts):

**Überschrift:** „Anhang X: Prompt X" — als `berschrift1`-Style, OHNE Nummerierung

**Inhalt:** Den vollständigen Text aus der jeweiligen Prompt-Datei 1:1 übernehmen, ohne jede Bearbeitung.

Die Prompt-Dateien befinden sich im Projektroot als `.docx` und müssen zuerst entpackt und als Text extrahiert werden:

```bash
# Für jede Prompt-Datei:
python "c:/Users/engel/.claude/skills/docx/scripts/office/unpack.py" \
  "c:/Users/engel/OneDrive/000000000000000000000000000 mg3/DATEINAME.docx" \
  /tmp/prompt_tmp/

# Dann Text aus document.xml extrahieren (alle <w:t>-Inhalte zusammenfügen)
```

| Anhang-Nr. | Dateiname | Zeichenanzahl |
|---|---|---|
| Anhang 1 | `Prompt 1 Workflow und MD Datei.docx` | ~9.300 |
| Anhang 1.5 | `Prompt 1.5 Vorarbeit Einleitung.docx` | ~6.000 |
| Anhang 2 | `Prompt 2 Einleitung schreiben.docx` | ~9.600 |
| Anhang 3 | `Prompt 3 Synthese Plan.docx` | ~16.200 |
| Anhang 3.5 | `Prompt 3.5 Literature Review.docx` | ~13.200 |
| Anhang 4 | `Prompt 4 Untersuchungsdesign Tiefenrecherche.docx` | ~28.200 |
| Anhang 5 | `Prompt 5.docx` | ~5.400 |
| Anhang 6 | `Prompt 6.docx` | ~31.600 |

**WICHTIG:** Die Prompts enthalten Markdown-Formatierung (##, **, ---, etc.). Diese soll als reiner Text erscheinen — KEINE Interpretation als Formatierung. Einfach als Monospace-Text (Courier New 9pt) oder als normaler Text (Times New Roman 10pt) setzen. Die Referenz-PDF zeigt die Prompts als normalen, kleineren Text.

**Zwischen jedem Prompt: Page Break**

### ELEMENT 19: Ehrenwörtliche Erklärung (letzte Seite)

Überschrift: **„Ehrenwörtliche Erklärung"** — als `berschrift1`-Style, OHNE Nummerierung

Text **wortgleich** wie folgt:

```
Wir versichern hiermit ehrenwörtlich:

1. dass wir unsere schriftliche Prüfungsleistung selbständig und ohne fremde Hilfe angefertigt und keine anderen Quellen und Hilfsmittel als die angegebenen verwendet haben,

2. dass wir wissen, dass wir stets zu wissenschaftlicher Redlichkeit verpflichtet sind und die Grundsätze guter wissenschaftlicher Praxis eingehalten haben – das schließt auch die ggf. durch die Prüfer*innen für meine Arbeit weiterführenden Auflagen zur Umsetzung der guten wissenschaftlichen Praxis (z. B. der Umgang/die Nutzung KI-gestützter Werkzeuge) ein.

3. dass wir insbesondere die Übernahme wörtlicher Zitate sowie die Verwendung oder Verarbeitung von Gedanken Dritter an den entsprechenden Stellen eindeutig gekennzeichnet haben.

Uns ist bewusst, dass die Unrichtigkeit dieser Erklärung zur Folge haben kann, dass wir von der Ableistung weiterer Prüfungsleistungen nach § 15 Abs.3 sowie § 17 Abs.1 der Studien- und Prüfungsordnung der Hochschule für Wirtschaft und Umwelt Nürtingen-Geislingen – Allgemeiner Teil für Bachelor- und Masterstudiengänge in der jeweils geltenden Fassung ausgeschlossen werden bzw. ausgeschlossen sein können und dadurch unter Umständen den Prüfungsanspruch im Studiengang endgültig verlieren.

Nürtingen, 18.05.2026
```

Darunter: Leerraum für Unterschrift und eine Linie: `_______________________________`

---

## SEITENNUMMERIERUNG — SECTION-MANAGEMENT

Das Dokument braucht **3 Sections** mit unterschiedlicher Nummerierung:

### Section 1: Deckblatt + Forschungsfrage (KEINE Seitenzahl)
- Umfasst: Element 1 + Element 2
- Footer: leer (keine Seitenzahl)
- Endet mit: `<w:sectPr>` nach der Forschungsfrage-Seite

```xml
<w:sectPr>
  <w:pgSz w:w="12240" w:h="15840"/>
  <w:pgMar w:top="1134" w:right="2835" w:bottom="1134" w:left="1134"
           w:header="720" w:footer="720" w:gutter="0"/>
  <w:cols w:space="720"/>
  <w:titlePg/>  <!-- Erste Seite hat eigenen Header/Footer (=leer) -->
</w:sectPr>
```

### Section 2: Vorspann (römische Seitenzahlen)
- Umfasst: Element 3 (Inhaltsverzeichnis) + Element 4 (Abkürzungsverzeichnis) + Element 5 (Abbildungsverzeichnis) + Element 6 (Gender-Disclaimer)
- Footer: Seitenzahl zentriert, römisch (I, II, III, ...)
- Endet mit: `<w:sectPr>` nach dem Gender-Disclaimer

```xml
<w:sectPr>
  <w:type w:val="nextPage"/>
  <w:pgSz w:w="12240" w:h="15840"/>
  <w:pgMar w:top="1134" w:right="2835" w:bottom="1134" w:left="1134"
           w:header="720" w:footer="720" w:gutter="0"/>
  <w:pgNumType w:fmt="lowerRoman"/>
  <w:cols w:space="720"/>
  <w:footerReference w:type="default" r:id="rIdFooterRoman"/>
</w:sectPr>
```

### Section 3: Body + alles danach (arabische Seitenzahlen ab 1)
- Umfasst: Element 7 (Body) + Element 8 (Literaturverzeichnis) + Element 9 (Anhangsverzeichnis) + Element 10-18 (Anhänge) + Element 19 (Ehrenwörtliche Erklärung)
- Footer: Seitenzahl zentriert, arabisch, beginnend bei 1
- Die **bestehende `<w:sectPr>` am Ende der document.xml** wird hierfür angepasst

```xml
<w:sectPr>
  <w:pgSz w:w="12240" w:h="15840"/>
  <w:pgMar w:top="1134" w:right="2835" w:bottom="1134" w:left="1134"
           w:header="720" w:footer="720" w:gutter="0"/>
  <w:pgNumType w:fmt="decimal" w:start="1"/>
  <w:cols w:space="720"/>
  <w:footerReference w:type="default" r:id="rIdFooterArabic"/>
</w:sectPr>
```

### Footer-Dateien erstellen

Es müssen **2 Footer-XML-Dateien** erstellt werden:

**`word/footer1.xml`** (römische Nummern):
```xml
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:ftr xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"
       xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">
  <w:p>
    <w:pPr>
      <w:jc w:val="center"/>
      <w:rPr>
        <w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/>
        <w:sz w:val="24"/>
      </w:rPr>
    </w:pPr>
    <w:r>
      <w:rPr>
        <w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/>
        <w:sz w:val="24"/>
      </w:rPr>
      <w:fldChar w:fldCharType="begin"/>
    </w:r>
    <w:r>
      <w:instrText> PAGE </w:instrText>
    </w:r>
    <w:r>
      <w:fldChar w:fldCharType="end"/>
    </w:r>
  </w:p>
</w:ftr>
```

**`word/footer2.xml`** (arabische Nummern — identische Struktur, Nummerierungsformat wird über `pgNumType` in der sectPr gesteuert):
```xml
<!-- Identisch zu footer1.xml — das Format kommt aus der Section Property -->
```

### Neue Relationships hinzufügen

In `word/_rels/document.xml.rels` folgende Einträge ergänzen:

```xml
<Relationship Id="rId9" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" Target="media/image2.png"/>
<Relationship Id="rId10" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/footer" Target="footer1.xml"/>
<Relationship Id="rId11" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/footer" Target="footer2.xml"/>
```

### Content_Types aktualisieren

In `[Content_Types].xml` hinzufügen:

```xml
<Default Extension="png" ContentType="image/png"/>
<Override PartName="/word/footer1.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.footer+xml"/>
<Override PartName="/word/footer2.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.footer+xml"/>
```

---

## IMPLEMENTIERUNGSSTRATEGIE

Da die XML-Manipulation sehr umfangreich ist (insbesondere die langen Prompt-Texte mit je bis zu 32.000 Zeichen), empfehle ich ein **Python-Script**, das:

1. Die entpackte `document.xml` einliest
2. Den `<w:body>`-Inhalt parst und die Position des ersten und letzten Body-Paragraphen identifiziert
3. XML-Fragmente für alle Rahmenelemente generiert (mit Escape für `&`, `<`, `>`, Anführungszeichen)
4. Die Fragmente vor/nach dem Body einfügt
5. Die Section Properties korrekt setzt
6. Alle Prompt-Dateien automatisch entpackt und deren Text extrahiert
7. Die Footer-Dateien erstellt
8. Relationships und Content_Types aktualisiert
9. Das Logo-Bild in `word/media/` kopiert
10. Alles zurückpackt

### XML-Escape-Regeln für Prompt-Texte
Die Prompt-Texte enthalten `&`, `<`, `>`, `"` und Sonderzeichen. Diese MÜSSEN escaped werden:
- `&` → `&amp;`
- `<` → `&lt;`
- `>` → `&gt;`
- `"` → `&quot;` (innerhalb von Attributen)
- Zeilenumbrüche (`\n`) → neue `<w:p>` Paragraphen

### Paragraph-XML-Template für normalen Text
```xml
<w:p>
  <w:pPr>
    <w:spacing w:after="120" w:line="360" w:lineRule="auto"/>
    <w:jc w:val="both"/>
    <w:rPr>
      <w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:cs="Times New Roman"/>
      <w:sz w:val="24"/>
      <w:szCs w:val="24"/>
    </w:rPr>
  </w:pPr>
  <w:r>
    <w:rPr>
      <w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:cs="Times New Roman"/>
      <w:sz w:val="24"/>
      <w:szCs w:val="24"/>
    </w:rPr>
    <w:t xml:space="preserve">TEXT HIER</w:t>
  </w:r>
</w:p>
```

### Heading-XML-Template (für Rahmenelemente-Überschriften)
```xml
<w:p>
  <w:pPr>
    <w:pStyle w:val="berschrift1"/>
    <w:rPr>
      <w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:cs="Times New Roman"/>
    </w:rPr>
  </w:pPr>
  <w:r>
    <w:rPr>
      <w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:cs="Times New Roman"/>
    </w:rPr>
    <w:t>ÜBERSCHRIFT HIER</w:t>
  </w:r>
</w:p>
```

### Section-Break-Paragraphen
```xml
<w:p>
  <w:pPr>
    <w:sectPr>
      <!-- Section Properties hier -->
    </w:sectPr>
  </w:pPr>
</w:p>
```

### Page-Break-Paragraphen
```xml
<w:p>
  <w:r>
    <w:br w:type="page"/>
  </w:r>
</w:p>
```

### Bild-Einbettung (Logo)
```xml
<w:p>
  <w:pPr>
    <w:jc w:val="center"/>
  </w:pPr>
  <w:r>
    <w:rPr>
      <w:noProof/>
    </w:rPr>
    <w:drawing>
      <wp:inline distT="0" distB="0" distL="0" distR="0"
                 xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing">
        <wp:extent cx="2268000" cy="1134000"/>
        <wp:effectExtent l="0" t="0" r="0" b="0"/>
        <wp:docPr id="2" name="HFWU Logo"/>
        <wp:cNvGraphicFramePr>
          <a:graphicFrameLocks xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" noChangeAspect="1"/>
        </wp:cNvGraphicFramePr>
        <a:graphic xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">
          <a:graphicData uri="http://schemas.openxmlformats.org/drawingml/2006/picture">
            <pic:pic xmlns:pic="http://schemas.openxmlformats.org/drawingml/2006/picture">
              <pic:nvPicPr>
                <pic:cNvPr id="0" name="image2.png"/>
                <pic:cNvPicPr/>
              </pic:nvPicPr>
              <pic:blipFill>
                <a:blip r:embed="rId9"/>
                <a:stretch>
                  <a:fillRect/>
                </a:stretch>
              </pic:blipFill>
              <pic:spPr>
                <a:xfrm>
                  <a:off x="0" y="0"/>
                  <a:ext cx="2268000" cy="1134000"/>
                </a:xfrm>
                <a:prstGeom prst="rect">
                  <a:avLst/>
                </a:prstGeom>
              </pic:spPr>
            </pic:pic>
          </a:graphicData>
        </a:graphic>
      </wp:inline>
    </w:drawing>
  </w:r>
</w:p>
```

**Logo-Dimensionen:** Original 346×173px. Bei 96 DPI → ca. 3,6×1,8 Zoll. Für das Deckblatt etwas vergrößern: 2268000×1134000 EMU (≈ 6×3 cm). Ggf. anpassen — Verhältnis 2:1 beibehalten.

---

## REPACK UND VALIDIERUNG

```bash
# Zurückpacken
python "c:/Users/engel/.claude/skills/docx/scripts/office/pack.py" \
  /tmp/expose_work/ \
  "c:/Users/engel/OneDrive/000000000000000000000000000 mg3/----Expose-----/Expose Mattis Engelhardt FINAL.docx" \
  --original "c:/Users/engel/OneDrive/000000000000000000000000000 mg3/----Expose-----/Expose Mattis Engelhardt.docx"

# Validieren
python "c:/Users/engel/.claude/skills/docx/scripts/office/validate.py" \
  "c:/Users/engel/OneDrive/000000000000000000000000000 mg3/----Expose-----/Expose Mattis Engelhardt FINAL.docx"
```

**Output-Datei:** `----Expose-----/Expose Mattis Engelhardt FINAL.docx` (nicht die Originaldatei überschreiben!)

---

## CHECKLISTE NACH FERTIGSTELLUNG

- [ ] Fließtext (Kapitel 1–3) ist identisch mit dem Original
- [ ] Deckblatt zeigt: „Handel, Vertrieb und E-Commerce" (ohne Social Entrepreneurship), MG3, SoSe 2026, 18.05.2026
- [ ] Forschungsfrage-Seite ist separat nach dem Deckblatt
- [ ] Inhaltsverzeichnis enthält TOC-Feld (aktualisierbar in Word)
- [ ] Abkürzungsverzeichnis enthält alle 14 Einträge
- [ ] Abbildungsverzeichnis enthält Abb. 1
- [ ] Gender-Disclaimer steht vor der Einleitung
- [ ] Literaturverzeichnis enthält exakt 11 Einträge in APA-Format
- [ ] Anhangsverzeichnis listet alle 10 Anhänge
- [ ] Anhang 0 enthält Anmerkung + KI-Dokumentationstabelle (8 Einträge)
- [ ] Alle 8 Prompts sind vollständig im Anhang (1:1 aus den Quelldateien)
- [ ] Ehrenwörtliche Erklärung ist wortgleich, Datum 18.05.2026
- [ ] Seitenzahlen: Deckblatt+FQ ohne, Vorspann römisch, Body arabisch ab 1
- [ ] HFWU-Logo erscheint auf dem Deckblatt
- [ ] Formatierung: Times New Roman 12pt, Blocksatz, 1,5-Zeilenabstand, Ränder 2/5/2/2 cm
- [ ] Dokument öffnet fehlerfrei in Word
