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
Is the topic CSAT / UPSC Paper-II (Quantitative Aptitude, Logical Reasoning, Analytical Ability)?
  Signal phrases: "time and distance", "blood relations", "seating arrangement", "coding decoding",
  "syllogisms", "data interpretation", "profit and loss", "number series", "permutation combination",
  "CSAT", "Paper II", "Paper-II", "aptitude test", "logical reasoning", "verbal reasoning"
  YES → Respond: "This skill covers UPSC GS Paper-I (Prelims GS) and Mains (GS1–GS4 + Essay) only.
                  CSAT / Paper-II topics have no indexed topic-maps or PYQ archive here — proceeding
                  would generate a note with fabricated frequency data.
                  I can generate a general study note for this topic without any PYQ metadata if you'd
                  like, or redirect you to a CSAT-focused resource."
        Do NOT proceed with the CDF workflow — no topic-maps or PYQ data exist for CSAT topics.

Is the exam clearly non-UPSC (JEE, NEET, CAT, CA, MBA, school)?
  YES → Ask: "Should I generate UPSC-style CDF notes, or a different format?"
        Proceed CDF only after confirmation.
        For confirmed non-UPSC: use 12-section structure with these substitutions:
          Section 1 metadata: replace `*~PYQ frequency*` with `*~question frequency* ;- [topic frequency in this exam]`
                              replace `*~revision priority*` with exam's own tier/weight label
          Section 12 (PYQ Archive): retitle as `**📚 Past Questions Archive**` and populate with
                              official past paper questions for that exam (JEE PYQs, NEET PYQs, etc.)
                              Use the same anchor + MCQ structure; verbatim only.
          Steps 2 and 3: skip entirely (no UPSC topic-maps or subject-guidelines apply).
          All other sections (2–11): keep as-is — the learning-ladder logic is exam-agnostic.

Does the request signal time pressure or a lightweight need?
  Signal phrases: "exam tomorrow", "quick revision", "before my exam", "just key points",
  "rapid review", "brush up", "short notes", "only the important points", "revise quickly",
  "in 10 minutes", "last-minute", "cram sheet"
  YES → QUICK REVISION MODE:
        Sections to generate: 1 (metadata only), 3 (Big Picture), 7 (One-Liners),
                               8 (Quick Revision), 12 (PYQ Archive)
        Skip: Sections 2, 4, 5, 6, 9, 10, 11
        Node floor: ≥ 30 nodes total
        Add to Section 1 metadata: *~mode* ;- QUICK REVISION — 5 sections only;
                                    run full CDF later for complete learning ladder
        Still run Steps 2 and 3 (PYQ lookup and subject guidelines) — no data shortcuts.
        File name: [subject]-[topic]-cdf-QUICK.md

Is the topic clearly UPSC but maps to 3+ substantially different subjects?
  (e.g., "capital" → Economy / Polity / Geography)
  YES → Ask which subject angle the user wants.

Is the request too broad to scope? (e.g., "Make notes on India", "Notes on GS2")
  YES → Ask to narrow down to a specific topic.

Has the user given NO specific topic — asking "what should I study?", "suggest a
topic", "where do I start?", "what's most important?", "I have [N] weeks/days left"?
  YES → Open `pyq-data/priority-list.md`. Identify the user's subject (or list
        across subjects if unspecified). Present the top Tier 1 topics for that
        subject with their PYQ count and last-asked year, and ask the user to pick
        one. Do NOT generate notes until a specific topic is chosen.
        Example prompt: "Here are your highest-ROI topics by PYQ frequency —
        which one should I build full notes for?"

Everything else (including partial ambiguity)?
  → State your assumption in Section 1 metadata and proceed immediately.
  → Default: Prelims + Mains, prior knowledge = complete beginner.
