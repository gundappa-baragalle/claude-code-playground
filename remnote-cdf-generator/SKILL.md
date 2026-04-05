---
name: remnote-cdf-generator
description: >
  Generates top-notch CDF (Concept Descriptor Framework) notes for UPSC and competitive exam preparation
  that are directly importable into RemNote. Use this skill whenever the user asks to create study notes,
  flashcard notes, revision notes, or CDF notes for any exam topic — especially UPSC (Ancient India,
  Medieval India, Modern India, Geography, Polity, Economy, Science & Tech, Environment, Art & Culture).
  Also trigger when user says "make CDF notes", "create RemNote notes", "notes for spaced repetition",
  "self-explanatory notes", or "notes from scratch for [any topic]".
  This skill produces notes that are: self-explanatory (no other source needed), conceptually deep,
  logically sequenced, analogy-rich, exam-trap-aware, and RemNote-ready with proper hierarchy,
  two-way flashcards, cloze deletions, and structured recall aids.
---

# RemNote CDF Notes Generator — Production Ready

## Core Philosophy

This skill produces notes engineered for **permanent memory** using cognitive science principles:

1. **Self-explanatory** — Zero prior knowledge needed; every term defined
2. **Conceptually clear** — Every fact has "why"; understanding before memorization
3. **Recall-optimized** — Multiple encoding pathways (verbal + visual + emotional + motor)
4. **Exam-ready** — UPSC pattern analysis, PYQ traps flagged, Mains frameworks included
5. **Spaced-repetition ready** — Proper flashcard structure for RemNote's algorithm

---

## THE SCIENCE: Why These Notes Work

### 🧠 Cognitive Principles Embedded in Every Note

| Principle | What It Does | How We Implement It |
|-----------|-------------|---------------------|
| **Dual Coding** (Paivio, 1986) | Verbal + Visual = 2× memory traces | ASCII diagrams, visual maps, spatial layouts |
| **Elaborative Interrogation** | "Why?" questions deepen encoding | Every concept has `*~why it arose*`, `*~significance*` |
| **Retrieval Practice** (Testing Effect) | Active recall > passive review | Cloze cards, MCQs, fill-in-the-blank |
| **Spaced Repetition** (Ebbinghaus) | Review at optimal intervals | RemNote's SRS algorithm + proper card structure |
| **Schema Building** | New info hooks to existing knowledge | `*📌 beginner note*` connects to familiar concepts |
| **Chunking** (Miller) | Group info into memorable units | Hierarchical nesting, mnemonics, numbered lists |
| **Concrete Examples** | Abstract → concrete = memorable | `*🧠 analogy*`, real-world examples |
| **Interleaving** | Mix related concepts for discrimination | `*⚡ contrast*` comparisons throughout |
| **Emotional Encoding** | Emotion strengthens memory | Story hooks, vivid imagery, surprising facts |
| **Method of Loci** | Spatial memory is powerful | Big Picture maps, visual structure |
| **Self-Explanation Effect** (Chi et al., 1994) | Generating your own explanation = 2–3× better comprehension than reading one | `*💭 self-explain*` prompts before revealing answers |
| **Productive Failure** (Kapur, 2016) | Struggling with a problem BEFORE instruction deepens conceptual understanding | `*🧪 try first*` challenge block before content |
| **Boundary Conditions** (Schwartz & Bransford, 1998) | Knowing WHEN a principle does NOT apply prevents shallow pattern-matching | `*~does NOT apply when*` for every major concept |
| **Feynman Technique** | If you can't explain it simply, you don't understand it — you've memorised it | Feynman Test block at end of notes |
| **Generative Learning** (Wittrock, 1990) | Creating your own examples encodes more deeply than receiving prepared ones | `*🔨 your example*` prompts after analogies |
| **Transfer-Appropriate Processing** (Morris et al., 1977) | Study format must match retrieval format — Prelims ≠ Mains retrieval | Explicit Prelims mode vs Mains mode study instructions |
| **Pre-questions / Advance Organizers** (Ausubel, 1960) | Questions BEFORE content activate prior knowledge and create memory "slots" | Pre-question block at top of every note |

---

## BEFORE GENERATING: Collect This Information

**Always clarify (ask if unclear):**

| Question | Why It Matters | Default |
|----------|---------------|---------|
| **Topic** | Scope of notes | Must specify |
| **Subject area** | Source references | Infer from topic |
| **Exam** | Depth & focus | UPSC CSE |
| **Prelims/Mains** | Factual vs analytical | Both |
| **Prior knowledge** | What to define vs assume | Assume complete beginner |
| **Standalone or series** | Affects connections | Standalone |

---

## MANDATORY STEP 0: Look Up Real PYQ Data First

**Do this BEFORE writing a single line of notes. Every note must use real exam intelligence, not generic guesses.**

This skill is bundled with a PYQ knowledge base covering 2,385+ tagged UPSC questions. Two files are always available:
- `pyq-data/concept-index.json` — 218 concepts with frequency, years, dimensions tested
- `pyq-data/topic-maps/{slug}.md` — 167 topic files with actual PYQ questions and patterns

### 0A — Search `pyq-data/concept-index.json`

Read `pyq-data/concept-index.json` and search for the user's topic (case-insensitive, partial match OK).

**Fields to extract:**

| Field | Where to Use It |
|-------|----------------|
| `total_count` | Section 1: `*~PYQ frequency*` |
| `prelims_count` / `mains_count` | Section 1: `*~Prelims weightage*` |
| `year_range` | Section 1: years span in frequency line |
| `last_asked` | Section 1: recency note (2020+ = very active) |
| `dimensions_tested` | Section 5 content emphasis + RAPID REVISION |
| `top_keywords` | Section 11 `*~PYQ pattern*` and cloze cards |

**Slug format** — lowercase, spaces → hyphens:
- "Buddhism" → `buddhism`
- "1857 Revolt" → `1857-revolt`
- "Fundamental Rights" → `fundamental-rights`
- "Indian Geography" → `indian-geography`

### 0B — Read `pyq-data/topic-maps/{slug}.md`

Read the matching topic-map file. Extract:
- **Prelims Questions** — actual PYQ text, year, dimension, priority (HIGH priority first)
- **Exam Patterns & Insights** — what UPSC specifically tests on this topic
- **Dimensions Tested** — WHO / WHAT / WHERE / WHY / HOW breakdown
- **Related Concepts** — use in Connections section

### 0C — Topic Not Found?

If no match in concept-index:
- Try the parent subject (search "Modern India" for a sub-topic within it)
- Use the closest related concept
- Note in Section 1 header: `*~PYQ data* ;- Not yet indexed; based on [Subject] patterns`

### 0D — How PYQ Data Flows Into the 11 Sections

| Section | How to Use PYQ Data |
|---------|-------------------|
| **1. Header & Metadata** | `*~PYQ frequency*` = real `total_count` + year range; `*~Prelims weightage*` = real `prelims_count`/year |
| **5. Content body** | Prioritize aspects matching `dimensions_tested` (e.g., if WHERE dominates, geographic facts get more depth) |
| **5. ⚠️ Exam Traps** | Pull traps from actual PYQ questions where wrong options reveal common misconceptions |
| **9. Practice MCQs** | Use real PYQ questions from topic-map as your FIRST 2–3 MCQs (real > synthetic) |
| **10. RAPID REVISION** | `🎯 LAST YEARS PYQ PATTERN` row = actual dimensions + question types from Exam Patterns & Insights |
| **11. UPSC Analysis** | `*~PYQ pattern*` = real question patterns from topic-map; `*~current affairs link*` = `last_asked` year context |

---

## CRITICAL: RemNote Hierarchical Structure

**THE GOLDEN RULE:** If Concept B is part of Concept A, then B must be INDENTED UNDER A.

### ❌ NEVER DO THIS
```
## Topic Header          ← WRONG: Markdown headers break RemNote hierarchy!
- **Concept A** :: ...

## Another Section       ← WRONG: Creates siblings, not children!
- **Concept B** :: ...
```

### ✅ ALWAYS DO THIS
```
- **Topic** :- Container
  - **Concept A** :: Definition
    - *~property* ;; value
    - **Sub-concept** :: Definition
  - **Concept B** :: Definition
```

---

## CDF Syntax Reference

### Concept Delimiters (for definitions)

| Delimiter | Name | Creates Flashcard? | When to Use |
|-----------|------|-------------------|-------------|
| `::` | Two-way | ✅ Both directions | **PRIMARY** — All main definitions |
| `:-` | Disabled | ❌ None | Category headers, containers |
| `:<` | Backward | ✅ Definition → term | "What is this called?" cards |

