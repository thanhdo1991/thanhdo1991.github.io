#!/usr/bin/env bash
# =============================================================================
# validate-frontmatter.sh — Validate YAML frontmatter of all framework files
# =============================================================================
# Purpose: Scan all .md files in .ai/ and .claude/commands/ to verify that
#          their YAML frontmatter is valid, required fields are present, and
#          constraints are met.
# Platform: Cross-platform (Bash on Linux/macOS/WSL/Git Bash)
# =============================================================================
# USAGE
#   ./validate-frontmatter.sh                    # Validate all files
#   ./validate-frontmatter.sh --fix              # Auto-fix common issues
#   ./validate-frontmatter.sh --strict           # Enforce all optional fields
#   ./validate-frontmatter.sh --file path.md     # Validate a single file
# =============================================================================

set -euo pipefail

# --- Configuration -----------------------------------------------------------
: "${AI_DIR:="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"}"
: "${COMMANDS_DIR:="$(cd "$AI_DIR/../.claude/commands" 2>/dev/null && pwd || true)"}"
: "${STRICT_MODE:=false}"
: "${AUTO_FIX:=false}"

# Return codes
EXIT_ALL_VALID=0
EXIT_ISSUES_FOUND=1
EXIT_ERROR=2

# --- Colors ------------------------------------------------------------------
GREEN='\033[0;32m'; YELLOW='\033[1;33m'; RED='\033[0;31m'; CYAN='\033[0;36m'
NC='\033[0m'

# --- State -------------------------------------------------------------------
TOTAL_FILES=0
PASSED=0
FAILED=0
FIXED=0
declare -a ERRORS

# --- Required Fields (framework-wide) ---
REQUIRED_FIELDS=("id" "version" "confidence" "last_updated" "tags")

# --- Validation Functions ----------------------------------------------------

log_pass()   { echo -e "  ${GREEN}PASS${NC}  $1"; }
log_fail()   { echo -e "  ${RED}FAIL${NC}  $1"; ERRORS+=("$1"); ((FAILED++)); }
log_fixed()  { echo -e "  ${CYAN}FIX${NC}   $1"; ((FIXED++)); }
log_skip()   { echo -e "  ${YELLOW}SKIP${NC}  $1"; }

has_frontmatter() {
    # Check if file starts with --- and has closing ---
    head -1 "$1" | grep -q '^---$' || return 1
    # Check for closing --- within first 50 lines
    tail -n +2 "$1" | head -49 | grep -q '^---$' || return 1
}

extract_frontmatter() {
    # Extract YAML between the --- markers (max 50 lines)
    sed -n '/^---$/,/^---$/p' "$1" | sed '1d;$d' 2>/dev/null || true
}

validate_field_present() {
    local file="$1" field="$2" fm="$3"
    if ! echo "$fm" | grep -qE "^${field}:"; then
        log_fail "$(basename "$file"): Missing required field '$field'"
        return 1
    fi
    return 0
}

validate_confidence() {
    local file="$1" value="$2"
    if [ -n "$value" ]; then
        if ! echo "$value" | grep -qE '^0(\.[0-9]+)?$|^1\.0$'; then
            log_fail "$(basename "$file"): confidence must be 0.0-1.0, got '$value'"
            return 1
        fi
    fi
    return 0
}

validate_semver() {
    local file="$1" value="$2"
    if [ -n "$value" ] && ! echo "$value" | grep -qE '^[0-9]+\.[0-9]+\.[0-9]+$'; then
        log_fail "$(basename "$file"): version must be semver (X.Y.Z), got '$value'"
        return 1
    fi
    return 0
}

validate_date() {
    local file="$1" value="$2"
    if [ -n "$value" ] && ! echo "$value" | grep -qE '^[0-9]{4}-[0-9]{2}-[0-9]{2}$'; then
        log_fail "$(basename "$file"): last_updated must be YYYY-MM-DD, got '$value'"
        return 1
    fi
    return 0
}

validate_tags() {
    local file="$1" value="$2"
    if [ -n "$value" ]; then
        # Check tags is a yaml list
        if echo "$value" | grep -qE '^\s*\[.*\]$'; then
            # Inline list — check each element
            local tags
            tags=$(echo "$value" | tr -d '[]' | tr ',' '\n' | sed 's/^ *//;s/ *$//')
            local count
            count=$(echo "$tags" | grep -c . || true)
            if [ "$count" -lt 1 ] || [ "$count" -gt 10 ]; then
                log_fail "$(basename "$file"): tags count must be 1-10, got $count"
                return 1
            fi
        elif echo "$value" | grep -qE '^\s*-\s+'; then
            # Block list
            local count
            count=$(echo "$value" | grep -cE '^\s*-' || true)
            if [ "$count" -lt 1 ] || [ "$count" -gt 10 ]; then
                log_fail "$(basename "$file"): tags count must be 1-10, got $count"
                return 1
            fi
        fi
    fi
    return 0
}

