# UPSC PYQ Enrichment Skill

You are helping the user enrich UPSC Previous Year Questions using the pipeline at `/workspaces/claude-code-playground/`.

## Workflow Overview

All 66 batch files are pre-generated in `batches/batch_001.json` through `batches/batch_066.json`.

The user processes each batch in Claude.ai, then saves the result as `batches/result_NNN.json`.

When all results are ready, one command merges everything:
```bash
python3 enrich_pipeline.py --merge-all
```

---

## Available Commands

```bash
# Check progress
python3 enrich_pipeline.py --stats

# Merge a single result file (if doing one at a time)
python3 enrich_pipeline.py --save-file batches/result_001.json

# Merge ALL result files at once (when all batches done)
python3 enrich_pipeline.py --merge-all

# Rebuild indexes after all questions enriched
python3 upsc-pyq-tagging/generate_indexes.py
```

---

## Checking Status

Run this to see what's done and what's pending:

!python3 enrich_pipeline.py --stats

---

## Validate a Result File

If the user drops a result file and wants it validated before merging:

1. Read the file
2. Check: all `idx` fields are 0-based integers
3. Check: all `subject` values are from the allowed list: History, Geography, Polity, Governance, Economy, Society, Environment, Science & Technology, International Relations, Internal Security, Ethics, CSAT
4. Check: no missing required fields (subject, category, topic, dimension, difficulty, prelims_priority, keywords)
5. Report any issues

---

## Merge All and Rebuild

When the user says all batches are done:

```bash
python3 enrich_pipeline.py --merge-all
python3 upsc-pyq-tagging/generate_indexes.py
```

This will:
1. Merge all `batches/result_*.json` into `questions_enriched.json`
2. Rebuild concept-index.json, topic-maps/, patterns.json, subject-index.json

---

## Claude.ai Project Setup (One-Time)

Tell the user: Create a **Project** in Claude.ai and upload `CLAUDE_AI_CONTEXT.md` to it once. Then all conversations in that project have the context automatically — no re-uploading needed.

Batch workflow per conversation in that project:
1. Upload `batches/batch_NNN.json`
2. Prompt: "Classify and enrich all questions in the uploaded batch file following the context. Return ONLY the JSON array starting with `[`."
3. Copy response → save as `batches/result_NNN.json` here

---

## File Map

| File | Purpose |
|------|---------|
| `CLAUDE_AI_CONTEXT.md` | Upload once to Claude.ai Project |
| `batches/batch_NNN.json` | Input: 75 questions per file (66 files total) |
| `batches/result_NNN.json` | Output: Claude.ai enriched JSON (save here) |
| `upsc-pyq-tagging/questions_enriched.json` | Final merged output |
| `upsc-pyq-tagging/enrichment_checkpoint.json` | Progress tracking |
