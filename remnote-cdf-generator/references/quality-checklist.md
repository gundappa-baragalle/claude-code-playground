# Pre-Output Quality Checklist

Run this checklist before finalising any CDF note output.
Every ✗ is a reason to revise before delivering.

---

## ⚡ Critical Path — Run These 10 First (Every Note, No Exceptions)

These are the highest-impact checks. If any fail, fix before continuing.

1. **No `##` markdown headers** anywhere in output
2. **Section 12 PYQ count** = `prelims_count` in topic-map (re-open file, count both)
3. **Section 12 questions are verbatim** — not paraphrased or reconstructed from memory
4. **Section 7 one-liners all use `;;`** — no plain `=` or `→ Back of card`
5. **Section 5 dimensions coverage** — open `dimensions_tested` in topic-map; for each dimension type listed (WHAT, HOW, WHERE, WHY, WHO, WHEN, VS), verify Section 5 has at least one concept node addressing that angle. WHAT-heavy topics (e.g. WHAT:45) need proportionally more WHAT-dimension content than HOW-dimension content.
6. **High-frequency traps extracted** — traps from Step 2c planning note appear as Category C one-liners in Section 7 and as distractor logic in Section 9 MCQs
7. **Dependency Map visible** — the `*~dependency chain* ;-` descriptor is present as the first child of Section 4 (not just built mentally)
8. **Correct answer is FIRST child** of every `>>A)` MCQ node
9. **Section 3 Big Picture is multi-line** — each ASCII branch on its own line, never pipe-separated inline
10. **No synthetic MCQs in Section 12** — Section 12 is verbatim PYQs only; predictive questions belong in Section 9

---

## Universal Checks (All Topics)

### Structure ✓
- [ ] No `##` markdown headers anywhere — only `:-` container nodes
- [ ] Minimum 3 indentation levels for each major concept
- [ ] All 12 sections present in correct order
- [ ] File named `[subject]-[topic]-cdf.md`

### Logical Flow ✓ (NEW — check every note)
- [ ] Section 4 entries are ordered from most foundational to most derived (prerequisite chain respected)
- [ ] Section 4 has minimum entry count: ≥6 entries for narrow topics, ≥12 for standard topics, ≥20 for flagship topics — every technical term used anywhere in Sections 5–12 must be defined here
- [ ] Every classification TYPE used in Section 5 (e.g., Demand-Pull, Cost-Push, Orographic) has its component terms defined in Section 4 first — type names are not self-explanatory to beginners
- [ ] No term appears in Section 5 before it is defined in Section 4 or earlier in Section 5
- [ ] Causes appear before effects throughout
- [ ] Mechanisms are explained before policies that respond to them
- [ ] Simpler/cleaner cases appear before complex/multi-variable cases
- [ ] Every concept's connection to the previous concept is made explicit ("this is why...")
- [ ] The Dependency Map was built before writing — sequence reflects understanding order, not textbook order
- [ ] The Dependency Map is **visible in the output** as `*~dependency chain* ;-` descriptor (first child of Section 4) — a mental-only map does not count

### Mathematical Clarity ✓ (NEW — check Economy, Science, Geography topics especially)
- [ ] Every concept with a mathematical relationship has its formula included (MV=PQ, Fiscal Deficit = E−R, etc.)
- [ ] Every formula has each variable explained
- [ ] Directional relationships use arrow notation: A ↑ → B ↓ → C ↑
- [ ] Price index calculations show the formula and what the number means
- [ ] Percentage comparisons are made explicit where helpful (CPI food weight is ~2× WPI food weight)
- [ ] ASCII graphs used for any concept with a supply-demand, growth-inflation, or rate-effect relationship
- [ ] Maths is used ONLY to clarify, never to show off — if prose is clearer, use prose