```

---

**[ ] Step 2 — PYQ Lookup (two sub-steps, both required)**

**2a — Find the slug:**
Open and search `pyq-data/concept-index.json` for the matching entry. The JSON keys are display names (e.g., `"Fundamental Rights"`, `"Indian Economy"`). To derive the topic-map file path from a key:
1. Lowercase the key
2. Replace spaces and `&` with hyphens
3. Remove all other special characters (commas, apostrophes, brackets, slashes)
4. Collapse any consecutive hyphens into one

Example: `"Time Speed Distance"` → `time-speed-distance` → file is `topic-maps/time-speed-distance.md`

If no entry matches exactly, try the parent topic key or a synonym key.

**2b — Read the topic-map file:**
Open and read `pyq-data/topic-maps/TOPIC-SLUG.md`. Finding the slug is not
sufficient — you must open the actual file.

Extract:
- `total_count`, `prelims_count`, `year_range`, `last_asked`, `dimensions_tested`, `revision_priority`, and every verbatim PYQ question.
- **`## Exam Patterns & Insights`** — copy the "Most tested dimension" line and "Common Trap Patterns" subsection verbatim. This feeds the `🎯 LAST YEARS PYQ PATTERN` block in Section 10.
- **`### Contemporary Relevance`** — copy the text verbatim. This feeds `*~contemporary_relevance*` in Section 11.

Do not reconstruct these from memory — they are factual records of examiner behaviour.

> **Why verbatim matters:** The most common fabrication pattern is: slug found
> in index → file never opened → questions reconstructed from memory →
> fabricated PYQs in Section 12. UPSC reuses exact phrasing; paraphrased
> questions do not train the right recall. This is explicitly prohibited.

**Self-audit before writing Section 12:** "Did I open the topic-map file and
copy questions from it, or reconstruct them from memory?" If the latter —
stop, open the file, then regenerate Section 12.

**2c — Extract high-frequency traps:**
While reading the topic-map, scan every `⚠️ **Trap:**` entry across ALL
priority sections (HIGH, MEDIUM, LOW). Build a running list of traps that
appear in 3 or more questions, or that target the same wrong assumption from
different angles. Write this list explicitly as a planning note:

```
High-frequency traps on this topic:
- [Wrong assumption 1] — appears in [year], [year], [year]
- [Wrong assumption 2] — appears in [year], [year]
```

This list directly feeds:
- **Section 7 one-liners** (Category C discrimination one-liners — the most
  exam-relevant `;;` cards)
- **Section 9 MCQ design** (trap patterns in distractor logic)

Do NOT skip this step for topics with ≥10 PYQs — high-frequency topics have
the densest trap patterns and the highest payoff from trap extraction.

**2d — Extract related concepts for Section 11:**
From the topic-map `## Related Concepts` and `## Cross-Paper Transfer`
sections, note the GS paper connections and essay angles. These feed
Section 11 Connections block directly — do not reconstruct from memory.

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

**Before writing any GS4 Ethics or Essay note:** Open `references/quote-bank.md`. Every `*~thinker quote*` must be copied verbatim from that file — never invented or paraphrased. If the theme you need is not in the file, use a `*~governance link* ;-` (Nolan Principle / constitutional article) instead.

**Before writing Section 9 Practice MCQs:** Open `pyq-data/elimination-patterns.md`. Identify which elimination pattern type dominates for this topic's subject (e.g., History → General Factual 62%; Polity → Statement-Based). Design distractor logic in Section 9 MCQs to match that dominant pattern — not invented patterns.

**Section output order — re-read this before starting:**
- Standard (80–150 nodes): generate sections **1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9 → 10 → 11 → 12** in sequence.
- Flagship (>150 nodes): generate **1 → 2 → 3 → 4 → 5 → 12** first, then **6 → 7 → 8 → 9 → 10 → 11** (see INTERRUPTION NOTICE above — this ordering ensures PYQ Archive survives a context cutoff).

**Coverage floors** (a node = any indented bullet with a delimiter or descriptor):
- Narrow topics (single amendment, one person): ≥ 40 nodes
- Standard topics: ≥ 80 nodes
- Flagship topics (Fundamental Rights, Indian Economy): ≥ 200 nodes

