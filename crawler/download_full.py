"""
Batch MEGA story downloader for sachiepvien.net.

Dùng mega.py (có monkey-patch for Python 3.14) để tải và giải mã
file từ MEGA.nz thông qua link.sachiepvien.net.

Usage:
    python crawler/download_full.py              # tải tất cả
    python crawler/download_full.py --resume     # tải tiếp
    python crawler/download_full.py --test       # tải 2 truyện đầu
"""

import asyncio
import json
import os
import re
import sys
import tempfile
import time
import traceback
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

# Monkey-patch asyncio.coroutine cho Python 3.14 (mega.py dùng API cũ)
if not hasattr(asyncio, "coroutine"):
    asyncio.coroutine = lambda x: x

import shutil
from mega import Mega

# --- Paths ---
BASE_DIR = Path(__file__).resolve().parent.parent
METADATA_FILE = BASE_DIR / "crawled_data" / "metadata.json"
STORIES_DIR = BASE_DIR / "crawled_data" / "stories"
LOG_FILE = BASE_DIR / "crawled_data" / "download_full_log.json"

RATE_LIMIT = 3.0  # seconds between downloads (respect server)


def base64_decode(s):
    """Decode MEGA base64-url encoding."""
    import base64
    s = s.replace("-", "+").replace("_", "/")
    remainder = len(s) % 4
    if remainder:
        s += "=" * (4 - remainder)
    return base64.b64decode(s)


def parse_redirect_url(url):
    """Decode sachiepvien.net redirect URL to get the real MEGA link."""
    if "redirect.html" in url and "url=" in url:
        encoded = url.split("url=")[1].split("&")[0]
        try:
            decoded = base64_decode(encoded).decode("utf-8")
            return decoded
        except Exception:
            return None
    if "link.sachiepvien.net" in url:
        return url
    return None


def get_mega_url(story):
    """Extract MEGA URL from a story's download links."""
    for link in story.get("download_links", []):
        parsed = parse_redirect_url(link)
        if parsed:
            return parsed
        # Direct mega.nz link
        if "mega.nz" in link:
            return link
    return None


def resolve_mega_url(shortlink, timeout=15):
    """Follow HTTP redirect to resolve link.sachiepvien.net -> mega.nz URL."""
    import requests
    try:
        resp = requests.get(
            shortlink,
            headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                              "AppleWebKit/537.36 (KHTML, like Gecko) "
                              "Chrome/120.0.0.0 Safari/537.36"
            },
            allow_redirects=True,
            timeout=timeout,
        )
        final = resp.url
        if "mega.nz/file/" in final:
            return final
    except Exception:
        pass
    return None


def load_metadata():
    if METADATA_FILE.exists():
        with open(METADATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def save_metadata(metadata_list):
    with open(METADATA_FILE, "w", encoding="utf-8") as f:
        json.dump(metadata_list, f, ensure_ascii=False, indent=2)


def load_log():
    if LOG_FILE.exists():
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"completed": [], "errors": [], "skipped": []}


def save_log(log):
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        json.dump(log, f, ensure_ascii=False, indent=2)


def check_existing_full(slug):
    """Check if we already have a full download (>50KB) for this slug."""
    # Check all files in stories dir that start with the slug
    for fpath in STORIES_DIR.glob(f"{slug}_*.txt"):
        if fpath.stat().st_size > 50000:
            return True
    # Also check the slug.txt itself (but it was excerpt, so unlikely)
    fpath = STORIES_DIR / f"{slug}.txt"
    if fpath.exists() and fpath.stat().st_size > 50000:
        return True
    return False


