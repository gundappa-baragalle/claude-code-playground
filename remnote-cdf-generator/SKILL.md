---
name: remnote-cdf-generator
description: >
  Use this skill any time the user wants to study, revise, or make notes on
  any topic — especially for UPSC, UPPSC, State PSC, SSC, or any competitive
  exam. Triggers include: "make notes on X", "create a study file", "RemNote
  file on X", "notes for spaced repetition", "revise X for UPSC", "I need to
  study X", "help me prepare X", "notes for tomorrow's exam", "generate
  flashcards on X", "CDF notes", "I want to revise X quickly before my exam",
  "summarise X for competitive exam", "I'm weak in X, help me cover it". Covers
  all UPSC subjects: Ancient/Medieval/Modern India, Art & Culture, Geography,
  Polity, Economy, Science & Tech, Environment, Ethics GS4, Essay. Output is a
  RemNote-importable .md file with PYQ-driven content, two-way flashcards,
  cloze deletions, dependency-ordered learning ladder, and exam-trap awareness.
  When in doubt about whether to trigger — trigger. A student mentioning any
  exam, revision, or study need almost certainly wants this skill.
---

# RemNote CDF Notes Generator

---

> ⚠️ **INTERRUPTION NOTICE — Read before any long generation**
>
> CDF notes run 80–150 nodes (standard) or 200+ (flagship). If generation is
> cut off at any point:
> 1. Save completed content to `/mnt/user-data/outputs/[subject]-[topic]-cdf-PARTIAL.md`
> 2. Mark the cut point: `*~GENERATION INTERRUPTED* ;- stopped after Section [N] — request continuation to complete`
> 3. Deliver via `present_files` immediately — do not discard partial work.
> 4. Tell the user which sections are done and which remain.
>
> **Flagship output order** (>150 nodes): generate **1 → 2 → 3 → 4 → 5 → 12**
> first, then **6 → 7 → 8 → 9 → 10 → 11**. If cut off, the learning ladder
> and full PYQ Archive survive.
>
> Never use HTML comments (`<!-- ... -->`) as markers — they render as visible
> plain text in RemNote. Always use `;-` descriptors.

---

## Execution Checklist — Follow This Order Every Time

Complete these steps in sequence. Skipping a step silently is not permitted —
each exists because a specific, recurring failure mode was traced back to it.

---

**[ ] Step 1 — Scope Check**

Use the decision tree below. Do this before PYQ lookup so you do not run a
UPSC workflow on a JEE or CAT request.

```
Is the exam clearly non-UPSC (JEE, NEET, CAT, CA, MBA, school)?
  YES → Ask: "Should I generate UPSC-style CDF notes, or a different format?"
        Proceed CDF only after confirmation.
        For confirmed non-UPSC: use 12-section structure, replace PYQ Archive
        and revision priority with exam equivalents; skip Steps 2 and 3.

Is the topic clearly UPSC but maps to 3+ substantially different subjects?
  (e.g., "capital" → Economy / Polity / Geography)
  YES → Ask which subject angle the user wants.

Is the request too broad to scope? (e.g., "Make notes on India", "Notes on GS2")
  YES → Ask to narrow down to a specific topic.

Everything else (including partial ambiguity)?
  → State your assumption in Section 1 metadata and proceed immediately.
  → Default: Prelims + Mains, prior knowledge = complete beginner.
```

---

**[ ] Step 2 — PYQ Lookup (two sub-steps, both required)**

**2a — Find the slug:**
Open and search `pyq-data/concept-index.json` for the topic slug.

**2b — Read the topic-map file:**
Open and read `pyq-data/topic-maps/TOPIC-SLUG.md`. Finding the slug is not
sufficient — you must open the actual file.

Extract: `total_count`, `prelims_count`, `year_range`, `last_asked`,
`dimensions_tested`, `revision_priority`, and every verbatim PYQ question.

> **Why verbatim matters:** The most common fabrication pattern is: slug found
> in index → file never opened → questions reconstructed from memory →
> fabricated PYQs in Section 12. UPSC reuses exact phrasing; paraphrased
> questions do not train the right recall. This is explicitly prohibited.

**Self-audit before writing Section 12:** "Did I open the topic-map file and
copy questions from it, or reconstruct them from memory?" If the latter —
stop, open the file, then regenerate Section 12.

**If topic slug not found:** Try the parent subject slug (e.g., "inflation" →
"money-and-banking"), then a synonym. If truly absent:
- Set PYQ frequency: `Not yet indexed — estimate based on syllabus weight`
- Set revision priority: MEDIUM
- Set Section 12: `*~Prelims PYQs* ;- Not yet indexed — check topic-map after next UPSC cycle`
- Proceed immediately. A missing slug does not block any other section.

