"""
Download a single MEGA file using the pure-Python MEGA API client (mega_direct.py).
Usage: python crawler/download_mega.py <mega_url> [output_name]

Nhánh nhanh: dùng mega_direct để tải + giải mã 1 file mega.nz về crawled_data/stories.
"""
import sys
import os
import traceback
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))

from mega_direct import parse_mega_url, download_file  # noqa: E402

STORIES_DIR = BASE_DIR / "crawled_data" / "stories"


def main():
    if len(sys.argv) < 2:
        print("Usage: python crawler/download_mega.py <mega_url> [output_name]")
        sys.exit(1)
    mega_url = sys.argv[1].strip()
    out_name = sys.argv[2] if len(sys.argv) > 2 else None

    file_id, key_b64 = parse_mega_url(mega_url)
    if not file_id or not key_b64:
        print(f"ERROR: not a valid mega.nz/file URL: {mega_url}")
        sys.exit(1)

    if not out_name:
        out_name = file_id + ".txt"
    STORIES_DIR.mkdir(parents=True, exist_ok=True)
    out = STORIES_DIR / out_name

    print(f"File ID: {file_id}")
    print(f"Output : {out}")
    try:
        ok = download_file(file_id, key_b64, str(out))
        if ok:
            print(f"SUCCESS: {out} ({out.stat().st_size} bytes)")
            sys.exit(0)
        print("FAILED to download/decrypt")
        sys.exit(1)
    except Exception as e:
        print("ERROR: " + str(e))
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()