### PYQ Integration ✓
- [ ] PYQ lookup completed — concept-index.json checked (Step 2a) AND topic-map file opened and read (Step 2b)
- [ ] `*~PYQ frequency*` uses real `total_count` from the topic-map file (not a guess or memory estimate)
- [ ] `*~Prelims weightage*` uses real `prelims_count`
- [ ] `*~revision priority*` matches HIGH/MEDIUM/LOW thresholds
- [ ] Section 9 MCQs are **predictive only** — based on gap analysis (untested dimensions, gap years, post-`last_asked` developments, recurring trap patterns); no real PYQs here (all verbatim PYQs go to Section 12)
- [ ] Section 9 trap design matches UPSC's documented elimination patterns — `elimination-patterns.md` opened and the dominant pattern type for this topic's subject checked (e.g. History → General Factual 62%; Polity → Statement-Based)
- [ ] `🎯 LAST YEARS PYQ PATTERN` block present in Section 10 (RAPID REVISION), pulled from topic-map `## Exam Patterns & Insights` section (look for "Most tested dimension" and "Common Trap Patterns on This Topic" subsections) — real patterns only, not invented

### Cognitive Quality ✓
- [ ] Every unfamiliar term defined on first use (Beginner Test)
- [ ] Every major concept has `*~why it arose*` AND `*~significance*`
- [ ] At least 3 memory hook types per major concept
- [ ] At least 2 `*💭 self-explain*` prompts (placed BEFORE answer, not after)
- [ ] At least 1 `*🔨 your example*` generative prompt
- [ ] Every major concept has `*~does NOT apply when*`
- [ ] Feynman Test block present before Connections
- [ ] **Before You Read** pre-questions present in Section 2
- [ ] `*~Prelims mode*` and `*~Mains mode*` in Practice MCQs

### Flashcard Quality ✓
- [ ] `;;` used only for facts UPSC could ask directly
- [ ] `;-` used for explanations, analogies, hooks (no flashcard generated)
- [ ] Section 7 one-liners all use `;;` delimiter — no plain `=` or `→ Back of card` suffixes (plain text produces no flashcard)
- [ ] All Quick Revision answers wrapped in `{{cloze}}`
- [ ] Confusable items use `{{answer}}{({hint})}` format — NOT `{{answer::hint}}` (wrong syntax)
- [ ] MCQ correct answer is FIRST child option
- [ ] Statement-based MCQs: all numbered statements listed as sub-bullets BEFORE the `>>A)` options
- [ ] "How many of the above are correct?" MCQs: statements listed first, then options ("Only one", "Only two", etc.) with correct first
- [ ] Every MCQ has `#[[Extra Card Detail]]` explanation
- [ ] Table uses `*~RemNote setup* ;-` (column config) AND `*~Table* ;-` (wrapping the actual rows) — both as children of `**[Title] Table** :-`
- [ ] Table Name column is always first (left)
- [ ] Table cells are < 5 words

### Classification Quality ✓ (apply when topic has types/categories/kinds)
- [ ] Every classifiable concept in Section 5 has a **Classification Landscape** block (signal: "types of", "classified as", "on the basis of")
- [ ] Single-basis variant used when exactly 1 axis exists (Within-Basis Trap Zone, single Enumeration count) — multi-basis full template only when 2+ axes
- [ ] Section 3 Big Picture has a **classification matrix branch** for heavily classificatory topics (basis → types as leaves; no definitions — spatial overview only)
- [ ] Every basis has `*~all types* ;;>1.` with type names as ordered children — generates enumeration flashcard
- [ ] Every type node has `*~basis* ;;` descriptor — generates cross-basis attribution flashcard
- [ ] Every type node uses `*~trigger condition* ;-` (not `;;`) unless topic-map explicitly shows UPSC tested the trigger mechanism for that type
- [ ] Inline mini-tables use `*⚡ [Basis] types — side-by-side* ;-` with `;-` not `;;` (scaffold only — not a flashcard)
- [ ] `*~UPSC note*` uses `;-` (multi-fact planning note, not atomic — atomic facts go in Section 7 one-liners)
- [ ] **Cross-Basis Trap Zone** present when 2+ bases exist — names specific cross-basis confusions explicitly
- [ ] **Within-Basis Trap Zone** present in single-basis variant — names the most confused within-axis pair
- [ ] `*~UPSC note*` flags which bases/types are tested vs untested (untested = Section 9 targets)
- [ ] `**🔢 Enumeration Master**` block present with `*~[Basis] count* ;;` for each basis
- [ ] Section 7 has **classification one-liners** — Category A (Type → basis attribution) and Category B (Type → threshold/defining criterion) for every Classification Landscape
- [ ] Section 8 has **Classification Enumeration** cloze sub-block — one sentence per basis, count as hint on last cloze
- [ ] Section 9 has at least one cross-basis discrimination MCQ — Frame A (attribution), B (basis ID), or C (pair discrimination)
- [ ] Section 10 **⚠️ TRAP ALERTS** block contains cross-basis trap entries pulled from the Cross-Basis Trap Zone
- [ ] Section 10 **🔢 NUMBERS TO REMEMBER** block contains threshold and count entries from the Enumeration Master
- [ ] Section 10 **📋 FACTS TO MEMORIZE** table has classification rows (basis → compressed type list) for each Classification Landscape
- [ ] Classification content stays in Section 5 — never moved to a Section 6 table (Section 6 = entity comparison only)