**⚠️ AVOID `:>` (forward-only)** — Use `::` for better two-way learning.

### Descriptor Delimiters (for properties)

| Delimiter | Name | Creates Flashcard? | When to Use |
|-----------|------|-------------------|-------------|
| `;;` | Forward | ✅ Yes | **Facts to memorize** — dates, names, places, key facts |
| `;-` | Disabled | ❌ None | **Context only** — explanations, sources, memory hooks |
| `;<` | Backward | ✅ Value → property | Abbreviations, alternate names |
| `;;<` | Two-way | ✅ Both directions | Formulas, equations |

### Decision Tree: `;;` vs `;-`

```
Will UPSC ask this directly?
├── YES → Use `;;` (creates flashcard)
│   Examples: dates, Article numbers, names, places, definitions
│
└── NO → Use `;-` (context only, no flashcard)
    Examples: explanations, analogies, sources, beginner notes
```

### Special Syntax

| Syntax | Purpose | Example |
|--------|---------|---------|
| `{{text}}` | Cloze deletion (basic) | `{{Buddha}} was born at {{Lumbini}}` |
| `{{answer::hint}}` | Cloze with hint | `{{Sarnath::place of first sermon}} is where Buddha gave his first sermon` |
| `[[Term]]` | Link to concept | `Connected to [[Mauryan Empire]]` |
| `>>>` | Multi-line answer | List as flashcard answer |
| `>>1.` | Ordered list | Sequence that matters |
| `>>A)` | MCQ | **First option = correct answer** |
| `#[[Extra Card Detail]]` | Post-answer explanation | Shown to student AFTER they answer; use for MCQ explanations |

**`#[[Extra Card Detail]]` — how it works:** Add it as a tag on a child item nested under the MCQ. RemNote hides it during the question, then reveals it after the student answers. Use it to explain *why* the correct answer is right and *why* each wrong option is wrong.

```
- Question text? >>A)
  - Correct answer
  - Wrong option 1
  - Wrong option 2
  - Wrong option 3
  - **Explanation:** Why correct answer is right. Why wrong options are wrong. #[[Extra Card Detail]]
```

### Cloze Cards with Hints

**ALWAYS use hints for difficult/confusable items:**

```
Basic cloze (no hint):
- {{Buddha}} was born in {{563 BCE}}.

Cloze WITH hint (use for confusable facts):
- Buddha attained enlightenment at {{Bodh Gaya::place in Bihar, NOT Sarnath}}.
- First sermon was at {{Sarnath::Deer Park, NOT Bodh Gaya}}.
- {{Article 17::only absolute FR}} abolishes untouchability.
- {{44th Amendment::removed property right}} made Art 20 & 21 non-suspendable.
```

**When to use hints:**
- Commonly confused places/dates/names
- Similar-sounding terms
- Items frequently asked as "trap" questions
- Technical terms with specific meanings

---

## Descriptor Naming Convention

### Standard Descriptors (use `~` prefix)

```
- *~definition* :: ...
- *~born* ;; 563 BCE at Lumbini
- *~source* ;- NCERT Ch 5
```

### Emoji Descriptors (NO `~` prefix)

```
- *📌 beginner note* ;- Explains unfamiliar term for newcomers
- *🧠 analogy* ;- Connects abstract to familiar concrete thing
- *🧠 mnemonic* ;- Acronym or memory trick
- *🧠 etymology* ;- Word parts → meaning → insight
- *🧠 story* ;- Narrative that makes fact vivid and emotional
- *🧠 visual* ;- Mental image to picture the concept
- *⚡ vs [Other]* ;- Contrast that clarifies through difference
- *⚠️ exam trap* ;- Common wrong answer with fix
- *🔗 connects to* ;; Links to related topics
- *💡 insight* ;- Deep understanding point
- *🎯 Prelims focus* ;- What to memorize for Prelims
- *📝 Mains angle* ;- How to write about this in Mains
- *~does NOT apply when* ;- Boundary condition: when this concept/rule breaks down
- *💭 self-explain* ;- Prompt student to generate their own explanation BEFORE reading
- *🔨 your example* ;- Prompt student to generate their own real-world example
```

**Three new descriptors for conceptual clarity — use these on every major concept:**

