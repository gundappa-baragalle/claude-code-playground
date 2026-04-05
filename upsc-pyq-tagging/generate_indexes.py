#!/usr/bin/env python3
"""
Generate Concept Index and Topic Maps from tagged questions.
Creates token-efficient reference files for the RemNote CDF skill.

Output files:
  concept-index.json   — 218 concepts with frequency, dimensions, revision priority
  topic-maps/*.md      — Per-topic files with full MCQ data (HIGH), medium (MEDIUM), stubs (LOW)
  patterns.json        — Exam patterns & frequency analysis
  subject-index.json   — Hierarchical subject navigation
  priority-list.md     — All topics ranked by PYQ count, tiered for study planning
"""

import json
import os
from pathlib import Path
from collections import defaultdict

# ============================================================================
# LOAD INPUT
# ============================================================================

_script_dir = Path(__file__).parent
_candidates = [
    _script_dir / 'questions_tagged.json',
    _script_dir / 'questions_enriched.json',
]
_input_file = next((p for p in _candidates if p.exists()), None)
if not _input_file:
    raise FileNotFoundError("Neither questions_tagged.json nor questions_enriched.json found.")
with open(_input_file, 'r') as f:
    questions = json.load(f)
print(f"Using input file: {_input_file.name}")
print(f"Loaded {len(questions)} tagged questions")


# ============================================================================
# 1. GENERATE CONCEPT INDEX
# ============================================================================

print("\n" + "="*60)
print("GENERATING CONCEPT INDEX")
print("="*60)

concept_index = {}

# Group questions by topic (concept)
topic_questions = defaultdict(list)
for i, q in enumerate(questions):
    topic_questions[q['topic']].append((i, q))

for topic, qs in topic_questions.items():
    years      = [q['year']      for _, q in qs]
    papers     = [q['paper']     for _, q in qs]
    dimensions = [q['dimension'] for _, q in qs]

    prelims_qs = [(i, q) for i, q in qs if q['paper'] == 'PTGS']
    mains_qs   = [(i, q) for i, q in qs if q['paper'] != 'PTGS']

    # Top keywords by frequency
    all_keywords = []
    for _, q in qs:
        all_keywords.extend(q.get('keywords', []))
    kw_freq = defaultdict(int)
    for kw in all_keywords:
        kw_freq[kw] += 1
    top_keywords = [kw for kw, _ in sorted(kw_freq.items(), key=lambda x: -x[1])[:10]]

    # Related concepts (union across all questions)
    related = set()
    for _, q in qs:
        related.update(q.get('related_concepts', []))

    # Dimension distribution
    dim_dist = defaultdict(int)
    for d in dimensions:
        dim_dist[d] += 1

    # Revision priority: based on total PYQ count
    total = len(qs)
    if total >= 10:
        revision_priority = "HIGH"
    elif total >= 5:
        revision_priority = "MEDIUM"
    else:
        revision_priority = "LOW"

    concept_index[topic] = {
        "question_ids":      [i for i, _ in qs],
        "total_count":       total,
        "prelims_count":     len(prelims_qs),
        "mains_count":       len(mains_qs),
        "year_range":        [min(years), max(years)] if years else [0, 0],
        "last_asked":        max(years) if years else 0,
        "papers":            list(set(papers)),
        "dimensions_tested": dict(dim_dist),
        "top_keywords":      top_keywords,
        "related_concepts":  list(related)[:10],
        "subject":           qs[0][1].get('subject', '')   if qs else "",
        "category":          qs[0][1].get('category', '')  if qs else "",
        "syllabus_id":       qs[0][1].get('syllabus_id', '') if qs else "",
        "revision_priority": revision_priority,
    }

output_path = _script_dir / 'concept-index.json'
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(concept_index, f, indent=2, ensure_ascii=False)
print(f"✅ Generated concept index with {len(concept_index)} concepts  →  {output_path}")


# ============================================================================
# 2. GENERATE TOPIC MAPS (Markdown files)
# ============================================================================

print("\n" + "="*60)
print("GENERATING TOPIC MAPS")
print("="*60)

topic_maps_dir = _script_dir / 'topic-maps'
topic_maps_dir.mkdir(exist_ok=True)


