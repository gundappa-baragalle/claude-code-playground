---
name: upsc-cdf
description: >
  Generate exam-ready CDF (Concept Descriptor Framework) notes for UPSC preparation,
  enriched with PYQ (Previous Year Question) patterns from 2385+ tagged questions.
  Trigger when user asks to "make UPSC notes", "CDF notes", "RemNote notes", "notes on [topic]",
  "create flashcard notes", or "study notes for [any UPSC topic]".
---

# UPSC CDF Notes Generator — PYQ Enriched

## STEP 0: Read PYQ Data FIRST (Mandatory)

Before writing a single line of notes, read the PYQ data:

**Step 1 — Quick lookup:**
```
Read: upsc-pyq-tagging/concept-index.json
```
Find the user's topic (case-insensitive). Check `total_count`, `last_asked`, `prelims_count`, `mains_count`, `dimensions_tested`.

**Step 2 — Get full topic data:**
```
Read: upsc-pyq-tagging/topic-maps/{topic-slug}.md
```
The slug is lowercase with hyphens (e.g., `buddhism.md`, `indian-economy.md`, `climate-change.md`).

If topic not found exactly, check `related_concepts` in concept-index.json or try a parent topic (e.g., "Bodhisattva" → read `buddhism.md`).

**Step 3 — Use this data to power:**
- Frequency badges in metadata
- Trap alerts (from `trap_factor`)
- Actual PYQ questions in practice section
- Mains answer structure (from `mains.answer_structure`)
- Related concepts (from `related_concepts`)

---

## OUTPUT STRUCTURE (11 Sections — Always in This Order)

### Section 1: Header & Metadata

```
- **[Topic]** :- UPSC [Subject] | [Category]
  - *~source* ;- [NCERTs + standard books with chapter]
  - *~PYQ frequency* ;; [N questions (YYYY–YYYY)] — [HIGH/MEDIUM/LOW] priority
  - *~prelims count* ;; [N questions] | Last asked: [year]
  - *~mains relevance* ;; [GS paper] — [themes]
  - *~dimensions tested* ;- [WHAT: N, WHY: N, VS: N, HOW: N — from topic-map]
  - *~syllabus* ;; [syllabus_id from concept-index]
```

### Section 2: Why Study This?

```
  - **Why Study [Topic]?** :- Motivation & Context
    - *~exam relevance* ;; [Frequency + papers]
    - *~conceptual value* ;- [What this unlocks in other topics]
    - *~current affairs link* ;; [Most recent connection]
    - *📌 beginner note* ;- [Big picture in 2 lines — why this matters]
```

### Section 3: Big Picture (Visual Map — MANDATORY)

```
  - **Big Picture** :- Visual Overview
    - *~structure* ;-
      ```
      TOPIC NAME
      ├── Component 1
      │   ├── Sub-A
      │   └── Sub-B
      ├── Component 2
      └── Component 3

      TIMELINE (for historical topics):
      [Year]───[Year]───[Year]───[Year]
        │         │         │         │
      Event1   Event2   Event3   Event4
      ```
```

### Section 4: Key Terms Glossary

```
  - **Key Terms** :- Glossary
    - **[Term]** :: [Simple definition]
      - *📌 beginner note* ;- [Plain English + analogy for a newcomer]
    - **[Term 2]** :: [Definition]
```

### Section 5: Main Content Body

Hierarchically nested. **Every major concept MUST have:**

```
  - **[Concept]** :: [Definition]
    - *~why it arose* ;; [Root cause / need it addressed]
    - *~significance* ;; [Impact / why it matters]
    - *📌 beginner note* ;- [Simplest explanation + familiar analogy]
    - *🧠 analogy* ;- [Connects to everyday experience]
    - *⚡ vs [Related]* ;- [Key difference — prevents confusion]
    - *⚠️ exam trap* ;- [Common wrong answer + fix — from PYQ trap_factor]
    - *🎯 Prelims focus* ;- [What to memorize, from PYQ factual_hooks]
    - *📝 Mains angle* ;- [Essay angle, from PYQ mains.themes]
    - *🔗 connects to* ;; [[Related Concept]] — [relationship]
```

**DO NOT flatten everything at one level. Indent sub-parts under their parent.**

### Section 6: Flashcard Tables

For groups of comparable items (councils, articles, amendments, bodies, etc.):

```
  - **[Group Name]** :- Flashcard Table
    | Name | [Property 1] | [Property 2] | [Property 3] |
    |------|-------------|-------------|-------------|
    | **Item 1** | value | value | value |
    | **Item 2** | value | value | value |
```

Rules:
- First column = Name (bold)
- Cells < 5 words
- Most testable properties in early columns
- Put ⚠️ notes AFTER the table, not inside cells

### Section 7: One-Liners (Rapid Recall)

```
  - **One-Liners** :- Rapid Recall
    - [Fact 1] = [Value]
    - [Name] → [Key association]
    - [Date] = [Event]
    - [Term] ≠ [Common confusion]
```

