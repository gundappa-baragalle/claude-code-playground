## The 12 Sections — Templates

### Table of Contents

| Section | Name | Line (approx.) |
|---------|------|----------------|
| 1 | Header & Metadata | §Section 1 |
| 2 | Why Study + Before You Read | §Section 2 |
| 3 | Big Picture (Visual Map) | §Section 3 |
| 4 | Prerequisite Concepts & Key Terms | §Section 4 |
| 5 | Content — Main Body + Classification Landscape | §Section 5 |
| 6 | Flashcard Tables | §Section 6 |
| 7 | One-Liners (Rapid Recall) | §Section 7 |
| 8 | Quick Revision (Cloze Flashcards) | §Section 8 |
| 9 | Practice MCQs | §Section 9 |
| 10 | 🚀 RAPID REVISION | §Section 10 |
| 11 | Feynman Test + Connections + Mains Framework | §Section 11 |
| 12 | 📚 PYQ ARCHIVE | §Section 12 |

Search `### Section N:` to jump directly to any section.

---

### Section 1: Header & Metadata
```
- **[Topic]** :- UPSC [Subject]
  - *~version* ;- v[date] — refresh if >6 months old
  - *~source* ;- [Standard books with chapter numbers]
  - *~PYQ frequency* ;- [Step 2: "X total (Prelims: Y, Mains: Z), YYYY–YYYY"]
  - *~Prelims weightage* ;- [Step 2: real prelims_count from topic-map; last asked YYYY]
  - *~Mains relevance* ;- [Which GS paper, what themes]
  - *~revision priority* ;- [Step 2: HIGH / MEDIUM / LOW — see thresholds below]
  - *~beginner-audit* ;- [Added after Step 8 — write: PASSED: no undefined terms found | or GAPS FOUND: list each gap and the line where it was fixed]
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
- **Heavily classificatory topics** (inflation, earthquakes, soils, rocks, cells, ecosystems — any topic where classification IS the primary dimension): add a **classification matrix branch** to the ASCII tree showing each basis as a branch and its types as leaves. This gives the student a spatial overview of the entire classification landscape before they read Section 5.

```
      TOPIC NAME
      │
      ├── [Main conceptual branches...]
      │
      └── CLASSIFICATION MATRIX
              ├── By [Basis 1]: Type A | Type B | Type C
              ├── By [Basis 2]: Type X | Type Y
              └── By [Basis 3]: Type P | Type Q | Type R
              ⚠️ Cross-basis traps: [Type A] ≠ [Type X] (different axes)
```

This matrix branch in Section 3 is a spatial advance organiser (Ausubel, 1960) — it shows the full shape of the classification landscape before the student encounters any individual type. Do not put definitions here; put only the basis names and type names.

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

**The classification-type prerequisite rule:** If Section 5 will contain a Classification Landscape with types (e.g., Demand-Pull Inflation, Cost-Push Inflation), every classification TYPE must be defined in Section 4 first — before Section 5 uses it. The type names are not self-explanatory to a beginner. A student reading "Demand-Pull" in Section 5 must already know what "aggregate demand" means; a student reading "Orographic rainfall" must already know what "orography" means. Apply this chain:
1. List every type name that will appear in every Classification Landscape in Section 5
2. For each type, identify which component terms a beginner would not know
3. Add those component terms to Section 4, in prerequisite order, before the main concept definition

Example: for Inflation Classification Landscape → Section 4 must define **Aggregate Demand**, **Aggregate Supply**, **Cost of Production**, **Supply Shock**, **Structural rigidity** — before "Demand-Pull" or "Cost-Push" is named in Section 5.

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
      - *~why it arose* ;; [Root cause — what conditions produce this concept? This must use only already-explained concepts]
      - *~significance* ;; [Why does this matter? What does it cause or prevent? Link to real India/UPSC context]
      - *~mechanism* ;- [Step-by-step: how does this work? Use arrows: A → B → C. Use math where it adds precision]
      - *💭 self-explain* ;- [Ask the student to reason through something BEFORE revealing the answer — placed immediately before the key insight, never after]
      - *~formula / equation* ;; [If a mathematical relationship exists — always include it]
      - *🧠 analogy* ;- [One concrete, vivid comparison that makes the abstract tangible]
      - *⚡ vs [Most Confused Alternative]* ;- [Side-by-side contrast. Use a mini table if 3+ dimensions differ]
      - *⚠️ exam trap* ;- [Specific UPSC trap from PYQ data: state the wrong thinking → explain why it's wrong → give the correct logic]
      - *~does NOT apply when* ;- [Boundary condition: when is this concept NOT relevant or NOT the right frame?]
      - *~India context* ;; [Specific Indian example, data point, or institution — only use `;;` when confident the example is accurate. Prefer post-2022 examples.]
        ← If uncertain whether a post-2022 development occurred: write `*~India context* ;- Unverified — search "[topic] India 2024/2025" and replace with confirmed example` using `;-` (disabled). NEVER write a placeholder inside a `;;` flashcard — it generates a card where the "answer" is the placeholder text.
      - *🔨 your example* ;- [Ask the student to generate their own example — forces active processing]
```

