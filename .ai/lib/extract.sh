#!/usr/bin/env bash
# =============================================================================
# extract.sh — Extract knowledge after task
# =============================================================================
# Purpose: Capture knowledge, decisions, and reflections from a completed task
#          into the appropriate .ai directory as structured markdown files.
# Platform: Cross-platform (Bash on Linux/macOS/WSL/Git Bash)
# =============================================================================
# USAGE
#   ./extract.sh <type> <title>
#
# EXAMPLE
#   ./extract.sh reflection "Fixed database connection pool leak"
#   ./extract.sh decision "Use PostgreSQL instead of MySQL"
#   ./extract.sh pattern "Retry with exponential backoff"
# =============================================================================

set -euo pipefail

# --- Configuration -----------------------------------------------------------
: "${AI_DIR:="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"}"
: "${TEMPLATES_DIR:="$AI_DIR/templates"}"

# --- Type mapping -----------------------------------------------------------
declare -A TYPES
TYPES=(
    [reflection]="reflections"
    [decision]="decisions"
    [failure]="failures"
    [pattern]="patterns"
    [skill]="skills"
    [changelog]="changelog"
    [meeting]="meetings"
)

declare -A TEMPLATES
TEMPLATES=(
    [reflection]="$TEMPLATES_DIR/reflection.md"
    [decision]="$TEMPLATES_DIR/decision.md"
    [failure]="$TEMPLATES_DIR/failure.md"
    [pattern]="$TEMPLATES_DIR/pattern.md"
    [skill]="$TEMPLATES_DIR/skill.md"
    [changelog]="$TEMPLATES_DIR/changelog-entry.md"
    [meeting]="$TEMPLATES_DIR/meeting-notes.md"
)

# --- Functions ---------------------------------------------------------------

usage() {
    echo "Usage: $(basename "$0") <type> <title>"
    echo ""
    echo "Types: ${!TYPES[*]}"
    exit 0
}

slugify() {
    # Convert string to kebab-case filename slug
    echo "$1" \
        | tr '[:upper:]' '[:lower:]' \
        | sed -E 's/[^a-z0-9]+/-/g' \
        | sed -E 's/^-+|-+$//g'
}

# --- Main ---------------------------------------------------------------------

main() {
    if [ $# -lt 2 ]; then
        usage
    fi

    TYPE="$1"
    TITLE="$2"
    DATE="$(date +%Y%m%d)"
    TIMESTAMP="$(date +%Y-%m-%d)"

    # Validate type
    TARGET_DIR="${TYPES[$TYPE]:-}"
    TEMPLATE_FILE="${TEMPLATES[$TYPE]:-}"
    if [ -z "$TARGET_DIR" ]; then
        echo "Error: Unknown type '$TYPE'. Valid types: ${!TYPES[*]}"
        exit 1
    fi

    # Create target directory
    mkdir -p "$AI_DIR/$TARGET_DIR"

    # Generate filename
    SLUG="$(slugify "$TITLE")"
    FILENAME="${DATE}-${SLUG}.md"
    FILEPATH="$AI_DIR/$TARGET_DIR/$FILENAME"

    # --- PSEUDOCODE: Actual extraction logic ---
    # 1. Copy template from $TEMPLATE_FILE if it exists
    # 2. Prompt user to fill in template sections interactively
    #    OR accept structured input via stdin in YAML/JSON format
    # 3. Validate required frontmatter fields
    # 4. Set id = "$TYPE-${DATE}-${SLUG}"
    # 5. Compute initial confidence based on type defaults
    # 6. Write the file to $FILEPATH
    # 7. Optionally trigger index.sh to add to RAG
    #
    # Implementation example using template:
    #   cp "$TEMPLATE_FILE" "$FILEPATH"
    #   sed -i "s/\[Title\]/$TITLE/g" "$FILEPATH"
    #   sed -i "s/YYYY-MM-DD/$TIMESTAMP/g" "$FILEPATH"
    #   sed -i "s/id: template-.*/id: $TYPE-$DATE-$SLUG/" "$FILEPATH"

    echo ""
    echo "[DONE] Knowledge extracted: $TYPE"
    echo "  File: $FILEPATH"
    echo "  Date: $TIMESTAMP"
    echo ""
    echo "Next steps:"
    echo "  1. Open the file and fill in the template sections."
    echo "  2. Run './recall.sh' to verify it integrates with RAG."
    echo "  3. Commit the new knowledge file."
}

# --- Entry Point -------------------------------------------------------------
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    main "$@"
fi
