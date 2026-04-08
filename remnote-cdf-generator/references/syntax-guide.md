# RemNote Import Syntax Complete Reference

This document contains all syntax combinations for creating RemNote-compatible flashcards via text import.

## Basic Flashcards

| Type | Delimiter | Example | Result |
|------|-----------|---------|--------|
| Forward | `>>` or `==` | `Question >> Answer` | Show question, ask for answer |
| Backward | `<<` | `Question << Answer` | Show answer, ask for question |
| Two-way | `<>` or `><` | `Term <> Definition` | Both directions |
| Disabled | `>-` | `Info >- Details` | No flashcard generated |

## Concept Cards (Colon-based)

Concepts represent **things** — objects, ideas, or entities. Shown in **bold**.

| Type | Delimiter | Example |
|------|-----------|---------|
| Two-way (default) | `::` | `**Photosynthesis** :: Process converting light to energy` |
| Forward only | `:>` | `**Term** :> Definition` (name→def, no reverse card) |
| Backward only | `:<` | `**Term** :< Definition` (def→name only) |
| Disabled | `:-` | `**Category** :- Just a header, no flashcard` |



## Multi-line Flashcards

Use when the answer contains multiple points/items that should be shown together.

### Basic Multi-line
| Type | Delimiter | Description |
|------|-----------|-------------|
| Forward | `>>>` | Front side, children are back |
| Backward | `<<<` | Children shown, ask for parent |
| Two-way | `<><` | Both directions |

**Example:**
```markdown
- Main phases of the cell cycle >>>
  - Interphase
  - Mitotic phase
  - Cytokinesis
```

### Concept/Descriptor Multi-line
| Type | Concept | Descriptor |
|------|---------|------------|
| Forward | `:>>` | `;;>` |
| Backward | `:<<` | `;<<` |

## List-Answer Flashcards

Use when order matters and items should be numbered.

| Type | Delimiter | Description |
|------|-----------|-------------|
| Forward | `>>1.` | Show question, recall numbered list |
| Backward | `<<1.` | Show list, recall question |
| Two-way | `<>1.` | Both directions |
| Disabled | `>-1.` | No flashcard |

**Concept/Descriptor variants:**
| Type | Concept | Descriptor |
|------|---------|------------|
| Forward | `:>>1.` | `;;>1.` |
| Backward | `:<<1.` | `;<<1.` |
| Two-way | `::1.` | `;;<1.` |
| Disabled | `:-1.` | `;-1.` |

**Example:**
```markdown
- Steps to balance a chemical equation >>1.
  - Write the unbalanced equation
  - Count atoms on each side
  - Add coefficients to balance
  - Verify atom counts match
```

## Multiple-Choice Flashcards

First nested child is always the correct answer. RemNote shuffles options during practice.

| Type | Delimiter | Description |
|------|-----------|-------------|
| Enabled | `>>A)` | Multiple choice flashcard |
| Disabled | `>-A)` | No flashcard |

**Concept/Descriptor variants:**
| Type | Concept | Descriptor |
|------|---------|------------|
| Enabled | `:>>A)` | `;;>A)` |
| Disabled | `:-A)` | `;-A)` |

**Example (Basic):**
```markdown
- What is the powerhouse of the cell? >>A)
  - Mitochondria
  - Nucleus
  - Ribosome
  - Golgi apparatus
```

**Example (CDF-native — correct pattern for Section 12 PYQ Archive):**
```markdown
- **PYQ:2023-powerhouse** :-
  - Which of the following is the powerhouse of the cell? >>A)
    - Mitochondria          ← ALWAYS first child = correct answer
    - Nucleus
    - Ribosome
    - Golgi apparatus
    - ✅ Explanation #[[Extra Card Detail]]
      - ✅ Correct (Mitochondria): site of ATP synthesis via oxidative phosphorylation
      - ❌ Nucleus: stores DNA, does not produce energy
      - ⚠️ Trap: ribosome is common wrong pick (protein synthesis, not energy)
      - 🧠 Hook: "Mito = mighty energy factory"
```
> ⛔ **NEVER use `;;>A)` for MCQs in CDF notes.** `;;>A)` is a Descriptor MCQ type — it generates a different card format and breaks PYQ anchor linking. Always use `>>A)` for all MCQs (Section 9 practice MCQs AND Section 12 PYQ Archive).