**What to include / exclude:**
- Include EVERYTHING that a PYQ has tested about this concept — even seemingly trivial details
- Include every prerequisite relationship ("this works because X, which we established above")
- Include mathematical representations whenever they exist
- Exclude biographical trivia, excessive historical narrative, and content with zero PYQ relevance
- Never compress a concept to save space — if it needs 10 lines to be fully clear, write 10 lines

#### Classification Landscape — mandatory when a concept has types

**When to apply:** Any concept in Section 5 that has types, kinds, or categories — signal phrases: "types of", "classified as", "kinds of", "on the basis of". Applies across ALL subjects: inflation types, earthquake types, cell types, soil types, cloud types, ecosystem types, rights categories, writ types, etc.

**Why a dedicated block:** Classifications have three distinct recall levels that UPSC tests independently:
- **Level 1 — Within-basis:** "What is stagflation?" → Type → definition
- **Level 2 — Cross-basis attribution:** "Stagflation is classified by which basis?" → Type → its basis
- **Level 3 — Enumeration:** "Name all types of inflation by speed" → Basis → full ordered list

Flat bullet lists address only Level 1. The Classification Landscape addresses all three using the right RemNote syntax for each.

**Position:** Place the Classification Landscape as the last sub-block inside the concept node — after explaining the concept itself, before moving to the next concept in Section 5.

**Full template:**

```
    - **[Concept] — Classification Landscape** :- How [Concept] Is Classified
      - *~classification count* ;; [N] independent bases — each produces a different set of types
      - *~UPSC note* ;- [Which bases/types have been tested — from dimensions_tested in topic-map. Also flag untested bases as "not yet asked" — these are Section 9 targets.]
        ← `;-` not `;;`: this descriptor bundles multiple planning facts (tested bases, untested bases, PYQ years) into one note — it is not atomic enough for a clean flashcard. The individual atomic facts (e.g. "By Cause tested in 2019") belong in Section 7 one-liners or the `*~basis* ;;` descriptors on each type.

      - **By [Basis 1 name]: [The criterion — what property is being used to classify]** :- [N] types
        - *~all types* ;;>1.                     ← LIST-ANSWER flashcard: "All types by [Basis 1]?" → must recall ordered list
          - [Type A]
          - [Type B]
          - [Type C]
        - *⚡ [Basis 1] types — side-by-side* ;-          ← `;-` not `;;` — understanding aid, NOT a flashcard
          | Type | Defining feature | Trigger / Example | UPSC trap |
          |------|-----------------|-------------------|-----------|
          | **[Type A]** | [≤5 words] | [India example] | [confusion] |
          | **[Type B]** | [≤5 words] | [India example] | [confusion] |
          | **[Type C]** | [≤5 words] | [India example] | [confusion] |
        - **[Type A]** :: [One-sentence definition — what makes it THIS type and not another]
          - *~basis* ;; By [Basis 1]: [criterion]     ← cross-basis flashcard (Level 2): "Type A → which basis?"
          - *~trigger condition* ;- [What conditions produce/cause this type — use `;-` not `;;`; only upgrade to `;;` if topic-map shows UPSC has directly tested the trigger mechanism]
          - *~India example* ;; [Specific Indian instance + year if applicable]
          - *⚠️ exam trap* ;- [Most likely confusion: with which other type, and why the brain picks wrong]
        - **[Type B]** :: [definition]
          - *~basis* ;; By [Basis 1]: [criterion]
          - *~trigger condition* ;- [...]
          - *~India example* ;; [...]
          - *⚠️ exam trap* ;- [...]

      - **By [Basis 2 name]: [The criterion]** :- [N] types
        - *~all types* ;;>1.
          - [Type X]
          - [Type Y]
        - *⚡ [Basis 2] types — side-by-side* ;-
          | Type | Defining feature | Trigger / Example | UPSC trap |
          |------|-----------------|-------------------|-----------|
          | **[Type X]** | ... | ... | ... |
          | **[Type Y]** | ... | ... | ... |
        - **[Type X]** :: [definition]
          - *~basis* ;; By [Basis 2]: [criterion]
          - *~trigger condition* ;- [...]
          - *~India example* ;; [...]
          - *⚠️ exam trap* ;- [...]

      - **⚠️ Cross-Basis Trap Zone** :- Types From Different Bases That UPSC Conflates
        - *~[Type A] vs [Type X]* ;- Different bases: [Type A] = by [Basis 1] ([criterion 1]); [Type X] = by [Basis 2] ([criterion 2]). [One-line distinguishing logic — why they feel similar, what separates them]
        - *~[further cross-basis pairs as needed]* ;- [...]

      - **🔢 Enumeration Master** :- Full Count by Basis
        - *~[Basis 1] count* ;; [N] types: [Type A] | [Type B] | [Type C]
        - *~[Basis 2] count* ;; [N] types: [Type X] | [Type Y]
```

