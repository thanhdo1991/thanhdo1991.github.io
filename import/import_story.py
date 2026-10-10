# import/import_story.py
# Import 1 file truyện .txt vào Drupal (workspace local, XAMPP).
# Usage: python import_story.py <path-to-.txt> [--title "Tên truyện"]

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")


def main():
    parser = argparse.ArgumentParser(description="Import 1 truyện vào Drupal local")
    parser.add_argument("txt_path", help="Đường dẫn tới file .txt truyện")
    parser.add_argument("--title", default=None, help="Tiêu đề truyện (mặc định lấy từ tên file)")
    parser.add_argument("--type", default="story", help="Node type trong Drupal (mặc định: story)")
    parser.add_argument("--drush", default="drush", help="Lệnh drush (có thể chỉ path)")
    args = parser.parse_args()

    path = Path(args.txt_path)
    if not path.exists():
        print(f"ERROR: file không tồn tại: {path}")
        sys.exit(1)

    with open(path, "r", encoding="utf-8") as f:
        body = f.read()

    title = args.title or path.stem
    # Cố gắng đầy lên Drupal bằng drush (cần cài drush + site XAMPP đang chạy)
    try:
        cmd = [
            args.drush, "php:eval",
            "node import --title=" + json.dumps(title) +
            " --type=" + args.type +
            " --body=" + json.dumps(body[:100000])
        ]
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        if result.returncode == 0:
            print(f"IMPORTED: {title}")
        else:
            print(f"drush fail: {result.stderr.strip()[:300]}")
            sys.exit(1)
    except (FileNotFoundError, subprocess.TimeoutExpired) as e:
        print(f"ERROR: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()