**⚠️ CRITICAL — Extra Card Detail (ECD) with MCQs — PYQ ANCHOR SYSTEM:**

In CDF notes, every PYQ is wrapped in a **named outer parent anchor Rem** (`**PYQ:YEAR-slug** :-`) so that concepts elsewhere in the file can link to it via `[[PYQ:year-slug]]`. The MCQ is nested *inside* the anchor as a child. The `#[[Extra Card Detail]]` explanation is placed as a **sibling of the answer options** (direct child of `>>A)`), not nested under the correct answer.

```markdown
✅ CORRECT — anchor as outer parent, ECD as sibling of options:
- **PYQ:2023-powerhouse** :-                        ← outer parent anchor (named, no flashcard)
  - Which of the following is the powerhouse? >>A)  ← MCQ nested inside anchor
    - Mitochondria                                  ← first child = correct answer
    - Nucleus
    - Ribosome
    - Golgi apparatus
    - ✅ Explanation #[[Extra Card Detail]]          ← sibling of options; shown after answering
      - ✅ Correct (Mitochondria): [why right]
      - ❌ Nucleus: [why wrong]
      - ⚠️ Trap: [common confusion]
      - 🧠 Hook: [memory device]

❌ WRONG — anchor as child inside MCQ (breaks [[PYQ:year-slug]] linking):
- Which of the following is the powerhouse? >>A)
  - **PYQ:2023-powerhouse** :-   ← anchor must be outer parent, not a child
  - Mitochondria
  ...

❌ WRONG — ECD nested under correct answer (only shows for that one option):
- Question? >>A)
  - Mitochondria
    - ✅ Explanation #[[Extra Card Detail]]   ← grandchild of MCQ; only appears for Mitochondria option
  - Nucleus
  - Ribosome
```

**For Section 9 Practice MCQs** (no PYQ anchor needed — synthetic questions only):
```markdown
- Which of the following best describes demand-pull inflation? >>A)
  - Rise in prices caused by excess aggregate demand over supply
  - Rise in prices caused by increase in production costs
  - Fall in supply due to external supply shocks
  - Rise in interest rates by the central bank
  - ✅ Explanation #[[Extra Card Detail]]
    - ✅ Correct: demand-pull = demand > supply → prices rise
    - ❌ Cost increase = cost-push inflation, not demand-pull
    - ⚠️ Trap: supply shock = stagflation trigger, not demand-pull
    - 🧠 Hook: "Pull = demand pulling prices up"
```

## Cloze Deletions

Hide parts of text that you want to recall. Each cloze is independent.

**Syntax:** `{{text to hide}}`

**With hints:** `{{hidden text}}{({hint text})}`

**Examples:**
```markdown
- The {{mitochondria}} is the powerhouse of the cell.
- {{Water}} has the chemical formula {{H₂O}}.
- {{Paris}}{({Capital city})} is located in {{France}}{({Country})}.
```

## Indentation and Structure

### Rules
1. Use consistent spacing (2 spaces, 4 spaces, or tabs)
2. Dashes `-` at line start are optional
3. Nesting level determines hierarchy

### Example Structure
```markdown
- **Parent Concept** :: Definition of parent
  - *property one* ;; value
  - *property two* ;; value
    - Supporting detail
    - Another detail
  - **Child Concept** :: Nested concept definition
    - *its property* ;; its value
```

## Extra Card Detail

Add supplementary information shown after answering.

**Syntax:** Add `#[[Extra Card Detail]]` tag to nested content.

```markdown
- Question >> Answer
  - Additional context #[[Extra Card Detail]]
```

## Tables for Flashcards

Tables automatically generate Concept/Descriptor flashcards in RemNote.

**Structure:**
- Column 1 (Name) = Concepts
- Other columns = Descriptors

**Example:**
```markdown
| Element | Symbol | Atomic Number | Category |
|---------|--------|---------------|----------|
| **Hydrogen** | H | 1 | Nonmetal |
| **Helium** | He | 2 | Noble gas |
| **Lithium** | Li | 3 | Alkali metal |
```

## Complete Syntax Quick Reference Table