### Completeness ✓
- [ ] Big Picture ASCII map present and **multi-line** (each branch on its own line — never a single collapsed pipe-separated string)
- [ ] Timeline present (historical topics)
- [ ] **Section 4 entry count floor met:** ≥6 entries for narrow topics, ≥12 for standard topics, ≥20 for flagship topics
- [ ] Comparison table for most-confused pair
- [ ] RAPID REVISION section fits on 1 page
- [ ] `*~current affairs link*` filled (never blank)
- [ ] Cross-Paper Transfer block filled with all GS angles
- [ ] `*~GS4 angle*` filled for all History and Polity topics
- [ ] `*~Essay angle*` filled for all topics
- [ ] **Section 5 covers all `dimensions_tested`** — re-open topic-map `dimensions_tested` field; for each dimension type (WHAT, HOW, WHERE, WHY, WHO, WHEN, IMPACT, VS), confirm Section 5 has at least one concept node that would allow a student to answer a question of that type. If a dimension is present in the topic-map but absent from Section 5, add a concept node before finalising.
- [ ] **High-frequency traps appear in Section 7** — the trap list built in Step 2c must have at least one Category C discrimination one-liner (`;;`) per high-frequency trap in Section 7; traps that appear in 3+ PYQs must not be left out.
- [ ] **Section 12 (PYQ Archive) present** — all Prelims PYQs copied verbatim from topic-map
- [ ] **Section 12 count verified** — number of MCQ nodes = number of Prelims PYQs in topic-map (count both to confirm; re-open topic-map file to count — never use memory)
- [ ] **Section 12 ordering** — questions are newest-first (2024 → 2023 → oldest); verify before delivering
- [ ] **Mains PYQs in Section 12** — every Mains question has answer framework (or "None indexed" note if 0 Mains questions)

### Interruption / Partial Output ✓
- [ ] If generation was interrupted mid-output: partial file saved as `[subject]-[topic]-cdf-PARTIAL.md`
- [ ] Interruption marker added at exact cut point as a `;-` descriptor: `*~GENERATION INTERRUPTED* ;- stopped after Section [N] — request continuation to complete`
- [ ] **⚠️ Do NOT use HTML comments (`<!-- ... -->`) for interruption markers** — they render as visible text in RemNote
- [ ] `present_files` used to deliver partial file immediately — not discarded
- [ ] User told which section was completed and which remains

---

## Subject-Specific Checks

### Art & Culture ✓
- [ ] Visual identification hook present ("what makes this *visually* unique")
- [ ] `*~status* ;; Living tradition` or `Extinct` flag present
- [ ] Exam trap — the one feature UPSC uses to distinguish this from similar styles
- [ ] Comparison table against most-confused style
- [ ] Location cloze includes confusable wrong state as hint

### Geography — Map Questions ✓
- [ ] **Locate It** block present with location cloze cards
- [ ] Every location cloze includes the confusable wrong answer as hint
- [ ] Rivers: source + mouth + states traversed (all three in cloze)
- [ ] National Parks: state + flagship species + conservation status
- [ ] Passes: connects what to what (both sides named)

### Science & Technology ✓
- [ ] Question type identified (Mechanism / Application / Policy) and emphasis set accordingly
- [ ] `*~as of* ;; [year]` present on all data and status claims
- [ ] Indian govt program/agency linked for every S&T concept

### Current Affairs Integration ✓
- [ ] `*~current affairs link*` filled in every note (not left blank) — event must be post-2022 (prefer 2024–2025); if uncertain of a recent event, write the search prompt (`Verify: search [topic] + 2024/2025`) rather than using stale or invented news
- [ ] `*~contemporary_relevance*` from topic-map carried into note
- [ ] At least one current event cited with year in Mains Answer Framework body
- [ ] Recent policy/law cited where relevant (post-2020 preferred)

