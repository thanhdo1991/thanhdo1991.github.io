#!/usr/bin/env bash
# =============================================================================
# recall.sh — Recall knowledge before task
# =============================================================================
# Purpose: Query the RAG vector store for relevant knowledge before starting
#          a task, injecting context into the prompt.
# Platform: Cross-platform (Bash on Linux/macOS/WSL/Git Bash)
# =============================================================================
# USAGE
#   ./recall.sh "task description" [tags...]
#
# EXAMPLE
#   ./recall.sh "Add database migration for users table" "database" "migration"
# =============================================================================

set -euo pipefail

# --- Configuration -----------------------------------------------------------
: "${AI_DIR:="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"}"
: "${PROJECT_ROOT:="$(cd "$AI_DIR/.." && pwd)"}"
: "${CHROMA_DIR:="$PROJECT_ROOT/.chroma"}"
: "${TOP_K:=5}"
: "${CONFIDENCE_THRESHOLD:=0.6}"

# --- Colors ------------------------------------------------------------------
GREEN='\033[0;32m'; YELLOW='\033[1;33m'; RED='\033[0;31m'; NC='\033[0m'

# --- Functions ---------------------------------------------------------------

usage() {
    cat <<EOF
Usage: $(basename "$0") "task description" [tags...]

Search the RAG knowledge base for relevant context.

Arguments:
  task_description   Required. The task to find relevant knowledge for.
  tags               Optional. Filter by content tags.

Environment Variables:
  TOP_K               Max results to return (default: 5)
  CONFIDENCE_THRESHOLD  Minimum confidence [0-1] (default: 0.6)
EOF
    exit 0
}

log_info()  { echo -e "${GREEN}[INFO]${NC}  $*"; }
log_warn()  { echo -e "${YELLOW}[WARN]${NC}  $*"; }
log_error() { echo -e "${RED}[ERROR]${NC} $*"; }

validate_env() {
    if ! command -v python3 &>/dev/null && ! command -v python &>/dev/null; then
        log_error "Python is required but not found in PATH."
        exit 1
    fi
    if [ ! -d "$AI_DIR" ]; then
        log_error "AI directory not found: $AI_DIR"
        exit 1
    fi
}

# --- Main ---------------------------------------------------------------------

main() {
    if [ $# -lt 1 ]; then
        usage
    fi

    TASK_DESCRIPTION="$1"
    shift
    TAGS=("$@")

    validate_env

    log_info "Task: $TASK_DESCRIPTION"
    log_info "Tags: ${TAGS[*]:-(none)}"
    log_info "Threshold: $CONFIDENCE_THRESHOLD"

    # --- PSEUDOCODE: Actual RAG query logic ---
    # 1. Parse frontmatter from all .md files in .ai/{reflections,decisions,patterns,failures}
    # 2. Generate embedding for TASK_DESCRIPTION
    # 3. Query ChromaDB collection '$KNOWLEDGE_COLLECTION' (default: {{PROJECT_NAME}}_framework_knowledge) with cosine similarity
    # 4. Filter results where confidence >= CONFIDENCE_THRESHOLD
    # 5. Optionally filter by tags if provided
    # 6. Return top TOP_K results with similarity scores
    # 7. Print formatted results
    #
    # Python equivalent:
    #   python3 <<-EOF
    #     import chromadb
    #     client = chromadb.PersistentClient(path="$CHROMA_DIR")
    #     collection = client.get_collection("${KNOWLEDGE_COLLECTION:-{{PROJECT_NAME}}_framework_knowledge}")
    #     results = collection.query(
    #         query_texts=["$TASK_DESCRIPTION"],
    #         n_results=$TOP_K,
    #         where={"confidence": {"$gte": $CONFIDENCE_THRESHOLD}}
    #     )
    #     print(results)
    #   EOF

    echo ""
    log_info "=== Relevant Knowledge Retrieved ==="
    echo "  - Review the results above before starting the task."
    echo "  - Run the reflect command (e.g., '/reflect') after completion to save learnings."
    echo ""

    # --- Output placeholder for CLI integration ---
    cat <<RESULTS
| Field                 | Value                |
|-----------------------|----------------------|
| Task                  | $TASK_DESCRIPTION    |
| Tags filter           | ${TAGS[*]:-none}     |
| Top-K                 | $TOP_K               |
| Confidence threshold  | $CONFIDENCE_THRESHOLD |
| Results               | (see above)          |
RESULTS
}

# --- Entry Point -------------------------------------------------------------
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    main "$@"
fi