| Descriptor | Purpose | Always use `;-` (no flashcard — it's a process prompt) |
|------------|---------|--------------------------------------------------------|
| `*~does NOT apply when*` | Boundary condition — defines the edges of the concept | Prevents shallow pattern-matching |
| `*💭 self-explain*` | Ask student to reason it out before reading — activates Self-Explanation Effect | Place BEFORE the answer/analogy |
| `*🔨 your example*` | Ask student to generate their own example — Generative Learning | Place AFTER the skill's analogy |

### Emoji Reference

| Emoji | Meaning | Typical Delimiter | Science Principle |
|-------|---------|-------------------|-------------------|
| 📌 | Beginner explanation | `;-` | Schema building |
| 🧠 | Memory hook | `;-` | Elaborative encoding |
| ⚡ | Contrast | `;-` | Interleaving |
| ⚠️ | Exam trap | `;-` | Error correction |
| 🔗 | Connection | `;;` | Schema integration |
| 💡 | Insight | `;-` | Deep processing |
| 🎯 | Prelims focus | `;-` | Goal clarity |
| 📝 | Mains angle | `;-` | Application |
| 💭 | Self-explain prompt | `;-` | Self-Explanation Effect |
| 🔨 | Generate your own example | `;-` | Generative Learning |
| 🧪 | Try-first challenge | `;-` | Productive Failure |

---

## File Architecture (11 Sections)

Every output file contains these sections in order:

### 1. Header & Metadata
```
- **[Topic]** :- UPSC [Subject]
  - *~source* ;- [Standard books with chapter numbers]
  - *~PYQ frequency* ;- [Use Step 0 data: "X questions total (Prelims: Y, Mains: Z), YYYY–YYYY"]
  - *~Prelims weightage* ;- [Use Step 0 data: real prelims_count; last asked YYYY]
  - *~Mains relevance* ;- [Which GS paper, what themes]
  - *~revision priority* ;- [Use Step 0 revision_priority from concept-index: HIGH / MEDIUM / LOW]
```

**Fill from Step 0 data. Never guess — always use real numbers from `concept-index.json`. Example:**
```
  - *~PYQ frequency* ;- High — 14 questions total (Prelims: 12, Mains: 2), 1998–2019; last asked 2019
  - *~Prelims weightage* ;- ~1–2 direct questions/year; recurs every 2–3 years
  - *~revision priority* ;- HIGH — review daily in SRS until exam
```

**Revision priority convention** — drives RemNote SRS queue weight:

| `revision_priority` | Meaning | SRS Behaviour |
|---------------------|---------|---------------|
| `HIGH` (≥10 PYQs) | UPSC tests this frequently — must be rock solid | Daily review; tag all `;;` cards as high priority |
| `MEDIUM` (5–9 PYQs) | Tested occasionally — know the key facts | Weekly review cycle |
| `LOW` (<5 PYQs) | Rarely tested — skim and move on | Monthly review; only memorise the `⚠️ traps` |

### 2. Why Study This? (Motivation + Context + Pre-questions)
```
  - **Why Study [Topic]?** :- Motivation
    - *~exam relevance* ;; [Specific papers, frequency]
    - *~conceptual value* ;; [What understanding this unlocks]
    - *~real-world relevance* ;; [Current affairs connections]
    - *📌 beginner note* ;- [Why this matters in the big picture]
  
  - **Before You Read** :- Activate Prior Knowledge
    - *🧪 try first* ;- Think about these before reading the notes:
      1. [Question about what student likely already knows — even partially]
      2. [Question about WHY this topic/event/law might have come about]
      3. [A prediction: what do you think UPSC asks about this?]
    - *~revisit after* ;- Come back to these 3 questions after finishing — 
      can you answer them now? That's your comprehension check.
```

**Pre-question rules (Advance Organizer principle):**
- Question 1 should activate something the student already knows (even loosely)
- Question 2 should prompt them to reason about *why*, not *what*
- Question 3 builds exam metacognition — predicting UPSC's angle before reading
- These are `;-` (no flashcard) — they are cognitive primers, not recall targets

### 3. Big Picture (Visual Map)

**CRITICAL for dual coding — provides spatial memory anchor**

```
  - **Big Picture** :- Visual Overview
    - *~structure* ;-
      ```
      TOPIC NAME
      ├── Major Component 1
      │   ├── Sub-component A
      │   └── Sub-component B
      ├── Major Component 2
      │   ├── Sub-component C
      │   └── Sub-component D
      └── Major Component 3
      
      TIMELINE (if historical):
      [Date1]────[Date2]────[Date3]────[Date4]
         │          │          │          │
       Event1    Event2     Event3     Event4
      ```
```

### 4. Key Terms Glossary (For Complete Beginners)
```
  - **Key Terms** :- Glossary
    - **Term 1** :: Simple definition
      - *📌 beginner note* ;- Plain English explanation with analogy
    - **Term 2** :: Simple definition
```

### 5. Content (Main Body)

Hierarchically nested concepts following all quality standards.

**Every major concept MUST include:**
- Definition (`::`)
- Why it arose / significance (`*~why*`, `*~significance*`)
- Beginner note if complex (`*📌 beginner note*`)
- At least one memory hook (`*🧠 analogy/mnemonic/story*`)
- Contrast if similar concepts exist (`*⚡ vs*`)
- Exam trap if commonly confused (`*⚠️ exam trap*`)

**Depth requirements:**
- **Minimum 3 levels of indentation** for each major concept (concept → property → detail)
- **Minimum 2 memory hooks per major concept** (from different hook types: analogy + mnemonic, or story + etymology, etc.)
- **All PYQ-flagged sub-topics** (from Step 0 `dimensions_tested`) must get their own top-level concept node with full treatment
- **Never stop at "what"** — every concept needs `*~why it arose*` and `*~significance*`; omitting these is a quality failure

**Sequence rule:** Follow causal/chronological order within sections, not alphabetical. Causes before effects, earlier events before later ones, simpler concepts before complex ones that build on them.

**Coverage floor:** The content section must cover enough ground that a student who reads only this file could attempt any Prelims MCQ on the topic without needing another source.

### 6. Flashcard Tables (RemNote Format)

**CRITICAL: Tables must follow RemNote's flashcard generation format**

In RemNote tables:
- **Name column (first column)** = Concept (the thing being learned)
- **Other columns** = Descriptors (properties that become flashcards)
- Each cell in descriptor columns generates a flashcard

**Format for Testable Tables:**

```
  - **Buddhist Councils** :- Flashcard Table
    | Name | Place | Patron | President | Outcome |
    |------|-------|--------|-----------|---------|
    | **First Council** | Rajagriha | Ajatashatru | Mahakasyapa | Compiled Vinaya & Sutta |
    | **Second Council** | Vaishali | Kalashoka | Sabakami | First schism |
    | **Third Council** | Pataliputra | Ashoka | Moggaliputta Tissa | Abhidhamma added |
    | **Fourth Council** | Kashmir | Kanishka | Vasumitra | Mahayana emerged |
```

This generates flashcards like:
- "First Council → Place?" = Rajagriha
- "First Council → Patron?" = Ajatashatru
- "Rajagriha → Which council?" (backward card)

**Comparison Tables (for understanding, not direct testing):**

```
  - **Key Comparisons** :- Reference Tables
    - **Buddhism vs Jainism** :- Comparison
      | Aspect | Buddhism | Jainism |
      |--------|----------|---------|
      | Soul | Rejects (Anatta) | Accepts (Jiva) |
      | Asceticism | Middle Path | Extreme |
      | Ahimsa | Important but contextual | Absolute |
```

**Rules for Flashcard Tables:**
1. **First column = Name** (the Concept being tested)
2. **Bold the Name column entries** for clarity
3. **Keep cells short** (< 5 words) for easy recall
4. **No emojis inside cells** — put ⚠️ notes AFTER table
5. **Most important info in early columns** (tested more)

**Example with Hint Column:**

```
  - **Five Writs** :- Flashcard Table
    | Name | Meaning | Purpose | Hint |
    |------|---------|---------|------|
    | **Habeas Corpus** | "To have the body" | Against illegal detention | Can be against private persons too |
    | **Mandamus** | "We command" | Compel public duty | NOT against President/Governor |
    | **Certiorari** | "To be certified" | Quash lower court order | AFTER order passed (curative) |
    | **Prohibition** | "Stay" | Prevent excess jurisdiction | BEFORE order (preventive) |
    | **Quo Warranto** | "By what authority" | Challenge illegal office | Anyone can file, not just aggrieved |
```

### 7. One-Liners (Rapid Recall)

```
  - **One-Liners** :- Rapid Recall
    - Topic fact 1 = [condensed form]
    - Topic fact 2 = [condensed form]
    - [Name] = [key association]
    - [Date] = [event]
```

**Rules:**
- No full sentences — fragments, arrows, equals signs OK
- One line per fact
- Include all "frequently confused" items
- Should enable 70%+ recall of topic

### 8. Quick Revision (Cloze Flashcards with Hints)

```
  - **Quick Revision** :- Cloze Cards
    - {{Buddha::founder of Buddhism}} was born at {{Lumbini::in modern Nepal}} in {{563 BCE::6th century}}.
    - Buddha attained enlightenment at {{Bodh Gaya::NOT Sarnath}} under the {{Bodhi::Peepal}} tree.
    - First sermon at {{Sarnath::Deer Park, NOT Bodh Gaya}} is called {{Dharmachakra Pravartana::turning of wheel}}.
    - {{Article 17::abolishes untouchability}} is the only {{absolute::no exceptions}} Fundamental Right.
    - {{44th Amendment::1978}} removed Right to Property and protected Art {{20::criminal protection}} and {{21::life & liberty}}.
```

**Hint Guidelines:**
- Use `{{answer::hint}}` format
- Hints should help recall WITHOUT giving away the answer
- Good hints: context, category, what it's NOT, year/era
- Bad hints: synonyms or near-answers

**CRITICAL:** Every answer MUST use `{{}}`. Add hints for confusable items.

### 9. Practice MCQs

```
  - **Practice MCQs** :- Self-Test
    - [Question text]? >>A)
      - Correct answer           ← MUST be first
      - Wrong option 1
      - Wrong option 2
      - Wrong option 3
      - **Explanation:** [Why correct answer is right. Why each wrong option is wrong. PYQ year if applicable.] #[[Extra Card Detail]]
```

**MANDATORY: Every MCQ MUST have an `#[[Extra Card Detail]]` explanation.** RemNote hides it during the question and reveals it only after the student answers — so it never gives away the answer but always reinforces the learning.

**What to include in the explanation:**
- Why the correct answer is correct (the core fact/reasoning)
- Why each wrong option is wrong (trap logic — this is where real learning happens)
- PYQ year if it's a real question (e.g., `PYQ 2017`)
- Memory hook to prevent re-confusion (e.g., "Remember: Sermon → Sarnath, both start with S")

**Explanation format:**
```
- **Explanation:** ✅ [Correct answer] because [reason]. ❌ [Wrong 1] — [why wrong]. ❌ [Wrong 2] — [why wrong]. ❌ [Wrong 3] — [why wrong]. 🧠 [Memory hook if needed.] #[[Extra Card Detail]]
```

**Source of MCQs — priority order:**
1. **Real PYQ questions** from `pyq-data/topic-maps/{slug}.md` — use HIGH and MEDIUM priority questions verbatim (first 2–3 MCQs must be real PYQs)
2. **Synthetic questions** modelled on `dimensions_tested` and real patterns — fill remaining slots

**Always add study-mode instructions as the first child of the Practice MCQs block:**
```
  - **Practice MCQs** :- Self-Test
    - *~Prelims mode* ;- Cover the options. Read only the question stem. 
      Try to answer BEFORE seeing the choices — this matches real exam recall.
    - *~Mains mode* ;- Read only the topic name. Write 3 points from memory 
      before checking notes — this matches free-recall essay writing.
    - [MCQ 1 — real PYQ] >>A)
      ...
```

**Pattern variety:**
- Direct factual questions
- "Which is NOT" questions
- "Common to both X and Y" questions
- Match the following style
- Statement-based (I, II, III correct?)

### 10. 🚀 RAPID REVISION (Pre-Exam Section)

**This section is for last-minute revision — the entire topic at a glance**

```
  - **🚀 RAPID REVISION** :- Last-Minute Review
    - *~read time* ;- 5 minutes
    - *~covers* ;- All high-frequency facts for this topic
    
    - **📋 FACTS TO MEMORIZE** :- Core Data
      | Item | Value | Memory Hook |
      |------|-------|-------------|
      | Buddha born | 563 BCE, Lumbini | "563 = 5+6+3=14, 1+4=5 senses he renounced" |
      | Enlightenment | Bodh Gaya, age 35 | "Bodh = Buddha, Gaya = Got enlightenment" |
      | First Sermon | Sarnath | "Sarnath = Sermon" (both start with S) |
      | Death | 80 years, Kushinagar | "Kushi = end of journey" |
      | Four Truths | Dukkha, Samudaya, Nirodha, Magga | "DSNM = Don't Suffer, Nirvana's Method" |
    
    - **⚡ QUICK COMPARISONS** :- Key Differences
      - Buddhism vs Jainism: Soul? Buddhism = NO (Anatta), Jainism = YES (Jiva)
      - Middle Path: ONLY Buddhism (NOT Jainism — they do extreme asceticism)
      - Art 32 vs 226: 32 = SC, FR only, itself FR. 226 = HC, wider, not FR.
      - FR vs DPSP: FR = justiciable, DPSP = non-justiciable
    
    - **⚠️ TRAP ALERTS** :- Don't Confuse
      - Sarnath ≠ Bodh Gaya (Sermon ≠ Enlightenment)
      - Mahakasyapa presided First COUNCIL. Kondanna was at First SERMON.
      - Art 19 = Citizens only. Art 21 = All persons.
      - Art 17 = ONLY absolute FR (no exceptions even in Emergency)
    
    - **🔢 NUMBERS TO REMEMBER** :- Key Figures
      - 6 Fundamental Rights (originally 7, property removed)
      - 5 Writs (MHPCQ)
      - 4 Noble Truths
      - 8-fold Path
      - 3 Jewels (Buddha, Dharma, Sangha)
    
    - **📝 MAINS KEYWORDS** :- For Essay Writing
      - Buddhism: "rational inquiry", "social reform", "anti-ritualism", "democratic Sangha"
      - FR: "constitutional morality", "golden triangle (14-19-21)", "basic structure"
    
    - **🎯 LAST YEARS PYQ PATTERN** :- What UPSC Asks
      - [Use Step 0 data: pull from "Exam Patterns & Insights" in topic-map]
      - [List actual question types UPSC has asked, with year if notable]
      - [Note dominant dimensions_tested — e.g., "WHERE asked 4/6 times"]
```

**For `🎯 LAST YEARS PYQ PATTERN`:** Always pull from the "Exam Patterns & Insights" section of `pyq-data/topic-maps/{slug}.md`. Use real observed patterns — never fabricate. If topic-map is not available, note it explicitly.

**Rapid Revision Rules:**
1. **Maximum 1 page** when printed
2. **Tables for facts** — easy to scan
3. **Bullet points for comparisons** — quick to read
4. **Include memory hooks** — for last-minute anchoring
5. **Trap alerts prominent** — prevent silly mistakes
6. **Mains keywords** — for quick essay recall

### 11. Connections & Mains Frameworks

```
  - **Feynman Test** :- Conceptual Check
    - *🧪 try first* ;- Close your notes. Explain [Topic] to an imaginary 
      12-year-old using one analogy. If you can't — re-read Key Terms before continuing.
    - *~check* ;- Can you explain: (1) What it is, (2) Why it matters for UPSC, 
      (3) One trap UPSC sets on this topic?

  - **Connections** :- Knowledge Web
    - *~builds on* ;; [[Previous Topic]] — [relationship]
    - *~leads on* ;; [[Next Topic]] — [relationship]
    - *~compare with* ;; [[Similar Topic]]
    - *~current affairs link* ;; [Recent news/development]
  
  - **Cross-Paper Transfer** :- Use This Topic Elsewhere
    - *~GS1 angle* ;- [How facts/events from this topic appear in History/Geography/Society/Culture questions]
    - *~GS2 angle* ;- [Polity/Governance/Social Justice/IR dimension of this topic]
    - *~GS3 angle* ;- [Economy/Environment/Disaster Management/Security connection]
    - *~GS4 angle* ;- [Ethical dimension: which value, thinker, or case study this topic illustrates]
    - *~Essay angle* ;- [The abstract philosophical/civilizational theme this topic can anchor an essay on]
    - *~interdisciplinary hook* ;- [One-liner — the single most powerful cross-paper insight from this topic]

  - **Mains Answer Framework** :- Essay Structure
    - *~marks/word limit* ;- [10m = 150w | 15m = 250w | 20m = 350w — use topic-map's word_limit_suggested]
    - *~introduction angle* ;- [2–3 lines, ~30–40w: context + thesis. Use intro_approach from topic-map if available]
    - *~body points* ;- [Pull from topic-map's body_points; 4–6 points covering all dimensions_tested]
    - *~conclusion angle* ;- [1–2 lines, ~25–30w: forward-looking / quote / constitutional angle]
    - *~quote/committee* ;- [Relevant quote or committee reference for opening/closing]
```

**Filling Cross-Paper Transfer from Step 0 topic-map data:**

Read the `## Cross-Paper Transfer` section in `pyq-data/topic-maps/{slug}.md`. It contains:
- **GS Paper Connections** — aggregated from `interlinkages` field across all mains PYQs for this topic
- **Essay & Thematic Angles** — aggregated from `themes` across all mains PYQs
- **Contemporary Relevance** — best `contemporary_relevance` string from enriched questions

Map them to the correct descriptor:
| topic-map field | → SKILL.md descriptor |
|-----------------|----------------------|
| Link starts with "GS1" | → `*~GS1 angle*` |
| Link starts with "GS2" | → `*~GS2 angle*` |
| Link starts with "GS3" | → `*~GS3 angle*` |
| Link starts with "GS4" or "Ethics" | → `*~GS4 angle*` |
| Essay themes | → `*~Essay angle*` |
| Single strongest insight | → `*~interdisciplinary hook*` |

**Example — Gandhian Era:**
```
  - **Cross-Paper Transfer** :- Use This Topic Elsewhere
    - *~GS4 angle* ;- Gandhi = prime Ethics source: means vs ends (civil disobedience), 
      trusteeship theory (wealth as social trust), satyagraha (moral courage in civil service)
    - *~GS2 angle* ;- Decentralisation — Gram Swaraj; role of civil society in democracy
    - *~GS3 angle* ;- Khadi and village economy as alternative development model
    - *~Essay angle* ;- "Means are as important as ends" / "Non-violence as civilisational 
      force" / "Relevance of Gandhian thought in the age of climate change"
    - *~interdisciplinary hook* ;- Every Ethics case study on civil disobedience, 
      whistleblowing, or moral courage can cite Gandhi's Satyagraha as the canonical framework
```

**Word budget discipline** — the single biggest differentiator in Mains scoring:

| Marks | Total words | Intro | Body | Conclusion |
|-------|------------|-------|------|------------|
| 10m   | ~150w      | 30w   | 95w  | 25w        |
| 15m   | ~250w      | 40w   | 175w | 35w        |
| 20m   | ~350w      | 50w   | 260w | 40w        |

**Use Step 0 topic-map data:** Each mains question in `pyq-data/topic-maps/{slug}.md` includes `word_limit_suggested`, `intro_approach`, `body_points`, and `conclusion_approach` — pulled directly from the enrichment schema. Use these as the starting framework and adapt for the user's specific question.

---

## The ELEVEN Quality Standards

### Standard 1: Beginner Test 📌 (Schema Building)

**Rule:** Define every unfamiliar term on first use.

**Must explain:**
- Dynasty/ruler names (who, when, where, why significant)
- Geographical terms (location + significance)
- Sanskrit/Pali/Arabic/Persian terms (translation + meaning + usage)
- Historical figures (identification + role + significance)
- Technical terms (definition + example + analogy)

**Format:**
```
- **Sangha** :: Buddhist monastic community
  - *📌 beginner note* ;- "Sangha" = Sanskrit for "assembly/community". Unlike Hindu priests who lived in society, Buddhist monks formed separate communities with strict rules (Vinaya). Think of it like a university hostel with strict discipline for spiritual students.
```

### Standard 2: Conceptual Bridge 🧠 (Elaborative Interrogation + Boundary Conditions)

**Rule:** Every concept needs "why" and "how", not just "what" — AND must define when it does NOT apply.

**The WHY + BOUNDARY Framework:**
```
- **Concept** :: What it is
  - *💭 self-explain* ;- Before reading: why do you think [concept] works this way?
  - *~why it arose* ;; What problem/need it addressed
  - *~how it works* ;; The mechanism/process
  - *~significance* ;; Why it matters / impact
  - *~consequence* ;; What happened because of it
  - *~does NOT apply when* ;- [The boundary condition: when this rule/concept breaks down]
  - *🧠 plain English* ;- [Simplest possible explanation]
  - *🧠 analogy* ;- [Connects to familiar everyday experience]
  - *🔨 your example* ;- Can you think of a real example where [concept] applies? 
    Try before reading the next note.
  - *💡 insight* ;- [The deep understanding point]
```

**Boundary condition examples — what to write:**
```
- **Fundamental Rights** :: Guaranteed protections against State action
  - *~does NOT apply when* ;- (1) Against private individuals — only enforceable against 
    "State" as defined in Art 12. (2) During Emergency (Art 358–359) — Art 19 can be 
    suspended; Art 20–21 cannot.

- **Reasonable Classification (Art 14)** :: Allows differential treatment if classification is reasonable
  - *~does NOT apply when* ;- Classification is arbitrary (no rational nexus to object), 
    or creates a "class legislation" targeting one person/entity.

- **Mandamus** :: Writ compelling public officials to perform duty  
  - *~does NOT apply when* ;- Against President/Governor (constitutional immunity), 
    private individuals, or discretionary acts (only ministerial/mandatory duties).
```

### Standard 3: Dual Coding 🗺️ (Visual + Verbal)

**Rule:** Every file must have visual elements.

**Required visual elements:**
- Big Picture ASCII map (structure overview)
- Timeline for historical topics
- Comparison tables for related concepts
- Process flows for mechanisms
- Spatial descriptions ("northern India", "east of X")

**ASCII Templates:**
```
HIERARCHY:           TIMELINE:              PROCESS:
┌─────────┐          1900    1920    1940   [Input]
│  Parent │            │       │       │       │
└────┬────┘          Event1  Event2  Event3   ▼
     │                                      [Step 1]
┌────┴────┐                                   │
│         │                                   ▼
▼         ▼                                [Step 2]
Child1  Child2                                │
                                              ▼
                                           [Output]
```

### Standard 4: Memory Architecture 🧠 (Multi-Modal Encoding)

**Rule:** Every major concept needs multiple memory hooks.

**Required hook types (at least 3 per major concept):**

| Hook Type | Format | Encoding Channel |
|-----------|--------|------------------|
| **Acronym/Mnemonic** | `*🧠 mnemonic* ;- "HOMES" = Huron, Ontario, Michigan, Erie, Superior` | Verbal chunking |
| **Story** | `*🧠 story* ;- Imagine Buddha leaving his palace at midnight...` | Emotional + Narrative |
| **Analogy** | `*🧠 analogy* ;- Middle Path is like a guitar string — too tight snaps, too loose won't play` | Concrete + Familiar |
| **Etymology** | `*🧠 etymology* ;- Nirvana = Nir (out) + Vana (blow) = blowing out desire's flame` | Linguistic + Meaning |
| **Visual Image** | `*🧠 visual* ;- Picture Ashoka's remorse: battlefield with 100,000 corpses` | Imagery |
| **Contrast** | `*⚡ vs Jainism* ;- Buddhism = middle path; Jainism = extreme asceticism` | Discrimination |
| **One-liner** | `*🧠 summary* ;- "Hinduism = same soul, new body. Buddhism = no soul, just continuity"` | Compression |

### Standard 5: Exam Trap Test ⚠️ (Error Prevention)

**Rule:** Flag every common wrong answer with correction.

**Format:**
```
- *⚠️ exam trap* ;- [Wrong answer] often confused with [right answer]. 
  Remember: [memory hook to distinguish]. 
  (PYQ: [year] — [brief question context])
```

**Source traps from Step 0 data:** Read actual PYQ questions from `pyq-data/topic-maps/{slug}.md`. Questions where a common wrong assumption could lead to the wrong option are your best trap alerts. Use real PYQ year in the `(PYQ: YYYY —)` tag.

**High-frequency UPSC trap patterns:**
- Similar-sounding names (Kondanna vs Mahakasyapa)
- Similar concepts (Nirvana vs Moksha)
- "Common to both X and Y" — usually FALSE
- "Which is NOT" — read all options carefully
- Same word, different meaning (Dharma in Buddhism vs Hinduism)
- Chronological confusion (which came first?)
- Location confusion (where did X happen?)

### Standard 6: Retrieval Practice (Active Recall)

**Rule:** Notes must generate effective flashcards.

**Card quality checklist:**
- [ ] Each card tests ONE fact (atomic)
- [ ] Question is unambiguous
- [ ] Answer is specific (not vague)
- [ ] Cloze deletions have enough context
- [ ] MCQ first option is correct

**Good vs Bad flashcards:**
```
❌ BAD: What are the features of Buddhism? (too broad)
✅ GOOD: Buddhism's view on soul (Atman)? → Rejects it (Anatta)

❌ BAD: {{Buddhism}} is a religion. (too obvious)
✅ GOOD: Buddhism's stance on soul is called {{Anatta}} meaning {{no-self}}.
```

### Standard 7: Interleaving ⚡ (Contrast Learning)

**Rule:** Related concepts must be explicitly compared.

**When to use contrast:**
- Two traditions answer same question differently
- Similar terms with different meanings
- Commonly confused items in exams
- Evolution from one concept to another

**Format:**
```
- *⚡ Buddhism vs Jainism* ;-
  | Aspect | Buddhism | Jainism |
  | Soul | Rejects (Anatta) | Accepts (Jiva) |
  | Asceticism | Middle Path | Extreme |
  | Violence | Avoid | Absolute non-violence |
  
  KEY DIFFERENCE: Buddhism says no eternal soul exists. Jainism says soul exists but is trapped in karma.
```

### Standard 8: Chunking (Information Organization)

**Rule:** Group related information into memorable units.

**Chunking strategies:**
- **Numbered lists** for sequences: "3 Jewels", "4 Noble Truths", "8-fold Path"
- **Acronyms** for components: "FORCEPS" for writs
- **Categories** for types: Organelles → Energy, Synthesis, Transport
- **Timelines** for chronology: Dates grouped by century/era
- **Hierarchy** for relationships: Part-whole, Type-subtype

### Standard 9: Spaced Repetition Optimization

**Rule:** Structure notes for RemNote's SRS algorithm.

**Principles:**
- Break complex concepts into atomic flashcards
- Use `::` for important definitions (two-way review)
- Use `;;` for facts that might be asked
- Use `;-` for context that aids understanding but needn't be memorized
- Cloze cards for fill-in-the-blank practice
- MCQs for exam simulation

### Standard 10: UPSC-Specific Requirements

**For every topic, include:**

```
- **UPSC Analysis** :- Exam Strategy
  - *🎯 Prelims focus* ;- [What specific facts to memorize]
  - *📝 Mains angles* ;- [Themes, debates, analytical points]
  - *~PYQ pattern* ;- [How UPSC asks about this topic]
  - *~current affairs link* ;- [Recent relevance]
  - *~committee/report* ;- [Any relevant committee]
  - *~quote* ;- [Quotable line for answers]
```

### Standard 11: Conceptual Clarity 💭 (Self-Explanation + Productive Failure + Transfer)

**Rule:** Every note must include elements that force the student to *construct* understanding, not just *receive* it.

**Three mandatory conceptual clarity elements:**

**A. Self-Explanation prompts** (on every major concept — at least 2 per note)
```
- **Non-Cooperation Movement** :: Gandhi's first mass civil disobedience, 1920–1922
  - *💭 self-explain* ;- Before reading: Why do you think Gandhi STOPPED the movement 
    after Chauri Chaura? What does that tell you about his philosophy?
  [→ then reveal: because a mob burned a police station, violating non-violence — 
   Gandhi believed means matter as much as ends]
```

**B. Boundary conditions** (on every major concept — what breaks the rule)
```
- **Writ of Mandamus** :: Compels public official to perform mandatory duty
  - *~does NOT apply when* ;- (1) Against President/Governor, (2) Against private 
    individuals, (3) For discretionary acts — only ministerial/mandatory duties
```

**C. Feynman Test** (once per note, at the very end — before Connections)
```
  - **Feynman Test** :- Conceptual Check
    - *🧪 try first* ;- Close your notes. Explain [Topic] to an imaginary 
      12-year-old who has never heard of it. Use one analogy. 
      If you can't — re-read Key Terms and Content sections before continuing.
    - *~check* ;- Can you explain: (1) What it is, (2) Why it matters, 
      (3) One thing UPSC loves to trap students on?
```

**D. Study-mode tagging in Practice MCQs** (Transfer-Appropriate Processing)
```
  - **Practice MCQs** :- Self-Test
    - *~Prelims mode* ;- Cover the answer options. Read only the question stem. 
      Predict the correct answer BEFORE revealing options. This matches real exam recall.
    - *~Mains mode* ;- Read the topic heading only. Write 3 bullet points 
      from memory. Then check your notes. This matches essay retrieval.
```

**E. Generative example prompt** (on abstract concepts — at least 1 per note)
```
- **Reasonable Classification** :: Art 14 permits differential treatment if rational nexus exists
  - *🧠 analogy* ;- Wheelchair ramps treat disabled people differently — but it's reasonable
  - *🔨 your example* ;- Can you think of a government scheme or law that uses 
    reasonable classification? (Reservation? Senior citizen benefits?) 
    Try naming one before reading further.
```

---

## UPSC Subject-Specific Guidelines

### History (Ancient/Medieval/Modern)
- Always include: Timeline, Dynasty table, Key battles, Important personalities
- Connect to: Art & Architecture, Religion, Economy of the period
- PYQ patterns: Match the following, Chronological order, "Common to both"

### Polity
- Always include: Article numbers, Amendment numbers, Case laws, Committee names
- Comparison tables: FR vs DPSP, Lok Sabha vs Rajya Sabha, Governor vs President
- Connect to: Current constitutional debates, Recent amendments

### Geography
- Always include: Locations, Diagrams (processes), Maps (conceptual), Data
- Types: Physical, Human, Economic, Environmental
- Connect to: Climate change, Agriculture, Industries, Current disasters

### Economy
- Always include: Definitions, Formulas, Institutions, Recent data/reports
- Diagrams: Flow charts for policies, Graphs for trends
- Connect to: Budget, Economic Survey, RBI reports

### Science & Tech
- Always include: Mechanism/Process, Applications, Recent developments
- Diagrams: How it works
- Connect to: Government missions, Indian scientists, Indigenous technology

### Environment
- Always include: Species/Ecosystem details, Conservation status, Policies
- Connect to: International conventions, India's commitments, Recent reports

### Ethics (GS4)

Ethics notes have a fundamentally different character — less factual recall, more value frameworks and application. Adjust the 11-section structure as follows:

**What changes for Ethics:**
- **Section 1 header:** Add `*~GS4 paper* ;; [paper number and marks allocation]`
- **Section 3 Big Picture:** Use a value-framework map instead of a factual hierarchy:
  ```
  [Concept] — e.g., Integrity
  ├── Meaning & Components
  ├── Indian Thinkers (Gandhi, Kautilya, etc.)
  ├── Western Thinkers (Kant, Aristotle, Rawls)
  ├── Constitutional / Governance angle
  └── Case Study application
  ```
- **Section 5 Content:** For every ethical concept, include:
  - `*~thinker quote* ;;` — one attributable quote (Indian thinker preferred)
  - `*~case study angle* ;-` — how this value appears in a civil services scenario
  - `*~opposite value* ;-` — the tension/conflict (e.g., integrity vs loyalty)
  - `*~governance link* ;;` — how it connects to civil services conduct rules
- **Section 9 MCQs:** Ethics Prelims MCQs test definitions and thinkers — use HIGH priority questions from topic-map
- **Section 11 Mains Framework:** Ethics answers need intro (define + context) → body (dimensions: individual / institutional / societal) → conclusion (constitutional morality angle)

**Eight indexed Ethics topics in pyq-data** (use Step 0 to find them): Ethics Basics, Human Values, Emotional Intelligence, Attitude, Aptitude for Civil Service, Case Study Approach, Probity in Governance, Ethical Governance.

**Key rule:** Ethics notes should help the aspirant *reason through* a scenario, not just *recall* facts. Every flashcard should test application, not memorisation.

### CSAT (Paper 2) — Out of Scope

The 11-section CDF architecture is designed for **GS1–GS4 content notes** (factual, analytical, essay-type). CSAT Paper 2 covers comprehension passages, data interpretation, basic arithmetic, and logical reasoning — none of which benefit from concept-descriptor flashcard notes.

**Do NOT generate CDF notes for CSAT topics.** Instead, tell the user:
> "CSAT (Paper 2) requires practice sets, not concept notes. Use a dedicated CSAT practice book (e.g., Arihant, McGraw-Hill) for timed practice. The `pyq-data/` folder does contain CSAT PYQs tagged by type (Data Interpretation, Seating Arrangement, etc.) — you can use those for targeted practice directly."

---

## Complete Example Structure

```
- **Buddhism** :- UPSC Ancient History
  - *~source* ;- Tamil Nadu 11 (Ch 6), NCERT Class 6 (Ch 6), NCERT Class 12 (Themes)
  - *~PYQ frequency* ;- High — 18 questions total (Prelims: 15, Mains: 3), 1998–2023; last asked 2023
  - *~Prelims weightage* ;- ~1–2 direct questions/year; recurs every 1–2 years; indirect via Mauryas adds 2–3 more
  - *~Mains relevance* ;- GS1 (Indian culture), Essay (philosophical themes)
  
  - **Why Study Buddhism?** :- Motivation
    - *~exam relevance* ;; Most tested ancient religion in UPSC; connects to Mauryas, Art, Philosophy
    - *~conceptual value* ;; Understanding Buddhism unlocks Mauryan history, Ajanta-Ellora, India's soft power in Asia
    - *~real-world relevance* ;; India's cultural diplomacy, Buddhist circuit tourism, Dalai Lama connection
    - *📌 beginner note* ;- Buddhism is India's major "export" — it shaped half of Asia's culture. Understanding it helps you understand why Japanese, Chinese, Thai cultures have Indian elements.
  
  - **Big Picture** :- Visual Overview
    - *~structure* ;-
      ```
      BUDDHISM — India's Gift to Asia
      │
      ├── CONTEXT: Why Buddhism Arose (6th century BCE)
      │   └── Vedic ritualism → expensive, Brahmin monopoly → discontent
      │
      ├── FOUNDER: Siddhartha Gautama (563-483 BCE)
      │   └── Birth (Lumbini) → Renunciation (29) → Enlightenment (35) → Death (80)
      │
      ├── CORE TEACHINGS
      │   ├── Four Noble Truths (diagnosis of suffering)
      │   ├── Noble Eightfold Path (prescription)
      │   ├── Middle Path (avoid extremes)
      │   └── Three Marks: Anicca, Dukkha, Anatta
      │
      ├── SPREAD
      │   ├── Councils: Rajagriha → Vaishali → Pataliputra → Kashmir
      │   └── Schools: Hinayana (Theravada) vs Mahayana
      │
      └── DECLINE IN INDIA (after 12th century)
          └── Causes: Brahmanical revival, Muslim invasions, loss of patronage
      
      TIMELINE:
      563 BCE────483 BCE────483 BCE────383 BCE────250 BCE────78 CE
         │           │           │           │           │         │
       Birth      Death      Council I   Council II   Council III  Council IV
      Lumbini   Kushinagar  Rajagriha   Vaishali   Pataliputra  Kashmir
      ```
  
  - **Key Terms** :- Glossary
    - **Buddha** :: "The Awakened One" — title given to Siddhartha after enlightenment
      - *📌 beginner note* ;- From Sanskrit "budh" (to awaken). Not a god — a human who "woke up" to the truth about suffering and taught others.
    - **Sangha** :: Buddhist monastic community of monks and nuns
      - *📌 beginner note* ;- Like a spiritual university. Students (monks) lived together, followed rules (Vinaya), and studied under teachers.
    - **Dharma** :: Buddha's teachings (different from Hindu Dharma meaning duty)
      - *⚠️ exam trap* ;- Dharma means different things: Hindu = duty/righteousness; Buddhist = Buddha's teachings; Jain = nature of things
    - **Nirvana** :: Liberation from cycle of rebirth by extinguishing desire
      - *🧠 etymology* ;- Nir (out) + Vana (blowing) = "blowing out" the flame of desire
  
  [... Full content continues with all teachings, schools, councils, etc. ...]
  
  - **Key Comparisons** :- Tables
    - **Buddhism vs Jainism** :- Comparison
      | Aspect | Buddhism | Jainism |
      |--------|----------|---------|
      | **Soul** | Rejects (Anatta) | Accepts (Jiva) |
      | **Asceticism** | Middle Path (moderate) | Extreme (fasting to death OK) |
      | **Non-violence** | Important but contextual | Absolute (even insects) |
      | **Language** | Pali (common people) | Prakrit, then Sanskrit |
      | **Founder's status** | Human teacher | 24th Tirthankara |
      - *⚡ key difference* ;- Buddhism denies soul entirely; Jainism says soul exists but is trapped in karma matter.
      - *⚠️ exam trap* ;- "Middle Path is common to both" — FALSE. Only Buddhism. (PYQ 2017)
    
    - **Hinayana vs Mahayana** :- Comparison
      | Aspect | Hinayana (Theravada) | Mahayana |
      |--------|----------------------|----------|
      | **Goal** | Individual salvation (Arhat) | Universal salvation (Bodhisattva) |
      | **Buddha** | Human teacher | Divine being |
      | **Language** | Pali | Sanskrit |
      | **Spread** | Sri Lanka, SE Asia | China, Japan, Tibet |
      | **Ideal** | Arhat (saves self) | Bodhisattva (saves all) |
      - *🧠 analogy* ;- Hinayana Arhat = swims to shore alone. Mahayana Bodhisattva = lifeguard who stays in water until everyone is saved.
  
  - **One-Liners** :- Rapid Recall
    - Buddha: Lumbini (birth) → Bodh Gaya (enlightenment) → Sarnath (sermon) → Kushinagar (death)
    - Four Sights: OSCA = Old man, Sick man, Corpse, Ascetic
    - Four Truths: Dukkha (suffering) → Samudaya (cause) → Nirodha (end) → Magga (path)
    - Middle Path = ONLY Buddhism (NOT Jainism)
    - Anatta (no-self) = unique to Buddhism
    - Three Jewels: Buddha, Dharma, Sangha
    - First Council = Rajagriha under Ajatashatru, Mahakasyapa presided
    - Tripitaka = Vinaya + Sutta + Abhidhamma
    - Theravada = individual salvation; Mahayana = universal salvation
  
  - **Quick Revision** :- Cloze Cards
    - {{Buddha::founder of Buddhism}} was born at {{Lumbini::modern Nepal, NOT India}} in {{563 BCE::6th century BCE}}.
    - Buddha attained enlightenment at {{Bodh Gaya::NOT Sarnath}} under the {{Bodhi (Peepal)::fig tree}} tree at age {{35::not 29 or 80}}.
    - First sermon at {{Sarnath::Deer Park, NOT Bodh Gaya}} is called {{Dharmachakra Pravartana::turning of the wheel of law}}.
    - The Four Noble Truths are {{Dukkha::suffering}}, {{Samudaya::cause of suffering}}, {{Nirodha::end of suffering}}, and {{Magga::path to end suffering}}.
    - {{Middle Path::unique to Buddhism, NOT Jainism}} teaches avoiding extremes of {{luxury::householder life}} and {{severe asceticism::Jain-style fasting}}.
    - {{Anatta::no-self}} means rejection of eternal soul and is unique to {{Buddhism::not Hinduism or Jainism}}.
    - First Buddhist Council presided by {{Mahakasyapa::NOT Kondanna, who was at first sermon}} at {{Rajagriha::under Ajatashatru}}.
    - Second Council at {{Vaishali::NOT Rajagriha}} led to {{first schism::Hinayana vs Mahayana split began here}}.
    - {{Tripitaka::three baskets}} consists of {{Vinaya::monastic rules}}, {{Sutta::Buddha's discourses}}, and {{Abhidhamma::philosophical analysis}}.
    - {{Mahayana::greater vehicle}} emphasizes the {{Bodhisattva::one who delays own nirvana to save all beings}} ideal, unlike {{Hinayana::lesser vehicle, individual salvation only}}.
  
  - **Practice MCQs** :- Self-Test
    - Where did Buddha deliver his first sermon? >>A)
      - Sarnath
      - Bodh Gaya
      - Lumbini
      - Kushinagar
      - **Explanation:** ✅ Sarnath (Deer Park) — this is where Buddha gave the Dharmachakra Pravartana (first turning of the wheel of law). ❌ Bodh Gaya — that is where Buddha attained enlightenment, not the sermon. ❌ Lumbini — his birthplace in modern Nepal. ❌ Kushinagar — where he died (Mahaparinirvana). 🧠 Sermon → Sarnath, both start with S. #[[Extra Card Detail]]
    - Which concept is unique to Buddhism? >>A)
      - Anatta (No-self)
      - Karma
      - Rebirth
      - Non-violence
      - **Explanation:** ✅ Anatta (no-self) — Buddhism uniquely denies the existence of a permanent soul (Atman), which all other Indian religions accept. ❌ Karma — shared by Hinduism and Jainism too. ❌ Rebirth — common to Hinduism and Jainism as well. ❌ Non-violence (Ahimsa) — central to Jainism too (in fact more extreme in Jainism). 🧠 Anatta = the one idea that sets Buddhism apart. #[[Extra Card Detail]]
    - The Middle Path is a teaching of >>A)
      - Buddhism only
      - Both Buddhism and Jainism
      - Jainism only
      - All Indian religions
      - **Explanation:** ✅ Buddhism only — Middle Path means avoiding extremes of luxury and severe asceticism. ❌ Both Buddhism and Jainism — classic UPSC trap (PYQ 2017). Jainism actually prescribes extreme asceticism (fasting to death is acceptable). ❌ Jainism only — the opposite of true. ❌ All Indian religions — Hinduism and Jainism do not teach Middle Path. 🧠 Middle Path = ONLY Buddhism; Jainism = extreme. #[[Extra Card Detail]]
    - Who presided over the First Buddhist Council? >>A)
      - Mahakasyapa
      - Ananda
      - Upali
      - Ashoka
      - **Explanation:** ✅ Mahakasyapa — presided over First Council at Rajagriha under patron Ajatashatru. ❌ Ananda — Buddha's personal attendant, recited the Suttas at the First Council but did NOT preside. ❌ Upali — recited the Vinaya at the First Council but did NOT preside. ❌ Ashoka — patron of the Third Council (Pataliputra), not the First. 🧠 First = Mahakasyapa presided; Ananda + Upali recited. #[[Extra Card Detail]]
    - Which of the following is NOT part of Tripitaka? >>A)
      - Jataka
      - Vinaya Pitaka
      - Sutta Pitaka
      - Abhidhamma Pitaka
      - **Explanation:** ✅ Jataka — these are stories of Buddha's previous lives, considered later literature, NOT one of the three Pitakas. ❌ Vinaya Pitaka — IS part of Tripitaka (monastic rules). ❌ Sutta Pitaka — IS part of Tripitaka (Buddha's discourses). ❌ Abhidhamma Pitaka — IS part of Tripitaka (philosophical analysis, added at Third Council). 🧠 Tripitaka = Vinaya + Sutta + Abhidhamma. Jataka = bonus stories, outside the three baskets. #[[Extra Card Detail]]
    - Consider the following statements:
      1. Buddhism believes in the existence of soul
      2. Buddhism advocates Middle Path
      3. Buddhism was patronized by Ashoka
      Which of the above is/are correct? >>A)
      - 2 and 3 only
      - 1 and 2 only
      - 1, 2, and 3
      - 3 only
      - **Explanation:** ✅ 2 and 3 only. Statement 1 is FALSE — Buddhism rejects the existence of an eternal soul (Anatta = no-self), which is opposite to Hinduism and Jainism. Statement 2 is TRUE — Middle Path (avoiding extremes) is a core Buddhist teaching. Statement 3 is TRUE — Ashoka converted to Buddhism after the Kalinga War and sponsored the Third Buddhist Council at Pataliputra. #[[Extra Card Detail]]
  
  - **Connections** :- Knowledge Web
    - *~builds on* ;; [[Vedic Period]], [[Upanishads]] — arose as response to ritualism
    - *~leads to* ;; [[Mauryan Empire]] — Ashoka's patronage; [[Buddhist Art]] — Stupas, Caves
    - *~compare with* ;; [[Jainism]] — contemporary heterodox school
    - *~current affairs link* ;; Buddha Purnima, Buddhist circuit, India-Sri Lanka ties
  
  - **UPSC Analysis** :- Exam Strategy
    - *🎯 Prelims focus* ;- Four Sights, Four Truths, Eightfold Path, Councils (place + patron + president), Hinayana vs Mahayana differences, Key terms (Nirvana, Anatta, Sangha)
    - *📝 Mains angles* ;- (1) Buddhism's social reform (anti-caste); (2) Buddhism's spread as India's soft power; (3) Decline of Buddhism in India; (4) Buddhist ethics in modern governance
    - *~PYQ pattern* ;- Factual MCQs on councils, "common to both" traps, statement-based Qs
    - *~quote* ;- "Be a lamp unto yourself" — Buddha
  
  - **Mains Answer Framework** :- Essay Structure
    - *~introduction angle* ;- 6th century BCE India saw socio-religious ferment; Buddhism emerged as a revolutionary response
    - *~body points* ;-
      1. Context: Vedic ritualism, Brahmin monopoly, Kshatriya-Vaishya resentment
      2. Core philosophy: Four Truths, Middle Path, rejection of rituals
      3. Social impact: Anti-caste, opened Sangha to all, elevated women's status
      4. Political patronage: Mauryas, Kanishka
      5. Spread and influence: Asia-wide cultural transformation
      6. Decline in India: Brahmanical revival, institutional weakness
    - *~conclusion angle* ;- Buddhism's legacy: democratic Sangha, rational inquiry, India's civilizational gift to Asia
```

---

## Quality Checklist (Pre-Delivery)

### Content ✓
- [ ] Every unfamiliar term has 📌 definition on first use
- [ ] Every concept has "why" (not just "what")
- [ ] Major concepts have multiple 🧠 memory hooks
- [ ] Related concepts have ⚡ contrast tables
- [ ] Common errors flagged with ⚠️ and PYQ year
- [ ] Comparison tables present for similar concepts

### Science-Based Elements ✓
- [ ] Dual coding: Visual map + verbal explanation
- [ ] Elaborative interrogation: "Why" questions answered
- [ ] Retrieval practice: Cloze cards + MCQs + One-liners
- [ ] Chunking: Information grouped logically
- [ ] Interleaving: Contrasts included
- [ ] Multiple encoding: Acronym + Story + Analogy + Etymology

### Structure ✓
- [ ] NO markdown headers — pure indentation
- [ ] All 11 sections present
- [ ] Big Picture ASCII map present
- [ ] Logical order (causal/chronological)
- [ ] One-Liners section present
- [ ] Quick Revision cloze section present
- [ ] 🚀 RAPID REVISION section present
- [ ] Practice MCQs present (varied patterns)
- [ ] Connections section present
- [ ] UPSC Analysis section present
- [ ] Mains Framework present

### Tables ✓ (RemNote Flashcard Format)
- [ ] Flashcard tables have Name column first (Concept)
- [ ] Other columns are Descriptors (generate flashcards)
- [ ] Name column entries are **bolded**
- [ ] Cells are short (< 5 words)
- [ ] No emojis inside table cells
- [ ] ⚠️ notes placed AFTER tables, not inside

### Cloze Cards ✓
- [ ] All answers use `{{}}` syntax
- [ ] Confusable items have hints: `{{answer::hint}}`
- [ ] Hints help recall WITHOUT giving away answer
- [ ] Commonly confused facts have explicit hints

### UPSC-Specific ✓
- [ ] Source references included
- [ ] PYQ frequency noted
- [ ] Prelims focus identified
- [ ] Mains angles provided
- [ ] Current affairs connected
- [ ] Comparison tables for UPSC favorites

### PYQ Integration ✓ (Step 0 Mandatory)
- [ ] `pyq-data/concept-index.json` searched for topic
- [ ] `pyq-data/topic-maps/{slug}.md` read (or noted as not indexed)
- [ ] Section 1 `*~PYQ frequency*` uses real numbers from concept-index
- [ ] Section 1 `*~Prelims weightage*` uses real `prelims_count`
- [ ] At least 2–3 MCQs are real PYQ questions from topic-map
- [ ] RAPID REVISION `🎯 LAST YEARS PYQ PATTERN` uses actual patterns from topic-map
- [ ] Exam traps cross-referenced with actual PYQ questions where relevant
- [ ] `*~PYQ pattern*` in UPSC Analysis uses real question types observed

### Rapid Revision Section ✓
- [ ] 📋 Facts table with memory hooks
- [ ] ⚡ Quick comparisons (bullet points)
- [ ] ⚠️ Trap alerts (common mistakes)
- [ ] 🔢 Numbers to remember
- [ ] 📝 Mains keywords
- [ ] 🎯 PYQ pattern summary
- [ ] Fits on ~1 page when printed

### MCQ Explanations ✓
- [ ] Every MCQ has an `#[[Extra Card Detail]]` explanation child
- [ ] Explanation confirms why correct answer is right
- [ ] Explanation says why each wrong option is wrong (not just "incorrect")
- [ ] Explanation includes memory hook for any confusable item
- [ ] PYQ year cited in explanation for real PYQ questions
- [ ] Explanation uses `✅ / ❌ / 🧠` format for scannability

### Syntax ✓
- [ ] Definitions use `::`
- [ ] Categories use `:-`
- [ ] Memorizable facts use `;;`
- [ ] Context/explanations use `;-`
- [ ] Standard descriptors use `~` prefix
- [ ] Emoji descriptors don't use `~` prefix
- [ ] All Quick Revision answers use `{{}}`
- [ ] Cloze hints use `{{answer::hint}}` format
- [ ] MCQ correct answer is FIRST option
- [ ] Every MCQ has `#[[Extra Card Detail]]` explanation
- [ ] No ⚠️ inside tables
- [ ] References use `[[brackets]]`

### Beginner-Proofing ✓
- [ ] Every dynasty/ruler identified with context
- [ ] Every geographical term located and explained
- [ ] Every foreign term translated
- [ ] Every historical figure identified (not just named)
- [ ] Plain English + analogy for every abstract concept
- [ ] Big Picture map provides orientation

### Cross-Paper Transfer ✓
- [ ] `## Cross-Paper Transfer` section read from topic-map (if mains questions exist)
- [ ] `*~GS4 angle*` filled — at least one ethical dimension identified
- [ ] `*~Essay angle*` filled — at least one abstract philosophical theme
- [ ] `*~interdisciplinary hook*` — single most powerful cross-paper insight stated
- [ ] History topics: ethics angle identified (moral choice in the event)
- [ ] Polity topics: essay angle identified (constitutional philosophy)
- [ ] Economy/Environment topics: GS3 + essay angles both filled

### Conceptual Clarity ✓ (Standard 11 — New)
- [ ] Section 2 has **Before You Read** pre-questions block (3 questions)
- [ ] At least 2 `*💭 self-explain*` prompts in content (before revealing answers)
- [ ] Every major concept has `*~does NOT apply when*` boundary condition
- [ ] At least 1 `*🔨 your example*` generative prompt on abstract concepts
- [ ] Section 9 MCQs has `*~Prelims mode*` and `*~Mains mode*` study instructions
- [ ] Section 11 opens with **Feynman Test** block before Connections
- [ ] Feynman Test has 3-point check: what it is / why it matters / one UPSC trap

---

## Output File Naming

```
[subject]-[topic]-cdf.md

Examples:
- ancient-india-buddhism-cdf.md
- polity-fundamental-rights-cdf.md
- geography-indian-monsoon-cdf.md
- economy-monetary-policy-cdf.md
- environment-biodiversity-hotspots-cdf.md
```

---

## What to NEVER Do

| ❌ Don't | Why |
|---------|-----|
| Use `##` markdown headers | Breaks RemNote hierarchy |
| Use term before defining it | Fails Beginner Test |
| Put ⚠️ inside tables | Breaks table rendering |
| State fact without "why" | Fails Conceptual Bridge |
| Say "important" without explaining why | Empty statement |
| First table row not most fundamental | Misses key comparison |
| End without connections | Creates knowledge island |
| Use plain text in Quick Revision | Must be `{{cloze}}` |
| Skip hints for confusable items | Missing recall support |
| MCQ correct answer not first | RemNote expects first = correct |
| Skip visual elements | Misses dual coding |
| Only one memory hook | Needs multiple encoding channels |
| Ignore PYQ patterns | Missing exam intelligence |
| Skip Mains framework | Incomplete for serious aspirants |
| Skip Rapid Revision section | Missing pre-exam quick reference |
| Put Name column anywhere but first | Breaks RemNote table flashcards |
| Use long text in table cells | Hard to recall (keep < 5 words) |
| Skip Step 0 PYQ lookup | Notes miss real exam patterns — the whole point of this skill |
| Invent PYQ years or question counts | Only use data actually in `pyq-data/` files |
| Use generic "High/Medium/Low" for frequency | Must use real number from concept-index.json |
| Ignore `dimensions_tested` field | Tells you exactly what UPSC focuses on for this topic |
| Skip `*~does NOT apply when*` for major concepts | Shallow pattern-matching fails novel UPSC questions |
| Write `*💭 self-explain*` AFTER the answer | Must appear BEFORE the answer — order is the whole point |
| Skip the Feynman Test block | The most reliable signal of whether understanding is real or illusory |
| Skip `*~Prelims mode*` / `*~Mains mode*` instructions | Transfer-Appropriate Processing — study format must match retrieval format |
| Skip **Before You Read** pre-questions | Without activating prior knowledge, new information doesn't stick as well |
| Skip Cross-Paper Transfer block | Siloed knowledge — you'll know History but not use it in Ethics/Essay |
| Leave `*~GS4 angle*` empty for History topics | Every historical event has a moral dimension — Gandhi, Ambedkar, Partition all do |
| Leave `*~Essay angle*` empty | Essay paper rewards interdisciplinary thinking — every topic has one |
| Skip `*~interdisciplinary hook*` | This is the one sentence that makes revision sessions cross-pollinate |