def sanitize_filename(name: str) -> str:
    """Convert topic name to a safe filename slug."""
    return (name.lower()
               .replace(' ', '-')
               .replace('&', 'and')
               .replace('/', '-'))


# --------------------------------------------------------------------------
# Helper: format a single Prelims question at HIGH detail level
# Full question text, all options (correct marked), trap, elimination hint,
# factual hooks — everything the skill needs to build a real exam-aware MCQ.
# --------------------------------------------------------------------------
def format_prelims_high(lines: list, idx: int, q: dict) -> None:
    q_text = q['question'].replace('\n', ' ').strip()
    lines.append(f"**[Q{idx}]** [{q['year']}]")
    lines.append(f"> {q_text}")
    lines.append("")

    # Options — mark the correct one with ✅
    correct = q.get('correct_option', '').strip().upper()
    for key, label in [('option_a', 'A'), ('option_b', 'B'),
                        ('option_c', 'C'), ('option_d', 'D')]:
        opt = q.get(key, '').strip()
        if not opt:
            continue
        marker = "✅" if label == correct else "  "
        lines.append(f"  {marker} {label}) {opt}")
    lines.append("")

    # Enrichment data
    trap  = q['prelims'].get('trap_factor', '').strip()
    hint  = q['prelims'].get('elimination_hint', '').strip()
    hooks = [h.strip() for h in q['prelims'].get('factual_hooks', []) if h.strip()]

    if trap:
        lines.append(f"  ⚠️ **Trap:** {trap}")
    if hint:
        lines.append(f"  💡 **Eliminate:** {hint}")
    if hooks:
        lines.append(f"  📌 **Key facts:**")
        for hook in hooks[:4]:
            lines.append(f"     - {hook}")
    lines.append("")


# --------------------------------------------------------------------------
# Helper: format a single Prelims question at MEDIUM detail level
# Full question + options + trap factor only (no hooks/hints — saves tokens).
# --------------------------------------------------------------------------
def format_prelims_medium(lines: list, idx: int, q: dict) -> None:
    q_text = q['question'].replace('\n', ' ').strip()
    lines.append(f"**[Q{idx}]** [{q['year']}] {q_text}")
    lines.append("")

    correct = q.get('correct_option', '').strip().upper()
    for key, label in [('option_a', 'A'), ('option_b', 'B'),
                        ('option_c', 'C'), ('option_d', 'D')]:
        opt = q.get(key, '').strip()
        if not opt:
            continue
        marker = "✅" if label == correct else "  "
        lines.append(f"  {marker} {label}) {opt}")
    lines.append("")

    trap = q['prelims'].get('trap_factor', '').strip()
    if trap:
        lines.append(f"  ⚠️ **Trap:** {trap}")
        lines.append("")


# --------------------------------------------------------------------------
# Helper: format a single Prelims question at LOW detail (stub only).
# Minimal tokens — just enough to know what was asked.
# --------------------------------------------------------------------------
def format_prelims_low(lines: list, idx: int, q: dict) -> None:
    q_text = q['question'].replace('\n', ' ').strip()
    if len(q_text) > 130:
        q_text = q_text[:130] + "..."
    correct = q.get('correct_option', '?')
    dim     = q.get('dimension', '')
    lines.append(f"- **[Q{idx}]** [{q['year']}] {q_text}")
    lines.append(f"  - Dim: {dim} | Ans: {correct}")


