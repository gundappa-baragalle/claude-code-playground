#!/bin/bash
# Build upsc-cdf-skill.zip for upload to Claude.ai Skills
# Usage: bash build_package.sh

set -e
cd "$(dirname "$0")"

OUTPUT="upsc-cdf-skill.zip"

echo "Building $OUTPUT..."

# Remove old zip if exists
rm -f "$OUTPUT"

# Zip: SKILL.md + references/ + pyq-data/ (concept-index, topic-maps, priority-list)
zip -r "$OUTPUT" \
  SKILL.md \
  references/ \
  pyq-data/

echo ""
echo "Done! Created: $OUTPUT"
echo ""
echo "Contents:"
zip -sf "$OUTPUT"
echo ""
echo "Upload $OUTPUT to Claude.ai → Customize → Skills → + (upload)"
