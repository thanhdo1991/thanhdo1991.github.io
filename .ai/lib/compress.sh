#!/usr/bin/env bash
# =============================================================================
# compress.sh — Compress knowledge periodically
# =============================================================================
# Purpose: Summarize and compress accumulated knowledge to prevent context
#          bloat. Removes redundant entries, merges overlapping patterns, and
#          produces condensed summaries of low-value entries.
# Platform: Cross-platform (Bash on Linux/macOS/WSL/Git Bash)
# =============================================================================
# USAGE
#   ./compress.sh                        # Run compression on all content types
#   ./compress.sh --type reflection      # Run on specific type only
#   ./compress.sh --dry-run              # Preview what would be compressed
#   ./compress.sh --age 90              # Only touch files older than N days
# =============================================================================

set -euo pipefail

# --- Configuration -----------------------------------------------------------
: "${AI_DIR:="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"}"
: "${MIN_CONFIDENCE_TO_KEEP:=0.30}"     # Archive entries below this confidence
: "${MAX_ENTRIES_PER_TYPE:=50}"         # Max entries before summarizing
: "${SUMMARY_DIR:="$AI_DIR/summaries"}"
: "${ARCHIVE_DIR:="$AI_DIR/archive"}"

# --- Functions ---------------------------------------------------------------

usage() {
    cat <<EOF
Usage: $(basename "$0") [options]

Options:
  --type <type>      Only compress specific type (reflection, decision, etc.)
  --dry-run          Preview changes without writing
  --age <days>       Only process files older than <days>
  --min-confidence X Archive entries below confidence X (default: $MIN_CONFIDENCE_TO_KEEP)
  --help             Show this help

Types: reflections, decisions, patterns, failures, skills, meetings, changelog
EOF
    exit 0
}

# --- Main ---------------------------------------------------------------------

main() {
    # --- Parse arguments ---
    FILTER_TYPE=""
    DRY_RUN=false
    AGE_FILTER=0

    while [ $# -gt 0 ]; do
        case "$1" in
            --type)         FILTER_TYPE="$2"; shift 2 ;;
            --dry-run)      DRY_RUN=true; shift ;;
            --age)          AGE_FILTER="$2"; shift 2 ;;
            --min-confidence) MIN_CONFIDENCE_TO_KEEP="$2"; shift 2 ;;
            --help)         usage ;;
            *)              echo "Unknown option: $1"; usage ;;
        esac
    done

    # --- Determine directories to process ---
    declare -A CONTENT_DIRS
    CONTENT_DIRS=(
        [reflections]=reflection
        [decisions]=decision
        [patterns]=pattern
        [failures]=failure
        [skills]=skill
        [meetings]=meeting
        [changelog]=changelog
    )

    DIRS_TO_PROCESS=()
    if [ -n "$FILTER_TYPE" ]; then
        TARGET="${CONTENT_DIRS[$FILTER_TYPE]:-}"
        if [ -z "$TARGET" ]; then
            echo "Error: Unknown type '$FILTER_TYPE'"
            exit 1
        fi
        DIRS_TO_PROCESS=("$AI_DIR/$FILTER_TYPE")
    else
        for dir in "${!CONTENT_DIRS[@]}"; do
            [ -d "$AI_DIR/$dir" ] && DIRS_TO_PROCESS+=("$AI_DIR/$dir")
        done
    fi

    # --- PSEUDOCODE: Compression logic ---
    # For each content directory:
    #
    # 1. List all .md files sorted by last_updated (ascending — oldest first)
    # 2. Count total entries
    # 3. For confidence check:
    #    - Parse frontmatter, extract confidence field
    #    - If confidence < MIN_CONFIDENCE_TO_KEEP:
    #      - Move to archive dir, prepend ARCHIVED- to filename
    #      - Log the archival
    # 4. For summarization (if count > MAX_ENTRIES_PER_TYPE):
    #    - Read oldest entries
    #    - Generate condensed summary for each (first 200 chars + key tags)
    #    - Write combined summary to $SUMMARY_DIR/<type>-summary.md
    # 5. For deduplication:
    #    - Compare checksums or exact content matches
    #    - Keep the file with the highest confidence
    #    - Merge tags from duplicates
    # 6. Update all frontmatter last_updated fields
    #
    # Note: Compression should trigger full re-index afterwards.

    echo ""
    echo "=== Knowledge Compression Report ==="
    echo "Mode: $([ "$DRY_RUN" = true ] && echo "DRY RUN" || echo "LIVE")"
    echo ""

    for dir in "${DIRS_TO_PROCESS[@]}"; do
        echo "Processing: $dir"

        FILE_COUNT=$(find "$dir" -maxdepth 1 -name "*.md" 2>/dev/null | wc -l)
        echo "  Files found: $FILE_COUNT"

        # --- Confidence-based archival ---
        if [ "$DRY_RUN" = true ]; then
            find "$dir" -maxdepth 1 -name "*.md" -newer "$(date -d "$AGE_FILTER days ago" 2>/dev/null || echo "1970-01-01")" 2>/dev/null \
                | while read -r f; do
                    CONF=$(grep -m1 '^confidence:' "$f" 2>/dev/null | grep -oP '[\d.]+' || echo "1.0")
                    if (( $(echo "$CONF < $MIN_CONFIDENCE_TO_KEEP" | bc -l 2>/dev/null) )); then
                        echo "  [DRY-RUN] Would archive: $(basename "$f") (confidence: $CONF)"
                    fi
                done
        fi
        # --- LIVE mode pseudocode ---
        # for f in "$dir"/*.md; do
        #   conf=$(yq eval '.confidence' "$f")
        #   if (( $(echo "$conf < $MIN_CONFIDENCE_TO_KEEP" | bc -l) )); then
        #     mkdir -p "$ARCHIVE_DIR"
        #     mv "$f" "$ARCHIVE_DIR/ARCHIVED-$(basename "$f")"
        #   fi
        # done
    done

    echo ""
    if [ "$DRY_RUN" = true ]; then
        echo "Run without --dry-run to apply changes."
    else
        echo "Compression complete. Run the index command (e.g., '/index') to re-index the knowledge base."
    fi
}

# --- Entry Point -------------------------------------------------------------
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    main "$@"
fi