# --------------------------------------------------------------------------
# Helper: format a Mains question with full answer framework.
# Word budget discipline (intro / body / conclusion) comes from the
# enrichment schema's answer_structure field.
# --------------------------------------------------------------------------
def format_mains_full(lines: list, idx: int, q: dict) -> None:
    q_text  = q['question'].replace('\n', ' ').strip()
    marks   = q.get('marks', 0)
    paper   = q.get('paper', '')
    dim     = q.get('dimension', '')
    mains   = q.get('mains', {})
    wl      = mains.get('word_limit_suggested', 0)
    themes  = mains.get('themes', [])
    struct  = mains.get('answer_structure', {})
    intro   = (struct.get('intro_approach') or '').strip()
    body    = [p.strip() for p in struct.get('body_points', []) if p and p.strip()]
    concl   = (struct.get('conclusion_approach') or '').strip()
    links   = [l.strip() for l in mains.get('interlinkages', []) if l and l.strip()]
    contmp  = (mains.get('contemporary_relevance') or '').strip()

    meta_parts = [f"Paper: {paper}", f"Dim: {dim}"]
    if marks:
        meta_parts.append(f"{marks}m")
    if wl:
        meta_parts.append(f"~{wl}w")
    lines.append(f"**[{q['year']}]** {q_text}")
    lines.append(f"  *{' | '.join(meta_parts)}*")

    if themes:
        lines.append(f"  🏷️ Themes: {', '.join(themes)}")

    # Answer framework — only emit if there is actual content
    has_framework = any([intro, body, concl])
    if has_framework:
        lines.append("")
        lines.append("  **Answer Framework:**")
        if wl:
            # Distribute word budget: intro ~15%, body ~65%, conclusion ~20%
            w_intro = max(30, int(wl * 0.15))
            w_body  = max(80, int(wl * 0.65))
            w_concl = max(25, int(wl * 0.20))
            lines.append(f"  *(~{wl} words: intro {w_intro}w / body {w_body}w / conclusion {w_concl}w)*")
        if intro:
            lines.append(f"  - 🔑 **Intro:** {intro}")
        if body:
            lines.append(f"  - 📋 **Body:**")
            for pt in body[:6]:
                lines.append(f"      • {pt}")
        if concl:
            lines.append(f"  - 🎯 **Conclusion:** {concl}")

    if links:
        lines.append(f"  🔗 Interlinkages: {', '.join(links[:4])}")
    if contmp:
        lines.append(f"  🌐 Contemporary: {contmp}")

    lines.append("")


