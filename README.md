# 📚 Agentic Academic Workflows & Research Portfolio

A showcase of **sophisticated, constraint-driven AI Agent workflows** designed to produce high-fidelity academic research and automate complex document engineering.

Rather than just containing academic papers, this repository demonstrates how to architect **deterministic, rule-governed pipelines** for LLM agents (like Claude and Antigravity) to manage literature analysis, write academic drafts under strict constraints, and perform low-level OOXML document automation.

---

## 🧠 Core Architecture: The `CLAUDE.md` Brain

At the heart of the primary showcase (`AI in startup`) is [**`CLAUDE.md`**](AI%20in%20startup/CLAUDE.md) — the operational brain and context boundary of the AI Agent. 

### Why `CLAUDE.md` is the Central Engine:
*   **System Prompt Extension**: It serves as a local, persistent system prompt extension that any LLM agent automatically reads upon entering the directory.
*   **Strict Boundary Constraints**: Enforces absolute negative constraints (e.g., prohibition of empirical data fabrication, restricted citation pools, preventing use of unverified internet text).
*   **Source Fidelity Enforcement**: Defines precise rules for mapping arguments exclusively to raw markdown sources in `output_marker/` and `output_pymupdf/`.
*   **Workflow Orchestration**: Directs the agent step-by-step through structural formulation, citation checks, and quality gates.

---

## 🚀 Showcased Workflows

### 1. 🧠 [AI in Startup: Agentic Orchestration & OOXML Automation](AI%20in%20startup/)
An end-to-end framework for writing a 10-page research exposé (Methodische Grundlagen III) following strict methodological guidelines (Döring).

*   **Architecture & Workflow Highlights**:
    *   **Context Control via [CLAUDE.md](AI%20in%20startup/CLAUDE.md)**: Standardized rules preventing hallucinations, enforcing formatting, and controlling the agent's logical flow.
    *   **Copyright-Compliant Knowledge Skeletons**: To share the workflow publicly without distributing copyrighted papers, full-texts were moved to `literature_originals/` (git-ignored) and replaced with structured, standardized markdown metadata skeleton files in `output_marker/` and `output_pymupdf/`.
    *   **OOXML Python Automation**: Custom Python scripts (`build_expose.py`, etc.) that perform direct ZIP/XML manipulations on `.docx` structures. This automates the dynamic building of Tables of Contents, inserts text programmatically, and patches Word XML to enforce complex dual page-numbering (Roman numerals for headers, Arabic for content).
    *   **Chain-of-Thought Prompts**: Complete multi-step prompt pipelines (`prompts/`) designed to guide the model through individual chapter generation.
*   **Explore Pipeline**: 👉 [**Go to AI in Startup Workspace**](AI%20in%20startup/)

### 2. 🛍️ [AI-Driven E-Commerce Customer Acquisition](AI%20in%20E-Commerce/)
A case study of a 1.0-graded seminar paper (Methodische Grundlagen II) built via a closed-loop prompt chaining pipeline.

*   **Architecture & Workflow Highlights**:
    *   **Funnel-Based Constraint Prompts**: A structured 8-step prompting pipeline enforcing hard word counts, precise source positioning, and verbatim citation injection.
    *   **Closed-Loop QA Auditing**: Demonstrates a self-diagnostic audit prompt comparing the generated draft against target outlines and constraints, scoring compliance, and outputting an error report before final compilation.
*   **Explore Pipeline**: 👉 [**Go to AI in E-Commerce Workspace**](AI%20in%20E-Commerce/)

---

## 🛠️ Repository Layout & Data Flow

The repository structure reflects a separation of concerns between code automation, prompt sequences, source abstractions, and output formats:

```text
Seminar-Papers/ (Root Portfolio)
├── .gitignore          # Repository-wide git-ignore and tracking exceptions
├── README.md           # This architecture & portfolio showcase
├── AI in startup/      # Project 1: AI Agent Writing & OOXML Automation
│   ├── CLAUDE.md       # Operational AI Control Document (The Brain 🧠)
│   ├── paper/          # Generated final documents & Exposé outputs
│   ├── output_marker/  # Public metadata skeletons representing 10 research papers
│   ├── output_pymupdf/ # Public metadata skeleton representing the core Döring methodology textbook
│   ├── prompts/        # Context-bounded prompt templates for chapter generation
│   ├── scripts/        # Python scripts manipulating docx OOXML / XML tree structures
│   └── README.md       # Technical execution instructions for the scripts
└── AI in E-Commerce/   # Project 2: Funnel Prompt Chaining Case Study
    ├── paper/          # Final 1.0-graded seminar paper (PDF)
    └── README.md       # Documentation of the 8-step ChatGPT prompt chaining workflow
```

---

## 👨‍💻 Author & Concept
*   **Author**: Mattis Engelhardt
*   **Institution**: Hochschule für Wirtschaft und Umwelt Nürtingen-Geislingen (HfWU)
