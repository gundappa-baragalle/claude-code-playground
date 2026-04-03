#!/usr/bin/env python3
"""
Generate Concept Index and Topic Maps from tagged questions.
Creates token-efficient reference files for the RemNote CDF skill.
"""

import json
import os
from pathlib import Path
from collections import defaultdict

# Load tagged questions (works with both questions_tagged.json and questions_enriched.json)
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
    # Extract stats
    years = [q['year'] for _, q in qs]
    papers = [q['paper'] for _, q in qs]
    dimensions = [q['dimension'] for _, q in qs]
    
    prelims_qs = [(i, q) for i, q in qs if q['paper'] == 'PTGS']
    mains_qs = [(i, q) for i, q in qs if q['paper'] != 'PTGS']
    
    # Collect all keywords
    all_keywords = []
    for _, q in qs:
        all_keywords.extend(q['keywords'])
    keyword_freq = defaultdict(int)
    for kw in all_keywords:
        keyword_freq[kw] += 1
    top_keywords = sorted(keyword_freq.items(), key=lambda x: -x[1])[:10]
    
    # Collect traps (from factual_hooks that appear multiple times - likely confusion points)
    factual_hooks = []
    for _, q in qs:
        factual_hooks.extend(q['prelims'].get('factual_hooks', []))
    
    # Collect related concepts
    related = set()
    for _, q in qs:
        related.update(q['related_concepts'])
    
    # Dimension distribution
    dim_dist = defaultdict(int)
    for d in dimensions:
        dim_dist[d] += 1
    
    concept_index[topic] = {
        "question_ids": [i for i, _ in qs],
        "total_count": len(qs),
        "prelims_count": len(prelims_qs),
        "mains_count": len(mains_qs),
        "year_range": [min(years), max(years)] if years else [0, 0],
        "last_asked": max(years) if years else 0,
        "papers": list(set(papers)),
        "dimensions_tested": dict(dim_dist),
        "top_keywords": [kw for kw, _ in top_keywords],
        "related_concepts": list(related)[:10],
        "subject": qs[0][1]['subject'] if qs else "",
        "category": qs[0][1]['category'] if qs else "",
        "syllabus_id": qs[0][1]['syllabus_id'] if qs else ""
    }

# Save concept index
output_path = _script_dir / 'concept-index.json'
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(concept_index, f, indent=2, ensure_ascii=False)

print(f"✅ Generated concept index with {len(concept_index)} concepts")
print(f"   Saved to: {output_path}")

# ============================================================================
# 2. GENERATE TOPIC MAPS (Markdown files)
# ============================================================================

print("\n" + "="*60)
print("GENERATING TOPIC MAPS")
print("="*60)

topic_maps_dir = _script_dir / 'topic-maps'
topic_maps_dir.mkdir(exist_ok=True)

def sanitize_filename(name):
    """Convert topic name to valid filename."""
    return name.lower().replace(' ', '-').replace('&', 'and').replace('/', '-')

