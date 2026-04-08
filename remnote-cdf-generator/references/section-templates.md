## The 12 Sections — Templates

### Section 1: Header & Metadata
```
- **[Topic]** :- UPSC [Subject]
  - *~version* ;- v[date] — refresh if >6 months old
  - *~source* ;- [Standard books with chapter numbers]
  - *~PYQ frequency* ;- [Step 0: "X total (Prelims: Y, Mains: Z), YYYY–YYYY"]
  - *~Prelims weightage* ;- [Step 0: real prelims_count; last asked YYYY]
  - *~Mains relevance* ;- [Which GS paper, what themes]
  - *~revision priority* ;- [Step 0: HIGH / MEDIUM / LOW]
```
Revision priority thresholds: HIGH = ≥10 PYQs (daily SRS) | MEDIUM = 5–9 (weekly) | LOW = <5 (monthly)

### Section 2: Why Study This? + Before You Read
```
  - **Why Study [Topic]?** :- Motivation
    - *~exam relevance* ;; [Specific papers + frequency]
    - *~real-world relevance* ;; [Current affairs connections]

  - **Before You Read** :- Activate Prior Knowledge
    - *🧪 try first* ;- Think about these before reading:
      1. [Something the student likely already knows — even partially]
      2. [Why do you think this topic/law/event came about?]
      3. [Predict: what does UPSC test about this?]
    - *~revisit after* ;- Come back after finishing — can you answer all 3 now?
```
Pre-questions are `;-` (no flashcard). They are cognitive primers, not recall targets.

### Section 3: Big Picture (Visual Map)

The ASCII tree lives inside a triple-backtick code fence as the value of `*~structure* ;-`. Use the richest visual that fits the topic — box-drawing characters (`├──`, `└──`, `│`), geometric diagrams, timelines, triangles, arrows. The code fence renders as monospace in RemNote, so spatial layout is preserved exactly.

**Visual type guide:**
- **Hierarchical topics** (most topics): use `├──` / `└──` tree with `│` connectors
- **Relational/triangular concepts** (e.g., Golden Triangle, trilemma, three-pillar frameworks): draw a geometric ASCII diagram
- **Historical topics**: use a timeline with `────` connectors and vertical drops
- **Cyclical processes**: use arrow loops `→ A → B → C → A`
- **Comparisons**: use a side-by-side split with a `|` divider column

**Worked example (Inflation) — basic `+--` style:**

