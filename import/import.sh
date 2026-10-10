#!/usr/bin/env bash
# import/import.sh — import tất cả truyện .txt vào Drupal (dùng trên Linux/WSL/Git Bash)
set -euo pipefail
cd "$(dirname "$0")/.."

PY=${PYTHON:-python}
"$PY" import/import.py "$@"