**Worked example — Types of Inflation:**

```
    - **Inflation — Classification Landscape** :- How Inflation Is Classified
      - *~classification count* ;; 4 independent bases: cause, speed, scope, expectation
      - *~UPSC note* ;- Tested: By Cause (demand-pull, cost-push — PYQs 2012–2019); By Speed (hyperinflation 2017). Not yet asked: By Scope, By Expectation — high-probability Section 9 targets.

      - **By Cause: What pushes prices up** :- 3 types
        - *~all types* ;;>1.
          - Demand-Pull
          - Cost-Push
          - Structural
        - *⚡ By-Cause types — side-by-side* ;-
          | Type | Defining feature | India trigger | UPSC trap |
          |------|-----------------|---------------|-----------|
          | **Demand-Pull** | Demand > Supply | Fiscal stimulus; rising incomes | Confused with monetary inflation |
          | **Cost-Push** | Production costs rise | Oil shock; MSP hike; wage rise | Confused with demand-pull |
          | **Structural** | Supply-chain bottlenecks | Agricultural storage gaps | Confused with cost-push |
        - **Demand-Pull Inflation** :: Prices rise because aggregate demand exceeds aggregate supply
          - *~basis* ;; By Cause: demand exceeds supply
          - *~trigger condition* ;- Fiscal stimulus / rising incomes / loose monetary policy → AD ↑ > AS
          - *~India example* ;; Post-COVID stimulus 2021 → demand surge while supply constrained
          - *⚠️ exam trap* ;- "Both demand-pull and monetary inflation involve too much money" — true, but M↑ causes demand-pull; demand-pull is the result. They are measured differently on the AD-AS graph.
        - **Cost-Push Inflation** :: Prices rise because production costs increase, shifting supply left
          - *~basis* ;; By Cause: supply-side cost increase
          - *~trigger condition* ;- Oil shock / MSP hike / wage rise → AS ↓ → prices ↑
          - *~India example* ;; 2022 post-Ukraine oil shock → fuel price rise → cascading cost-push across sectors
          - *⚠️ exam trap* ;- Both demand-pull and cost-push raise prices — key: demand-pull = AD shifts right; cost-push = AS shifts left. Growth direction differs: demand-pull = output rises; cost-push = output falls (→ stagflation risk).

      - **By Speed: How fast prices rise** :- 4 types
        - *~all types* ;;>1.
          - Creeping (0–3%)
          - Walking (3–10%)
          - Galloping (10–50%)
          - Hyperinflation (>50%/month)
        - *⚡ By-Speed types — side-by-side* ;-
          | Type | Rate | Consequence | Canonical example |
          |------|------|-------------|-------------------|
          | **Creeping** | 0–3% | Tolerable; mild growth signal | Normal developed economy |
          | **Walking** | 3–10% | Warning; erodes real wages | India average 2010s |
          | **Galloping** | 10–50% | Dangerous; savings eroded | Venezuela 2010s |
          | **Hyperinflation** | >50%/month | Currency collapses | Zimbabwe 2008; Weimar 1923 |
        - **Hyperinflation** :: Inflation exceeding 50% per month — currency loses value faster than it can be spent
          - *~basis* ;; By Speed: rate >50%/month
          - *~trigger condition* ;- Govt prints money uncontrollably to finance deficit → M↑↑ → P↑↑
          - *~India example* ;; Not in India — Zimbabwe 2008 (canonical); Weimar Germany 1923
          - *⚠️ exam trap* ;- "Hyperinflation = very high inflation" is vague — UPSC expects the 50%/month threshold. Galloping (10–50%) ≠ hyperinflation.

      - **⚠️ Cross-Basis Trap Zone** :- Types From Different Bases That UPSC Conflates
        - *~Stagflation vs Cost-Push* ;- Different bases: Stagflation = by Growth outcome (inflation + stagnation together); Cost-Push = by Cause (supply-side cost rise). Cost-push CAN trigger stagflation but they are not in the same classification axis.
        - *~Hyperinflation vs Galloping* ;- Same basis (speed) but different thresholds — Galloping = 10–50%; Hyperinflation = >50%/month. Galloping is dangerous; hyperinflation is catastrophic currency collapse.
        - *~Disinflation vs Deflation* ;- Not even the same phenomenon: Disinflation = inflation rate is falling (still positive); Deflation = price level itself is falling (negative inflation). Disinflation ≠ prices falling.

      - **🔢 Enumeration Master** :- Full Count by Basis
        - *~By Cause count* ;; 3 types: Demand-Pull | Cost-Push | Structural
        - *~By Speed count* ;; 4 types: Creeping (0–3%) | Walking (3–10%) | Galloping (10–50%) | Hyperinflation (>50%/month)
        - *~By Scope count* ;; 2 types: Comprehensive (all goods) | Sporadic/Sectoral (specific sectors)
        - *~By Expectation count* ;; 2 types: Anticipated | Unanticipated
```