---

**[ ] Step 3 — Read Subject Guidelines**

Open `references/subject-guidelines.md`. Jump to the user's subject section
using the table of contents at the top of that file. Apply those requirements
on top of everything below. Do not rely on memory — open the file.

---

**[ ] Step 4 — Read Section Templates**

Open `references/section-templates.md`. All 12 section structures, descriptors,
and formatting rules live there. Templates recalled from previous sessions may
be incomplete — always read fresh.

---

**[ ] Step 5 — Read a Worked Example**

Open `references/examples.md`. Use the table of contents to jump directly to
the example for the closest subject. Read one fully worked example before
writing any output.

Why this step matters: seeing what "complete" looks like before you begin is
the single most reliable guard against shallow output. Memory of a past example
is not equivalent to reading the current file — it may have been updated.

---

**[ ] Step 6 — Build the Dependency Map**

This is the most important planning step. Build it as a visible scratchpad —
"mentally" is not sufficient, because the map must be output as a descriptor
in the final file (see below).

Ask three questions:
1. What does the student already know from everyday life that connects to this
   topic? (This is your starting point.)
2. What chain of concepts connects that everyday knowledge to the main topic?
   (These become Section 4 entries, in order.)
3. Within the main topic, what is the logical sequence? Which concept must be
   understood before which? (This determines Section 5 order.)

Write the chain explicitly:
```
Everyday knowledge → Prerequisite A → Prerequisite B → Core Concept → Sub-concept 1 → Sub-concept 2
```

**Examples by subject:**

*Economy (Inflation):*
```
"Prices went up at the market" → Output/Goods & Services → Aggregate Demand + Supply → Price Level → Inflation → Types, WPI, CPI, RBI tools
```

*Polity (Fundamental Rights):*
```
"Government makes rules that affect me" → What is the State (Art 12) → Why rights need protection → FR (Part III) → Individual articles → Exceptions & writs
```

*History (Mughal Empire):*
```
"Kingdoms fight for territory" → Pre-Mughal landscape → Babur's entry → Establishment → Administration → Art/Culture → Decline causes
```

If you cannot trace this chain, read the reference files and topic-map first.

**Output the chain** as a disabled descriptor at the top of Section 4,
immediately before the first prerequisite entry:
```
  - *~dependency chain* ;- [everyday knowledge] → [A] → [B] → [C] → [main topic] → [sub-concepts]
```

**This map determines the order of Sections 4 and 5. Stick to it.**

---

**[ ] Step 7 — Generate All 12 Sections**

Use templates from `references/section-templates.md`. Completeness beats brevity.

**Coverage floors** (a node = any indented bullet with a delimiter or descriptor):
- Narrow topics (single amendment, one person): ≥ 40 nodes
- Standard topics: ≥ 80 nodes
- Flagship topics (Fundamental Rights, Indian Economy): ≥ 200 nodes

No upper cap — never truncate to hit a length target. Do not stop until every
major concept, every PYQ dimension, and every exam trap has been addressed.

**Section 3 Big Picture — the most common failure in this skill:**

The `*~structure* ;-` descriptor MUST be a proper multi-line ASCII tree. Tree
content starts on the LINE AFTER `;-`, each branch on its own line.

```
NEVER:   *~structure* ;- TOPIC | +-- A | +-- B | +-- C
         (collapses into one garbled unreadable line in RemNote)

ALWAYS:
    - *~structure* ;-
      TOPIC
      +-- A
      +-- B
      +-- C
```

Full worked example → `references/section-templates.md` § Section 3.

**Section index** (orientation only — full templates in section-templates.md):

| # | Name | Purpose |
|---|------|---------|
| 1 | Header & Metadata | Topic, PYQ frequency, revision priority |
| 2 | Why Study + Before You Read | Motivation, prior-knowledge activation |
| 3 | Big Picture | Multi-line ASCII structure / timeline map |
| 4 | Prerequisite Concepts & Key Terms | Foundation layer in dependency order |
| 5 | Content (Main Body) | Learning ladder in dependency order |
| 6 | Flashcard Tables | Structured comparison tables |
| 7 | One-Liners | Rapid recall fragments (all with `;;`) |
| 8 | Quick Revision | Cloze flashcard sentences |
| 9 | Practice MCQs | 5–8 synthetic self-test questions |
| 10 | Rapid Revision | 1-page last-minute review |
| 11 | Feynman Test + Connections + Mains Framework | Comprehension + cross-paper links |
| 12 | PYQ Archive | All verbatim past year questions — Prelims + Mains |

