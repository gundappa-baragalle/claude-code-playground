#!/usr/bin/env python3
"""
UPSC PYQ Tagging Engine v1.0
Tags 5,044 questions with full conceptual metadata for Prelims + Mains preparation.

Output Schema:
- Administrative: syllabus_id, subject, category, topic
- Conceptual: concept, dimension, aspect
- Prelims: priority, trap_factor, elimination_hint, factual_hooks
- Mains: relevance, themes, answer_structure, key_arguments, interlinkages
- Connections: prerequisite_concepts, related_concepts, contrast_with
- Search: keywords
"""

import json
import re
from pathlib import Path
from collections import defaultdict
from typing import Dict, List, Optional, Tuple

# Load taxonomy
with open('/home/claude/pyq-tagging/taxonomy.json', 'r') as f:
    TAXONOMY = json.load(f)

# Load questions
with open('/mnt/user-data/uploads/questions.json', 'r') as f:
    raw_data = json.load(f)
    
# Flatten questions
ALL_QUESTIONS = []
for record in raw_data:
    if 'json_result' in record:
        ALL_QUESTIONS.extend(record['json_result'])

print(f"Loaded {len(ALL_QUESTIONS)} questions")

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def clean_text(text: str) -> str:
    """Normalize text for matching."""
    if not text:
        return ""
    text = text.lower()
    text = re.sub(r'[^\w\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def extract_keywords_from_question(question: str) -> List[str]:
    """Extract significant words from question text."""
    # Common stopwords to ignore
    stopwords = {
        'the', 'a', 'an', 'is', 'are', 'was', 'were', 'be', 'been', 'being',
        'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'could',
        'should', 'may', 'might', 'must', 'shall', 'can', 'need', 'dare',
        'which', 'what', 'who', 'whom', 'whose', 'where', 'when', 'why', 'how',
        'this', 'that', 'these', 'those', 'it', 'its', 'they', 'their', 'them',
        'of', 'in', 'to', 'for', 'with', 'on', 'at', 'by', 'from', 'as', 'into',
        'through', 'during', 'before', 'after', 'above', 'below', 'between',
        'under', 'again', 'further', 'then', 'once', 'here', 'there', 'all',
        'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor',
        'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 'just',
        'and', 'but', 'if', 'or', 'because', 'until', 'while', 'although',
        'consider', 'following', 'statement', 'statements', 'given', 'above',
        'below', 'correct', 'incorrect', 'true', 'false', 'select', 'answer',
        'code', 'codes', 'using', 'regarding', 'respect', 'reference', 'context',
        'one', 'two', 'three', 'four', 'many', 'much', 'any', 'both', 'neither',
        'either', 'none', 'also', 'however', 'therefore', 'thus', 'hence'
    }
    
    words = clean_text(question).split()
    keywords = [w for w in words if len(w) > 2 and w not in stopwords]
    return keywords

def match_topic(question: str, options: str = "") -> Tuple[str, str, str, str, List[str], float]:
    """
    Match question to best topic in taxonomy.
    Returns: (subject, category, topic, syllabus_id, matched_keywords, confidence)
    """
    text = clean_text(question + " " + options)
    
    best_match = None
    best_score = 0
    best_keywords = []
    
    for subject, subject_data in TAXONOMY['subjects'].items():
        for category, cat_data in subject_data.get('categories', {}).items():
            for topic, topic_data in cat_data.get('topics', {}).items():
                keywords = topic_data.get('keywords', [])
                
                # Count keyword matches
                matched = []
                for kw in keywords:
                    kw_lower = kw.lower()
                    if kw_lower in text:
                        matched.append(kw)
                        
                score = len(matched)
                
                # Boost score for multiple matches
                if score > 1:
                    score = score * 1.5
                
                if score > best_score:
                    best_score = score
                    best_keywords = matched
                    # Get syllabus IDs for this subject
                    syllabus_ids = subject_data.get('syllabus_ids', [])
                    syllabus_id = syllabus_ids[0] if syllabus_ids else ""
                    best_match = (subject, category, topic, syllabus_id, matched, score)
    
    if best_match:
        return best_match
    else:
        return ("General", "Miscellaneous", "Uncategorized", "PTGS.1", [], 0)

def determine_dimension(question: str) -> str:
    """Determine what dimension (WHAT/WHY/HOW/etc.) the question tests."""
    q_lower = question.lower()
    
    # WHY patterns
    why_patterns = [
        r'\bwhy\b', r'\breason\b', r'\bcause\b', r'\bfactor\b', 
        r'\bexplain.*significance\b', r'\bimportance\b', r'\bresponsible for\b'
    ]
    for pattern in why_patterns:
        if re.search(pattern, q_lower):
            return "WHY"
    
    # HOW patterns
    how_patterns = [
        r'\bhow\b', r'\bprocess\b', r'\bmechanism\b', r'\bmethod\b',
        r'\bprocedure\b', r'\bsteps\b', r'\bmanner\b'
    ]
    for pattern in how_patterns:
        if re.search(pattern, q_lower):
            return "HOW"
    
    # VS/COMPARISON patterns
    vs_patterns = [
        r'\bcompare\b', r'\bcontrast\b', r'\bdifference\b', r'\bsimilarity\b',
        r'\bdistinguish\b', r'\bvs\b', r'\bversus\b', r'\bbetween\b.*and\b'
    ]
    for pattern in vs_patterns:
        if re.search(pattern, q_lower):
            return "VS"
    
    # IMPACT patterns
    impact_patterns = [
        r'\bimpact\b', r'\beffect\b', r'\bconsequence\b', r'\bresult\b',
        r'\bimplication\b', r'\binfluence\b', r'\baffect\b'
    ]
    for pattern in impact_patterns:
        if re.search(pattern, q_lower):
            return "IMPACT"
    
    # WHO patterns
    who_patterns = [
        r'\bwho\b', r'\bwhich person\b', r'\bwhich leader\b', r'\bfounder\b',
        r'\bassociated with\b'
    ]
    for pattern in who_patterns:
        if re.search(pattern, q_lower):
            return "WHO"
    
    # WHERE patterns
    where_patterns = [
        r'\bwhere\b', r'\blocation\b', r'\bplace\b', r'\bsite\b', r'\bregion\b',
        r'\bgeograph\b'
    ]
    for pattern in where_patterns:
        if re.search(pattern, q_lower):
            return "WHERE"
    
    # WHEN patterns
    when_patterns = [
        r'\bwhen\b', r'\byear\b', r'\bperiod\b', r'\bcentury\b', r'\bchronolog\b',
        r'\bsequence\b', r'\border\b.*events\b'
    ]
    for pattern in when_patterns:
        if re.search(pattern, q_lower):
            return "WHEN"
    
    # Default to WHAT (factual)
    return "WHAT"

def determine_question_type(question: str, paper: str) -> str:
    """Determine question type: Factual/Conceptual/Analytical/Application."""
    q_lower = question.lower()
    
    # Application type
    if any(word in q_lower for word in ['suggest', 'recommend', 'solve', 'address', 'tackle', 'measure', 'strategy']):
        return "Application"
    
    # Analytical type
    if any(word in q_lower for word in ['analyze', 'analyse', 'evaluate', 'assess', 'examine', 'critically', 'critique']):
        return "Analytical"
    
    # Conceptual type
    if any(word in q_lower for word in ['explain', 'discuss', 'elaborate', 'describe', 'define', 'meaning', 'concept']):
        return "Conceptual"
    
    # Default for Prelims is Factual
    if paper == "PTGS":
        return "Factual"
    
    # Default for Mains
    return "Conceptual"

def determine_difficulty(question: str, options: dict) -> str:
    """Estimate difficulty based on question structure."""
    q_lower = question.lower()
    
    # Hard indicators
    hard_indicators = [
        'critically', 'evaluate', 'complex', 'nuanced', 'controversial',
        'multiple statements', 'all of the above', 'none of the above'
    ]
    
    # Medium indicators
    medium_indicators = [
        'explain', 'discuss', 'compare', 'contrast', 'analyze',
        '1 and 2', '2 and 3', 'both'
    ]
    
    hard_count = sum(1 for ind in hard_indicators if ind in q_lower)
    medium_count = sum(1 for ind in medium_indicators if ind in q_lower)
    
    if hard_count >= 2:
        return "Hard"
    elif hard_count >= 1 or medium_count >= 2:
        return "Medium"
    else:
        return "Easy"

def determine_prelims_priority(subject: str, topic: str, year: int, frequency: int) -> str:
    """Determine prelims priority based on subject, recency, and frequency."""
    # High priority subjects for Prelims
    high_priority_subjects = ["Environment", "Economy", "Polity", "Science & Technology"]
    
    if subject in high_priority_subjects:
        if frequency >= 3 or year >= 2022:
            return "HIGH"
        elif frequency >= 2:
            return "MEDIUM"
    
    if frequency >= 4:
        return "HIGH"
    elif frequency >= 2:
        return "MEDIUM"
    else:
        return "LOW"

def get_related_concepts(topic: str, category: str, subject: str) -> List[str]:
    """Get related concepts for a topic."""
    relations = {
        "Buddhism": ["Jainism", "Mauryan Empire", "Ashoka", "Buddhist Art", "Vedic Age"],
        "Jainism": ["Buddhism", "Mahavira", "Chandragupta Maurya", "Jain Art"],
        "Mauryan Empire": ["Ashoka", "Chanakya", "Buddhism", "Arthashastra"],
        "Gupta Empire": ["Golden Age", "Gupta Art", "Nalanda", "Sanskrit Literature"],
        "Delhi Sultanate": ["Mughal Empire", "Indo-Islamic Architecture", "Iqta System"],
        "Mughal Empire": ["Delhi Sultanate", "Mansabdari", "Mughal Art", "Maratha Rise"],
        "Fundamental Rights": ["DPSP", "Writs", "Article 21", "Constitutional Remedies"],
        "Federalism": ["Centre-State Relations", "Local Government", "Finance Commission"],
        "Monetary Policy": ["RBI", "Inflation", "Banking", "Interest Rates"],
        "GST": ["Indirect Tax", "Fiscal Federalism", "Finance Commission"],
        "Climate Change": ["Paris Agreement", "UNFCCC", "NDC", "Renewable Energy"],
        "Biodiversity": ["Protected Areas", "IUCN", "Wildlife Conservation", "Ecosystem"],
    }
    
    return relations.get(topic, [category, subject])

def generate_mains_metadata(question: str, topic: str, dimension: str) -> dict:
    """Generate Mains-specific metadata."""
    mains_data = {
        "relevance": [],
        "themes": [],
        "answer_structure": {
            "intro_approach": "",
            "body_points": [],
            "conclusion_approach": ""
        },
        "interlinkages": [],
        "contemporary_relevance": "",
        "word_limit_suggested": 250
    }
    
    q_lower = question.lower()
    
    # Determine themes
    theme_patterns = {
        "Social Reform": ["reform", "social change", "empowerment", "equality"],
        "Governance": ["governance", "administration", "bureaucracy", "policy"],
        "Development": ["development", "growth", "poverty", "inclusion"],
        "Environment": ["environment", "climate", "conservation", "sustainable"],
        "Security": ["security", "terrorism", "border", "cyber"],
        "International": ["international", "bilateral", "global", "diplomacy"],
        "Ethics": ["ethics", "integrity", "values", "moral"]
    }
    
    for theme, keywords in theme_patterns.items():
        if any(kw in q_lower for kw in keywords):
            mains_data["themes"].append(theme)
    
    # Answer structure hints based on dimension
    if dimension == "WHY":
        mains_data["answer_structure"]["intro_approach"] = "Define concept briefly, then state you'll explore causes"
        mains_data["answer_structure"]["body_points"] = ["Historical factors", "Social factors", "Economic factors", "Political factors"]
        mains_data["answer_structure"]["conclusion_approach"] = "Synthesize factors and their interplay"
    elif dimension == "HOW":
        mains_data["answer_structure"]["intro_approach"] = "State the process/mechanism being discussed"
        mains_data["answer_structure"]["body_points"] = ["Step 1/Phase 1", "Step 2/Phase 2", "Key actors involved", "Challenges faced"]
        mains_data["answer_structure"]["conclusion_approach"] = "Summarize process and its effectiveness"
    elif dimension == "VS":
        mains_data["answer_structure"]["intro_approach"] = "Introduce both concepts briefly"
        mains_data["answer_structure"]["body_points"] = ["Similarities", "Differences", "Contextual factors", "Relative merits"]
        mains_data["answer_structure"]["conclusion_approach"] = "Balanced assessment, avoid declaring winner"
    elif dimension == "IMPACT":
        mains_data["answer_structure"]["intro_approach"] = "Context of the phenomenon/event"
        mains_data["answer_structure"]["body_points"] = ["Positive impacts", "Negative impacts", "Short-term vs long-term", "Different stakeholders affected"]
        mains_data["answer_structure"]["conclusion_approach"] = "Net assessment and way forward"
    else:  # WHAT
        mains_data["answer_structure"]["intro_approach"] = "Clear definition/identification"
        mains_data["answer_structure"]["body_points"] = ["Key features", "Examples", "Significance", "Current status"]
        mains_data["answer_structure"]["conclusion_approach"] = "Relevance today"
    
    return mains_data

# ============================================================================
# MAIN TAGGING FUNCTION
# ============================================================================

def tag_question(q: dict, topic_frequency: dict) -> dict:
    """Tag a single question with full conceptual metadata."""
    
    question_text = q.get('question', '')
    options_text = " ".join([
        q.get('option_a', ''),
        q.get('option_b', ''),
        q.get('option_c', ''),
        q.get('option_d', '')
    ])
    
    paper = q.get('paper', 'PTGS')
    year = q.get('year', 2020)
    
    # Match to taxonomy
    subject, category, topic, syllabus_id, matched_kw, confidence = match_topic(question_text, options_text)
    
    # Determine dimension
    dimension = determine_dimension(question_text)
    
    # Determine question type
    question_type = determine_question_type(question_text, paper)
    
    # Determine difficulty
    difficulty = determine_difficulty(question_text, {})
    
    # Get topic frequency
    freq = topic_frequency.get(topic, 1)
    
    # Determine prelims priority
    prelims_priority = determine_prelims_priority(subject, topic, year, freq)
    
    # Get related concepts
    related = get_related_concepts(topic, category, subject)
    
    # Generate Mains metadata
    mains_meta = generate_mains_metadata(question_text, topic, dimension)
    
    # Extract question keywords
    q_keywords = extract_keywords_from_question(question_text)
    
    # Build tagged question
    tagged = {
        # Original fields
        "question": question_text,
        "year": year,
        "paper": paper,
        "marks": q.get('marks', 2 if paper == 'PTGS' else 10),
        "option_a": q.get('option_a', ''),
        "option_b": q.get('option_b', ''),
        "option_c": q.get('option_c', ''),
        "option_d": q.get('option_d', ''),
        "correct_option": q.get('correct_option', ''),
        "word_limit": q.get('word_limit', 0),
        
        # Administrative
        "syllabus_id": syllabus_id,
        "subject": subject,
        "category": category,
        "topic": topic,
        
        # Conceptual
        "concept": topic,  # Can be refined later
        "dimension": dimension,
        "aspect": f"{dimension} - {topic}",
        
        # Exam intelligence
        "question_type": question_type,
        "difficulty": difficulty,
        "confidence_score": confidence,
        
        # Prelims specific
        "prelims": {
            "priority": prelims_priority,
            "trap_factor": "",  # To be filled by AI review
            "elimination_hint": "",
            "factual_hooks": matched_kw[:5],
            "paired_with": related[:3]
        },
        
        # Mains specific
        "mains": mains_meta,
        
        # Connections
        "prerequisite_concepts": [],  # To be filled by AI review
        "related_concepts": related,
        "contrast_with": [],  # To be filled by AI review
        
        # Search
        "keywords": list(set(matched_kw + q_keywords[:10]))[:15]
    }
    
    return tagged

# ============================================================================
# PROCESS ALL QUESTIONS
# ============================================================================

print("\n" + "="*60)
print("PHASE 2: TAGGING ALL QUESTIONS")
print("="*60)

# First pass: count topic frequency
topic_frequency = defaultdict(int)
for q in ALL_QUESTIONS:
    question_text = q.get('question', '')
    options_text = " ".join([q.get('option_a', ''), q.get('option_b', ''), q.get('option_c', ''), q.get('option_d', '')])
    subject, category, topic, _, _, _ = match_topic(question_text, options_text)
    topic_frequency[topic] += 1

print(f"\nIdentified {len(topic_frequency)} unique topics")

# Second pass: tag all questions
tagged_questions = []
for i, q in enumerate(ALL_QUESTIONS):
    tagged = tag_question(q, topic_frequency)
    tagged_questions.append(tagged)
    
    if (i + 1) % 500 == 0:
        print(f"  Tagged {i + 1}/{len(ALL_QUESTIONS)} questions...")

print(f"\n✅ Tagged all {len(tagged_questions)} questions")

# ============================================================================
# GENERATE STATISTICS
# ============================================================================

print("\n" + "="*60)
print("TAGGING STATISTICS")
print("="*60)

# By subject
subject_counts = defaultdict(int)
for q in tagged_questions:
    subject_counts[q['subject']] += 1

print("\nBy Subject:")
for subject, count in sorted(subject_counts.items(), key=lambda x: -x[1]):
    print(f"  {subject}: {count}")

# By dimension
dimension_counts = defaultdict(int)
for q in tagged_questions:
    dimension_counts[q['dimension']] += 1

print("\nBy Dimension:")
for dim, count in sorted(dimension_counts.items(), key=lambda x: -x[1]):
    print(f"  {dim}: {count}")

# By paper
paper_counts = defaultdict(int)
for q in tagged_questions:
    paper_counts[q['paper']] += 1

print("\nBy Paper:")
for paper, count in sorted(paper_counts.items(), key=lambda x: -x[1]):
    print(f"  {paper}: {count}")

# Prelims priority
priority_counts = defaultdict(int)
for q in tagged_questions:
    if q['paper'] == 'PTGS':
        priority_counts[q['prelims']['priority']] += 1

print("\nPrelims Priority Distribution:")
for priority, count in sorted(priority_counts.items()):
    print(f"  {priority}: {count}")

# Topics with most questions
topic_counts = defaultdict(int)
for q in tagged_questions:
    topic_counts[q['topic']] += 1

print("\nTop 20 Topics:")
for topic, count in sorted(topic_counts.items(), key=lambda x: -x[1])[:20]:
    print(f"  {topic}: {count}")

# ============================================================================
# SAVE OUTPUT
# ============================================================================

output_path = Path('/home/claude/pyq-tagging/questions_tagged.json')
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(tagged_questions, f, indent=2, ensure_ascii=False)

print(f"\n✅ Saved tagged questions to: {output_path}")
print(f"   Total questions: {len(tagged_questions)}")
print(f"   File size: {output_path.stat().st_size / 1024 / 1024:.2f} MB")
