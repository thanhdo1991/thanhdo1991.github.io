# import/import.py
# Import các file .txt truyện từ crawled_data/stories vào WPDrupal (local).
# Tương thích workflow Drupal + XAMPP trên Windows.
# Usage: python import/import.py

import json
import os
import re
import subprocess
import sys
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

BASE_DIR = Path(__file__).resolve().parent.parent
STORIES_DIR = BASE_DIR / "crawled_data" / "stories"
METADATA_FILE = BASE_DIR / "crawled_data" / "metadata.json"


def parse_title_from_filename(filename):
    # Lấy phần tên trước dấu "(" hoặc trước đuôi .txt
    name = filename
    for marker in [" (", "（"]:
        if marker in name:
            name = name.split(marker)[0]
    return name.strip()


def slugify(name):
    """Tạo slug ASCII từ tên truyện."""
    import unicodedata
    s = unicodedata.normalize("NFKD", name)
    s = s.encode("ascii", "ignore").decode("ascii")
    s = re.sub(r"[^a-zA-Z0-9]+", "-", s).strip("-").lower()
    return s or "story"


def main():
    if not STORIES_DIR.exists():
        print("No stories dir; nothing to import.")
        return

    # Gộp metadata (nếu có) để lấy tiêu đề gốc
    metadata = {}
    if METADATA_FILE.exists():
        with open(METADATA_FILE, "r", encoding="utf-8") as f:
            for story in json.load(f):
                slug = story.get("slug")
                if slug:
                    metadata[slug] = story.get("title", slug)

    for path in sorted(STORIES_DIR.glob("*.txt")):
        title = parse_title_from_filename(path.name)
        slug = path.stem if path.stem.islower().replace("-", "") else slugify(title)
        if slug in metadata:
            title = metadata[slug]
        print(f"IMPORT: {title}  ({path.name})")
        # Gọi import_story.py để đẩy vào Drupal
        try:
            subprocess.run(
                [sys.executable, str(Path(__file__).parent / "import_story.py"),
                 str(path), "--title", title],
                check=True,
            )
        except subprocess.CalledProcessError as e:
            print(f"  ❌ {e}")


if __name__ == "__main__":
    main()