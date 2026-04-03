# UPSC PYQ Tagging System — Handoff Guide for New Chat

## Quick Start Prompt
Copy-paste this to start your new chat:

```
I have an existing UPSC PYQ tagging project. Files are at:
- `/mnt/user-data/uploads/questions.json` — 5,044 source questions
- `/mnt/user-data/outputs/upsc-pyq-tagging/` — all generated files
- `/mnt/user-data/outputs/upsc-pyq-tagging.zip` — 1.4 MB complete package

Also have RemNote CDF Generator skill at:
- `/mnt/user-data/outputs/remnote-cdf-generator/` — SKILL.md, syntax-guide.md, examples.md

Please review the README.md and continue development. I want: [YOUR CHOICE FROM OPTIONS BELOW]
```

---

## Project Status: COMPLETE (Phase 1 & 2)

### Files Created

| File | Location | Description |
|------|----------|-------------|
| `taxonomy.json` | `/mnt/user-data/outputs/upsc-pyq-tagging/` | 10 subjects, ~160 topics with keyword mappings |
| `tag_questions.py` | Same | Tagging engine (keyword matching, dimensions, difficulty) |
| `questions_tagged.json` | Same | **All 5,044 questions tagged** (9 MB) |
| `concept-index.json` | Same | 159 concepts indexed (170 KB) |
| `topic-maps/` | Same | **128 markdown files** — one per topic with 3+ questions |
| `patterns.json` | Same | Exam frequency & trend analysis |
| `subject-index.json` | Same | Hierarchical navigation |
| `PYQ-SKILL.md` | Same | Integration guide for RemNote CDF |
| `README.md` | Same | Master index |
| `upsc-pyq-tagging.zip` | `/mnt/user-data/outputs/` | Complete 1.4 MB package |

---

## Tagged Question Schema

Each question now has:

```json
{
  // ORIGINAL (unchanged)
  "question", "year", "paper", "marks", "option_a/b/c/d", "correct_option", "word_limit",
  
  // ADMINISTRATIVE
  "syllabus_id": "GS1.1",    // Maps to UPSC syllabus
  "subject": "History",
  "category": "Ancient India",
  "topic": "Buddhism",
  
  // CONCEPTUAL
  "concept": "Buddhism",
  "dimension": "WHAT",       // WHAT/WHY/HOW/WHEN/WHERE/WHO/VS/IMPACT
  "aspect": "Core Teachings",
  "question_type": "factual", // factual/analytical/evaluative/applied
  "difficulty": "medium",
  "confidence_score": 0.85,
  
  // PRELIMS SPECIFIC
  "prelims": {
    "priority": "HIGH",
    "trap_factor": "",       // ⚠️ NEEDS AI ENRICHMENT
    "elimination_hint": "",  // ⚠️ NEEDS AI ENRICHMENT
    "factual_hooks": ["Ashoka", "Dhamma"],
    "paired_with": []
  },
  
  // MAINS SPECIFIC
  "mains": {
    "relevance": "HIGH",
    "themes": ["Philosophy", "Polity"],
    "answer_structure": {    // ⚠️ NEEDS AI ENRICHMENT
      "intro_approach": "",
      "body_points": [],
      "conclusion_approach": ""
    },
    "interlinkages": [],
    "contemporary_relevance": "",
    "word_limit_suggested": 200
  },
  
  // CONNECTIONS
  "prerequisite_concepts": [], // ⚠️ EMPTY
  "related_concepts": ["Jainism", "Vedic Age"],
  "contrast_with": [],        // ⚠️ EMPTY
  
  // SEARCH
  "keywords": ["Buddha", "Sangha", "Tripitaka"]
}
```

---

## Known Quality Issues to Fix

### 1. **GS4 Ethics Misclassification** (HIGH PRIORITY)
- Ethics questions getting tagged as "Industries" due to keyword overlap
- Fix: Improve taxonomy.json with Ethics-specific keywords, add paper-based priority

### 2. **Prelims Priority Skew**
- 3,863 of 3,892 prelims questions marked HIGH
- Fix: Refine scoring logic in tag_questions.py