> **Flagship threshold vs. coverage floor — two separate rules:**
> - **Ordering rule (>150 nodes):** Any note expected to exceed 150 nodes uses flagship generation order (1→2→3→4→5→12 first). This is a *generation strategy* to survive context cutoffs.
> - **Coverage floor (≥200 nodes):** Inherently flagship topics (Fundamental Rights, Indian Economy) require ≥200 nodes regardless of ordering chosen. These topics have enough PYQ breadth that 150 nodes would leave gaps.
> A note can trigger the flagship *ordering* at 151 nodes while still being under the flagship *floor* — that means more content is needed, not that the ordering was wrong.

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
| 5 | Content (Main Body) | Learning ladder; includes **Classification Landscape** blocks when concept has types |
| 6 | Flashcard Tables | Entity-to-entity comparison tables (WPI vs CPI, SC vs HC) |
| 7 | One-Liners | Rapid recall fragments (all with `;;`) |
| 8 | Quick Revision | Cloze flashcards + **Classification Enumeration** sub-block when topic has types |
| 9 | Practice MCQs | 5–8 predictive questions; **cross-basis MCQ mandatory** when topic has classifications; open `pyq-data/elimination-patterns.md` to match trap design to UPSC's documented elimination patterns |
| 10 | Rapid Revision | 1-page last-minute review |
| 11 | Feynman Test + Connections + Mains Framework | Comprehension + cross-paper links |
| 12 | PYQ Archive | All verbatim past year questions — Prelims + Mains |

**Classification Landscape — trigger check before writing Section 5:**

Before writing each concept node in Section 5, ask: *"Does this concept have types, kinds, or categories?"* Signal phrases: "types of", "classified as", "kinds of", "on the basis of". If yes → the concept node must end with a **Classification Landscape** block covering:
1. Every independent basis (`**By [Basis]** :-` with `;;>1.` enumeration)
2. Every type (`**[Type]** ::` with `*~basis* ;;`)
3. Cross-Basis Trap Zone (when 2+ bases exist)
4. Enumeration Master

Full template and inflation worked example → `references/section-templates.md` § Classification Landscape.

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

After running the full checklist, open `references/examples.md` and jump to the
Verification Checklist at the end of the file (Section 5 in its table of contents).
Use it as a quick benchmark comparison: does your output match the same structural
quality as the worked example for this subject? The examples.md checklist is a
calibration tool — the quality-checklist.md is the definitive pass/fail gate.

**Top 3 failure modes — check these before opening the checklist:**
1. **Section 12 PYQ count mismatch** — count MCQ nodes in output vs
   `prelims_count` in the topic-map file (re-open the file; do not use memory).
   Any mismatch = fabricated or missing questions.
2. **Section 7 one-liners missing `;;`** — plain `[Fact] = [value]` or
   `→ Back of card` produces no flashcard; these are silent failures.
3. **`##` markdown headers anywhere** — every instance breaks RemNote hierarchy.

**Table flashcard setup — verify every table in Sections 6 and 10:**

Every Markdown table must use `*~RemNote setup* ;-` (for column configuration)
AND `*~Table* ;-` (which contains the actual table rows) — both as children of
the parent `**[Title] Table** :-` Rem.

```
CORRECT — setup and table wrapped in *~Table* ;- descriptor:
  - **WPI vs CPI** :- Flashcard Table
    - *~RemNote setup* ;- After import → click each column header → Flashcard Configuration → Enable For This Column | WPI: Both directions | CPI: Both directions | Notes: Skip
    - *~Table* ;-
    | Feature | WPI | CPI | Notes |
    |---------|-----|-----|-------|

WRONG — table rows not wrapped in *~Table* ;-:
  - **WPI vs CPI** :- Flashcard Table
    - *~RemNote setup* ;- ...
    | Feature | WPI | CPI |   ← table rows must be inside *~Table* ;- descriptor
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
| Table rows not wrapped in `*~Table* ;-` descriptor | Wrap table in `- *~Table* ;-` child of the parent Rem |

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
| `references/quote-bank.md` | Step 7 — before writing any GS4 Ethics or Essay note; every `*~thinker quote*` must come from this file |
| `references/core-philosophy.md` | When you need rationale for a principle (links to cognitive-science.md at its end) |
| `pyq-data/elimination-patterns.md` | Step 7 — before writing Section 9 MCQs; match trap design to UPSC's 10 documented elimination patterns |

---