### Concepts (Bold, Colon-based)
| Direction | Basic | Multi-line | List-Answer | Multiple-Choice |
|-----------|-------|------------|-------------|-----------------|
| Forward | `:>` | `:>>` | `:>>1.` | `:>>A)` |
| Backward | `:<` | `:<<` | `:<<1.` | — |
| Two-way | `::` | — | `::1.` | — |
| Disabled | `:-` | — | `:-1.` | `:-A)` |

### Descriptors (Italics, Semicolon-based)
| Direction | Basic | Multi-line | List-Answer | Multiple-Choice |
|-----------|-------|------------|-------------|-----------------|
| Forward | `;;` | `;;>` | `;;>1.` | `;;>A)` |
| Backward | `;<` | `;<<` | `;<<1.` | — |
| Two-way | `;;<` | — | `;;<1.` | — |
| Disabled | `;-` | — | `;-1.` | `;-A)` |

### Basic (Non-CDF)
| Direction | Basic | Multi-line | List-Answer | Multiple-Choice |
|-----------|-------|------------|-------------|-----------------|
| Forward | `>>` | `>>>` | `>>1.` | `>>A)` |
| Backward | `<<` | `<<<` | `<<1.` | — |
| Two-way | `<>` | `<><` | `<>1.` | — |
| Disabled | `>-` | — | `>-1.` | `>-A)` |

## Special Characters and Formatting

### References (Links)
- Use `[[Term]]` to create references to other concepts
- Creates bidirectional links in RemNote

### Bold and Italics
- `**bold**` for concepts in running text
- `*italics*` for descriptors in running text

### Code
- Use backticks for inline code: `` `code` ``
- Use triple backticks for code blocks

### Math (LaTeX)
- Inline: `$formula$`
- Block: `$$formula$$`

---

## CDF Descriptor Naming Convention

```
Standard descriptors:
  *~definition* :: ...    *~born* ;; 1869    *~source* ;- NCERT Ch 5

Emoji descriptors (no ~ prefix):
  *📌 beginner note* ;-    *🧠 analogy* ;-      *🧠 mnemonic* ;-
  *🧠 etymology* ;-        *🧠 story* ;-         *🧠 visual* ;-
  *⚡ vs [Other]* ;-       *⚠️ exam trap* ;-     *🔗 connects to* ;;
  *💡 insight* ;-          *🎯 Prelims focus* ;- *📝 Mains angle* ;-
  *~does NOT apply when* ;-  *💭 self-explain* ;-  *🔨 your example* ;-
  *🧪 try first* ;-

Mathematical / Flow descriptors:
  *~formula* ;;             → The mathematical relationship (e.g., MV = PQ)
  *~mechanism* ;-           → Step-by-step causal chain: A ↑ → B ↓ → C ↑
  *~graph* ;-               → ASCII graph showing the relationship visually
  *~prerequisite* ;-        → "To understand this, first understand: [X]"
  *~builds from* ;-         → "This follows from [earlier concept] because..."
  *~why it matters here* ;- → One-line bridge to the next concept
```

## Flashcard Type Decision Rule

```
Will UPSC ask this fact directly?   YES → ;;    NO → ;-
Need two-way recall?                YES → ;;<
Main concept definition?            Use ::  (always two-way)
MCQ (Section 9 or 12)?              Use >>A)  — NEVER ;;>A)
```

## Section 7 One-Liner Pattern

One-liners generate flashcards ONLY when written with `;;`:

```
CORRECT (generates flashcard):
  - National Income = ;; NNP at Factor Cost
  - GNP formula ;; GDP + NFIA
  - India's GDP base year (since 2015) ;; 2011-12

WRONG (plain text, no flashcard):
  - National Income = NNP at Factor Cost → Back of card
  - GNP = GDP + NFIA → Back of card
```

`→ Back of card` is a RemNote UI label — it has no effect in a file.

## Output File Naming

```
[subject]-[topic]-cdf.md  (lowercase, hyphens, drop prepositions/articles/conjunctions)

Examples:
  polity-fundamental-rights-cdf.md
  economy-water-food-security-cdf.md   ← "Water and Food Security" drops "and"
  ancient-india-buddhism-cdf.md
  geography-indian-monsoon-cdf.md
  gs4-ethics-integrity-cdf.md
  essay-democracy-india-cdf.md
```