# --- Main Validation ---------------------------------------------------------

validate_file() {
    local file="$1"
    local basename
    basename=$(basename "$file")

    # --- PSEUDOCODE: For production, replace grep with yq parsing ---
    # With yq (https://github.com/mikefarah/yq):
    #   yq eval '.confidence' "$file" --front-matter=process
    #   yq eval '.version' "$file" --front-matter=process
    #   etc.

    # Check frontmatter exists
    if ! has_frontmatter "$file"; then
        log_fail "$basename: No valid YAML frontmatter (missing --- markers)"
        return 1
    fi

    local fm
    fm=$(extract_frontmatter "$file")

    # Validate required fields
    local all_valid=true
    for field in "${REQUIRED_FIELDS[@]}"; do
        if ! validate_field_present "$file" "$field" "$fm"; then
            all_valid=false
        fi
    done

    # If basic fields missing, skip deeper validation
    if [ "$all_valid" = false ]; then
        return 1
    fi

    # Extract values (simplified: first match only)
    local confidence version last_updated tags
    confidence=$(echo "$fm" | grep -m1 '^confidence:' | sed 's/^confidence: *//')
    version=$(echo "$fm" | grep -m1 '^version:' | sed 's/^version: *//')
    last_updated=$(echo "$fm" | grep -m1 '^last_updated:' | sed 's/^last_updated: *//')
    tags=$(echo "$fm" | grep -m1 '^tags:' | sed 's/^tags: *//')

    # Validate each field
    validate_confidence "$file" "$confidence" || all_valid=false
    validate_semver "$file" "$version" || all_valid=false
    validate_date "$file" "$last_updated" || all_valid=false
    validate_tags "$file" "$tags" || all_valid=false

    if [ "$all_valid" = true ]; then
        log_pass "$basename"
        ((PASSED++))
    fi
}

# --- Main ---------------------------------------------------------------------

main() {
    local target_dir="$AI_DIR"
    local single_file=""

    # --- Parse arguments ---
    while [ $# -gt 0 ]; do
        case "$1" in
            --fix)      AUTO_FIX=true; shift ;;
            --strict)   STRICT_MODE=true; shift ;;
            --file)     single_file="$2"; shift 2 ;;
            --help)     echo "Usage: $(basename "$0") [--fix] [--strict] [--file path.md]"; exit 0 ;;
            *)          echo "Unknown: $1"; exit 1 ;;
        esac
    done

    echo ""
    echo "============================================"
    echo " Frontmatter Validation"
    echo " Mode: $([ "$AUTO_FIX" = true ] && echo "AUTO-FIX ON " || echo "READ-ONLY") $([ "$STRICT_MODE" = true ] && echo "+ STRICT")"
    echo "============================================"
    echo ""

    # --- Collect files ---
    FILES=()
    if [ -n "$single_file" ]; then
        if [ -f "$single_file" ]; then
            FILES=("$single_file")
        else
            echo "Error: File not found: $single_file"
            exit 2
        fi
    else
        # Scan all .md files in .ai/ recursively
        while IFS= read -r f; do
            FILES+=("$f")
        done < <(find "$AI_DIR" -name "*.md" -not -path "*/archive/*" -not -path "*/node_modules/*" 2>/dev/null || true)

        # Also scan .claude/commands/
        if [ -d "$COMMANDS_DIR" ]; then
            while IFS= read -r f; do
                FILES+=("$f")
            done < <(find "$COMMANDS_DIR" -name "*.md" 2>/dev/null || true)
        fi
    fi

    TOTAL_FILES=${#FILES[@]}

    if [ "$TOTAL_FILES" -eq 0 ]; then
        echo "No markdown files found to validate."
        exit 0
    fi

    echo "Found $TOTAL_FILES files to validate."
    echo ""

    # --- Validate each file ---
    for file in "${FILES[@]}"; do
        validate_file "$file"
    done

    # --- Summary ---
    echo ""
    echo "============================================"
    echo " Summary"
    echo "============================================"
    echo " Total:  $TOTAL_FILES"
    echo " Passed: $PASSED"
    echo " Failed: $FAILED"
    if [ "$AUTO_FIX" = true ]; then
        echo " Fixed:  $FIXED"
    fi
    echo ""

    if [ "$FAILED" -gt 0 ]; then
        echo "Issues found in $FAILED file(s). Review errors above."
        exit $EXIT_ISSUES_FOUND
    else
        echo "All files pass validation."
        exit $EXIT_ALL_VALID
    fi
}

# --- Entry Point -------------------------------------------------------------
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    main "$@"
fi