### Ethics Notes (GS4) ✓
- [ ] Section 3 Big Picture uses value-framework map (not factual hierarchy)
- [ ] Every concept has `*~thinker quote*` — from Quote Bank only, NEVER invented
- [ ] Every concept has `*~case study angle*` — civil service scenario
- [ ] Every concept has `*~opposite value*` — conflict named + resolution method stated
- [ ] Every concept has `*~governance link*` — Nolan Principle / CCS Rule / Article cited
- [ ] Every concept has `*~real example*` — non-textbook Indian example
- [ ] Every concept has `*~ethical theory*` — primary framework named
- [ ] GS4 Paper 2 case study questions use 5-step framework
- [ ] Flashcards test application (scenario-based), not memorisation

### Essay Notes ✓
- [ ] Note is flagged as Essay Paper content (not GS answer)
- [ ] Opening uses quote / paradox / anecdote — NOT a definition
- [ ] All 4 quadrants covered: Historical/Philosophical + Contemporary + Challenges + Way Forward
- [ ] At least one interdisciplinary argument present
- [ ] Indian example + global comparison paired in at least one paragraph
- [ ] Clear thesis stated in intro (not the opening line)
- [ ] Conclusion echoes Preamble / Art 21 / civilizational vision — NOT a summary
- [ ] Quotes are attributable (from Quote Bank only)

---

## NEVER DO (Quick Reminder)