# --------------------------------------------------------------------------
# Main topic-map generator
# --------------------------------------------------------------------------
def generate_topic_map(topic: str, qs: list, index_data: dict) -> str:
    lines = []

    # ── Header ──────────────────────────────────────────────────────────────
    total    = index_data['total_count']
    rev_pri  = index_data['revision_priority']
    pri_icon = {"HIGH": "🔴", "MEDIUM": "🟡", "LOW": "🟢"}.get(rev_pri, "")

    lines.append(f"# {topic}")
    lines.append("")
    lines.append(f"**Subject:** {index_data['subject']} > {index_data['category']}")
    lines.append(f"**Syllabus ID:** {index_data['syllabus_id']}")
    lines.append(f"**Total Questions:** {index_data['total_count']} "
                 f"(Prelims: {index_data['prelims_count']}, Mains: {index_data['mains_count']})")
    lines.append(f"**Year Range:** {index_data['year_range'][0]} – {index_data['year_range'][1]}")
    lines.append(f"**Last Asked:** {index_data['last_asked']}")
    lines.append(f"**Revision Priority:** {pri_icon} {rev_pri}")
    lines.append("")

    # ── Keywords ────────────────────────────────────────────────────────────
    if index_data['top_keywords']:
        lines.append("## Keywords")
        lines.append(", ".join(index_data['top_keywords']))
        lines.append("")

    # ── Dimensions Tested ───────────────────────────────────────────────────
    lines.append("## Dimensions Tested")
    for dim, count in sorted(index_data['dimensions_tested'].items(), key=lambda x: -x[1]):
        lines.append(f"- **{dim}**: {count} questions")
    lines.append("")

    # ── Related Concepts ────────────────────────────────────────────────────
    if index_data['related_concepts']:
        lines.append("## Related Concepts")
        for concept in index_data['related_concepts'][:8]:
            lines.append(f"- {concept}")
        lines.append("")

    # ── Prelims Questions ────────────────────────────────────────────────────
    prelims_qs = [(i, q) for i, q in qs if q['paper'] == 'PTGS']
    if prelims_qs:
        lines.append("## Prelims Questions")
        lines.append("")

        # Bucket by priority; within each bucket sort by year descending
        high_qs   = sorted([(i, q) for i, q in prelims_qs
                            if q['prelims'].get('priority') == 'HIGH'],
                           key=lambda x: -x[1]['year'])
        medium_qs = sorted([(i, q) for i, q in prelims_qs
                            if q['prelims'].get('priority') == 'MEDIUM'],
                           key=lambda x: -x[1]['year'])
        low_qs    = sorted([(i, q) for i, q in prelims_qs
                            if q['prelims'].get('priority') == 'LOW'],
                           key=lambda x: -x[1]['year'])

        if high_qs:
            lines.append("### 🔴 HIGH Priority — Full MCQ + Trap Intelligence")
            lines.append("")
            lines.append("*Use these verbatim as Practice MCQs in CDF notes.*")
            lines.append("")
            for i, q in high_qs:
                format_prelims_high(lines, i, q)

        if medium_qs:
            lines.append("### 🟡 MEDIUM Priority — Full Options")
            lines.append("")
            for i, q in medium_qs:
                format_prelims_medium(lines, i, q)

        if low_qs:
            lines.append("### 🟢 LOW Priority — Reference Stubs")
            lines.append("")
            for i, q in low_qs:
                format_prelims_low(lines, i, q)
            lines.append("")

    # ── Mains Questions ──────────────────────────────────────────────────────
    mains_qs = [(i, q) for i, q in qs if q['paper'] not in ('PTGS', 'Essay')]
    if mains_qs:
        lines.append("## Mains Questions")
        lines.append("")
        lines.append("*Each question includes answer framework with word budget.*")
        lines.append("")

        by_paper = defaultdict(list)
        for i, q in mains_qs:
            by_paper[q['paper']].append((i, q))

        for paper in ['GS1', 'GS2', 'GS3', 'GS4']:
            if paper not in by_paper:
                continue
            lines.append(f"### {paper}")
            lines.append("")
            for i, q in sorted(by_paper[paper], key=lambda x: -x[1]['year']):
                format_mains_full(lines, i, q)

    # ── Essay Questions ──────────────────────────────────────────────────────
    essay_qs = [(i, q) for i, q in qs if q['paper'] == 'Essay']
    if essay_qs:
        lines.append("## Essay Questions")
        lines.append("")
        for i, q in sorted(essay_qs, key=lambda x: -x[1]['year']):
            q_text = q['question'].replace('\n', ' ').strip()
            lines.append(f"- **[{q['year']}]** {q_text}")
        lines.append("")

    # ── Cross-Paper Transfer ─────────────────────────────────────────────────
    # Aggregate interlinkages, themes, contemporary relevance from all mains Qs.
    # This is the "use this topic in other GS papers" intelligence.
    all_links   = []
    all_themes  = []
    all_cr      = []
    for _, q in qs:
        if q['paper'] == 'PTGS':
            continue
        for l in q['mains'].get('interlinkages', []):
            l = l.strip()
            if l:
                all_links.append(l)
        for t in q['mains'].get('themes', []):
            t = t.strip()
            if t:
                all_themes.append(t)
        cr = (q['mains'].get('contemporary_relevance') or '').strip()
        if cr:
            all_cr.append(cr)

    # Deduplicate while preserving insertion order
    unique_links  = list(dict.fromkeys(all_links))
    unique_themes = list(dict.fromkeys(all_themes))

    if unique_links or unique_themes:
        lines.append("## Cross-Paper Transfer")
        lines.append("")
        lines.append("*Use these when this topic appears in other GS papers or Essay.*")
        lines.append("")
        if unique_links:
            lines.append("### GS Paper Connections")
            for link in unique_links[:10]:
                lines.append(f"- {link}")
            lines.append("")
        if unique_themes:
            lines.append("### Essay & Thematic Angles")
            for theme in unique_themes[:8]:
                lines.append(f"- {theme}")
            lines.append("")
        if all_cr:
            # Pick the longest (usually most informative) contemporary relevance
            best_cr = max(all_cr, key=len)
            lines.append("### Contemporary Relevance")
            lines.append(best_cr)
            lines.append("")

    # ── Exam Patterns & Insights ─────────────────────────────────────────────
    lines.append("## Exam Patterns & Insights")
    lines.append("")

    # Dominant dimension
    if index_data['dimensions_tested']:
        top_dim = max(index_data['dimensions_tested'].items(), key=lambda x: x[1])
        pct = int(top_dim[1] / total * 100) if total else 0
        lines.append(f"- **Most tested dimension:** {top_dim[0]} "
                     f"({top_dim[1]}/{total} = {pct}% of questions)")

    # Question-type breakdown (prelims only)
    type_dist = defaultdict(int)
    for _, q in qs:
        if q['paper'] == 'PTGS':
            type_dist[q.get('question_type', 'Factual')] += 1
    if type_dist:
        type_str = ", ".join(f"{t}: {c}" for t, c in
                             sorted(type_dist.items(), key=lambda x: -x[1]))
        lines.append(f"- **Question types (Prelims):** {type_str}")

    # Recency trend
    year_counts = defaultdict(int)
    for _, q in qs:
        year_counts[q['year']] += 1
    recent = sum(year_counts.get(y, 0) for y in range(2020, 2026))
    if recent > 0:
        lines.append(f"- **Recent frequency (2020–2025):** {recent} questions")
    elif max(index_data['year_range']) < 2015:
        lines.append(f"- **Trend:** Not asked since {index_data['last_asked']} — "
                     f"lower probability but classic syllabus topic")

    # Aggregate trap intelligence: collect unique, non-empty trap_factors
    traps_seen = set()
    unique_traps = []
    for _, q in qs:
        if q['paper'] != 'PTGS':
            continue
        trap = q['prelims'].get('trap_factor', '').strip()
        if trap and trap not in traps_seen:
            traps_seen.add(trap)
            unique_traps.append(trap)
    if unique_traps:
        lines.append("")
        lines.append("### Common Trap Patterns on This Topic")
        for t in unique_traps[:5]:
            lines.append(f"- {t}")

    lines.append("")
    return "\n".join(lines)


