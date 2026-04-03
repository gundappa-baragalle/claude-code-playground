# UPSC PYQ Tagging System v1.0

## 📊 Summary

| Metric | Value |
|--------|-------|
| Total Questions Tagged | **5,044** |
| Year Range | 1995-2025 |
| Unique Topics | 159 |
| Topic Maps Generated | 128 |
| Subjects Covered | 13 |

## 📁 Files Overview

### Core Data Files

| File | Purpose | Size | Use Case |
|------|---------|------|----------|
| `questions_tagged.json` | All questions with full metadata | ~9 MB | Supabase import |
| `concept-index.json` | Quick topic lookup | ~50 KB | Note generation lookup |
| `subject-index.json` | Hierarchical navigation | ~30 KB | Subject-wise browsing |
| `patterns.json` | Exam patterns & frequency | ~100 KB | Study planning |

### Topic Maps (`topic-maps/`)

128 markdown files, one per significant topic. Each contains:
- Question count & year range
- Dimension distribution (WHAT/WHY/HOW/etc.)
- Related concepts
- Actual PYQs (Prelims & Mains)
- Exam patterns & insights

### Skill Integration

| File | Purpose |
|------|---------|
| `PYQ-SKILL.md` | Instructions for using PYQ data in CDF notes |
| `taxonomy.json` | Complete UPSC syllabus concept hierarchy |

## 📈 Statistics

### By Subject
```
Geography:              1,699 questions
History:                1,164 questions
Governance:               882 questions
Polity:                   308 questions
Economy:                  276 questions
International Relations:  233 questions
Science & Technology:     143 questions
Society:                  125 questions
Environment:               75 questions
Internal Security:         53 questions
Ethics:                    31 questions
```

### By Paper
```
Prelims (PTGS):  3,892 questions
GS1:               275 questions
GS3:               268 questions
GS2:               265 questions
GS4:               244 questions
Essay:             100 questions
```

### By Dimension
```
WHAT:    3,314 (66%) — Factual recall
HOW:       466 (9%)  — Process/mechanism
WHY:       347 (7%)  — Causes/reasons
WHEN:      294 (6%)  — Timeline
WHO:       243 (5%)  — People/attribution
WHERE:     150 (3%)  — Location
VS:        129 (3%)  — Comparison
IMPACT:    101 (2%)  — Effects/consequences
```

### Top 20 Most Tested Topics
1. Industries (930)
2. Welfare of Vulnerable Sections (762)
3. Rise of Nationalism (263)
4. Revolutionary Movement (206)
5. United Nations (168)
6. Oceanography (118)
7. Climatology (113)
8. Parliament (90)
9. Geomorphology (84)
10. Minerals & Energy (80)
11. Drainage System (79)
12. Agriculture (78)
13. Energy (70)
14. Social & Religious Reform (63)
15. Continents & Regions (60)
16. Statutory Bodies (58)
17. Gandhian Era (54)
18. Buddhism (52)
19. British Expansion (49)
20. Biogeography (49)

## 🎯 Prelims vs Mains Preparation

### Prelims Focus (3,892 questions)
- **Primary Dimension**: WHAT (66%)
- **Priority Distribution**: HIGH (99%), MEDIUM (0.5%), LOW (0.2%)
- **Key Data**: `trap_factor`, `elimination_hint`, `factual_hooks`

### Mains Focus (1,152 questions)
- **Primary Dimensions**: WHAT (40%), HOW (25%), WHY (15%)
- **Key Data**: `themes`, `answer_structure`, `interlinkages`
- **Papers**: GS1-GS4, Essay

## 🔧 Usage

### For Supabase Import
1. Use `questions_tagged.json`
2. All original fields preserved
3. New fields add conceptual metadata

### For Note Generation (RemNote CDF Skill)
1. Read `concept-index.json` to check topic
2. Read `topic-maps/{topic}.md` for PYQ data
3. Integrate patterns into note sections

### For Study Planning
1. Use `patterns.json` for frequency analysis
2. Use `subject-index.json` for topic navigation
3. Prioritize HIGH frequency topics

## 📝 Schema: Tagged Question

```json
{
  // ORIGINAL (unchanged)
  "question": "...",
  "year": 2023,
  "paper": "PTGS",
  "marks": 2,
  "option_a": "...",
  "option_b": "...",
  "option_c": "...",
  "option_d": "...",
  "correct_option": "B",
  "word_limit": 0,
  
  // ADMINISTRATIVE
  "syllabus_id": "PTGS.2",
  "subject": "History",
  "category": "Ancient India",
  "topic": "Buddhism",
  
  // CONCEPTUAL
  "concept": "Buddhism",
  "dimension": "WHAT",
  "aspect": "WHAT - Buddhism",
  "question_type": "Factual",
  "difficulty": "Medium",
  
  // PRELIMS
  "prelims": {
    "priority": "HIGH",
    "trap_factor": "",
    "elimination_hint": "",
    "factual_hooks": ["buddha", "sangha"],
    "paired_with": ["Jainism", "Mauryan Empire"]
  },
  
  // MAINS
  "mains": {
    "relevance": [],
    "themes": [],
    "answer_structure": {
      "intro_approach": "...",
      "body_points": ["...", "..."],
      "conclusion_approach": "..."
    },
    "interlinkages": [],
    "contemporary_relevance": "",
    "word_limit_suggested": 250
  },
  
  // CONNECTIONS
  "prerequisite_concepts": [],
  "related_concepts": ["Jainism", "Mauryan Empire"],
  "contrast_with": [],
  
  // SEARCH
  "keywords": ["buddha", "buddhism", "sangha", "nirvana"]
}
```

## 🔄 Update Process

To update with new questions:
1. Add new questions to Supabase export
2. Run `tag_questions.py`
3. Run `generate_indexes.py`
4. Copy to output directory

## 📚 Cognitive Science Alignment

This tagging system supports all 10 principles from the RemNote CDF skill:

| Principle | How Supported |
|-----------|---------------|
| Dual Coding | `related_concepts` for visual maps |
| Elaborative Interrogation | `dimension` (WHY/HOW) guides depth |
| Schema Building | `prerequisite_concepts`, `related_concepts` |
| Interleaving | `contrast_with`, cross-topic connections |
| Spaced Retrieval | Year-wise organization enables spacing |
| Active Recall | Actual MCQs for practice |
| Concrete Examples | Real PYQs as examples |
| Error Prevention | `trap_factor` for common mistakes |
| Metacognition | `priority` guides focus |
| Generation Effect | `mains.answer_structure` prompts active thinking |

---

*Generated: 2025*
*Version: 1.0*
*Questions: 5,044*