def download_story(story, mega_instance):
    """Download one story from MEGA and save it."""
    slug = story["slug"]
    title = story.get("title", slug)

    # Check if already downloaded
    if check_existing_full(slug):
        print(f"  Already have full download: {slug}")
        return {"status": "skipped", "reason": "already_exists"}

    # Get MEGA URL
    shortlink = get_mega_url(story)
    if not shortlink:
        print(f"  No MEGA/shortlink found: {slug}")
        return {"status": "error", "reason": "no_link"}

    # Resolve shortlink -> mega.nz URL
    print(f"  Resolving link...")
    mega_url = resolve_mega_url(shortlink)
    if not mega_url:
        print(f"  Could not resolve to MEGA: {shortlink[:80]}")
        return {"status": "error", "reason": "resolve_failed", "url": shortlink}

    print(f"  MEGA URL: {mega_url[:80]}...")

    # Prepare output filename (use slug prefix)
    # mega.py will try to name the file after the original filename
    # We need to handle the file after download
    temp_dir = STORIES_DIR  # download directly here

    try:
        # mega.py's download_url downloads to a temp file then moves
        # The move can fail on Windows with Unicode filenames
        # So we intercept with a custom temp download

        # Use a custom approach: download to temp, then copy with proper name
        file_id = mega_url.split("file/")[1].split("#")[0]
        key = mega_url.split("#")[1] if "#" in mega_url else ""

        # Download using mega.py's internal method
        result = mega_instance.download_url(
            mega_url,
            dest_path=str(temp_dir),
        )

        if result and os.path.exists(result):
            # Rename to standardized name
            ext = ".txt"  # All stories should be .txt
            proper_name = f"{slug}_full{ext}"
            proper_path = STORIES_DIR / proper_name

            # If the result has a weird name, rename it
            if Path(result).name != proper_name:
                # Check if already exists
                if proper_path.exists():
                    proper_path.unlink()
                shutil.move(result, str(proper_path))
                result = str(proper_path)

            file_size = os.path.getsize(result)
            print(f"  ✅ SUCCESS: {proper_name} ({file_size:,} bytes)")

            # Update metadata
            story["txt_file"] = proper_name
            story["txt_size_bytes"] = file_size

            return {"status": "success", "file": proper_name, "size": file_size}
        else:
            print(f"  ❌ mega.py returned None or empty")
            return {"status": "error", "reason": "mega_returned_none"}

    except Exception as e:
        print(f"  ❌ Error: {e}")
        traceback.print_exc()

        # Check if file was actually downloaded despite error
        # Sometimes shutil.move fails but file is in temp
        return {"status": "error", "reason": str(e)[:200]}


def main():
    args = set(sys.argv[1:])
    is_test = "--test" in args
    is_resume = "--resume" in args

    print("=" * 60)
    print("  MEGA Story Downloader for sachiepvien.net")
    print("=" * 60)
    print()

    # Load data
    metadata = load_metadata()
    log = load_log()
    total = len(metadata)
    print(f"Total stories in metadata: {total}")
    print(f"Already completed (log): {len(log['completed'])}")
    print(f"Errors so far: {len(log['errors'])}")
    print()

    # Filter stories to process
    to_process = []
    for story in metadata:
        slug = story["slug"]
        if slug in log["completed"]:
            continue
        if slug in log.get("skipped", []):
            continue
        # Check if already have full download
        if check_existing_full(slug):
            log.setdefault("completed", []).append(slug)
            continue
        to_process.append(story)

    if is_test:
        to_process = to_process[:2]

    if not to_process:
        print("✅ All stories already downloaded!")
        return

    print(f"Stories to download: {len(to_process)}")
    print()

    # Initialize MEGA
    print("Initializing MEGA client...")
    mega = Mega()
    print("  Authenticated (anonymous)")
    print()

    # Process
    success_count = 0
    error_count = 0
    skip_count = 0

    for i, story in enumerate(to_process):
        slug = story["slug"]
        title = story.get("title", slug)[:60]

        print(f"[{i+1}/{len(to_process)}] {title}")
        print(f"  Slug: {slug}")

        result = download_story(story, mega)

        if result["status"] == "success":
            success_count += 1
            log["completed"].append(slug)
            # Update metadata in-place
            story["txt_file"] = result["file"]
            story["txt_size_bytes"] = result["size"]
            story["download_source"] = "mega_full"
            save_metadata(metadata)
            save_log(log)
        elif result["status"] == "skipped":
            skip_count += 1
            log["completed"].append(slug)
            save_log(log)
        else:
            error_count += 1
            log_entry = {"slug": slug, "reason": result.get("reason", "unknown")}
            if "url" in result:
                log_entry["url"] = result["url"]
            log["errors"].append(log_entry)
            save_log(log)

        print()
        time.sleep(RATE_LIMIT)

        if is_test and success_count >= 2:
            break

    # Summary
    print("=" * 60)
    print("  DOWNLOAD SUMMARY")
    print("=" * 60)
    print(f"  Total processed: {len(to_process)}")
    print(f"  ✅ Success: {success_count}")
    print(f"  ⏭️  Skipped: {skip_count}")
    print(f"  ❌ Errors: {error_count}")
    print()
    print(f"  Total downloaded: {len(log['completed'])}/{total}")
    print()

    # Show any errors
    if log["errors"]:
        print("Recent errors:")
        for err in log["errors"][-5:]:
            print(f"  - {err['slug']}: {err['reason']}")
        print()


if __name__ == "__main__":
    main()