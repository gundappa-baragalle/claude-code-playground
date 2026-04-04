#!/usr/bin/env python3
"""
UPSC PYQ Enrichment Pipeline — Direct Processing Edition
=========================================================
This script prepares batches for Claude to process directly in-conversation.
No API key or subprocess needed — Claude Code processes questions directly.

Workflow:
    1. Run: python3 enrich_pipeline.py --next-batch
       → Prints the next unprocessed batch of questions to screen

    2. Claude reads the batch output, classifies each question, calls:
       python3 enrich_pipeline.py --save '[...enriched JSON array...]'

    3. Repeat until done. Fully resumable.

Check progress:
    python3 enrich_pipeline.py --stats

Rebuild indexes after completion:
    python3 upsc-pyq-tagging/generate_indexes.py
"""

import json
import sys
import argparse
from pathlib import Path
from datetime import datetime
from collections import Counter

# ── Paths ────────────────────────────────────────────────────────────────────
BASE_DIR        = Path(__file__).parent
QUESTIONS_FILE  = BASE_DIR / "questions.json"
CHECKPOINT_FILE = BASE_DIR / "upsc-pyq-tagging" / "enrichment_checkpoint.json"
OUTPUT_FILE     = BASE_DIR / "upsc-pyq-tagging" / "questions_enriched.json"
TAGGED_FILE     = BASE_DIR / "upsc-pyq-tagging" / "questions_tagged.json"

BATCH_SIZE = 30   # Questions per batch — adjust based on conversation context


# ── Checkpoint ───────────────────────────────────────────────────────────────

def load_checkpoint() -> dict:
    if CHECKPOINT_FILE.exists():
        with open(CHECKPOINT_FILE) as f:
            cp = json.load(f)
        cp["processed_indices"] = set(cp.get("processed_indices", []))
        return cp
    return {
        "version": "2.0",
        "total": 0,
        "processed_count": 0,
        "processed_indices": set(),
        "created_at": datetime.now().isoformat(),
        "last_updated": datetime.now().isoformat(),
    }


def save_checkpoint(cp: dict):
    to_save = {
        **cp,
        "processed_indices": sorted(cp["processed_indices"]),
        "last_updated": datetime.now().isoformat(),
    }
    with open(CHECKPOINT_FILE, "w") as f:
        json.dump(to_save, f)


# ── Results ───────────────────────────────────────────────────────────────────

def load_results() -> dict:
    if OUTPUT_FILE.exists():
        with open(OUTPUT_FILE) as f:
            data = json.load(f)
        return {q["_original_idx"]: q for q in data if "_original_idx" in q}
    return {}


def save_results(results: dict, total: int):
    ordered = [results[i] for i in range(total) if i in results]
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(ordered, f, indent=2, ensure_ascii=False)


# ── Build tagged question ─────────────────────────────────────────────────────

def build_tagged(orig: dict, e: dict, idx: int) -> dict:
    paper = orig.get("paper", "")
    is_pre = paper == "PTGS"
    return {
        "question":       orig.get("question", ""),
        "year":           orig.get("year", 0),
        "paper":          paper,
        "marks":          orig.get("marks", 2 if is_pre else 10),
        "option_a":       orig.get("option_a", ""),
        "option_b":       orig.get("option_b", ""),
        "option_c":       orig.get("option_c", ""),
        "option_d":       orig.get("option_d", ""),
        "correct_option": orig.get("correct_option", ""),
        "word_limit":     orig.get("word_limit", 0),
        "syllabus_id":    e.get("syllabus_id", ""),
        "subject":        e.get("subject", "General"),
        "category":       e.get("category", "Miscellaneous"),
        "topic":          e.get("topic", "Uncategorized"),
        "concept":        e.get("topic", ""),
        "dimension":      e.get("dimension", "WHAT"),
        "aspect":         f"{e.get('dimension','WHAT')} – {e.get('topic','')}",
        "question_type":  e.get("question_type", "Factual"),
        "difficulty":     e.get("difficulty", "Medium"),
        "confidence_score": float(e.get("confidence_score") or 0.0),
        "prelims": {
            "priority":         e.get("prelims_priority", "MEDIUM"),
            "trap_factor":      e.get("trap_factor") or "",
            "elimination_hint": e.get("elimination_hint") or "",
            "factual_hooks":    e.get("factual_hooks") or [],
            "paired_with":      (e.get("related_concepts") or [])[:3],
        },
        "mains": {
            "relevance": "HIGH" if e.get("mains_themes") else ("MEDIUM" if not is_pre else "LOW"),
            "themes": e.get("mains_themes") or [],
            "answer_structure": {
                "intro_approach":      e.get("mains_intro") or "",
                "body_points":         e.get("mains_body_points") or [],
                "conclusion_approach": e.get("mains_conclusion") or "",
            },
            "interlinkages":          e.get("mains_interlinkages") or [],
            "contemporary_relevance": e.get("contemporary_relevance") or "",
            "word_limit_suggested":   orig.get("word_limit") or (0 if is_pre else 250),
        },
        "prerequisite_concepts": e.get("prerequisite_concepts") or [],
        "related_concepts":      e.get("related_concepts") or [],
        "contrast_with":         e.get("contrast_with") or [],
        "keywords":              e.get("keywords") or [],
        "_original_idx":         idx,
        "_enriched":             True,
    }