# Generate topic maps for all topics with ≥ 3 questions
generated_count = 0
for topic, qs_list in topic_questions.items():
    if len(qs_list) >= 3:
        index_data = concept_index.get(topic, {})
        if index_data:
            content  = generate_topic_map(topic, qs_list, index_data)
            filename = sanitize_filename(topic) + ".md"
            filepath = topic_maps_dir / filename
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            generated_count += 1

print(f"✅ Generated {generated_count} topic map files  →  {topic_maps_dir}")


# ============================================================================
# 3. GENERATE PATTERNS ANALYSIS
# ============================================================================

print("\n" + "="*60)
print("GENERATING PATTERNS ANALYSIS")
print("="*60)

patterns = {
    "overview": {
        "total_questions": len(questions),
        "year_range": [min(q['year'] for q in questions), max(q['year'] for q in questions)],
        "papers": list(set(q['paper'] for q in questions))
    },
    "by_subject": {},
    "by_year": {},
    "by_paper": {},
    "high_frequency_topics": [],
    "dimension_patterns": {},
    "prelims_traps": [],
    "mains_themes": {}
}

# By subject
for q in questions:
    subj = q['subject']
    if subj not in patterns['by_subject']:
        patterns['by_subject'][subj] = {"total": 0, "prelims": 0, "mains": 0, "topics": set()}
    patterns['by_subject'][subj]['total'] += 1
    patterns['by_subject'][subj]['topics'].add(q['topic'])
    if q['paper'] == 'PTGS':
        patterns['by_subject'][subj]['prelims'] += 1
    else:
        patterns['by_subject'][subj]['mains'] += 1

for subj in patterns['by_subject']:
    patterns['by_subject'][subj]['topics'] = list(patterns['by_subject'][subj]['topics'])

# By year
for q in questions:
    year = str(q['year'])
    if year not in patterns['by_year']:
        patterns['by_year'][year] = {"total": 0, "PTGS": 0, "GS1": 0, "GS2": 0, "GS3": 0, "GS4": 0, "Essay": 0}
    patterns['by_year'][year]['total'] += 1
    patterns['by_year'][year][q['paper']] = patterns['by_year'][year].get(q['paper'], 0) + 1

# By paper
for q in questions:
    paper = q['paper']
    if paper not in patterns['by_paper']:
        patterns['by_paper'][paper] = {"total": 0, "top_subjects": defaultdict(int), "top_topics": defaultdict(int)}
    patterns['by_paper'][paper]['total'] += 1
    patterns['by_paper'][paper]['top_subjects'][q['subject']] += 1
    patterns['by_paper'][paper]['top_topics'][q['topic']] += 1

for paper in patterns['by_paper']:
    subj_items  = sorted(patterns['by_paper'][paper]['top_subjects'].items(), key=lambda x: -x[1])[:10]
    topic_items = sorted(patterns['by_paper'][paper]['top_topics'].items(),   key=lambda x: -x[1])[:15]
    patterns['by_paper'][paper]['top_subjects'] = dict(subj_items)
    patterns['by_paper'][paper]['top_topics']   = dict(topic_items)

