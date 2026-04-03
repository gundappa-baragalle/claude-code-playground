# PYQ Reference Skill for RemNote CDF Generator

## Overview

This skill provides UPSC Previous Year Question (PYQ) data to enhance CDF note generation with:
- **5,044 tagged questions** (1995-2025)
- **159 concepts** indexed with metadata
- **128 topic maps** with exam patterns
- **Prelims + Mains** preparation data

## Directory Structure

```
/mnt/skills/user/pyq-reference/
├── SKILL.md                    (this file)
├── questions_tagged.json       (all 5,044 questions with full metadata)
├── concept-index.json          (quick lookup: concept → stats)
├── subject-index.json          (hierarchical navigation)
├── patterns.json               (exam frequency & trends)
└── topic-maps/                 (128 markdown files)
    ├── buddhism.md
    ├── federalism.md
    ├── climate-change.md
    └── ...
```

## When to Use This Skill

**ALWAYS** read relevant PYQ data when generating UPSC CDF notes.

Workflow:
1. User requests notes on a topic (e.g., "Buddhism")
2. Read `concept-index.json` → Check if topic exists
3. Read `topic-maps/{topic}.md` → Get PYQs, patterns, dimensions
4. Integrate into CDF note generation

## How to Use PYQ Data in Notes

### 1. Metadata Section
```markdown
## Metadata :- Source & Relevance
- *~prelims frequency* ;; {{12 questions::2013-2025}} — HIGH priority
- *~mains frequency* ;; {{5 questions::GS1}} — Moderate
- *~last asked* ;; 2024 (Prelims), 2021 (Mains)
- *~dimensions tested* ;; WHAT (65%), WHY (15%), VS (10%), HOW (10%)
```

### 2. Prelims Focus Section
```markdown
## 🎯 Prelims Focus

### High-Frequency Facts (from PYQs)
| Fact | Asked In | Trap Alert |
|------|----------|------------|
| First Buddhist Council at Rajagriha | 2021, 2018, 2015 | ⚠️ Confused with Vaishali |
| Bodhisattva = Mahayana (NOT Hinayana) | 2023, 2016 | ⚠️ Common trap |

### Elimination Strategies
- Council locations: Raja-Vai-Pat-Kash (1-2-3-4)
- Ashoka = 3rd Council (NOT 1st or 4th)
```

### 3. Mains Framework Section
```markdown
## 📝 Mains Framework

### PYQ: [2020, GS1, 10M] "Pala period is the most significant phase in the history of Buddhism in India. Enumerate."

**Answer Structure:**
- **Introduction** (40 words): Define Pala period, state significance claim
- **Body**:
  - Para 1: Revival of Buddhism under Pala patronage
  - Para 2: Nalanda & Vikramashila universities
  - Para 3: Vajrayana development
  - Para 4: Buddhist art & iconography
- **Conclusion**: Lasting legacy despite eventual decline
```

### 4. Rapid Revision Section
```markdown
## 🚀 RAPID REVISION

### From PYQs: Most Tested Facts
1. Buddhist Councils — locations (6 times)
2. Bodhisattva concept — Mahayana only (4 times)
3. Chaitya vs Vihara — difference (3 times)
4. Nirvana definition — NOT heaven (2 times)
```

## Question Schema Reference

Each tagged question contains:

```json
{
  // Original
  "question": "...",
  "year": 2023,
  "paper": "PTGS",
  "correct_option": "B",
  
  // Classification
  "subject": "History",
  "category": "Ancient India", 
  "topic": "Buddhism",
  "syllabus_id": "PTGS.2",
  
  // Analysis
  "dimension": "WHAT",           // WHAT/WHY/HOW/WHEN/WHERE/WHO/VS/IMPACT
  "question_type": "Factual",    // Factual/Conceptual/Analytical/Application
  "difficulty": "Medium",
  
  // Prelims
  "prelims": {
    "priority": "HIGH",
    "factual_hooks": ["Bodhisattva", "Mahayana"],
    "paired_with": ["Jainism", "Ashoka"]
  },
  
  // Mains
  "mains": {
    "themes": ["Social Reform"],
    "answer_structure": {...},
    "interlinkages": ["Mauryan Empire", "Trade Routes"]
  },
  
  // Connections
  "related_concepts": ["Jainism", "Mauryan Empire"],
  "keywords": ["buddha", "sangha", "nirvana"]
}
```

## Concept Index Format

```json
{
  "Buddhism": {
    "question_ids": [123, 456, ...],
    "total_count": 52,
    "prelims_count": 50,
    "mains_count": 2,
    "year_range": [1995, 2024],
    "last_asked": 2024,
    "dimensions_tested": {"WHAT": 33, "WHO": 7, ...},
    "top_keywords": ["buddha", "sangha", "nirvana"],
    "related_concepts": ["Jainism", "Mauryan Empire"],
    "subject": "History",
    "category": "Ancient India"
  }
}
```

## Integration with CDF Note Generation

When generating notes, the CDF skill should:

1. **Check topic existence** in concept-index.json
2. **Read topic map** for PYQ patterns
3. **Apply cognitive principles** with PYQ data:
   - **Dual Coding**: Use PYQ patterns for visual concept maps
   - **Elaborative Interrogation**: WHY/HOW dimensions guide depth
   - **Error Prevention**: Use trap_factor for ⚠️ markers
   - **Retrieval Practice**: Include actual MCQs for practice
   - **Interleaving**: Use related_concepts for connections

## Sample Integration

```markdown
# Buddhism — CDF Notes for UPSC

## 🗺️ Big Picture
[Concept map showing connections identified from related_concepts]

## Core Doctrines
- **Four Noble Truths** :: {{Dukkha, Samudaya, Nirodha, Magga::foundation of Buddhism}}
  - *🎯 PYQ* ;; Asked 2023, 2019, 2015 — know exact sequence
  - *⚠️ trap* ;; Don't confuse with Eightfold Path (PYQ 2023 tested this)

## Buddhist Councils
[Table with trap alerts from prelims.trap_factor]

## 📝 Mains: Pala Period Question
[Framework from mains.answer_structure]
```

## File Sizes (for context management)

- `questions_tagged.json`: ~9 MB (don't load fully)
- `concept-index.json`: ~50 KB (safe to load)
- `topic-maps/*.md`: 2-10 KB each (load as needed)
- `patterns.json`: ~100 KB (safe to load)

## Best Practices

1. **Read concept-index.json first** — lightweight lookup
2. **Load only relevant topic map** — token efficient
3. **Never load full questions_tagged.json** — too large
4. **Use patterns.json for overview** — exam trends
5. **Cite PYQ years** — builds credibility
6. **Flag traps explicitly** — prevents exam mistakes
