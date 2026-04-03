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
| Two-way | `::` | `**Photosynthesis** :: Process converting light to energy` |
| Forward | `:>` | `**Term** :> Definition` |
| Backward | `:<` | `**Term** :< Definition` |
| Disabled | `:-` | `**Category** :- Just a header, no flashcard` |

## Descriptor Cards (Semicolon-based)

Descriptors represent **properties** of concepts. Shown in *italics*. Must be indented under a concept.

| Type | Delimiter | Example |
|------|-----------|---------|
| Forward | `;;` | `*purpose* ;; To generate ATP` |
| Backward | `;<` | `*abbreviation* ;< ATP` |
| Two-way | `;;<` | `*formula* ;;< E=mc²` |
| Disabled | `;-` | `*note* ;- Additional info, no card` |

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

First nested item is always the correct answer. RemNote shuffles options during practice.

| Type | Delimiter | Description |
|------|-----------|-------------|
| Enabled | `>>A)` | Multiple choice flashcard |
| Disabled | `>-A)` | No flashcard |

**Concept/Descriptor variants:**
| Type | Concept | Descriptor |
|------|---------|------------|
| Enabled | `:>>A)` | `;;>A)` |
| Disabled | `:-A)` | `;-A)` |

**Example:**
```markdown
- What is the powerhouse of the cell? >>A)
  - Mitochondria
  - Nucleus
  - Ribosome
  - Golgi apparatus
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