Rules: Fragments only, no full sentences. Cover all frequently confused items.

### Section 8: Quick Revision (Cloze Cards)

```
  - **Quick Revision** :- Cloze Cards
    - {{Answer::hint}} was [context with {{another answer::hint}}].
    - {{Term::category, NOT other-term}} means [usage in sentence].
```

**Always use `{{answer::hint}}` format — never bare `{{answer}}` for confusable items.**

### Section 9: Practice MCQs (From Actual PYQs First)

```
  - **Practice MCQs** :- Self-Test
    - [Question from topic-map, or newly created]? >>A)
      - [Correct answer — MUST be first]
      - [Wrong option 1]
      - [Wrong option 2]
      - [Wrong option 3]
```

**Use actual PYQ questions from the topic-map when available. Cite year.**
Variety: factual → "which NOT" → statement-based → match-the-following.

### Section 10: RAPID REVISION (Pre-Exam One-Pager)

```
  - **🚀 RAPID REVISION** :- Last-Minute Review
    - *~read time* ;- 5 minutes

    - **📋 FACTS TO MEMORIZE** :- Core Data
      | Item | Value | Memory Hook |
      |------|-------|-------------|
      | [fact] | [value] | [hook] |

    - **⚡ QUICK COMPARISONS** :- Key Differences
      - [X] vs [Y]: [distinguisher] → [X has this, Y has that]

    - **⚠️ TRAP ALERTS** :- Don't Confuse
      - [Wrong belief] ≠ [Correct fact] — use PYQ trap_factor

    - **🔢 NUMBERS TO REMEMBER** :- Key Figures
      - [N] = [what it counts]

    - **📝 MAINS KEYWORDS** :- For Essay Writing
      - [Topic]: "[keyword 1]", "[keyword 2]", "[keyword 3]"

    - **🎯 PYQ PATTERN** :- What UPSC Actually Asks
      - [Pattern 1] (from topic-map dimensions_tested)
      - [Pattern 2]
```

### Section 11: Connections & Mains Framework

```
  - **Connections** :- Knowledge Web
    - *~builds on* ;; [[Previous Topic]] — [relationship]
    - *~leads to* ;; [[Next Topic]] — [relationship]
    - *~compare with* ;; [[Contrasting Topic]]
    - *~current affairs link* ;; [News item/policy/event]

  - **Mains Answer Framework** :- Essay Structure
    - *~introduction angle* ;- [Opening line approach]
    - *~body points* ;-
      >>>
      1. [Main argument/aspect]
      2. [Second aspect]
      3. [Third aspect]
      4. [Contemporary relevance]
    - *~conclusion angle* ;- [How to close the answer]
    - *~relevant PYQ* ;- [Actual mains question from topic-map if available]
```

---

## CDF Syntax Quick Reference

| Type | Delimiter | Flashcard? | Use For |
|------|-----------|-----------|---------|
| Definition | `::` | Both directions | Main concepts |
| Container | `:-` | None | Category headers |
| Backward def | `:<` | Def→term | "What is this called?" |
| Fact (testable) | `;;` | Yes | Dates, names, places |
| Context (no card) | `;-` | None | Explanations, analogies |
| Backward fact | `;<` | Value→property | Abbreviations |
| Cloze | `{{answer::hint}}` | Yes | Sentences with gaps |
| MCQ | `>>A)` | Yes | Multiple choice |
| Link | `[[Term]]` | No | Cross-references |

**⚠️ NEVER use Markdown `##` headers inside note content — they break RemNote hierarchy. Use only `- **Name** :-` for sections.**

---

## Quality Standards Checklist

Before finalizing, verify:

- [ ] Every unfamiliar term defined with `📌 beginner note`
- [ ] Every concept has WHY (not just WHAT)
- [ ] At least one `🧠 analogy` per major concept
- [ ] Every confusable item has `⚠️ exam trap`
- [ ] Big Picture ASCII diagram present
- [ ] Flashcard table for any group of 3+ comparable items
- [ ] PYQ traps from `trap_factor` field incorporated
- [ ] Actual PYQ questions used in Practice MCQs
- [ ] `{{answer::hint}}` format used (not bare `{{}}`)
- [ ] RAPID REVISION section is ≤ 1 page scannable

---

## Integration with Remaining Questions

As more batch results are enriched and merged:

```bash
# 1. Add result files to batches/
# 2. Merge:
python3 enrich_pipeline.py --merge-all

# 3. Rebuild indexes:
python3 upsc-pyq-tagging/generate_indexes.py

# 4. Skills auto-pick up updated concept-index.json and topic-maps/
# No changes to this skill file needed.
```

Current coverage: **2,385 questions enriched** (batches 001–030 + manual 0–134).
Remaining: **2,659 questions** (batches 031–066) — will expand concept-index as added.