---

**[ ] Step 8 — Beginner Walk-Through**

Read your own output as if you are a complete beginner opening this file for
the first time. At every concept, check:

- Does this term appear before it was defined? → Add definition earlier.
- Does this explanation depend on something not yet explained? → Reorder or add
  a prerequisite.
- Could a student with only everyday Hindi-medium vocabulary understand this? →
  If no, simplify.
- Is there a formula that replaces three sentences of explanation? → Add it.
- Can you trace the logical chain from the first concept to this one without
  any gaps? → If no, fill the gap.

"Everyone knows what that means" is never a reason to skip a definition. Every
technical term (aggregate demand, fiscal deficit, MSP, velocity of money) must
be defined.

**Add this audit descriptor as the last child of the Section 1 metadata block:**
```
  - *~beginner-audit* ;- [PASSED — no undefined terms found]
                     OR [GAPS FOUND: list each gap and where it was fixed]
```

---

**[ ] Step 9 — Run Quality Checklist + Syntax Verifications**

Open `references/quality-checklist.md`. Verify all universal checks, then
subject-specific checks. Open the file — do not run from memory.

**Top 3 failure modes — check these before opening the checklist:**
1. **Section 12 PYQ count mismatch** — count MCQ nodes in output vs
   `prelims_count` in the topic-map file (re-open the file; do not use memory).
   Any mismatch = fabricated or missing questions.
2. **Section 7 one-liners missing `;;`** — plain `[Fact] = [value]` or
   `→ Back of card` produces no flashcard; these are silent failures.
3. **`##` markdown headers anywhere** — every instance breaks RemNote hierarchy.

**Table flashcard setup — verify every table in Sections 6 and 10:**

Every Markdown table needs a `*~RemNote setup* ;-` descriptor as a sibling of
the table rows (same indentation level, both direct children of the parent Rem).

```
CORRECT — setup and table rows at same indent:
  - **WPI vs CPI** :- Flashcard Table
    - *~RemNote setup* ;- WPI: Both directions | CPI: Both directions | Notes: Skip
    | Feature | WPI | CPI | Notes |
    |---------|-----|-----|-------|

WRONG — table rows indented one level under setup:
  - **WPI vs CPI** :- Flashcard Table
    - *~RemNote setup* ;- ...
      | Feature | WPI | CPI |   ← extra indent concatenates into garbled output
```

Never use `<!-- RemNote Setup: -->` HTML comments — they render as visible text.

**PYQ anchor structure — verify every MCQ:**
- `**PYQ:[YEAR]-[slug]** :-` is the outer parent; `>>A)` MCQ is its child — never reversed.
- `✅ Explanation #[[Extra Card Detail]]` is a sibling of answer options (direct
  child of `>>A)`), never nested under a single answer option.
- All MCQs use `>>A)` — never `;;>A)`.
- Inline PYQ mentions in Sections 4/5 use `[[PYQ:YEAR-slug]]` linking.
- Section 12 order: newest-first (2024 → 2023 → oldest).

---

**[ ] Step 10 — Final Syntax Scan**

Scan the entire output for these errors before saving:

| Pattern found | Fix |
|---|---|
| `;;>A)` anywhere | Replace with `>>A)` |
| `{{answer::hint}}` cloze | Replace with `{{answer}}{({hint})}` |
| `## ` markdown headers | Replace with `:-` container node |
| ECD nested under single answer option | Move to sibling level under `>>A)` |
| Correct answer NOT first child of `>>A)` | Reorder — correct answer must be first |
| `<!-- RemNote Setup: -->` before tables | Replace with `*~RemNote setup* ;-` |
| `→ Back of card` in Section 7 | Replace whole line with `[label] ;; [value]` |
| Bare bullets in Section 7 (no delimiter) | Add `;;` delimiter |
| `*~structure* ;- TOPIC \| +-- A ...` inline | Rewrite as multi-line inside triple-backtick fence |
| Table rows indented under setup descriptor | Dedent to sibling level |

---

**[ ] Step 11 — Save and Deliver**

Save output to `/mnt/user-data/outputs/[subject]-[topic]-cdf.md`

**File naming** (lowercase, hyphens, drop prepositions/articles/conjunctions):
```
polity-fundamental-rights-cdf.md
economy-water-food-security-cdf.md    ← "Water and Food Security" drops "and"
ancient-india-buddhism-cdf.md
geography-indian-monsoon-cdf.md
gs4-ethics-integrity-cdf.md
essay-democracy-india-cdf.md
```