**Single-basis variant — use when the concept has exactly 1 basis of classification:**

Many UPSC topics have only one axis of classification with multiple types — clouds (by altitude/form), rocks (by origin), constitutional amendments (by procedure), soil types (by composition). For these, the multi-basis machinery (Cross-Basis Trap Zone, Enumeration Master with multiple counts) is either empty or redundant. Use this stripped-down variant instead:

```
    - **[Concept] — Classification Landscape** :- How [Concept] Is Classified
      - *~classification count* ;; 1 basis: [basis name]
      - *~UPSC note* ;- [Which types have been tested; which are untested — Section 9 targets]

      - **By [Basis]: [The criterion]** :- [N] types
        - *~all types* ;;>1.
          - [Type A]
          - [Type B]
          - [Type C]
        - *⚡ [Basis] types — side-by-side* ;-
          | Type | Defining feature | Example | UPSC trap |
          |------|-----------------|---------|-----------|
          | **[Type A]** | [≤5 words] | [...] | [...] |
          | **[Type B]** | [≤5 words] | [...] | [...] |
        - **[Type A]** :: [One-sentence definition]
          - *~basis* ;; By [Basis]: [criterion]
          - *~trigger condition* ;- [What produces/causes this type]
          - *~India example* ;; [...]
          - *⚠️ exam trap* ;- [Most common confusion — often within-basis: Type A confused with Type B]
        - **[Type B]** :: [...]
          - *~basis* ;; By [Basis]: [criterion]
          - *~trigger condition* ;- [...]
          - *~India example* ;; [...]
          - *⚠️ exam trap* ;- [...]

      - **⚠️ Within-Basis Trap Zone** :- Most Confused Pair
        - *~[Type A] vs [Type B]* ;- [What makes them feel similar; what actually separates them]

      - **🔢 Enumeration** :- Full Count
        - *~[Basis] count* ;; [N] types: [Type A] | [Type B] | [Type C]
```

**When to use single-basis vs multi-basis variant:**

| Condition | Use |
|-----------|-----|
| 1 axis of classification | Single-basis variant (no Cross-Basis Trap Zone) |
| 2+ independent axes | Multi-basis full template (with Cross-Basis Trap Zone) |
| Unclear how many axes | Start with the axes you know; add more as Section 5 content demands |

The within-basis trap zone in the single-basis variant replaces the cross-basis trap zone — it still forces discrimination, just between types within the same axis.

**Six design rules — enforce without exception:**

1. **Every basis gets `;;>1.` (list-answer descriptor).** This is the enumeration flashcard — "Name all types by [basis]?" with children as the ordered list. This is the only RemNote syntax that forces recall of a complete set in order.

2. **Every type gets `*~basis* ;;`.** This creates the cross-basis attribution flashcard. Without it, students can define all types but cannot answer "stagflation belongs to which classification axis?"

3. **`*~trigger condition*` always uses `;-` by default.** Trigger conditions are mechanistic/causal context — they aid understanding but are rarely tested directly. Only upgrade to `;;` when the topic-map's `dimensions_tested` shows UPSC has explicitly tested the trigger mechanism for that specific type. Defaulting to `;;` floods the SRS queue with low-value cards.

4. **The inline mini-table uses `;-` not `;;`.** It is an understanding scaffold — the flashcards come from `::` on each type and `;;>1.` on each basis. Never make the table itself a flashcard target.

5. **Cross-Basis Trap Zone is mandatory when 2+ bases exist.** UPSC's hardest classification questions force cross-basis discrimination. Naming the confusion explicitly is more powerful than hoping students notice it.

6. **Do NOT create a Section 6 table for the classification landscape.** The inline mini-table in Section 5 is sufficient. Section 6 tables are for entity-to-entity comparison (WPI vs CPI), not for type landscapes which require the full `::` / `;;>1.` / `*~basis*` structure.

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

#### Full Template