# ── --next-batch ──────────────────────────────────────────────────────────────

def cmd_next_batch(batch_size: int):
    """Print the next unprocessed batch of questions for Claude to classify."""
    with open(QUESTIONS_FILE) as f:
        raw = json.load(f)
    questions = raw[0]["json_result"]
    total = len(questions)

    cp = load_checkpoint()
    cp["total"] = total
    processed = cp["processed_indices"]

    pending = [i for i in range(total) if i not in processed]
    if not pending:
        print("ALL DONE — all questions enriched.")
        return

    batch_indices = pending[:batch_size]
    done = len(processed)
    pct  = done / total * 100

    print(f"=== BATCH: indices {batch_indices[0]}–{batch_indices[-1]} "
          f"({len(batch_indices)} questions) | Progress: {done}/{total} ({pct:.1f}%) ===\n")
    print("CLASSIFY each question and return a JSON array using --save.\n")
    print("SUBJECTS: History, Geography, Polity, Governance, Economy, Society, Environment,")
    print("  Science & Technology, International Relations, Internal Security, Ethics, CSAT\n")
    print("RULES:")
    print("  - Math/arithmetic/geometry/volumes/percentages → CSAT > Quantitative Aptitude")
    print("  - Seating/blood-relations/direction/logic/coding → CSAT > Logical Reasoning")
    print("  - English reading/vocab → CSAT > Reading Comprehension")
    print("  - Paper=GS4 → Ethics subject ALWAYS (ignore question content)")
    print("  - Paper=Essay → subject = dominant theme of essay")
    print("  - Priority: ~45% HIGH / ~35% MEDIUM / ~20% LOW (enforce distribution)\n")
    print("OUTPUT: JSON array, one object per question, in order. Schema:\n")
    print('{"idx":<int>,"subject":"...","category":"...","topic":"...",')
    print(' "syllabus_id":"...","dimension":"WHAT|WHY|HOW|WHEN|WHERE|WHO|VS|IMPACT",')
    print(' "question_type":"Factual|Conceptual|Analytical|Application|CSAT",')
    print(' "difficulty":"Easy|Medium|Hard","confidence_score":0.9,')
    print(' "prelims_priority":"HIGH|MEDIUM|LOW",')
    print(' "trap_factor":"why wrong options look right (MCQ only, else null)",')
    print(' "elimination_hint":"specific strategy to find answer (MCQ only, else null)",')
    print(' "factual_hooks":["key fact 1","key fact 2"],')
    print(' "prerequisite_concepts":["concept A","concept B"],')
    print(' "related_concepts":["topic X","topic Y"],')
    print(' "contrast_with":["ConceptZ — key differentiator"],')
    print(' "mains_themes":["theme1"] (empty for prelims),')
    print(' "mains_intro":"intro approach (null for prelims)",')
    print(' "mains_body_points":["point 1","point 2"] (null for prelims),')
    print(' "mains_conclusion":"conclusion (null for prelims)",')
    print(' "mains_interlinkages":[] (empty for prelims),')
    print(' "contemporary_relevance":"one sentence or null",')
    print(' "keywords":["kw1","kw2","kw3"]}\n')
    print("--- QUESTIONS ---\n")

    for pos, idx in enumerate(batch_indices):
        q = questions[idx]
        paper = q.get("paper", "?")
        print(f"[{pos}] idx={idx} | Year:{q.get('year','?')} Paper:{paper} Marks:{q.get('marks','?')}")
        qtext = (q.get("question") or "").strip().replace("\n", " ")
        print(f"Q: {qtext[:500]}")
        if q.get("option_a"):
            print(f"A) {str(q.get('option_a',''))[:180]}")
            print(f"B) {str(q.get('option_b',''))[:180]}")
            print(f"C) {str(q.get('option_c',''))[:180]}")
            print(f"D) {str(q.get('option_d',''))[:180]}")
            print(f"Correct: {q.get('correct_option','?')}")
        print()

    print(f"--- END OF BATCH (indices {batch_indices[0]}–{batch_indices[-1]}) ---")
    print(f"\nAfter classifying, run:")
    print(f"  python3 enrich_pipeline.py --save '<json_array>'")
    print(f"  or: python3 enrich_pipeline.py --save-file /tmp/batch_result.json")