Use `present_files` so the user can download and import directly into RemNote.
Do not paste notes inline — files are too long to read in chat.

---

## Core Philosophy — The Seven Principles

> These notes are a **learning ladder**, not a reference manual — built from
> zero, carrying a beginner to the point where they can solve every PYQ without
> any other source.
>
> 1. **Build from zero** — no assumed knowledge; define every technical term
> 2. **Logical flow** — prerequisites before concepts, causes before effects
> 3. **Clarity over coverage** — depth beats breadth; every concept passes the Feynman test
> 4. **Mathematics as a clarity tool** — formulas, arrow notation, ASCII graphs when they clarify
> 5. **Every fact has a "why"** — understanding before memorization
> 6. **Exam-intelligence woven in** — traps explained as cognitive patterns, not lists
> 7. **No isolation** — every concept connects to other papers and current affairs
>
> Full rationale → `references/core-philosophy.md`

---

## RemNote Structure — The Golden Rule

If Concept B is part of Concept A, B must be indented under A. Never use `##`
markdown headers — they break RemNote's hierarchy. Use `:-` container nodes.

```
CORRECT:
- **Topic** :- Container
  - **Concept A** :: Definition
    - *~property* ;; value
    - **Sub-concept** :: Definition
  - **Concept B** :: Definition

WRONG:
## Topic Header        ← Breaks RemNote!
- **Concept A** :: ...
## Another Section     ← Creates orphan nodes!
```

Full CDF syntax reference (all delimiters, flashcard types, cloze syntax,
descriptor naming conventions) → `references/syntax-guide.md`

---

## Reference Files

| File | Read at Step |
|------|-------------|
| `pyq-data/concept-index.json` | Step 2a — find topic slug |
| `pyq-data/topic-maps/TOPIC-SLUG.md` | Step 2b — verbatim questions |
| `references/subject-guidelines.md` | Step 3 — your subject section |
| `references/section-templates.md` | Step 4 — always, full templates |
| `references/examples.md` | Step 5 — one worked example |
| `references/quality-checklist.md` | Step 9 — full checklist |
| `references/syntax-guide.md` | Steps 9–10 — syntax edge cases |
| `references/core-philosophy.md` | When you need rationale for a principle (links to cognitive-science.md at its end) |
| `pyq-data/elimination-patterns.md` | When user asks about Prelims strategy |

---

## Changelog

| Date | Change |
|------|--------|
| 2026-04-08 | Section 3 (Big Picture) upgraded: box-drawing characters (├──, └──, │) now preferred over +-- style; geometric/relational ASCII diagrams (triangles, trilemmas) added as a visual type; visual type guide added; FR example in both section-templates.md and examples.md updated to full rich ├──/└── style with Golden Triangle diagram. |
| 2026-04-08 | Section 3 (Big Picture) template updated: ASCII tree now wrapped in triple-backtick code fences inside the `*~structure* ;-` descriptor. Old "no code fences" Rule 3 and inline-pipe failure-mode warning removed. examples.md Big Picture updated to match. SKILL.md syntax scan row updated accordingly. |
| 2026-04-08 | Phase 3 & 4: subject-guidelines.md — 11-section ToC with accurate line numbers added (models can now `view` target line range directly). cognitive-science.md removed from SKILL.md reference table and Core Philosophy pointer — it is a rationale-only file with no generation-time trigger; pointer folded into core-philosophy.md closing line so it remains discoverable. 4a/4b/4c confirmed already resolved in Phase 1. |
| 2026-04-08 | Phase 2: examples.md — stripped 17-principle table, memory hook quick-reference, and mathematical/flow descriptors (all already canonical in cognitive-science.md and syntax-guide.md); duplicate heading/dep-map removed; 3-line ToC added at top; stale verification rows updated; cognitive-science.md header fixed from "13 Principles" to "17 Principles". |
| 2026-04-08 | Phase 1 restructure: 11-step clean checklist (was 0/1/1.5/2/3/3.5/3.6/4/4.5/5/5.5/5.6/6/7), scope-check moved before PYQ lookup, interruption notice moved to top-of-file, CDF syntax reference moved to syntax-guide.md (pointer added), philosophy compressed to 7 one-liners, redundant reference table removed, file-naming consolidated into Step 11, node definition added to coverage floors, dependency map output made mandatory (removed "mentally" option), decision tree added for scope ambiguity. |
