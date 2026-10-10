"""
Batch MEGA downloader: đọc danh sách link mega từ metadata.json (crawled_data)
rồi tải lần lượt bằng mega_direct hoặc megatools.

Usage:
    python crawler/batch_download.py                  # tải tất cả story trong metadata
    python crawler/batch_download.py <file-of-urls>   # tải các URL mega trong 1 file văn bản
"""
import sys
import os
import time
import traceback
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))

from mega_direct import parse_mega_url, download_file  # noqa: E402

STORIES_DIR = BASE_DIR / "crawled_data" / "stories"
METADATA_FILE = BASE_DIR / "crawled_data" / "metadata.json"
RATE_LIMIT = 3.0


def iter_mega_urls():
    """Yields (slug_or_name, mega_url) pairs."""
    # Nếu argument là file text chứa URL dòng này nọ
    if len(sys.argv) > 1 and os.path.exists(sys.argv[1]):
        with open(sys.argv[1], "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    name = os.path.splitext(os.path.basename(line.split("/")[-1]))[0]
                    yield name, line
        return

    # Mặc định: đọc metadata.json, lấy download_links -> parse redirect
    import json
    import requests  # noqa: F401  (dùng cho fetch, giữ import cho rõ)

    if not METADATA_FILE.exists():
        print("No metadata.json found; pass a file-of-urls instead.")
        return
    with open(METADATA_FILE, "r", encoding="utf-8") as f:
        metadata = json.load(f)

    def base64_decode(s):
        import base64
        s = s.replace("-", "+").replace("_", "/")
        while len(s) % 4:
            s += "="
        return base64.b64decode(s).decode("utf-8", errors="replace")

    def resolve(link):
        if "mega.nz" in link:
            return link
        if "redirect.html" in link and "url=" in link:
            enc = link.split("url=")[1].split("&")[0]
            return resolve(base64_decode(enc))
        if "link.sachiepvien.net" in link:
            import requests
            try:
                return requests.get(link, timeout=15, allow_redirects=True).url or link
            except Exception:
                return None
        return None

    for story in metadata:
        slug = story.get("slug", "story")
        for link in story.get("download_links", []):
            mega = resolve(link)
            if mega and "mega.nz/file/" in mega:
                yield slug, mega
                break


def main():
    STORIES_DIR.mkdir(parents=True, exist_ok=True)
    seen = set()
    ok = fail = 0
    for name, mega_url in iter_mega_urls():
        if mega_url in seen:
            continue
        seen.add(mega_url)
        file_id, key_b64 = parse_mega_url(mega_url)
        if not file_id or not key_b64:
            print(f"  skip (bad url): {mega_url[:60]}")
            fail += 1
            continue
        out = STORIES_DIR / f"{name}_full.txt"
        print(f"[{len(seen)}] {name}")
        try:
            if download_file(file_id, key_b64, str(out)):
                ok += 1
                print(f"    ✅ {out.name} ({out.stat().st_size} bytes)")
            else:
                fail += 1
                print(f"    ❌ failed")
        except Exception as e:
            fail += 1
            print(f"    ❌ {e}")
            traceback.print_exc()
        time.sleep(RATE_LIMIT)

    print(f"\nDone: {ok} ok, {fail} failed, {len(seen)} unique.")


if __name__ == "__main__":
    main()