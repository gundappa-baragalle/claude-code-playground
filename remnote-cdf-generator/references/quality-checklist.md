# Pre-Output Quality Checklist

Run this checklist mentally before finalising any CDF note output.
Every ✗ is a reason to revise before delivering.

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
- [ ] No term appears in Section 5 before it is defined in Section 4 or earlier in Section 5
- [ ] Causes appear before effects throughout
- [ ] Mechanisms are explained before policies that respond to them
- [ ] Simpler/cleaner cases appear before complex/multi-variable cases
- [ ] Every concept's connection to the previous concept is made explicit ("this is why...")
- [ ] The Dependency Map was built before writing — sequence reflects understanding order, not textbook order

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
- [ ] Section 9 MCQs are **synthetic only** — no real PYQs here (all verbatim PYQs go to Section 12)
- [ ] `🎯 LAST YEARS PYQ PATTERN` block present in Section 10 (RAPID REVISION), pulled from topic-map "Exam Patterns & Insights" section — real patterns only, not invented

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
- [ ] Table Name column is always first (left)
- [ ] Table cells are < 5 words

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
- [ ] `*~current affairs link*` filled in every note (not left blank) — event must be post-2022; if uncertain of a recent event, write the search prompt rather than using stale news
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
| Skip the Dependency Map (Step 3.5) before writing Sections 4 and 5 | Sections 4 and 5 will reflect textbook order, not understanding order — the entire learning ladder architecture collapses |
| Place synthetic MCQs in Section 12 (PYQ Archive) | Section 12 is verbatim PYQs only — synthetic questions belong exclusively in Section 9; mixing them destroys the archive's integrity |
| Explain Concept B without first explaining Concept A that B depends on | Forces student to work backwards — destroys comprehension and flow |
| Skip a formula when one exists | Equations reveal relationships more precisely than prose; student is comfortable with elementary maths |
| State directional relationships without showing direction | Always use arrow notation: A ↑ → B ↓; never say "A affects B" without showing how |
| Cover a concept without tracing its prerequisite chain | Creates isolated knowledge islands that cannot be connected or reconstructed |
| Assume student knows aggregate demand, fiscal deficit, MSP, or any technical term | All technical terms must be defined in Section 4 in prerequisite order, regardless of how basic they seem |