# High-frequency topics
topic_freq = defaultdict(int)
for q in questions:
    topic_freq[q['topic']] += 1
patterns['high_frequency_topics'] = [
    {"topic": t, "count": c, "subject": concept_index.get(t, {}).get('subject', '')}
    for t, c in sorted(topic_freq.items(), key=lambda x: -x[1])[:30]
]

# Dimension patterns by paper
for q in questions:
    paper = q['paper']
    dim   = q['dimension']
    if paper not in patterns['dimension_patterns']:
        patterns['dimension_patterns'][paper] = defaultdict(int)
    patterns['dimension_patterns'][paper][dim] += 1

for paper in patterns['dimension_patterns']:
    patterns['dimension_patterns'][paper] = dict(patterns['dimension_patterns'][paper])

# Mains themes
mains_themes = defaultdict(int)
for q in questions:
    if q['paper'] != 'PTGS':
        for theme in q['mains'].get('themes', []):
            mains_themes[theme] += 1
patterns['mains_themes'] = dict(sorted(mains_themes.items(), key=lambda x: -x[1]))

patterns_path = _script_dir / 'patterns.json'
with open(patterns_path, 'w', encoding='utf-8') as f:
    json.dump(patterns, f, indent=2, ensure_ascii=False)
print(f"✅ Generated patterns analysis  →  {patterns_path}")


# ============================================================================
# 4. GENERATE SUBJECT-WISE INDEX
# ============================================================================

print("\n" + "="*60)
print("GENERATING SUBJECT-WISE INDEX")
print("="*60)

subject_index = {}
for q in questions:
    subj  = q['subject']
    cat   = q['category']
    topic = q['topic']

    if subj not in subject_index:
        subject_index[subj] = {}
    if cat not in subject_index[subj]:
        subject_index[subj][cat] = {}
    if topic not in subject_index[subj][cat]:
        subject_index[subj][cat][topic] = {
            "count": 0, "prelims": 0, "mains": 0,
            "years": [],
            "file": sanitize_filename(topic) + ".md",
            "revision_priority": concept_index.get(topic, {}).get('revision_priority', 'LOW'),
        }

    subject_index[subj][cat][topic]["count"] += 1
    subject_index[subj][cat][topic]["years"].append(q['year'])
    if q['paper'] == 'PTGS':
        subject_index[subj][cat][topic]["prelims"] += 1
    else:
        subject_index[subj][cat][topic]["mains"] += 1

for subj in subject_index:
    for cat in subject_index[subj]:
        for topic in subject_index[subj][cat]:
            years = subject_index[subj][cat][topic]["years"]
            subject_index[subj][cat][topic]["years"] = sorted(set(years), reverse=True)[:10]

subject_index_path = _script_dir / 'subject-index.json'
with open(subject_index_path, 'w', encoding='utf-8') as f:
    json.dump(subject_index, f, indent=2, ensure_ascii=False)
print(f"✅ Generated subject-wise index  →  {subject_index_path}")


# ============================================================================
# 5. GENERATE PRIORITY STUDY LIST
# ============================================================================

print("\n" + "="*60)
print("GENERATING PRIORITY STUDY LIST")
print("="*60)

