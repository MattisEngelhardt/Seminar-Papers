# Aufgabenbeschreibung: Exposé-Projekt mit KI-gestütztem Workflow

---

## Übergeordnetes Ziel

Das übergeordnete Ziel dieser ersten Phase ist die Erstellung einer sehr genauen, strukturierten Planung, die als vollständiges Framework für den gesamten weiteren Schreibprozess dient. Zentrales Element dieser Planung ist eine professionell ausgearbeitete Markdown-Datei, die als operatives Steuerungsdokument fungiert. Diese Datei muss die Kernaufgabenstellung präzise beschreiben, das methodische Vorgehen klar darlegen, alle relevanten Dateien im Projektordner benennen und eindeutig kategorisieren — insbesondere welche Dateien bei jedem neuen Prompt zwingend gelesen werden müssen (Pflichtlektüre) und welche nur kontextabhängig hinzugezogen werden sollten, um unnötigen Token-Verbrauch zu vermeiden.

---

## Die eigentliche Aufgabe: Das Exposé

Die abzugebende und bewertete Leistung ist ein akademisches Exposé. Ein Exposé in diesem Sinne bedeutet: kein inhaltliches Beantworten der Forschungsfrage, sondern das schriftliche Niederlegen eines Untersuchungsdesigns — also die theoretische Darlegung, wie man methodisch vorgehen würde, um die Forschungsfrage wissenschaftlich zu beantworten.

Die Forschungsfrage ist bereits festgelegt und lautet:

„Welche Rolle spielt KI in der Gründungsphase von B2C-E-Commerce-Startups bei der Stärkung des Unit-Profitability-First-Gedankens?"

Diese Forschungsfrage findet sich ebenfalls in der Markdown-Datei „Notwendiges zu meiner Hausarbeit (Forschungsfrage etc)".

---

## Struktur des Exposés

Das Exposé gliedert sich in zwei Hauptteile:

**1. Einleitung**

Die Einleitung folgt dem Prinzip der Makro-zu-Mikro-Hinführung: Ausgehend von einem übergeordneten gesellschaftlichen oder wirtschaftlichen Problem wird schrittweise und präzise auf die konkrete Forschungsfrage hingeführt. Für diesen Teil sind ausschließlich die 10 inhaltlichen Quellen in `output_marker/` maßgeblich. Sie haben zur Definition der Forschungsfrage geführt und liefern die argumentative Grundlage für die Einleitung.

**2. Hauptteil: Untersuchungsdesign**

Im Hauptteil wird das Untersuchungsdesign ausgeführt. Jede methodische Aussage muss zwingend mit der Forschungsmethoden-Quelle belegt werden. Es darf im Hauptteil keine unbelegte Begründung geben, die das Untersuchungsdesign betrifft. Die inhaltlichen Quellen spielen im Hauptteil keine Rolle mehr, da sie lediglich zur Herleitung der Forschungsfrage dienten, nicht zur methodischen Begründung.

---

## Dateistruktur des Projektordners und Nutzungslogik

Alle Quellen wurden einmalig mit spezialisierten Tools vorverarbeitet und liegen als Markdown-Dateien vor. Es wird ausschließlich mit diesen Markdown-Dateien gearbeitet — die originalen PDFs sind nicht mehr relevant und werden ignoriert. Der `.venv`-Ordner war nur für die einmalige Installation der Verarbeitungstools notwendig und spielt im Schreibprozess keine Rolle.

---

### `output_marker/` — Hauptquellenordner (10 inhaltliche Quellen + 4 weitere Dokumente)

Dieser Ordner enthält die mit dem Tool **Marker** verarbeiteten Inhalte. Marker wurde gewählt weil es neuronale Layout-Erkennung einsetzt, Grafiken extrahiert und inhaltlich vollständiger ist als einfache Textextraktion.

Jede Quelle liegt in einem eigenen Unterordner mit folgender Struktur:

```

Beispiel für ein gutes Expose/

  ├── Beispiel für ein gutes Expose.md       ← die zu lesende Datei

  ├── Beispiel für ein gutes Expose_meta.json

  ├── _page_0_Picture_0.jpeg                  ← extrahierte Grafiken (falls vorhanden)

  └── _page_4_Picture_3.jpeg

```

**Ausschließlich die `.md`-Datei wird gelesen.** Die `_meta.json` und Bilddateien sind Nebenprodukte der Extraktion und werden nur bei Bedarf hinzugezogen.

---

**Wichtiger Hinweis zur Struktur von `output_marker/`:**

Der Ordner `output_marker/` enthält insgesamt 14 Unterordner — nicht nur die 10 inhaltlichen Quellen. Die restlichen 4 Unterordner enthalten keine wissenschaftlichen Quellen, sondern die formalen Rahmendokumente des Projekts (Vorlesungsskript, Beispiel-Exposé, KI-Nutzung, Hausarbeitsinfos). Beide Gruppen befinden sich gleichrangig im selben Ordner. Die Unterscheidung ist rein funktional: Die 10 wissenschaftlichen Quellen sind ausschließlich für die Einleitung relevant, die 4 formalen Dokumente strukturieren den gesamten Arbeitsprozess. Es darf keine Verwechslung oder Vermischung dieser beiden Gruppen stattfinden.

---

**10 inhaltliche Quellen — ausschließlich für die Einleitung:**

- `Does overconfidence of CEOs increase startup performance The role of marketing capability/`

- `Founders and the success of start-ups  An integrative review (9)/`

- `How do small-to-medium-sized/`

- `Inside the black box How business model innovation contributes to digital start-up performance/`