```
  - **[Title] Table** :- Flashcard Table
    - *~RemNote setup* ;- After import → click each column header → Flashcard Configuration → Enable For This Column | [Column 2]: Both directions | [Column 3]: Forward only | [Column 4]: Skip
    - *~Table* ;-
    | Name | [Column 2] | [Column 3] | [Column 4] |
    |------|-----------|-----------|-----------|
    | **Row 1** | cell | cell | cell |
    | **Row 2** | cell | cell | cell |
```

**Worked example — Buddhist Sites Table:**

```
  - **Key Buddhist Sites Table** :- Flashcard Table
    - *~RemNote setup* ;- After import → click each column header → Flashcard Configuration → Enable For This Column | Location: Both directions (Site → Location AND Location → Site; PYQ trap area) | Known For: Forward only | Memory Hook: Skip
    - *~Table* ;-
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

**Classification one-liners — mandatory when topic has Classification Landscapes:**

Every Classification Landscape must contribute all three categories of one-liners to Section 7. These are the atomic flashcard form of the Section 5 classification content — the student hits them in SRS daily, long after the full Section 5 detail has faded. They are distinct from the `;;>1.` enumeration flashcard in Section 5 (which tests the full ordered list) — they test atomic facts that each deserve their own SRS card. Do not skip any category.

**Category A — Cross-basis attribution** (Type → its basis — directly maps to Level 2 recall):
```
    - Demand-Pull inflation ;; By Cause: demand exceeds supply
    - Stagflation basis ;; By Growth outcome — NOT by cause
    - Hyperinflation basis ;; By Speed (>50%/month) — NOT by cause
    - Structural inflation basis ;; By Cause: supply-chain bottleneck
```

**Category B — Threshold / count facts** (the crisp numbers and counts UPSC tests directly):
```
    - Hyperinflation threshold ;; >50%/month
    - Galloping inflation range ;; 10–50%
    - Inflation classification bases ;; 4 (cause, speed, scope, expectation)
    - Creeping inflation range ;; 0–3% (tolerable)
```

**Category C — Cross-basis discrimination** (the "NOT" one-liners that nail the trap):
```
    - Disinflation ≠ Deflation ;; Disinflation = rate falling (still +ve); Deflation = price level falling
    - Stagflation ≠ Cost-Push ;; Stagflation = growth outcome axis; Cost-Push = cause axis
    - Galloping ≠ Hyperinflation ;; Galloping = 10–50%; Hyper = >50%/month
```

**Rule:** All three categories use `;;` (forward flashcard — UPSC tests these directly). Category A and B generate atomic recall cards. Category C uses the "≠" format to force the student to process both sides of the confusion at SRS time. Do not use `;-` for any category.

### Section 8: Quick Revision (Cloze Flashcards)
```
  - **Quick Revision** :- Cloze Cards
    - {{Buddha}}{({founder})} was born at {{Lumbini}}{({modern Nepal})} in {{563 BCE}}{({6th century})}.
    - Enlightenment at {{Bodh Gaya}}{({NOT Sarnath})} under {{Bodhi}}{({Peepal})} tree.
    - {{Article 17}}{({abolishes untouchability})} = only {{absolute}}{({no exceptions})} FR.
```
Every answer MUST use `{{}}`. Use `{{cloze}}{({hint})}` for confusable items.
Good hints: context, category, what it's NOT, year/era. Bad hints: near-synonyms.

**Classification Enumeration sub-block — add when the topic has Classification Landscapes:**

Every Classification Landscape from Section 5 must produce enumeration cloze cards in Section 8. These force recall of the complete set per basis — the exact skill UPSC's "how many of the following" questions demand.

**Pattern:** One sentence per basis. Cloze each type name. Use the count as a hint on the last item.

```
  - **Classification Enumeration** :- Recall Full Lists by Basis
    - Types of [concept] by [Basis 1]: {{[Type A]}}{({1st})}, {{[Type B]}}{({2nd})}, {{[Type C]}}{({3rd — [N] total})}.
    - Types of [concept] by [Basis 2]: {{[Type X]}}{({[hint])}}, {{[Type Y]}}{({last of [N])}}.
    - [Basis 1] that produced [specific India example] ;; [Type name] — because [one-line reason]
```

**Worked example — Inflation enumeration clozes:**

```
  - **Classification Enumeration** :- Recall Full Lists by Basis
    - Types of inflation by cause: {{Demand-Pull}}{({excess demand})}, {{Cost-Push}}{({supply cost rise})}, {{Structural}}{({bottleneck — 3 total})}.
    - Types of inflation by speed: {{Creeping}}{({0–3%})}, {{Walking}}{({3–10%})}, {{Galloping}}{({10–50%})}, {{Hyperinflation}}{({>50%/month — 4 total})}.
    - 2022 post-Ukraine fuel price rise in India ;; Cost-Push — because input costs rose, not because demand increased
    - Inflation rate falling but still positive ;; {{Disinflation}}{({NOT deflation})} — price level is not falling, only the rate is