# ── --save ────────────────────────────────────────────────────────────────────

def cmd_save(json_str: str):
    """Save a batch of enriched questions from Claude's JSON output."""
    try:
        enrichments = json.loads(json_str)
    except json.JSONDecodeError as e:
        print(f"ERROR: Invalid JSON — {e}")
        sys.exit(1)

    with open(QUESTIONS_FILE) as f:
        raw = json.load(f)
    questions = raw[0]["json_result"]
    total = len(questions)

    cp = load_checkpoint()
    cp["total"] = total
    results = load_results()

    pending = [i for i in range(total) if i not in cp["processed_indices"]]
    batch_indices = pending[:len(enrichments)]

    saved = 0
    for e in enrichments:
        pos = e.get("idx")
        if pos is None or pos >= len(batch_indices):
            continue
        orig_idx = batch_indices[pos]
        results[orig_idx] = build_tagged(questions[orig_idx], e, orig_idx)
        cp["processed_indices"].add(orig_idx)
        saved += 1

    cp["processed_count"] = len(cp["processed_indices"])
    save_checkpoint(cp)
    save_results(results, total)

    print(f"Saved {saved} enriched questions.")
    print(f"Progress: {cp['processed_count']}/{total} ({cp['processed_count']/total*100:.1f}%)")

    if cp["processed_count"] == total:
        import shutil
        shutil.copy(OUTPUT_FILE, TAGGED_FILE)
        print(f"\nALL DONE! Copied to {TAGGED_FILE}")
        print("Next: python3 upsc-pyq-tagging/generate_indexes.py")
    else:
        remaining = total - cp["processed_count"]
        print(f"Remaining: {remaining} questions. Run --next-batch to continue.")


# ── --save-file ───────────────────────────────────────────────────────────────

def cmd_save_file(path: str):
    with open(path) as f:
        json_str = f.read()
    cmd_save(json_str)


# ── --extract-all ─────────────────────────────────────────────────────────────