### 3. **Empty Fields** (Need AI Review)
- `trap_factor` — empty for all questions
- `elimination_hint` — empty for all questions
- `prerequisite_concepts` — empty for all
- `contrast_with` — empty for all
- `mains.answer_structure` — has templates but needs real content

### 4. **Some Mains Themes Empty**
- Questions without detected themes

---

## Pending Improvements (Choose in New Chat)

### Option A: AI Review Pass
Enrich empty fields for top 50 topics using Claude API:
- Generate `trap_factor` (why wrong options are tempting)
- Generate `elimination_hint` (how to eliminate wrong options)
- Fill `prerequisite_concepts` and `contrast_with`
- Write real `answer_structure` for mains questions

### Option B: Update RemNote CDF Skill
Modify `/mnt/user-data/outputs/remnote-cdf-generator/SKILL.md` to:
- Auto-fetch PYQs for any concept being studied
- Generate "Exam Pattern" section in notes
- Add "Top PYQs" flashcards

### Option C: Generate Sample Complete Note
Create one exemplary CDF note (e.g., Buddhism) that:
- Uses tagged PYQ data
- Shows ideal integration
- Serves as template for all topics

### Option D: Fix Taxonomy Issues
- Rework Ethics classification
- Add missing keywords
- Rerun tagging on all 5,044 questions

### Option E: Build PYQ Practice Interface
Create React artifact that:
- Filters questions by topic/year/dimension
- Shows hints progressively
- Tracks practice history

---

## Statistics Summary

**By Subject:**
| Subject | Count |
|---------|-------|
| Geography | 1,699 |
| History | 1,164 |
| Governance | 882 |
| Polity | 308 |
| Economy | 276 |
| International Relations | 233 |
| Science & Technology | 143 |
| Society | 125 |
| Environment | 75 |
| Internal Security | 53 |
| Ethics | 31 |

**By Dimension:**
- WHAT: 3,314 (66%)
- HOW: 466 (9%)
- WHY: 347 (7%)
- WHEN: 294 (6%)
- WHO: 243 (5%)
- WHERE: 150 (3%)
- VS: 129 (3%)
- IMPACT: 101 (2%)

**Top Topics by Question Count:**
1. Industries (930) — ⚠️ inflated due to misclassification
2. Welfare of Vulnerable Sections (762)
3. Rise of Nationalism (263)
4. Revolutionary Movement (206)
5. United Nations (168)
6. Oceanography (118)
7. Climatology (113)
8. Parliament (90)
9. Geomorphology (84)
10. Buddhism (52)

---

## Related Project: RemNote CDF Generator

**Location:** `/mnt/user-data/outputs/remnote-cdf-generator/`

**Files:**
- `SKILL.md` (v6, 940 lines) — Main skill with 10 cognitive science principles
- `syntax-guide.md` — RemNote CDF syntax reference
- `examples.md` — Sample notes

**Cognitive Science Principles Embedded:**
1. Active Recall
2. Spaced Repetition
3. Elaborative Interrogation
4. Dual Coding
5. Concrete Examples
6. Interleaving
7. Retrieval Practice
8. Generation Effect
9. Testing Effect
10. Desirable Difficulties

---

## File Locations Quick Reference

```
/mnt/user-data/uploads/
  └── questions.json          # Original 5,044 questions

/mnt/user-data/outputs/
  ├── upsc-pyq-tagging.zip    # 1.4 MB complete package
  ├── upsc-pyq-tagging/
  │   ├── README.md
  │   ├── taxonomy.json
  │   ├── tag_questions.py
  │   ├── questions_tagged.json
  │   ├── generate_indexes.py
  │   ├── concept-index.json
  │   ├── patterns.json
  │   ├── subject-index.json
  │   ├── PYQ-SKILL.md
  │   └── topic-maps/         # 128 .md files
  │
  └── remnote-cdf-generator/
      ├── SKILL.md
      ├── syntax-guide.md
      └── examples.md
```

---

## Recommended Next Steps Priority

1. **Fix Ethics misclassification** — Quick win, high impact
2. **AI review pass on top 20 topics** — Quality improvement
3. **Integrate PYQ into CDF skill** — Connects both projects
4. **Build practice interface** — User-facing value

Good luck with your continued development! 🚀