```

**Rules for Classification Enumeration clozes:**
- One sentence per basis — never mix two bases in one sentence
- Always include the total count as a hint on the last cloze in each sentence
- Add at least one "identify the type from a description" cloze per basis (the hardest Level 2 recall)
- For cross-basis traps, add a discrimination cloze: "{{Disinflation}}{({NOT deflation})} = rate falling"

### Section 9: Practice MCQs

Section 9 contains **5–8 predictive questions** — purpose-built MCQs designed to anticipate what UPSC is *likely to ask next*, based on rigorous analysis of the PYQ record. These are not random practice questions; each one is a deliberate prediction grounded in gap analysis, pattern logic, and examiner behaviour.

**Do NOT put real PYQs here.** All verbatim past questions belong exclusively in Section 12 (PYQ Archive). Mixing the two creates duplicate flashcards in RemNote.

#### Pre-writing: Predictive Analysis (mandatory before writing a single question)

Before writing any MCQ, open the topic-map file and extract the following signals:

**Signal 1 — Gap years:** Which years in the `year_range` have NO question? A topic asked in 2014, 2016, 2019, 2022 has gaps in 2015, 2017–18, 2020–21, 2023. UPSC frequently returns to a topic after a 2–4 year gap. The next exam falls into a gap → elevated probability.

**Signal 2 — Untested dimensions:** `dimensions_tested` lists what has already been asked. Everything in `dimensions_tested` that has NOT been asked yet is a candidate. If UPSC has tested "location" and "known for" but never "who built it" — the builder dimension is overdue.

**Signal 3 — Partial coverage:** Some dimensions have been tested only once. A dimension asked in 2013 and never since has 10+ years of accumulated probability. Treat single-test dimensions as high priority.

**Signal 4 — Post-syllabus events:** Any development after the last PYQ year (`last_asked`) that connects to the topic is a new testable angle UPSC has not yet exploited. For example, if a site got UNESCO status after the last question, that status is now a live target. Check the `## Cross-Paper Transfer` and `contemporary_relevance` fields in the topic-map first — these index known post-`last_asked` developments. If a development is not in the topic-map and you are not certain it occurred, write `*~unverified development* ;- search [topic] + 2024/2025 to confirm before including` using `;-` (disabled). Never state unverified events as fact. Never use cloze syntax `{{...}}` for unverified content — it creates a broken flashcard with placeholder text as the hidden answer.

**Signal 5 — Recurring question patterns:** What *type* of question does UPSC prefer for this topic? Some topics always get statement-based (I, II, III) questions; others always get direct factual or "Which is NOT" questions. Match the predicted question to the established pattern type.

**Signal 6 — Examiner trap patterns:** From `exam_traps` or `dimensions_tested`, identify which confusions UPSC has already exploited. New questions often introduce *new* traps on the same topic — a confusion adjacent to the ones already used.

Write a one-line prediction rationale for each question before drafting it:
```
Prediction rationale: Dimension "X" untested since 2014 (10-year gap); statement-based pattern; trap = confusing X with Y
```
This rationale goes into the `*~prediction basis*` descriptor on each question (see template below).

#### Pattern variety — match to topic-map pattern history

Use the pattern types UPSC has already used for this topic (from `dimensions_tested` / question history), then extend to adjacent untested patterns:

- **Statement-based (I, II, III):** Most common for multi-faceted topics (Buddhism, Polity, Economy). Use when testing whether multiple claims about a concept are correct.
- **"Which is NOT correct":** Use when the trap is a plausible-sounding false claim — forces the student to verify every option.
- **"Common to both X and Y":** Use for comparison topics where UPSC tests overlap knowledge.
- **Direct factual:** Use for dimensions with a single crisp answer (year, location, person, body).
- **Match-the-following / Pairs:** Use when UPSC has tested association between two sets.
- **"How many of the following are correct?" (post-2022 pattern):** Use for topics with 3+ discrete facts — options are "Only one", "Only two", "All three", "None".
- **Cross-basis classification (mandatory when topic has Classification Landscapes):** When the topic has a Classification Landscape in Section 5, at least one Section 9 question MUST be a cross-basis discrimination question. See rule below.

**Cross-basis classification MCQ rule — mandatory trigger:**

If the topic has a Classification Landscape in Section 5, include at least one MCQ that forces the student to discriminate between types from different bases. This is the hardest classification recall level and the one most likely to appear in the next exam cycle (UPSC has shifted toward cross-basis questions post-2020).