def cmd_extract_all(batch_size: int, out_dir: str):
    """Pre-generate ALL remaining batch files at once into out_dir."""
    import math
    with open(QUESTIONS_FILE) as f:
        raw = json.load(f)
    questions = raw[0]["json_result"]
    total = len(questions)

    cp = load_checkpoint()
    processed = cp.get("processed_indices", set())
    pending = [i for i in range(total) if i not in processed]

    if not pending:
        print("ALL DONE — no questions left to extract.")
        return

    Path(out_dir).mkdir(parents=True, exist_ok=True)
    n_batches = math.ceil(len(pending) / batch_size)
    print(f"Generating {n_batches} batch files ({len(pending)} questions, {batch_size}/batch) → {out_dir}/")
    print()

    for batch_num in range(n_batches):
        start = batch_num * batch_size
        batch_indices = pending[start:start + batch_size]
        batch = []
        for pos, idx in enumerate(batch_indices):
            q = questions[idx]
            batch.append({
                "idx": pos,
                "original_idx": idx,
                "year": q.get("year"),
                "paper": q.get("paper"),
                "marks": q.get("marks"),
                "question": q.get("question", "").strip(),
                "option_a": q.get("option_a", ""),
                "option_b": q.get("option_b", ""),
                "option_c": q.get("option_c", ""),
                "option_d": q.get("option_d", ""),
                "correct_option": q.get("correct_option", ""),
                "word_limit": q.get("word_limit", 0),
            })

        filename = f"batch_{batch_num+1:03d}.json"
        filepath = Path(out_dir) / filename
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(batch, f, indent=2, ensure_ascii=False)

        q_range = f"{batch_indices[0]}–{batch_indices[-1]}"
        print(f"  {filename}  ({len(batch)} questions, orig idx {q_range})")

    print()
    print(f"Done. {n_batches} files in {out_dir}/")
    print()
    print("Next steps:")
    print(f"  1. Open Claude.ai Project (context already uploaded there)")
    print(f"  2. Upload each batch_NNN.json → get result → save as result_NNN.json in {out_dir}/")
    print(f"  3. When all results ready: python3 enrich_pipeline.py --merge-all {out_dir}")


# ── --merge-all ───────────────────────────────────────────────────────────────

def cmd_merge_all(results_dir: str):
    """Merge all result_NNN.json files from results_dir into questions_enriched.json.

    Uses the corresponding batch_NNN.json to get the authoritative original_idx mapping,
    so the checkpoint state does not affect which question each enrichment is assigned to.
    """
    results_path = Path(results_dir)
    result_files = sorted(results_path.glob("result_*.json"))

    if not result_files:
        print(f"No result_*.json files found in {results_dir}/")
        return

    with open(QUESTIONS_FILE) as f:
        raw = json.load(f)
    questions = raw[0]["json_result"]
    total = len(questions)

    cp = load_checkpoint()
    cp["total"] = total
    results = load_results()

    print(f"Found {len(result_files)} result files to merge:")
    total_saved = 0
    for rf in result_files:
        # Derive the batch number from the result filename (result_NNN → batch_NNN)
        batch_num_str = rf.stem.replace("result_", "")  # e.g. "001"
        batch_file = results_path / f"batch_{batch_num_str}.json"

        if not batch_file.exists():
            print(f"  Merging {rf.name} ... SKIPPED (no matching {batch_file.name})")
            continue

        with open(batch_file) as f:
            batch_data = json.load(f)
        # Build pos→original_idx map from the batch file (authoritative)
        idx_map = {item["idx"]: item["original_idx"] for item in batch_data}

        print(f"  Merging {rf.name} (batch {batch_num_str}) ...", end=" ")
        with open(rf) as f:
            json_str = f.read()
        try:
            enrichments = json.loads(json_str)
        except json.JSONDecodeError as e:
            print(f"SKIPPED (invalid JSON: {e})")
            continue

        saved = 0
        for e in enrichments:
            pos = e.get("idx")
            if pos is None or pos not in idx_map:
                continue
            orig_idx = idx_map[pos]
            results[orig_idx] = build_tagged(questions[orig_idx], e, orig_idx)
            cp["processed_indices"].add(orig_idx)
            saved += 1

        total_saved += saved
        print(f"done ({saved} questions, original_idx {batch_data[0]['original_idx']}–{batch_data[-1]['original_idx']})")

    cp["processed_count"] = len(cp["processed_indices"])
    save_checkpoint(cp)
    save_results(results, total)

    print()
    print(f"Total merged: {total_saved} questions")
    cmd_stats()

    if cp["processed_count"] == total:
        import shutil
        shutil.copy(OUTPUT_FILE, TAGGED_FILE)
        print(f"\nALL DONE! Copied to {TAGGED_FILE}")
        print("Next: python3 upsc-pyq-tagging/generate_indexes.py")


# ── --extract ─────────────────────────────────────────────────────────────────