def generate_topic_map(topic: str, qs: list, index_data: dict) -> str:
    """Generate markdown content for a topic."""
    
    lines = []
    
    # Header
    lines.append(f"# {topic}")
    lines.append("")
    lines.append(f"**Subject:** {index_data['subject']} > {index_data['category']}")
    lines.append(f"**Syllabus ID:** {index_data['syllabus_id']}")
    lines.append(f"**Total Questions:** {index_data['total_count']} (Prelims: {index_data['prelims_count']}, Mains: {index_data['mains_count']})")
    lines.append(f"**Year Range:** {index_data['year_range'][0]} - {index_data['year_range'][1]}")
    lines.append(f"**Last Asked:** {index_data['last_asked']}")
    lines.append("")
    
    # Keywords
    lines.append("## Keywords")
    lines.append(", ".join(index_data['top_keywords']))
    lines.append("")
    
    # Dimensions Tested
    lines.append("## Dimensions Tested")
    for dim, count in sorted(index_data['dimensions_tested'].items(), key=lambda x: -x[1]):
        lines.append(f"- **{dim}**: {count} questions")
    lines.append("")
    
    # Related Concepts
    lines.append("## Related Concepts")
    for concept in index_data['related_concepts'][:8]:
        lines.append(f"- {concept}")
    lines.append("")
    
    # Prelims Questions
    prelims_qs = [(i, q) for i, q in qs if q['paper'] == 'PTGS']
    if prelims_qs:
        lines.append("## Prelims Questions")
        lines.append("")
        
        # Group by year (most recent first)
        by_year = defaultdict(list)
        for i, q in prelims_qs:
            by_year[q['year']].append((i, q))
        
        for year in sorted(by_year.keys(), reverse=True)[:10]:  # Last 10 years
            lines.append(f"### {year}")
            for i, q in by_year[year]:
                q_text = q['question'][:200] + "..." if len(q['question']) > 200 else q['question']
                q_text = q_text.replace('\n', ' ')
                lines.append(f"- **[Q{i}]** {q_text}")
                lines.append(f"  - Dimension: {q['dimension']} | Type: {q['question_type']} | Priority: {q['prelims']['priority']}")
                if q['correct_option']:
                    lines.append(f"  - Answer: {q['correct_option']}")
            lines.append("")
    
    # Mains Questions
    mains_qs = [(i, q) for i, q in qs if q['paper'] != 'PTGS' and q['paper'] != 'Essay']
    if mains_qs:
        lines.append("## Mains Questions")
        lines.append("")
        
        by_paper = defaultdict(list)
        for i, q in mains_qs:
            by_paper[q['paper']].append((i, q))
        
        for paper in ['GS1', 'GS2', 'GS3', 'GS4']:
            if paper in by_paper:
                lines.append(f"### {paper}")
                for i, q in sorted(by_paper[paper], key=lambda x: -x[1]['year']):
                    q_text = q['question'][:300] + "..." if len(q['question']) > 300 else q['question']
                    q_text = q_text.replace('\n', ' ')
                    lines.append(f"- **[{q['year']}]** {q_text}")
                    lines.append(f"  - Dimension: {q['dimension']} | Marks: {q['marks']}")
                    if q['mains']['themes']:
                        lines.append(f"  - Themes: {', '.join(q['mains']['themes'])}")
                lines.append("")
    
    # Essay Questions
    essay_qs = [(i, q) for i, q in qs if q['paper'] == 'Essay']
    if essay_qs:
        lines.append("## Essay Questions")
        lines.append("")
        for i, q in sorted(essay_qs, key=lambda x: -x[1]['year']):
            q_text = q['question'][:300] + "..." if len(q['question']) > 300 else q['question']
            lines.append(f"- **[{q['year']}]** {q_text}")
        lines.append("")
    
    # Exam Patterns
    lines.append("## Exam Patterns & Insights")
    lines.append("")
    
    # Most common dimension
    if index_data['dimensions_tested']:
        top_dim = max(index_data['dimensions_tested'].items(), key=lambda x: x[1])
        lines.append(f"- **Most tested dimension:** {top_dim[0]} ({top_dim[1]} times)")
    
    # Frequency trend
    year_counts = defaultdict(int)
    for _, q in qs:
        year_counts[q['year']] += 1
    recent_years = [year_counts.get(y, 0) for y in range(2020, 2026)]
    if sum(recent_years) > 0:
        lines.append(f"- **Recent frequency (2020-2025):** {sum(recent_years)} questions")
    
    lines.append("")
    
    return "\n".join(lines)

# Generate topic maps for all topics with significant questions
generated_count = 0
for topic, qs_list in topic_questions.items():
    if len(qs_list) >= 3:  # Only topics with 3+ questions
        index_data = concept_index.get(topic, {})
        if index_data:
            content = generate_topic_map(topic, qs_list, index_data)
            filename = sanitize_filename(topic) + ".md"
            filepath = topic_maps_dir / filename
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            generated_count += 1

print(f"✅ Generated {generated_count} topic map files")
print(f"   Saved to: {topic_maps_dir}")

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

# Convert sets to lists for JSON
for subj in patterns['by_subject']:
    patterns['by_subject'][subj]['topics'] = list(patterns['by_subject'][subj]['topics'])