def generate_priority_list(concept_index: dict) -> str:
    """
    Rank all topics by PYQ count across 4 tiers.
    The single most actionable output for study planning:
    you always know exactly which topic to study next.
    """
    total_questions = sum(d['total_count'] for d in concept_index.values())
    year_min = min(d['year_range'][0] for d in concept_index.values() if d['year_range'][0])
    year_max = max(d['year_range'][1] for d in concept_index.values() if d['year_range'][1])

    # Tier thresholds (will scale naturally as more questions are enriched)
    TIER1 = 30   # Elite — must-cover
    TIER2 = 15   # High
    TIER3 = 7    # Medium
    # Below TIER3 = LOW

    lines = []
    lines.append("# UPSC PYQ Priority Study List")
    lines.append("")
    lines.append(f"Ranked by PYQ frequency across **{total_questions} questions** "
                 f"({year_min}–{year_max}).")
    lines.append("**Study in this order — higher count = higher exam ROI.**")
    lines.append("")
    lines.append("## Tier Guide")
    lines.append(f"| Tier | PYQ Count | Meaning |")
    lines.append(f"|------|-----------|---------|")
    lines.append(f"| 🔴 Tier 1 | {TIER1}+ | Elite — always in exam |")
    lines.append(f"| 🟠 Tier 2 | {TIER2}–{TIER1-1} | High — cover before exam |")
    lines.append(f"| 🟡 Tier 3 | {TIER3}–{TIER2-1} | Medium — cover if time permits |")
    lines.append(f"| 🟢 Tier 4 | 3–{TIER3-1} | Low — targeted gap-fill |")
    lines.append("")
    lines.append("*P = Prelims | M = Mains | Last = last year asked*")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Sort all topics by total_count descending
    all_topics = sorted(concept_index.items(), key=lambda x: -x[1]['total_count'])

    # Group by subject (preserving rank order within subject groups)
    by_subject = defaultdict(list)
    subject_totals = defaultdict(int)
    global_rank = 1

    for topic, data in all_topics:
        subj = data.get('subject', 'Other')
        by_subject[subj].append((global_rank, topic, data))
        subject_totals[subj] += data['total_count']
        global_rank += 1

    # Emit subjects ordered by their total PYQ weight
    for subj in sorted(by_subject.keys(), key=lambda s: -subject_totals[s]):
        entries = by_subject[subj]
        s_total = subject_totals[subj]
        lines.append(f"## {subj}  ·  {s_total} PYQs across {len(entries)} topics")
        lines.append("")
        lines.append("| Rank | Topic | PYQs | P | M | Last | Tier | File |")
        lines.append("|------|-------|------|---|---|------|------|------|")

        for rank, topic, data in entries:
            t   = data['total_count']
            p   = data['prelims_count']
            m   = data['mains_count']
            last = data['last_asked']

            if t >= TIER1:
                tier = "🔴 T1"
            elif t >= TIER2:
                tier = "🟠 T2"
            elif t >= TIER3:
                tier = "🟡 T3"
            else:
                tier = "🟢 T4"

            slug = sanitize_filename(topic) + ".md"
            lines.append(f"| {rank} | {topic} | {t} | {p} | {m} | {last} | {tier} | {slug} |")

        lines.append("")

    lines.append("---")
    lines.append(f"*{len(concept_index)} topics indexed. "
                 f"Regenerate after enriching more batches.*")
    return "\n".join(lines)


priority_list_content = generate_priority_list(concept_index)
priority_list_path = _script_dir / 'priority-list.md'
with open(priority_list_path, 'w', encoding='utf-8') as f:
    f.write(priority_list_content)
print(f"✅ Generated priority study list  →  {priority_list_path}")


# ============================================================================
# SUMMARY
# ============================================================================

print("\n" + "="*60)
print("GENERATION COMPLETE — SUMMARY")
print("="*60)

tier1 = sum(1 for d in concept_index.values() if d['revision_priority'] == 'HIGH')
tier2 = sum(1 for d in concept_index.values() if d['revision_priority'] == 'MEDIUM')
tier3 = sum(1 for d in concept_index.values() if d['revision_priority'] == 'LOW')

print(f"""
Files Generated:
  concept-index.json   — {len(concept_index)} concepts indexed
  topic-maps/          — {generated_count} markdown files
                         (HIGH: full MCQ + trap | MEDIUM: options + trap | LOW: stubs)
  patterns.json        — Exam patterns & frequency analysis
  subject-index.json   — Hierarchical subject navigation
  priority-list.md     — {len(concept_index)} topics ranked by PYQ count

Revision Priority Breakdown:
  🔴 HIGH  (≥10 PYQs): {tier1} topics
  🟡 MEDIUM (5–9 PYQs): {tier2} topics
  🟢 LOW    (<5 PYQs): {tier3} topics

Next step:
  cp upsc-pyq-tagging/concept-index.json remnote-cdf-generator/pyq-data/
  cp -r upsc-pyq-tagging/topic-maps/     remnote-cdf-generator/pyq-data/
  cp upsc-pyq-tagging/priority-list.md   remnote-cdf-generator/pyq-data/
  bash remnote-cdf-generator/build_package.sh
""")