- `MANAGERIAL COGNITIVE CAPABILITIES AND THEMICROFOUNDATIONS OF DYNAMIC CAPABILITIES/`

- `Measure Twice, Cut Once Unit Profitability, Scalability, and the/`

- `PLATFORM-DEPENDENT ENTREPRENEURS/`

- `Strategic organization, dynamic/`

- `The double-edged sword of delivery guarantee in E-commerce/`

- `The evolving direct-to-consumer retail model A review and/`

**4 weitere Dokumente in `output_marker/`:**

- `Vorlesungsskript zur Aufgabenleistung/` — enthält die vollständige Kernaufgabenstellung, alle Anforderungen des Professors sowie den Bewertungsbogen. Eines der wichtigsten Dokumente überhaupt.

- `Notwendiges zu meiner Hausarbeit (Forschungsfrage etc)/` — enthält die Forschungsfrage sowie allgemeine Informationen wie das Literaturverzeichnis. Kurzes Dokument, gilt als Pflichtlektüre bei jedem Prompt.

- `Beispiel für ein gutes Expose/` — kein permanentes Pflichtdokument, muss jedoch zu Beginn des Hauptteils vollständig und analytisch gelesen werden. Dabei soll nicht nur verstanden werden, was gut ist, sondern auch wo mögliche Schwächen oder Lücken liegen könnten.

- `KI in der Hausarbeit verwenden/` — beschreibt den Umgang mit KI im Rahmen der Arbeit. Muss gut bekannt sein, wird aber nicht vor jedem Prompt erneut gelesen.

---

### `output_pymupdf/` — Eine einzige relevante Quelle

Dieser Ordner enthält die mit **PyMuPDF4LLM** verarbeiteten Markdown-Dateien. Da Marker qualitativ besser ist, ist aus diesem Ordner nur eine einzige Datei relevant — die methodische Pflichtquelle, die aufgrund ihrer Größe nicht mit Marker verarbeitet werden konnte:

- `Forschungsmethoden und Evaluation in den Sozial- und Humanwissenschaften. Springer Berlin Heidelberg.md`

Diese Quelle ist die methodische Basis für den gesamten Hauptteil. Jede Aussage zum Untersuchungsdesign muss mit ihr belegt werden. Alle anderen `.md`-Dateien in `output_pymupdf/` werden ignoriert, da ihre Marker-Versionen in `output_marker/` qualitativ überlegen sind.

---

## Nutzungslogik der Dateien nach Phase

**Planungsphase (jetzt) — vollständig lesen:**

- `output_marker/Vorlesungsskript zur Aufgabenleistung/Vorlesungsskript zur Aufgabenleistung..md`

- `output_marker/Notwendiges zu meiner Hausarbeit (Forschungsfrage etc)/Notwendiges zu meiner Hausarbeit (Forschungsfrage etc).md`

- `output_marker/KI in der Hausarbeit verwenden/KI in der Hausarbeit verwenden.md`

**Einleitungsphase — einzeln und nur bei direktem Bedarf:**

- Jeweilige inhaltliche Quellen aus `output_marker/` — immer nur die für den aktuellen Abschnitt relevante Quelle, nie alle auf einmal

**Hauptteilphase — gezielt und nie vollständig auf einmal:**

- `output_pymupdf/Forschungsmethoden und Evaluation in den Sozial- und Humanwissenschaften. Springer Berlin Heidelberg.md` — Struktur inspizieren, per Keyword suchen, maximal 20–30 relevante Seiten laden

- Vor Einstieg in den Hauptteil: `output_marker/Beispiel für ein gutes Expose/Beispiel für ein gutes Expose.md` vollständig lesen

**Permanent bei jedem Prompt:**

- `output_marker/Notwendiges zu meiner Hausarbeit (Forschungsfrage etc)/Notwendiges zu meiner Hausarbeit (Forschungsfrage etc).md`

---

## Zitierregeln für die Forschungsmethoden-Quelle

Halluzinierte Seitenangaben oder falsche Zitate sind unter keinen Umständen akzeptabel. Beim Zitieren muss stets angegeben werden, welche Textstelle entnommen wurde und warum sie an dieser Stelle passt. Seitenangaben müssen exakt so übernommen werden, wie sie im Markdown-Dokument erscheinen. Im Zweifel lieber keine Seitenzahl angeben als eine falsche.

---

## Dokumentationspflicht der KI-Nutzung

Ein zentraler und nicht verhandelbarer Aspekt des gesamten Projekts ist die lückenlose Dokumentation der KI-Nutzung. Wenn wichtige Arbeitsschritte vollzogen werden — insbesondere bei zentralen Prompts oder bedeutsamen Aufgabenstellungen — muss dies präzise und sauber in der Markdown-Datei dokumentiert werden. Wird die Nutzung von KI nicht transparent ausgewiesen, handelt es sich um ein Plagiat. Das ist unter keinen Umständen akzeptabel.

KI: Claude Code Opus 4.6 (Planning mit High Effort)

 ---

## Zusammenfassung der unmittelbaren Aufgabe

Die unmittelbare Aufgabe besteht darin, auf Grundlage aller vorliegenden Informationen eine sehr genaue, professionelle Planung zu erstellen und diese in einer strukturierten Markdown-Datei niederzulegen. Diese Datei bildet das operative Grundgerüst für den gesamten weiteren Schreibprozess. Sie muss so vollständig und präzise sein, dass direkt im Anschluss mit dem Schreiben der Einleitung begonnen werden kann, ohne dass Unklarheiten über Vorgehen, Dateinutzung oder Zitierregeln bestehen.

