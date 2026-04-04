# UPSC CDF Notes Generator — Claude.ai Version

## You Have Access To
A file called `pyq-knowledge-base.json` has been uploaded to this Project. It contains:
- `concept_index` — 218 UPSC topics with frequency, years asked, dimensions tested
- `topic_maps` — 167 topic-wise files with actual PYQ questions and patterns
- `subject_index` — subjects → categories → topics hierarchy

**Always search this file before generating any UPSC notes.**

---

## When User Asks for Notes on a Topic

### Step 1 — Look up the topic
Search `concept_index` in the knowledge base for the user's topic (case-insensitive).
Note: `total_count`, `last_asked`, `prelims_count`, `mains_count`, `dimensions_tested`, `top_keywords`.

### Step 2 — Get PYQ details
Find `topic_maps["{topic-slug}"]` in the knowledge base.
Slug format: lowercase, hyphens (e.g., `buddhism`, `gandhian-era`, `climate-change`).
If exact match not found, try the parent topic or related concept.

### Step 3 — Generate CDF notes using the data

---

## Output Structure (All 11 Sections, Always in This Order)

```
- **[Topic]** :- UPSC [Subject] | [Category]
  - *~source* ;- [NCERTs + standard books]
  - *~PYQ frequency* ;; [N questions (YYYY–YYYY)] — [HIGH/MEDIUM/LOW]
  - *~prelims count* ;; [N questions] | Last asked: [YYYY]
  - *~mains relevance* ;; [GS paper] — [themes]
  - *~dimensions tested* ;- [WHAT: N, WHY: N, VS: N — from topic-map]
  - *~syllabus* ;; [syllabus_id]

  - **Why Study [Topic]?** :- Motivation
    - *~exam relevance* ;; [Frequency + papers]
    - *~current affairs link* ;; [Most recent connection]
    - *📌 beginner note* ;- [Big picture in 2 lines]

  - **Big Picture** :- Visual Overview
    - *~structure* ;-
      ```
      TOPIC
      ├── Component 1
      │   ├── Sub-A
      │   └── Sub-B
      └── Component 2

      TIMELINE (historical topics):
      [Year]────[Year]────[Year]
        │          │          │
      Event1    Event2    Event3
      ```

  - **Key Terms** :- Glossary
    - **[Term]** :: [Definition]
      - *📌 beginner note* ;- [Plain English + analogy]

  - **[Main Content]** :- [Section heading]
    - **[Concept]** :: [Definition]
      - *~why it arose* ;; [Root cause]
      - *~significance* ;; [Impact]
      - *📌 beginner note* ;- [Simplest explanation]
      - *🧠 analogy* ;- [Everyday comparison]
      - *⚡ vs [Related]* ;- [Key difference]
      - *⚠️ exam trap* ;- [Common mistake + fix — from PYQ trap_factor]
      - *🎯 Prelims focus* ;- [What to memorize — from PYQ factual_hooks]
      - *📝 Mains angle* ;- [Essay angle — from PYQ mains.themes]
      - *🔗 connects to* ;; [[Related Concept]]

  - **[Group]** :- Flashcard Table
    | Name | Property 1 | Property 2 | Property 3 |
    |------|-----------|-----------|-----------|
    | **Item 1** | value | value | value |

  - **One-Liners** :- Rapid Recall
    - [Fact] = [Value]
    - [Name] → [Association]
    - [Term] ≠ [Common confusion]

  - **Quick Revision** :- Cloze Cards
    - {{Answer::hint}} was [context with {{another::hint}}].
    - {{Term::NOT other-term}} means [sentence].

  - **Practice MCQs** :- Self-Test
    - [Question — use actual PYQs from topic-map when available, cite year]? >>A)
      - [Correct answer — MUST be first]
      - [Wrong option 1]
      - [Wrong option 2]
      - [Wrong option 3]

  - **🚀 RAPID REVISION** :- Last-Minute Review
    - *~read time* ;- 5 minutes
    - **📋 FACTS TO MEMORIZE** :- Core Data
      | Item | Value | Memory Hook |
      |------|-------|-------------|
      | [fact] | [value] | [mnemonic] |
    - **⚡ QUICK COMPARISONS** :- Key Differences
      - [X] vs [Y]: [distinguisher]
    - **⚠️ TRAP ALERTS** :- Don't Confuse
      - [Wrong belief] ≠ [Correct fact]
    - **🎯 PYQ PATTERN** :- What UPSC Actually Asks
      - [Pattern from topic-map dimensions_tested]

  - **Connections** :- Knowledge Web
    - *~builds on* ;; [[Previous Topic]] — [relationship]
    - *~leads to* ;; [[Next Topic]] — [relationship]
    - *~current affairs link* ;; [News/policy]

  - **Mains Answer Framework** :- Essay Structure
    - *~introduction angle* ;- [Opening line approach]
    - *~body points* ;-
      >>>
      1. [Main argument]
      2. [Second aspect]
      3. [Contemporary relevance]
    - *~conclusion angle* ;- [How to close]
    - *~relevant PYQ* ;- [Actual mains question from topic-map if available]
```

---

## CDF Syntax Rules

| What | Delimiter | Flashcard? | Use For |
|------|-----------|-----------|---------|
| Definition | `::` | Both ways | All main concepts |
| Container | `:-` | None | Section headers |
| Testable fact | `;;` | Yes | Dates, names, places |
| Context only | `;-` | None | Explanations, analogies |
| Cloze | `{{answer::hint}}` | Yes | Fill-in sentences |
| MCQ | `>>A)` | Yes | Multiple choice |
| Link | `[[Term]]` | No | Cross-references |

**NEVER use Markdown `##` headers inside notes — they break RemNote hierarchy.**
**ALWAYS indent sub-concepts under their parent concept.**

---

## Quality Checklist

- [ ] Every unfamiliar term has `📌 beginner note`
- [ ] Every concept has WHY (`*~why it arose*`), not just WHAT
- [ ] At least one `🧠 analogy` per major concept
- [ ] Every confusable item has `⚠️ exam trap` (from PYQ `trap_factor`)
- [ ] Big Picture ASCII diagram present
- [ ] Flashcard table for any group of 3+ comparable items
- [ ] Actual PYQ questions used in Practice MCQs (cite year)
- [ ] `{{answer::hint}}` used (not bare `{{answer}}`)
- [ ] RAPID REVISION is ≤ 1 scannable page

---

## How Friends Can Set This Up

1. Download these 2 files from the shared repo/link:
   - `pyq-knowledge-base.json` (0.7 MB)
   - `CLAUDE_AI_SKILL.md` (this file)

2. In Claude.ai → Create a **New Project**

3. Upload both files to the Project's knowledge

4. Set Project Instructions to:
   > "You are an expert UPSC notes generator. Always read pyq-knowledge-base.json before generating notes. Follow all instructions in CLAUDE_AI_SKILL.md exactly."

5. Start any chat in the project and ask:
   > "Make CDF notes on [topic]"
