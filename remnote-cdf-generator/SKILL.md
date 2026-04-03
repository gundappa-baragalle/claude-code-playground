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
```

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

---

## File Architecture (11 Sections)

Every output file contains these sections in order:

### 1. Header & Metadata
```
- **[Topic]** :- UPSC [Subject]
  - *~source* ;- [Standard books with chapter numbers]
  - *~PYQ frequency* ;- [High/Medium/Low with years]
  - *~Prelims weightage* ;- [X questions/year average]
  - *~Mains relevance* ;- [Which GS paper, what themes]
```

### 2. Why Study This? (Motivation + Context)
```
  - **Why Study [Topic]?** :- Motivation
    - *~exam relevance* ;; [Specific papers, frequency]
    - *~conceptual value* ;; [What understanding this unlocks]
    - *~real-world relevance* ;; [Current affairs connections]
    - *📌 beginner note* ;- [Why this matters in the big picture]
```

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
    
    - **🎯 LAST 5 YEARS PYQ PATTERN** :- What UPSC Asks
      - Councils: Place + Patron (Match the following)
      - "Common to both Buddhism and Jainism" — usually FALSE for Middle Path
      - Statement-based: I, II, III — which correct?
```

**Rapid Revision Rules:**
1. **Maximum 1 page** when printed
2. **Tables for facts** — easy to scan
3. **Bullet points for comparisons** — quick to read
4. **Include memory hooks** — for last-minute anchoring
5. **Trap alerts prominent** — prevent silly mistakes
6. **Mains keywords** — for quick essay recall

### 11. Connections & Mains Frameworks

```
  - **Connections** :- Knowledge Web
    - *~builds on* ;; [[Previous Topic]] — [relationship]
    - *~leads to* ;; [[Next Topic]] — [relationship]
    - *~compare with* ;; [[Similar Topic]]
    - *~current affairs link* ;; [Recent news/development]
  
  - **Mains Answer Framework** :- Essay Structure
    - *~introduction angle* ;- [How to open an answer on this topic]
    - *~body points* ;- [Key arguments/aspects to cover]
    - *~conclusion angle* ;- [How to conclude]
    - *~quote/committee* ;- [Relevant quote or committee reference]
```

---

## The TEN Quality Standards

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

### Standard 2: Conceptual Bridge 🧠 (Elaborative Interrogation)

**Rule:** Every concept needs "why" and "how", not just "what".

**The WHY Framework:**
```
- **Concept** :: What it is
  - *~why it arose* ;; What problem/need it addressed
  - *~how it works* ;; The mechanism/process
  - *~significance* ;; Why it matters / impact
  - *~consequence* ;; What happened because of it
  - *🧠 plain English* ;- [Simplest possible explanation]
  - *🧠 analogy* ;- [Connects to familiar everyday experience]
  - *💡 insight* ;- [The deep understanding point]
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

---

## Complete Example Structure

```
- **Buddhism** :- UPSC Ancient History
  - *~source* ;- Tamil Nadu 11 (Ch 6), NCERT Class 6 (Ch 6), NCERT Class 12 (Themes)
  - *~PYQ frequency* ;- High (3-5 questions/year in Prelims)
  - *~Prelims weightage* ;- Direct: 2-3 Qs; Indirect (Mauryas): 2-3 Qs
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
    - {{Buddha}} was born at {{Lumbini}} in {{563 BCE}}.
    - Buddha attained enlightenment at {{Bodh Gaya}} under the {{Bodhi (Peepal)}} tree.
    - First sermon at {{Sarnath}} is called {{Dharmachakra Pravartana}} meaning {{turning of the wheel of law}}.
    - The Four Noble Truths are {{Dukkha}}, {{Samudaya}}, {{Nirodha}}, and {{Magga}}.
    - {{Middle Path}} teaches avoiding extremes of {{luxury}} and {{severe asceticism}}.
    - {{Anatta}} means {{no-self}} and is unique to {{Buddhism}}.
    - Buddhism rejects the concept of {{eternal soul (Atman)}} unlike {{Hinduism}} and {{Jainism}}.
    - First Buddhist Council at {{Rajagriha}} was presided by {{Mahakasyapa}} under {{Ajatashatru}}.
    - {{Tripitaka}} consists of {{Vinaya}} (rules), {{Sutta}} (teachings), and {{Abhidhamma}} (philosophy).
    - {{Mahayana}} Buddhism emphasizes the {{Bodhisattva}} ideal of helping {{all beings}} attain salvation.
  
  - **Practice MCQs** :- Self-Test
    - Where did Buddha deliver his first sermon? >>A)
      - Sarnath
      - Bodh Gaya
      - Lumbini
      - Kushinagar
    - Which concept is unique to Buddhism? >>A)
      - Anatta (No-self)
      - Karma
      - Rebirth
      - Non-violence
    - The Middle Path is a teaching of >>A)
      - Buddhism only
      - Both Buddhism and Jainism
      - Jainism only
      - All Indian religions
    - Who presided over the First Buddhist Council? >>A)
      - Mahakasyapa
      - Ananda
      - Upali
      - Ashoka
    - Which of the following is NOT part of Tripitaka? >>A)
      - Jataka
      - Vinaya Pitaka
      - Sutta Pitaka
      - Abhidhamma Pitaka
    - Consider the following statements:
      1. Buddhism believes in the existence of soul
      2. Buddhism advocates Middle Path
      3. Buddhism was patronized by Ashoka
      Which of the above is/are correct? >>A)
      - 2 and 3 only
      - 1 and 2 only
      - 1, 2, and 3
      - 3 only
  
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

### Rapid Revision Section ✓
- [ ] 📋 Facts table with memory hooks
- [ ] ⚡ Quick comparisons (bullet points)
- [ ] ⚠️ Trap alerts (common mistakes)
- [ ] 🔢 Numbers to remember
- [ ] 📝 Mains keywords
- [ ] 🎯 PYQ pattern summary
- [ ] Fits on ~1 page when printed

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
- [ ] No ⚠️ inside tables
- [ ] References use `[[brackets]]`

### Beginner-Proofing ✓
- [ ] Every dynasty/ruler identified with context
- [ ] Every geographical term located and explained
- [ ] Every foreign term translated
- [ ] Every historical figure identified (not just named)
- [ ] Plain English + analogy for every abstract concept
- [ ] Big Picture map provides orientation

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