```
  - **Big Picture** :- Visual Overview
    - *~structure* ;-
      ```
      INFLATION (sustained rise in general price level)
      |
      +-- CAUSES (Three channels)
      |   +-- 1. Demand-Pull: Too much money chasing too few goods
      |   |       Expansionary policy / Fiscal stimulus / Rising income
      |   +-- 2. Cost-Push: Production costs rise → prices rise
      |   |       Oil shock / MSP hike / Wage rise / Supply shock
      |   +-- 3. Monetary: Excess money supply (MV = PQ)
      |           RBI prints money → more rupees chase same goods
      |
      +-- MEASUREMENT (India's price indices)
      |   +-- WPI (Wholesale Price Index)
      |   |   +-- Tracks: Primary articles + Fuel + Manufactured goods
      |   |   +-- Services: NOT covered
      |   |   +-- Frequency: Monthly | Base year: 2011-12
      |   |   +-- Weight: Food ~24%; was India's headline until 2014
      |   +-- CPI (Consumer Price Index)
      |       +-- Variants: CPI-Combined (Urban+Rural), CPI-IW, CPI-AL
      |       +-- Services: YES covered
      |       +-- Weight: Food ~46% (CPI-IW) | Base year: 2012
      |       +-- RBI's headline measure since 2014 (Urjit Patel Committee)
      |
      +-- RELATED PHENOMENA
      |   +-- Deflation: Sustained fall in general price level
      |   +-- Disinflation: Inflation rate falling (still positive)
      |   +-- Stagflation: Inflation + Stagnation (high inflation + low growth)
      |   +-- Hyperinflation: Inflation > 50%/month; currency collapse
      |   +-- Base Effect: Statistical illusion from low/high base year
      |
      +-- CONTROL MECHANISMS
          +-- Monetary (RBI): Repo rate, CRR, SLR, OMO, MSF
          +-- Fiscal (Govt): Cut spending, raise taxes, release buffer stocks
          +-- Supply-side: Import, release reserves, price stabilization fund

      INDIA's INFLATION TARGETING FRAMEWORK:
      2016 RBI Act amendment → MPC (Monetary Policy Committee)
      Target: 4% CPI inflation ± 2% band (2%–6%)
      Breach: If outside band for 3 consecutive quarters → RBI explains to Govt
      ```
```

**Worked example (Fundamental Rights) — rich `├──` / `└──` style with geometric diagram:**

```
  - **Big Picture** :- Visual Overview
    - *~structure* ;-
      ```
      FUNDAMENTAL RIGHTS (Part III, Art 12-35)
      │
      ├── Art 12-13 : DEFINITION & ENFORCEABILITY
      │       ├── Art 12: What is "State"?
      │       └── Art 13: Laws inconsistent with FRs = void
      │
      ├── Art 14-18 : RIGHT TO EQUALITY
      │       ├── Art 14: Equality before law + Equal protection
      │       ├── Art 15: No discrimination (sex, religion, race, caste, birthplace)
      │       ├── Art 16: Equal opportunity in public employment
      │       ├── Art 17: Abolition of untouchability [ABSOLUTE]
      │       └── Art 18: Abolition of titles (no "Sir", "Rao Bahadur")
      │
      ├── Art 19-22 : RIGHT TO FREEDOM
      │       ├── Art 19: 6 freedoms (speech, assembly, movement, profession...)
      │       ├── Art 20: Protection in conviction (no double jeopardy, no self-incrimination)
      │       ├── Art 21: Right to Life & Personal Liberty [MOST EXPANDED]
      │       │       └── Art 21A: Free & compulsory education (6-14 yrs) [86th Amend]
      │       └── Art 22: Protection against arrest & detention
      │
      ├── Art 23-24 : RIGHT AGAINST EXPLOITATION
      │       ├── Art 23: No trafficking, forced labour (Begar)
      │       └── Art 24: No child labour in hazardous work (<14 yrs)
      │
      ├── Art 25-28 : RIGHT TO FREEDOM OF RELIGION
      │       ├── Art 25: Freedom of conscience & free profession of religion
      │       ├── Art 26: Freedom to manage religious affairs
      │       ├── Art 27: No tax for promotion of religion
      │       └── Art 28: No religious instruction in state-funded institutions
      │
      ├── Art 29-30 : CULTURAL & EDUCATIONAL RIGHTS
      │       ├── Art 29: Protection of distinct language/culture
      │       └── Art 30: Right of minorities to establish educational institutions
      │
      └── Art 32-35 : RIGHT TO CONSTITUTIONAL REMEDIES
              ├── Art 32: Right to move SC [Ambedkar: "Heart & Soul of Constitution"]
              ├── Art 33: Parliament may modify FRs for armed forces
              ├── Art 34: Parliament may restrict FRs during martial law
              └── Art 35: Parliament alone can make laws to enforce FRs

      GOLDEN TRIANGLE:
      Art 14 (Equality) ───────── Art 19 (Freedoms)
              │                          │
              └─────── Art 21 ───────────┘
                    (Life & Liberty)
      → Any law attacking all three = unconstitutional
      ```
```

**Full Template:**

```
  - **Big Picture** :- Visual Overview
    - *~structure* ;-
      ```
      TOPIC NAME
      │
      ├── Major Component 1
      │       ├── Sub-component A
      │       └── Sub-component B
      │
      └── Major Component 2
              ├── Sub-component C
              └── Sub-component D

      TIMELINE (historical topics):
      [Date1]────[Date2]────[Date3]
         │           │          │
       Event1     Event2     Event3

      GEOMETRIC / RELATIONAL (triangles, trilemmas, cycles):
      [Corner A] ─────────── [Corner B]
            │                     │
            └──────[Corner C]─────┘
      → Relationship or constraint label
      ```
```

### Section 4: Prerequisite Concepts & Key Terms (The Foundation Layer)

**This section is not a glossary to be skimmed. It is the foundation on which Section 5 rests.**

Before writing Section 4, do this thinking exercise:
1. List every concept Section 5 will use
2. For each concept, ask: "Does a complete beginner already know this from everyday life?" If NO → it goes in Section 4
3. Order Section 4 entries from most basic to most derived — concepts that depend on earlier concepts come later
4. For each entry, write it as if speaking to a smart person who has never studied economics/polity/science

**Section 4 must contain — without exception:**
- Every technical term used anywhere in Sections 5–12
- Every prerequisite concept that the topic depends on (even if it "belongs" to another topic)
- Every institution, body, law, or index mentioned in PYQs
- Every comparison partner (e.g., if comparing WPI vs CPI, both must be defined here first)

**The prerequisite chain rule:** If Term B requires Term A to be understood, Term A must appear BEFORE Term B in this section. Work backwards from the main topic until you hit concepts the beginner already knows from daily life.

Example chain for Inflation:
```
Daily life knowledge: "prices went up at the market"
    ↓ needs to understand
Output / Goods & Services (what an economy produces)
    ↓ needs to understand
Aggregate Demand + Aggregate Supply (total buying vs total producing)
    ↓ needs to understand
Price Level (average price of all goods)
    ↓ NOW can define
Inflation (sustained rise in price level)
    ↓ NOW can understand
Types of Inflation, WPI, CPI, RBI tools etc.
```

**Template for each entry:**
```
    - **Term** :: One-sentence precise definition — use the simplest words possible
      - *📌 beginner note* ;- Explain in plain language. Use a concrete everyday example or analogy. If applicable, use a simple equation or formula to show the relationship. Connect to something the student already knows.
      - *🧠 analogy* ;- [Only if the beginner note isn't enough — an analogy that makes it click]
      - *~formula* ;; [If there is a mathematical relationship — always include it when it exists]
      - *~why it matters for this topic* ;- [One line: how does knowing this term unlock understanding of the main topic?]
```

**Mathematics rule for Section 4:** Whenever a concept has a mathematical relationship, express it. Examples:
- Fiscal Deficit: `Fiscal Deficit = Total Expenditure − Total Revenue (excl. borrowings)` → if positive, govt borrows
- QTM: `M × V = P × Q` → if M rises and V, Q are stable, P must rise
- Real vs Nominal: `Real Return = Nominal Return − Inflation Rate` → why bondholders lose when inflation rises
- Price Index: `Index = (Current Price / Base Year Price) × 100` → index 330 means prices 3.3× base year

Do not use maths for its own sake. Use it when the equation reveals a relationship faster or more precisely than prose.

### Section 5: Content — The Main Body (Built as a Learning Ladder)

**The single most important rule for Section 5:** Concepts must appear in the order a student needs to learn them, not in the order a textbook chapter happens to list them. Every concept must be fully understandable using only: (a) everyday knowledge, (b) things defined in Section 4, and (c) concepts already covered earlier in Section 5.

#### Pre-writing check — build the dependency map first

Before writing Section 5, mentally map the concept dependencies:

```
Which concept is the ROOT (can be understood with zero prior knowledge of this topic)?
    → Explain this first

Which concepts DEPEND ON the root?
    → Explain these second, using the root as foundation

Which concepts depend on THOSE?
    → Explain these third

...and so on until all PYQ-tested dimensions are covered
```

This produces a logical sequence — not alphabetical, not textbook order, but **understanding order**.

#### Flow rules — enforce these without exception

**Rule 1: Never use a term in Section 5 that hasn't been defined yet.** If you find yourself using a term that appears for the first time in the middle of Section 5 — stop. Either add it to Section 4, or define it inline as a sub-concept before using it.

**Rule 2: Causes always before effects.** If A causes B, explain A fully before explaining B.

**Rule 3: Mechanism before policy.** Explain how something works before explaining what the government does about it. E.g., explain how inflation erodes purchasing power before explaining why RBI raises rates.

**Rule 4: Simple case before complex case.** Explain demand-pull inflation (clean, one-variable) before stagflation (multi-variable, counterintuitive).

**Rule 5: Use mathematics to show direction and relationships.** When a concept has a directional relationship, show it with arrows and simple math, not just words:
```
Repo Rate ↑ → Borrowing cost ↑ → Credit ↓ → Spending ↓ → Demand ↓ → Inflation ↓
M ↑ (V, Q constant) → P ↑  [from MV = PQ]
Real Return = Nominal Return − Inflation Rate  →  if inflation ↑, real return ↓
```
ASCII graphs are encouraged for any relationship that has a direction:
```
    Price
      |         S (supply falls)
      |    S'  /
      |   /   /
      |  /   /
      | /   /   D (demand unchanged)
      |/___/__________
                   Quantity
  Result: same demand, less supply → price rises (supply shock inflation)
```

**Rule 6: Build the "so what?" at every step.** After each concept, explicitly state its consequence for the next concept. Never leave the student wondering "okay, but why does this matter for what I'm learning?"

#### Template for each major concept node

Every concept that UPSC has tested or could test gets this full treatment:

```
    - **[Concept Name]** :: [Precise one-sentence definition — no jargon unless already defined]
      - *📌 beginner note* ;- [How does this relate to something the student already knows from daily life? What would a non-economist call this?]
      - *~why it arises* ;; [Root cause — what conditions produce this concept? This must use only already-explained concepts]
      - *~significance* ;; [Why does this matter? What does it cause or prevent? Link to real India/UPSC context]
      - *~mechanism* ;- [Step-by-step: how does this work? Use arrows: A → B → C. Use math where it adds precision]
      - *💭 self-explain* ;- [Ask the student to reason through something BEFORE revealing the answer — placed immediately before the key insight, never after]
      - *~formula / equation* ;; [If a mathematical relationship exists — always include it]
      - *🧠 analogy* ;- [One concrete, vivid comparison that makes the abstract tangible]
      - *⚡ vs [Most Confused Alternative]* ;- [Side-by-side contrast. Use a mini table if 3+ dimensions differ]
      - *⚠️ exam trap* ;- [Specific UPSC trap from PYQ data: state the wrong thinking → explain why it's wrong → give the correct logic]
      - *~does NOT apply when* ;- [Boundary condition: when is this concept NOT relevant or NOT the right frame?]
      - *~India context* ;; [Specific Indian example, data point, institution, or case — prefer post-2022 examples. If uncertain of recency, write: `Verify: search [topic] + 2024/2025 for current data` rather than using potentially stale news]
      - *🔨 your example* ;- [Ask the student to generate their own example — forces active processing]
```

**What to include / exclude:**
- Include EVERYTHING that a PYQ has tested about this concept — even seemingly trivial details
- Include every prerequisite relationship ("this works because X, which we established above")
- Include mathematical representations whenever they exist
- Exclude biographical trivia, excessive historical narrative, and content with zero PYQ relevance
- Never compress a concept to save space — if it needs 10 lines to be fully clear, write 10 lines

#### Coverage floor — non-negotiable

After writing Section 5, ask: "If a student read only this section, could they answer every Prelims question in the PYQ Archive?" If the answer is no for even one question — find the gap and fill it.

**Special rule for Economy topics:** Every number (percentage, year, rate) must be accompanied by:
1. Its formula or source (where does this number come from?)
2. Why it is what it is (why 4% target? why 2-6% band?)
3. What happens when it changes (what if inflation goes above 6%?)

**Special rule for mathematical relationships:** Do not just state the formula. Walk through what each variable means and what happens when one variable changes while others are held constant. Example:
```
MV = PQ
M = money supply, V = velocity, P = price level, Q = real output

If M doubles (RBI prints money), and V and Q stay constant:
P must double → inflation

If Q falls (drought destroys crops), and M and V stay constant:
P must rise → supply shock inflation

This is why BOTH printing money AND output collapse cause inflation.
```

### Section 6: Flashcard Tables

**CRITICAL — RemNote Simple Table Flashcard Design:**

When RemNote imports a Markdown table, it becomes a **Simple Table**. In Simple Tables:
- The **first column = Concept column** (shown in gray = the "Name" of each row)
- Every **other column = Descriptor column** (can generate flashcards per column)
- For each non-Name column, the user enables flashcards via: click column header → Flashcard Configuration → Enable For This Column → choose direction

**Design rules for every table:**
1. **Name column must be the primary identity** of each row — the thing being studied (e.g., the Council name, the Site name, the Concept name). Never put a generic label like "Feature" or "Item" as the first-column value.
2. **Each non-Name column should test one discrete fact** — keep cells ≤5 words so flashcard answers are crisp.
3. **After every table, add a RemNote Flashcard Setup descriptor** specifying which columns to enable and which direction. This is mandatory — it tells the user exactly what to configure after import.

**Flashcard direction guide:**
- `Forward` (Name + column header → cell value): Use when you see the concept and need to recall the fact
- `Backward` (column header + cell value → Name): Use when you see the fact and need to recall the concept
- `Both`: Use when recall in both directions is valuable (e.g., location ↔ site name)
- `Skip`: Use for context/memory-hook columns that are not worth drilling

#### ⛔ CRITICAL INDENTATION RULE — THE MOST COMMON TABLE FAILURE

The `*~RemNote setup* ;-` descriptor and the Markdown table rows are **siblings** — both are direct children of the parent `**[Title] Table** :-` Rem. The table is NOT nested inside or under the setup descriptor.

**WRONG (table nested under setup descriptor — produces garbled output):**
```
  - **WPI vs CPI Table** :- Flashcard Table
    - *~RemNote setup* ;- After import → click each column header → Flashcard Configuration → Enable For This Column | WPI: Both directions | CPI: Both directions | Notes: Skip
      | Feature | WPI | CPI-Combined | Notes |
      |---------|-----|--------------|-------|
      | **Full name** | Wholesale Price Index | Consumer Price Index | — |
```
In RemNote this concatenates the setup descriptor text with the table pipe characters into one unreadable garbled line.

**CORRECT (setup descriptor and table rows are siblings at the same indentation level):**
```
  - **WPI vs CPI Comparison** :- Flashcard Table
    - *~RemNote setup* ;- After import → click each column header → Flashcard Configuration → Enable For This Column | WPI: Both directions | CPI: Both directions | Notes: Skip
    | Feature | WPI | CPI-Combined | Notes |
    |---------|-----|--------------|-------|
    | **Full name** | Wholesale Price Index | Consumer Price Index | — |
    | **Tracks prices at** | Wholesale/producer level | Retail/consumer level | CPI = what YOU pay |
    | **Covers services?** | NO | YES | Key WPI limitation |
    | **Food weight** | ~24% | ~39% (combined) | CPI more food-sensitive |
    | **Base year** | 2011-12 | 2012 | — |
    | **Frequency** | Monthly | Monthly | WPI = monthly |
    | **RBI's measure?** | Was until 2014 | YES (since 2014) | MPC targets CPI |
    | **Published by** | Office of Economic Adviser (DPIIT) | MoSPI | Different ministries |
```

Notice: the `| Feature | WPI |...` table row is at the **same indentation** as `- *~RemNote setup* ;-`, not further indented under it.

#### Full Template

```
  - **[Title] Table** :- Flashcard Table
    - *~RemNote setup* ;- After import → click each column header → Flashcard Configuration → Enable For This Column | [Column 2]: Both directions | [Column 3]: Forward only | [Column 4]: Skip
    | Name | [Column 2] | [Column 3] | [Column 4] |
    |------|-----------|-----------|-----------|
    | **Row 1** | cell | cell | cell |
    | **Row 2** | cell | cell | cell |
```

**⚠️ Do NOT use HTML comments (`<!-- RemNote Setup: ... -->`).** RemNote renders HTML comments as visible plain text. Always use the `*~RemNote setup* ;-` descriptor format — but ensure it is a **sibling** of the table rows, not their parent.

**Worked example — Buddhist Sites Table:**
```
  - **Key Buddhist Sites Table** :- Flashcard Table
    - *~RemNote setup* ;- After import → click each column header → Flashcard Configuration → Enable For This Column | Location: Both directions (Site → Location AND Location → Site; PYQ trap area) | Known For: Forward only | Memory Hook: Skip
    | Site | Location | Known For | Memory Hook |
    |------|----------|-----------|-------------|
    | **Sanchi** | Madhya Pradesh | Greatest stupa; Torana; UNESCO | Ashoka built |
    | **Amaravati** | Andhra Pradesh | Major stupa; Guntur district | "Amara" = immortal AP |
```

**Column design decision rules:**
- If a column contains the **primary UPSC-testable fact** about the Name → Both directions
- If a column contains **supplementary context** (dates, notes) → Forward only
- If a column contains **memory hooks, analogies, or "NOT X" traps** → Skip (or Forward only if the trap itself is testable)
- Comparison tables (Hinayana vs Mahayana): Name = the Feature being compared; other columns = the sect values → Forward only per column (Feature + Sect → Value)

Rules: Name column ALWAYS first. Bold Name entries. Cells < 5 words. No emojis inside cells. Most important columns placed early.

### Section 7: One-Liners (Rapid Recall)
```
  - **One-Liners** :- Rapid Recall
    - [Fact label] ;; [condensed answer]
    - [Name] ;; [key association]
    - [Date] = ;; [event]
```
Every one-liner **must** use `;;` (forward-only descriptor) to generate an actual flashcard. Plain `=` or `→` without a delimiter produces no card — it just appears as static text. No full sentences. Fragments and arrow notation OK inside the value half. Include all "frequently confused" items.

> **⚠️ Do NOT use `→ Back of card` suffix.** This is a RemNote UI label, not a syntax delimiter — it has no effect in imported files and appears as literal text. Use `;;` instead.

### Section 8: Quick Revision (Cloze Flashcards)
```
  - **Quick Revision** :- Cloze Cards
    - {{Buddha}}{({founder})} was born at {{Lumbini}}{({modern Nepal})} in {{563 BCE}}{({6th century})}.
    - Enlightenment at {{Bodh Gaya}}{({NOT Sarnath})} under {{Bodhi}}{({Peepal})} tree.
    - {{Article 17}}{({abolishes untouchability})} = only {{absolute}}{({no exceptions})} FR.
```
Every answer MUST use `{{}}`. Use `{{cloze}}{({hint})}` for confusable items.
Good hints: context, category, what it's NOT, year/era. Bad hints: near-synonyms.

### Section 9: Practice MCQs
```
  - **Practice MCQs** :- Self-Test
    - *~Prelims mode* ;- Cover options. Read stem only. Predict answer BEFORE seeing choices.
    - *~Mains mode* ;- Read topic heading only. Write 3 points from memory. Then check notes.
    - [Question text]? >>A)
      - Correct answer                    ← ALWAYS first
      - Wrong option 1
      - Wrong option 2
      - Wrong option 3
      - ✅ Explanation #[[Extra Card Detail]]   ← sibling of options; ECD powerup makes this show after answering
        - ✅ **Correct:** [why this answer is right]
        - ❌ **[Wrong option 1]:** [why it's wrong]
        - ❌ **[Wrong option 2]:** [why it's wrong]
        - ❌ **[Wrong option 3]:** [why it's wrong]
        - 🧠 **Trick:** [exam trap / memory hook]
```
Source priority: **Synthetic questions only**, modelled on `dimensions_tested` from the topic-map. Do NOT put real PYQs here — all verbatim PYQs belong exclusively in Section 12 (PYQ Archive). Mixing the two creates duplicate flashcards in RemNote.
Pattern variety: direct factual, "Which is NOT", "Common to both X and Y", match-the-following, statement-based (I, II, III).

**CRITICAL:** Section 9 is a *sampler* only (5–8 questions max). ALL remaining PYQs go into Section 12 (PYQ Archive) below.

> **Note on ECD placement:** The `✅ Explanation #[[Extra Card Detail]]` rem is always a **sibling of the answer options** (direct child of `>>A)`), NOT nested under the correct answer. Nesting it under the correct answer causes it to show only for that one option. The sibling placement + ECD powerup ensures it displays after any option is selected. This applies to both Section 9 and Section 12 MCQs.

### Section 10: 🚀 RAPID REVISION
```
  - **🚀 RAPID REVISION** :- Last-Minute Review
    - *~read time* ;- 5 minutes

    - **📋 FACTS TO MEMORIZE** :- Core Data
      - *~RemNote setup* ;- After import → click each column header → Flashcard Configuration → Enable For This Column | Value: Both directions (Item → Value AND Value → Item; core recall target) | Memory Hook: Skip (context only, not a recall target)
      | Item | Value | Memory Hook |
      |------|-------|-------------|
      | [fact] | [value] | [hook] |

    - **⚡ QUICK COMPARISONS** :- Key Differences
      - [Concept A] vs [Concept B]: [key distinguishing fact]

    - **⚠️ TRAP ALERTS** :- Don't Confuse
      - [Wrong assumption] ≠ [Correct fact]

    - **🔢 NUMBERS TO REMEMBER** :- Key Figures
      - [Number] = [what it counts]

    - **📝 MAINS KEYWORDS** :- For Essay Writing
      - [Topic]: "[keyword1]", "[keyword2]", "[keyword3]"

    - **🎯 LAST YEARS PYQ PATTERN** :- What UPSC Asks
      - [Pull from "Exam Patterns & Insights" in topic-map — real patterns only]
```
Maximum 1 page when printed. Tables for facts, bullets for comparisons.

### Section 11: Feynman Test + Connections + Mains Framework
```
  - **Feynman Test** :- Conceptual Check
    - *🧪 try first* ;- Close notes. Explain [Topic] to a smart friend who graduated in a different stream (arts/science/commerce) with no background in this subject. Use one analogy. If you can't — re-read Key Terms first.
    - *~check* ;- Can you explain: (1) What it is, (2) Why it matters, (3) One UPSC trap?

  - **Connections** :- Knowledge Web
    - *~builds on* ;; [[Previous Topic]] — [relationship]
    - *~leads on* ;; [[Next Topic]] — [relationship]
    - *~compare with* ;; [[Similar Topic]]
    - *~current affairs link* ;; [Post-2022 event only — if uncertain, write: "Verify: search [topic] + 2024/2025 for latest hook" rather than using stale news]

  - **Cross-Paper Transfer** :- Use This Topic Elsewhere
    - *~GS1 angle* ;- [History/Geography/Society/Culture dimension]
    - *~GS2 angle* ;- [Polity/Governance/Social Justice dimension]
    - *~GS3 angle* ;- [Economy/Environment/Security connection]
    - *~GS4 angle* ;- [Ethical dimension: value, thinker, civil service scenario]
    - *~Essay angle* ;- [Abstract philosophical/civilizational theme]
    - *~interdisciplinary hook* ;- [Single most powerful cross-paper insight]

  - **Mains Answer Framework** :- Essay Structure
    - *~marks/word limit* ;- [10m=150w | 15m=250w | 20m=350w]
    - *~introduction angle* ;- [~30–40w: context + thesis]
    - *~body points* ;- [4–6 points covering all dimensions_tested]
    - *~conclusion angle* ;- [~25–30w: forward-looking / constitutional angle]
    - *~quote/committee* ;- [Relevant quote or committee for opening/closing]
```

Word budget:
| Marks | Total | Intro | Body | Conclusion |
|-------|-------|-------|------|------------|
| 10m | ~150w | 30w | 95w | 25w |
| 15m | ~250w | 40w | 175w | 35w |
| 20m | ~350w | 50w | 260w | 40w |

### Section 12: 📚 PYQ ARCHIVE — Complete Question Bank

**This section is MANDATORY. No exceptions.**

#### PYQ Anchor System — How Inline Linking Works

Every PYQ in Section 12 is wrapped in a **named parent Rem (the anchor)** so that concepts in Sections 4 and 5 can link directly to it with `[[PYQ:year-slug]]`. Clicking the link in RemNote navigates straight to that question.

---

#### ⚠️ CRITICAL: TWO STRUCTURAL RULES — BOTH AFFECT RENDERING

**RULE A — Anchor is the OUTER PARENT, not a child:**

The `**PYQ:[YEAR]-[slug]** :-` Rem **wraps** the MCQ node as its parent container. The MCQ question is a child *inside* the anchor, not the anchor is a child inside the MCQ.

```
CORRECT ✅
  - **PYQ:2020-shramana** :-                    ← anchor = OUTER PARENT (no flashcard, just a named node)
    - [2020] Question text >>A)                 ← MCQ nested INSIDE the anchor; >>A) = standard forward MCQ
      - 1 and 3 only                            ← correct answer (ALWAYS first child)
      - 1 and 2 only
      - 2 and 3 only
      - 1, 2 and 3
      - ✅ Explanation #[[Extra Card Detail]]   ← sibling of options; children hold actual explanation

WRONG ❌
  - [2020] Question text >>A)
    - **PYQ:2020-shramana** :-    ← anchor as a child INSIDE the MCQ — breaks RemNote linking
    - 1 and 3 only
    ...
```

Why: `[[PYQ:2020-shramana]]` links to the Rem named "PYQ:2020-shramana". That Rem must exist as a top-level node with the MCQ as its child. If it's a child of the MCQ, clicking the link navigates into the MCQ options, not to the question.

---

**RULE B — Extra Card Detail is a sibling of the answer options, with explanation as its children:**

The `✅ Explanation #[[Extra Card Detail]]` rem sits at the **same indentation level as the answer options** (direct child of `>>A)`). RemNote's ECD powerup causes it to display after the card is answered rather than as a selectable choice. Detailed explanation lines go as **children of this ECD rem**.

```
CORRECT ✅
  - **PYQ:2020-shramana** :-
    - [2020] Question text >>A)
      - 1 and 3 only                         ← first child = correct answer (ALWAYS first)
      - 1 and 2 only
      - 2 and 3 only
      - 1 only
      - ✅ Explanation #[[Extra Card Detail]]  ← sibling of options; ECD powerup handles display
        - ✅ **Correct (1 and 3):** [why correct]
        - ❌ **1 and 2:** [why wrong]
        - ❌ **2 and 3:** [why wrong]
        - ⚠️ **Trap:** [exam trap]
        - 🧠 **Hook:** [memory hook]

WRONG ❌
  - [2020] Question text >>A)
    - 1 and 3 only
      - ✅ Explanation nested under correct answer   ← puts explanation inside one option only
```

---

**Complete correct template:**

```
  - **📚 PYQ ARCHIVE** :- Complete Past Year Questions
    - *~how to use* ;- Attempt BEFORE checking answers. Cover the options. Predict. Only then reveal.
    - *~why this exists* ;- UPSC repeats patterns every 2–4 years. Seeing every real question is non-negotiable for full coverage.

    - **Prelims PYQs** :- All Prelims Questions (Year-wise, Newest First)

      - **PYQ:[YEAR]-[slug]** :-                              ← OUTER PARENT anchor; linkable via [[PYQ:year-slug]]
        - [EXACT question stem verbatim, with year] >>A)      ← MCQ nested INSIDE anchor; >>A) = standard forward MCQ
          - [Correct answer — ALWAYS FIRST]                   ← first child = correct answer
          - [Wrong option A]
          - [Wrong option B]
          - [Wrong option C]
          - ✅ Explanation #[[Extra Card Detail]]             ← sibling of options; ECD powerup handles display
            - ✅ **Correct ([answer]):** [why this is right]
            - ❌ **[Wrong A]:** [why wrong]
            - ❌ **[Wrong B]:** [why wrong]
            - ❌ **[Wrong C]:** [why wrong]
            - ⚠️ **Trap:** [what UPSC is testing / common confusion]
            - 🧠 **Hook:** [memory device]

    - **Mains PYQs** :- All Mains Questions (Year-wise, Newest First)

      - **PYQ:[YEAR]-[slug]** :-                              ← OUTER PARENT anchor
        - [EXACT question verbatim, with year and marks]      ← Mains question nested inside
          - *~answer approach* ;-
            >>> Introduction (~30w): [angle + thesis]
                Body point 1: [key dimension]
                Body point 2: [key dimension]
                Body point 3: [key dimension with case law / data]
                Conclusion (~25w): [forward-looking / constitutional angle]
          - *~keywords* ;- [3–5 Mains keywords essential for this answer]
          - *~common mistake* ;- [What most answers miss — the distinguishing insight]
```

**Slug naming rules:**
- Format: `PYQ:[YEAR]-[2-3-word-slug]` — all caps PYQ, year, then lowercase slug
- Slug names the **concept being tested**: `PYQ:2020-shramana`, `PYQ:2024-epithets`, `PYQ:2013-nirvana`
- Must be unique per file. If two questions in same year test similar concept: `PYQ:2020-shramana`, `PYQ:2020-upasaka`

**Inline reference format in Sections 4/5:** Replace plain-text PYQ mentions with `[[PYQ:YEAR-slug]]`
```
Old: "2020 PYQ trap: confusing Shramana with a priest"
New: "[[PYQ:2020-shramana]] trap: confusing Shramana with a priest"

Old: "UPSC tested this in 2013 — correct answer was extinction of flame"
New: "[[PYQ:2013-nirvana]] — correct answer was extinction of flame"
```

**When to add inline links (Sections 4/5):**
- Every `⚠️ exam trap` descriptor that mentions a year → link to that PYQ
- Every `📌 beginner note` that says "UPSC tested" or "PYQ" → link to that PYQ
- Every `;;` descriptor that cites a year as evidence → link to that PYQ
- Do NOT add `[[]]` links inside Section 12 itself (the anchors are the destination)

**MANDATORY RULES for Section 12 — READ CAREFULLY:**

1. **Include EVERY Prelims PYQ from the topic-map.** Do not skip any — not even "easy" or "obvious" ones. UPSC repeats patterns.
2. **Include EVERY Mains PYQ from the topic-map.** Each gets a full answer framework, not just a bullet list.
3. **Copy question stems VERBATIM** from the topic-map. Do NOT paraphrase, summarize, or rewrite.
4. **Anchor wraps MCQ as outer parent.** `**PYQ:[YEAR]-[slug]** :-` is always the outer container; the `>>A)` MCQ node is its child. Never reverse this. Never use `;;>A)` — use `>>A)` for all MCQs.
5. **Correct answer MUST be first child** of the `>>A)` MCQ node. RemNote shuffles options at practice time, but on import the first child is set as correct.
6. **ECD explanation is a sibling of the answer options.** Place `✅ Explanation #[[Extra Card Detail]]` as a direct child of the `>>A)` node (same level as the options). Add detailed explanation lines as children of this ECD rem — one bullet per option explanation, plus trap and hook. Never nest ECD under an individual answer option.
7. **For statement-based questions:** copy all numbered statements inside the question node text itself (not as separate children), then list options as children.
8. **For "How many correct?" questions (post-2022 pattern):** same structure; options are "Only one", "Only two", "All three", "None" — correct answer first.
9. **Sequence:** newest year first (2024 → 2023 → ... → oldest).
10. **If topic has 0 Mains PYQs:** write `- *~Mains PYQs* ;- None indexed yet — check topic-map after next UPSC cycle`.
11. **Do not merge questions.** Each PYQ gets its own anchor + MCQ structure, even if questions look similar.

---