| ❌ Don't | Why |
|---------|-----|
| Use `##` markdown headers | Breaks RemNote hierarchy |
| Use term before defining it | Fails Beginner Test |
| Put ⚠️ inside table cells | Breaks table rendering |
| State fact without "why" | Fails Conceptual Bridge |
| Put `*💭 self-explain*` AFTER the answer | Defeats the entire principle |
| MCQ correct answer not first | RemNote expects first = correct |
| Skip `#[[Extra Card Detail]]` on MCQs | Students never see the explanation |
| Skip Feynman Test | Most reliable comprehension check |
| Leave `*~current affairs link*` blank | Static notes fail at Mains level |
| Invent PYQ years or question counts | Only use data from pyq-data/ files |
| Skip opening `elimination-patterns.md` before Section 9 | Section 9 MCQ distractor logic must match UPSC's actual elimination pattern frequency — invented traps miss what the exam tests |
| Leave Section 7 empty of Category C discrimination one-liners when high-frequency traps exist | The trap list from Step 2c must produce `;;` one-liners — traps that appear in 3+ PYQs are prime atomic recall targets |
| State post-`last_asked` developments as fact without verification | If not in topic-map, mark as `{{development}}{(verify: search [topic] + 2024/2025)}` — never invent |
| Invent quotes in Ethics notes | Fabricated quotes destroy credibility |
| Start Essay with a definition | Penalised by examiners; always quote/paradox/anecdote |
| Write Essay as a list of points | Essay is prose — bullets lose marks |
| Use only textbook examples in Ethics | Use Ashok Khemka, Sanjiv Chaturvedi, Aruna Roy |
| Skip `*~as of*` on S&T/Economy notes | Undated tech/data facts become liabilities |
| Resolve value-conflict vaguely | Name the resolution principle explicitly |
| Write location cloze without wrong answer as hint | The confusable wrong state IS the exam trap |
| Use `;;>A)` for MCQs | `;;>A)` is a Descriptor MCQ — it breaks PYQ anchor linking and generates wrong card format; always use `>>A)` |
| Write Section 7 one-liners without `;;` | Plain `[Fact] = [value]` or `→ Back of card` produces no flashcard — it's static text in RemNote |
| Collapse Section 3 Big Picture to one line | Each tree branch must be on its own line; inline `|`-separated strings are unreadable in RemNote |
| Use `{{answer::hint}}` cloze hint syntax | Wrong — RemNote requires `{{answer}}{({hint})}`; the `::` version imports as literal text |
| Skip Section 12 (PYQ Archive) | Students exposed only to 5–6 MCQs instead of all real questions; UPSC repeats patterns |
| Paraphrase PYQ question stems | Exact wording matters — UPSC reuses phrasing; always copy verbatim |
| Omit Mains PYQs from Section 12 | Mains preparation requires exposure to every real essay question from the topic |
| List wrong answer first in MCQ | RemNote reads FIRST child as correct; wrong order breaks the flashcard |
| Skip the Dependency Map (Step 6) before writing Sections 4 and 5 | Sections 4 and 5 will reflect textbook order, not understanding order — the entire learning ladder architecture collapses |
| Skip `📊 Prediction basis` in Section 9 MCQ explanations | Every Section 9 question must state which signal (gap year / untested dimension / post-last_asked development / pattern) justified including it |
| Place synthetic or predictive MCQs in Section 12 (PYQ Archive) | Section 12 is verbatim PYQs only — predictive questions belong exclusively in Section 9; mixing them destroys the archive's integrity |
| List types as flat bullets under a concept without a Classification Landscape | Flat lists create Level 1 recall only; UPSC tests Level 2 (cross-basis) and Level 3 (enumeration) — these require the full `;;>1.` / `*~basis* ;;` / Cross-Basis Trap Zone structure |
| Use `;;` on `*~trigger condition*` unconditionally | Trigger conditions are causal/mechanistic — `;-` by default; only use `;;` when topic-map confirms UPSC directly tested the trigger for that specific type |
| Use `;;` on inline mini-tables inside Classification Landscape | The `*⚡ [Basis] types — side-by-side* ;-` table is a scaffold — it uses `;-`; the flashcards come from `::` on each type and `;;>1.` on each basis |
| Omit `*~basis* ;;` from individual type nodes | Without it, students can define every type but cannot answer "stagflation belongs to which classification axis?" — the cross-basis attribution flashcard is what `*~basis* ;;` generates |
| Skip classification one-liners in Section 7 | Cross-basis attribution facts (Type → basis) and thresholds are prime `;;` targets; leaving them out means SRS misses atomic Level 2 recall cards entirely |
| Skip Classification Enumeration clozes in Section 8 | "How many of the following are correct?" questions require recall of the complete set per basis — enumeration clozes train exactly this |
| Skip the cross-basis MCQ in Section 9 when topic has classifications | Cross-basis discrimination is UPSC's post-2020 pattern shift — at least one Section 9 question must use Frame A, B, or C |
| Leave Section 10 TRAP ALERTS generic when Cross-Basis Trap Zone exists in Section 5 | The Cross-Basis Trap Zone must feed directly into Section 10 TRAP ALERTS — this is the student's last-minute reminder of the most dangerous confusions |
| Leave Section 10 NUMBERS generic when Enumeration Master exists in Section 5 | Thresholds and type counts from the Enumeration Master belong in Section 10 NUMBERS TO REMEMBER |
| Use multi-basis template for a single-axis concept | Single-axis concepts (rocks, clouds, soils) use the single-basis variant — empty Cross-Basis Trap Zones waste space and signal sloppy application |
| Create a Section 6 table for a Classification Landscape | Section 6 is for entity-to-entity comparison (WPI vs CPI); classification landscapes belong entirely in Section 5 with the full `::` / `;;>1.` / `*~basis*` structure |
| Skip the classification matrix branch in Section 3 for heavily classificatory topics | For topics where classification IS the primary dimension, the ASCII tree must include a classification matrix branch — it is the spatial advance organiser for the entire Section 5 landscape |
| Explain Concept B without first explaining Concept A that B depends on | Forces student to work backwards — destroys comprehension and flow |
| Use a classification type name in Section 5 without defining its component terms in Section 4 | Type names like "Demand-Pull" or "Orographic" are not self-explanatory — the prerequisite chain rule applies to types too; undefined terms make Section 5 incomprehensible to beginners |
| Skip a formula when one exists | Equations reveal relationships more precisely than prose; student is comfortable with elementary maths |
| State directional relationships without showing direction | Always use arrow notation: A ↑ → B ↓; never say "A affects B" without showing how |
| Cover a concept without tracing its prerequisite chain | Creates isolated knowledge islands that cannot be connected or reconstructed |
| Assume student knows aggregate demand, fiscal deficit, MSP, or any technical term | All technical terms must be defined in Section 4 in prerequisite order, regardless of how basic they seem |