**Three valid cross-basis question frames:**

Frame A — Attribution: "Which of the following types of [concept] is classified by [Basis X]?"
Frame B — Basis identification: "[Type] is an example of inflation classified on the basis of ___?"
Frame C — Pair discrimination: "[Type A] and [Type B] are both types of [concept]. Which statement correctly distinguishes them?"

The `📊 Prediction basis` bullet for cross-basis questions should always note: "Cross-basis discrimination — untested dimension; UPSC post-2020 pattern shift toward basis-attribution questions."

#### Template

```
  - **Practice MCQs** :- Self-Test
    - *~Prelims mode* ;- Cover options. Read stem only. Predict answer BEFORE seeing choices.
    - *~Mains mode* ;- Read topic heading only. Write 3 points from memory. Then check notes.
    - *~prediction basis* ;- Questions generated by gap analysis: untested dimensions from topic-map, gap years in PYQ record, post-[last_asked year] developments, and recurring examiner trap patterns.

    - [Question text based on untested/gap dimension]? >>A)
      - Correct answer                              ← ALWAYS first child
      - Wrong option 1
      - Wrong option 2
      - Wrong option 3
      - ✅ Explanation #[[Extra Card Detail]]        ← sibling of options; ECD powerup shows after answering
        - ✅ **Correct:** [why this is right]
        - ❌ **[Wrong option 1]:** [why wrong]
        - ❌ **[Wrong option 2]:** [why wrong]
        - ❌ **[Wrong option 3]:** [why wrong]
        - 🧠 **Trick:** [exam trap / memory hook]
        - 📊 **Prediction basis:** [one line: which signal made this a target — gap year / untested dimension / post-last_asked development / recurring pattern]
```

#### What makes a good predictive MCQ

**Target untested dimensions first.** If UPSC has asked about a Buddhist site's location and significance but never its architectural style, write a question on architectural style.

**Target gap years.** If the topic was last asked in 2021 and the exam is in 2025, that's a 4-year gap — prime territory. Design the question to test the angle UPSC hasn't hit yet.

**Use the established trap structure.** UPSC doesn't randomly select wrong options — distractors are always plausible adjacent facts. Model distractors on the same logic as existing PYQ distractors: same category, similar sound, geographically adjacent, historically proximate.

**Do not repeat what Section 12 already covers.** Every real PYQ is in Section 12. Section 9 tests the *next* questions, not the past ones.

**Difficulty calibration:** Aim for questions a prepared student would get 50–70% of the time — not trivially easy, not impossibly obscure. The sweet spot is a question that is answerable if the student has studied the notes carefully, but trips up anyone relying on surface memory.

> **Note on ECD placement:** The `✅ Explanation #[[Extra Card Detail]]` rem is always a **sibling of the answer options** (direct child of `>>A)`), NOT nested under the correct answer. Nesting it under the correct answer causes it to show only for that one option. The sibling placement + ECD powerup ensures it displays after any option is selected. This applies to both Section 9 and Section 12 MCQs.

### Section 10: 🚀 RAPID REVISION
```
  - **🚀 RAPID REVISION** :- Last-Minute Review
    - *~read time* ;- 5 minutes

    - **📋 FACTS TO MEMORIZE** :- Core Data
      - *~RemNote setup* ;- After import → click each column header → Flashcard Configuration → Enable For This Column | Value: Both directions (Item → Value AND Value → Item; core recall target) | Memory Hook: Skip (context only, not a recall target)
      - *~Table* ;-
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
Target: fits on 1 printed page (guideline, not a hard cap — never cut content to hit this; instead compress wording). Tables for facts, bullets for comparisons. "Completeness beats brevity" applies to Sections 4 and 5; Section 10 is the exception — it is a summary by design.

**Classification feed into Section 10 — mandatory when topic has Classification Landscapes:**

The Classification Landscape in Section 5 generates content that must appear in three specific Section 10 blocks. Do not leave these generic when classification content exists:

**→ `**⚠️ TRAP ALERTS**` block:** Pull every entry from the Cross-Basis Trap Zone verbatim in compressed form. These are the highest-value last-minute reminders because students most often confuse types from different axes under exam pressure.
```
    - **⚠️ TRAP ALERTS** :- Don't Confuse
      - Stagflation ≠ Cost-Push — different axes: stagflation = growth outcome; cost-push = cause
      - Disinflation ≠ Deflation — disinflation = rate falling (still +ve); deflation = price level falling
      - Galloping ≠ Hyperinflation — galloping = 10–50%; hyperinflation = >50%/month
