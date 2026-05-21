# AI-Driven Customer Acquisition in E-Commerce: Opportunities & Risks 📄

> *A structured academic workflow — how a 1.0-graded seminar paper was built with AI, not just written by it.*

**Final grade: 1.0** &nbsp;·&nbsp; HfWU Nürtingen-Geislingen &nbsp;·&nbsp; WS 2025/26

---

## The Paper

**Research question:** *What opportunities and risks does the use of AI in e-commerce offer for customer acquisition?*

A 12,000-word academic seminar paper analyzing AI-driven customer acquisition along the conversion funnel — from awareness and targeting through personalization, conversion optimization, and governance trade-offs. Based on 15 peer-reviewed sources from Web of Science and Google Scholar.

**Core topics covered:**
- AI marketing (AIM) and its measurable impact on customer acquisition metrics (CAC, conversion rate, CLV, ROMI)
- Funnel-based targeting and personalization mechanics — how AI maps to each acquisition stage
- Clickstream-based conversion prediction using graph-theoretic and ML approaches
- Generative AI as a pre-funnel acquisition lever (text-to-image, content automation)
- Data strategy, governance, and ethical constraints: transparency, fairness, privacy, and bias as systemic trade-offs

The paper directly maps to the problem space dema.ai operates in: AI-powered ecommerce analytics, marketing mix modeling, and data-driven customer acquisition for online retailers.

---

## The Workflow

This isn't a paper written by AI. It's a paper produced through a deliberately architected multi-stage AI workflow — where the author controlled the evidence, the structure, and the quality gates, and the AI handled formulation.

### Phase 1 — Manual Literature Research
All sources were identified and selected by the author via **Web of Science** and **Google Scholar** only. The AI was explicitly prohibited from performing its own research or sourcing any material from the internet at any point in the process.

### Phase 2 — Source Analysis & Citation Pool Construction
Relevant passages were extracted verbatim from each source by the author, annotated with page numbers, and compiled into a structured analysis file. This file — not the AI's training data — became the sole evidence base for the entire paper.

### Phase 3 — Structure Prompt (ChatGPT07)
Before a single word of the paper was written, a dedicated prompt was used to generate the outline. The prompt instructed the model to read the source analysis file, cluster all sources by theme, and derive a chapter structure following a strict funnel logic (broad review → conceptual frameworks → empirical evidence → synthesis). Every section had to be traceable to specific sources — no filler headings.

### Phase 4 — Chapter Prompts (ChatGPT01–06)
Each of the six chapters was generated through its own standalone prompt. These were not simple "write me a chapter" instructions. Each prompt specified:

- **Hard word count targets** (e.g. 600 ± 30 words) enforced to the paragraph level
- **Exact source constraints** — only the pre-defined citation pool was permitted; any use of external material was a violation
- **Verbatim citation injection** — the author's extracted source passages were embedded directly into the prompt as the evidence input; the AI reformulated them as German indirect citations
- **Placement plans** — each citation had an assigned position in the argument chain; the AI was told which sentence to place it at and what argumentative function it had to fulfill
- **Structural enforcement** — exact number of sections, paragraphs, and transitions specified per prompt
- **Temperature settings** (0.1–0.2) — low creativity, high factual fidelity
- **Silent preflight checks** — each prompt included an internal self-verification checklist (word count, structure, citation completeness, absence of fabrication) that the model had to pass before producing output

### Phase 5 — QA Audit Prompt (ChatGPT08)
After all chapters were complete, a dedicated audit prompt performed a systematic review of the full paper against three reference documents: the planned outline, the citation placement plan, and the constraint specifications from each chapter prompt. The audit produced a structured diagnostic report with a scoring matrix across eight criteria and a prioritized list of revisions. Identified issues were corrected before final submission.

---

## What This Demonstrates

The AI was never given a blank canvas. At every step:

- The **intellectual work** — identifying sources, extracting evidence, defining the argument structure, setting quality constraints, evaluating output — was done by the author.
- The **formulation work** — turning structured inputs into coherent academic prose — was delegated to the model under strict, verifiable constraints.
- The **verification loop** was built into the system: a final audit prompt compared the output against every spec before submission.

This is the same design principle behind reliable AI agent workflows: define the task precisely, constrain the input space, enforce output structure, and close the loop with a verification step. The difference here is that the output wasn't code — it was academic prose that had to meet citation standards and pass faculty review.

**It did. Grade: 1.0.**

---

## Repository Contents

```
README.md                    ← this file
paper/
  AI-Driven_Customer_Acquisition_in_E-Commerce.pdf   ← full paper incl. all prompts
```

The PDF includes the complete paper and, starting from page 17, the full prompt documentation: a table describing the intent and constraints of each prompt (ChatGPT01–08), followed by the complete prompt text for every chapter.

---

## Why This Is Relevant to dema.ai

dema.ai builds AI systems that help ecommerce companies make better decisions about marketing spend, customer acquisition, and profitability. This paper analyzes the research literature on exactly those mechanisms — how AI targeting, personalization, and funnel analytics affect acquisition costs and conversion outcomes, and what governance and data quality requirements constrain their real-world effectiveness.

The content is relevant. The workflow is the point.