def cmd_extract(batch_size: int, out_path: str):
    """Extract next N unprocessed questions into a small JSON file for Claude.ai."""
    with open(QUESTIONS_FILE) as f:
        raw = json.load(f)
    questions = raw[0]["json_result"]
    total = len(questions)

    cp = load_checkpoint()
    processed = cp.get("processed_indices", set())
    pending = [i for i in range(total) if i not in processed]

    if not pending:
        print("ALL DONE — no questions left to extract.")
        return

    batch_indices = pending[:batch_size]
    batch = []
    for pos, idx in enumerate(batch_indices):
        q = questions[idx]
        batch.append({
            "idx": pos,
            "original_idx": idx,
            "year": q.get("year"),
            "paper": q.get("paper"),
            "marks": q.get("marks"),
            "question": q.get("question", "").strip(),
            "option_a": q.get("option_a", ""),
            "option_b": q.get("option_b", ""),
            "option_c": q.get("option_c", ""),
            "option_d": q.get("option_d", ""),
            "correct_option": q.get("correct_option", ""),
            "word_limit": q.get("word_limit", 0),
        })

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(batch, f, indent=2, ensure_ascii=False)

    done = len(processed)
    print(f"Extracted {len(batch)} questions (idx {batch_indices[0]}–{batch_indices[-1]}) → {out_path}")
    print(f"Progress: {done}/{total} ({done/total*100:.1f}%) | Remaining after this batch: {len(pending)-len(batch)}")
    print(f"\nNext steps:")
    print(f"  1. Upload CLAUDE_AI_CONTEXT.md + {out_path} to Claude.ai")
    print(f"  2. Save Claude.ai's JSON output to /tmp/result.json")
    print(f"  3. Run: python3 enrich_pipeline.py --save-file /tmp/result.json")


# ── --stats ───────────────────────────────────────────────────────────────────

def cmd_stats():
    with open(QUESTIONS_FILE) as f:
        total = len(json.load(f)[0]["json_result"])
    cp = load_checkpoint()
    results = load_results()
    done = len(cp.get("processed_indices", []))
    pct = done / total * 100 if total else 0

    print(f"\n{'─'*45}")
    print(f"  Progress: {done}/{total} ({pct:.1f}%)")
    print(f"  Remaining: {total - done}")
    if results:
        print(f"\n  Subjects so far:")
        for s, c in Counter(q["subject"] for q in results.values()).most_common(10):
            print(f"    {s:<35} {c:>5}")
        prelims_r = [q for q in results.values() if q.get("paper") == "PTGS"]
        pri = Counter(q["prelims"]["priority"] for q in prelims_r)
        print(f"\n  Prelims priority: HIGH={pri.get('HIGH',0)} MEDIUM={pri.get('MEDIUM',0)} LOW={pri.get('LOW',0)}")
    if cp.get("last_updated"):
        print(f"  Last updated: {cp['last_updated']}")
    print(f"{'─'*45}\n")


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--next-batch",   action="store_true", help="Print next batch for classification")
    parser.add_argument("--batch-size",   type=int, default=BATCH_SIZE)
    parser.add_argument("--extract",      type=int, metavar="N", help="Extract next N questions to a file for Claude.ai")
    parser.add_argument("--extract-out",  type=str, default="next_batch.json", help="Output path for --extract (default: next_batch.json)")
    parser.add_argument("--extract-all",  action="store_true", help="Pre-generate ALL remaining batch files at once")
    parser.add_argument("--batches-dir",  type=str, default="batches", help="Directory for --extract-all and --merge-all (default: batches/)")
    parser.add_argument("--merge-all",    action="store_true", help="Merge all result_NNN.json files from --batches-dir")
    parser.add_argument("--save",         type=str,  help="JSON string of enriched batch to save")
    parser.add_argument("--save-file",    type=str,  help="Path to JSON file of enriched batch to save")
    parser.add_argument("--stats",        action="store_true")
    args = parser.parse_args()

    if args.stats:
        cmd_stats()
    elif args.next_batch:
        cmd_next_batch(args.batch_size)
    elif args.extract:
        cmd_extract(args.extract, args.extract_out)
    elif args.extract_all:
        cmd_extract_all(args.batch_size, args.batches_dir)
    elif args.merge_all:
        cmd_merge_all(args.batches_dir)
    elif args.save:
        cmd_save(args.save)
    elif args.save_file:
        cmd_save_file(args.save_file)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