```

**→ `**🔢 NUMBERS TO REMEMBER**` block:** Pull every threshold and count from the Enumeration Master.
```
    - **🔢 NUMBERS TO REMEMBER** :- Key Figures
      - Inflation bases ;; 4 (cause, speed, scope, expectation)
      - Hyperinflation threshold ;; >50%/month
      - Galloping range ;; 10–50% | Creeping ;; 0–3%
```

**→ `**📋 FACTS TO MEMORIZE**` table:** Add a classification row for each basis showing the count and types in compressed form.
```
      | **Inflation by cause** | 3 types: Demand-Pull, Cost-Push, Structural | Cause = WHY prices rose |
      | **Inflation by speed** | 4 types: Creeping/Walking/Galloping/Hyper | Speed = HOW FAST |
```

### Section 11: Feynman Test + Connections + Mains Framework
```
  - **Feynman Test** :- Conceptual Check
    - *🧪 try first* ;- Close notes. Explain [Topic] to a smart friend who graduated in a different stream (arts/science/commerce) with no background in this subject. Use one analogy. If you can't — re-read Key Terms first.
    - *~check* ;- Can you explain: (1) What it is, (2) Why it matters, (3) One UPSC trap?

  - **Connections** :- Knowledge Web
    - *~builds on* ;; [[Previous Topic]] — [relationship]
    - *~leads on* ;; [[Next Topic]] — [relationship]
    - *~compare with* ;; [[Similar Topic]]
    - *~contemporary_relevance* ;- [Copy verbatim from topic-map `### Contemporary Relevance` section — do not paraphrase; this is the topic's ongoing policy/political/academic significance]
    - *~current affairs link* ;; [Post-2022 event — only use `;;` when confident the event is accurate and post-2022]
      ← If uncertain: write `*~current affairs link* ;- Unverified — search "[topic] + 2024/2025" and replace with confirmed event` using `;-` (disabled). A `;;` placeholder creates a RemNote flashcard where the "answer" is the placeholder text — silent data corruption in the student's SRS deck.

  - **Cross-Paper Transfer** :- Use This Topic Elsewhere
    - *~GS1 angle* ;- [History/Geography/Society/Culture dimension]
    - *~GS2 angle* ;- [Polity/Governance/Social Justice dimension]
    - *~GS3 angle* ;- [Economy/Environment/Security connection]
    - *~GS4 angle* ;- [Ethical dimension: value, thinker, civil service scenario]
    - *~Essay angle* ;- [Abstract philosophical/civilizational theme]
    - *~interdisciplinary hook* ;- [Single most powerful cross-paper insight]

  - **Mains Answer Framework** :- Essay Structure
    - *~marks/word limit* ;- [10m=150w | 15m=250w | 20m=350w]
    - *~paper* ;- [GS1 / GS2 / GS3 / GS4 / Essay — pick one; determines structure below]
    - *~introduction angle* ;- [~30–40w: context + thesis — see paper-specific note below]
    - *~body points* ;- [4–6 points covering all dimensions_tested — see paper-specific note below]
    - *~conclusion angle* ;- [~25–30w: see paper-specific note below]
    - *~quote/committee* ;- [Relevant quote or committee for opening/closing]

**Paper-specific answer structures — fill the three fields above using the right row:**

| Paper | Introduction (~30–40w) | Body structure | Conclusion (~25–30w) |
|-------|----------------------|---------------|---------------------|
| **GS1** (History / Geography / Society) | Historical/geographical/societal context + thesis | Causes/features → Significance/Impact → Contemporary relevance → India-specific dimension | Civilizational or national-identity forward look; connect to Constitution's Preamble values |
| **GS2** (Polity / Governance / IR / Social Justice) | Constitutional/legal context + problem statement (lead with Article / provision if applicable) | Constitutional provisions → Implementation gap → Government initiatives → Judicial/committee view → Way forward | Rights-based or constitutional morality angle; cite SC judgment or Nolan Principle if applicable |
| **GS3** (Economy / Environment / Disaster / Security) | Data point or statistic + why it matters now | Causes → Multidimensional impacts (economic/social/environmental) → Government response → Structural challenges → Specific way forward | Sustainable development goal / national security / SDG link; avoid vague optimism |
| **GS4** (Ethics) | Define the concept + civil service relevance in one sentence | Individual dimension → Institutional safeguard → Societal/constitutional angle (use the 3-dimension structure from subject-guidelines.md) | Quote from `references/quote-bank.md` + constitutional morality angle |
| **Essay** | Quote / Paradox / Anecdote (NEVER a definition) + thesis | 4 quadrants: Historical/Philosophical + Contemporary + Challenges + Way Forward; ≥1 interdisciplinary argument; Indian example + global comparison | Echoes Preamble / Article 21 / civilizational vision — NOT a summary |
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