# By year
for q in questions:
    year = str(q['year'])
    if year not in patterns['by_year']:
        patterns['by_year'][year] = {"total": 0, "PTGS": 0, "GS1": 0, "GS2": 0, "GS3": 0, "GS4": 0, "Essay": 0}
    patterns['by_year'][year]['total'] += 1
    patterns['by_year'][year][q['paper']] = patterns['by_year'][year].get(q['paper'], 0) + 1

# By paper with topics
for q in questions:
    paper = q['paper']
    if paper not in patterns['by_paper']:
        patterns['by_paper'][paper] = {"total": 0, "top_subjects": defaultdict(int), "top_topics": defaultdict(int)}
    patterns['by_paper'][paper]['total'] += 1
    patterns['by_paper'][paper]['top_subjects'][q['subject']] += 1
    patterns['by_paper'][paper]['top_topics'][q['topic']] += 1

# Convert to regular dicts and get top items
for paper in patterns['by_paper']:
    subj_items = sorted(patterns['by_paper'][paper]['top_subjects'].items(), key=lambda x: -x[1])[:10]
    topic_items = sorted(patterns['by_paper'][paper]['top_topics'].items(), key=lambda x: -x[1])[:15]
    patterns['by_paper'][paper]['top_subjects'] = dict(subj_items)
    patterns['by_paper'][paper]['top_topics'] = dict(topic_items)

# High frequency topics
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
    dim = q['dimension']
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

# Save patterns
patterns_path = _script_dir / 'patterns.json'
with open(patterns_path, 'w', encoding='utf-8') as f:
    json.dump(patterns, f, indent=2, ensure_ascii=False)

print(f"✅ Generated patterns analysis")
print(f"   Saved to: {patterns_path}")

# ============================================================================
# 4. GENERATE SUBJECT-WISE INDEX
# ============================================================================

print("\n" + "="*60)
print("GENERATING SUBJECT-WISE INDEX")
print("="*60)

subject_index = {}
for q in questions:
    subj = q['subject']
    cat = q['category']
    topic = q['topic']
    
    if subj not in subject_index:
        subject_index[subj] = {}
    if cat not in subject_index[subj]:
        subject_index[subj][cat] = {}
    if topic not in subject_index[subj][cat]:
        subject_index[subj][cat][topic] = {
            "count": 0,
            "prelims": 0,
            "mains": 0,
            "years": [],
            "file": sanitize_filename(topic) + ".md"
        }
    
    subject_index[subj][cat][topic]["count"] += 1
    subject_index[subj][cat][topic]["years"].append(q['year'])
    if q['paper'] == 'PTGS':
        subject_index[subj][cat][topic]["prelims"] += 1
    else:
        subject_index[subj][cat][topic]["mains"] += 1

# Clean up years (unique, sorted)
for subj in subject_index:
    for cat in subject_index[subj]:
        for topic in subject_index[subj][cat]:
            years = subject_index[subj][cat][topic]["years"]
            subject_index[subj][cat][topic]["years"] = sorted(set(years), reverse=True)[:10]

subject_index_path = _script_dir / 'subject-index.json'
with open(subject_index_path, 'w', encoding='utf-8') as f:
    json.dump(subject_index, f, indent=2, ensure_ascii=False)

print(f"✅ Generated subject-wise index")
print(f"   Saved to: {subject_index_path}")

# ============================================================================
# SUMMARY
# ============================================================================

print("\n" + "="*60)
print("GENERATION COMPLETE - SUMMARY")
print("="*60)
print(f"""
Files Generated:
1. questions_tagged.json    - {len(questions)} tagged questions (8.9 MB)
2. concept-index.json       - {len(concept_index)} concepts indexed
3. topic-maps/              - {generated_count} markdown files
4. patterns.json            - Exam patterns & frequency analysis
5. subject-index.json       - Hierarchical subject navigation

Ready for:
- Supabase import (questions_tagged.json)
- RemNote CDF skill integration (topic-maps/, concept-index.json)
- Pattern-based study planning (patterns.json)
""")
