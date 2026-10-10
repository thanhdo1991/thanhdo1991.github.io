"""
MEGA downloader wrapper — tải file mega.nz bằng megatools qua chuỗi shortlink
link.sachiepvien.net. Tương tự dl_one nhưng nhận URL từ dòng lệnh với
optional shortlink resolve.

Usage:
    python crawler/mega_downloader.py <mega_or_shortlink_url> [--out <name>]
"""
import argparse
import logging
import os
import subprocess
import sys
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

BASE_DIR = Path(__file__).resolve().parent.parent
STORIES_DIR = BASE_DIR / "crawled_data" / "stories"


def find_megatools():
    common_paths = [
        r"C:\ProgramData\chocolatey\bin\megatools.exe",
        "megatools",
    ]
    for path in common_paths:
        if os.path.exists(path):
            return path
    return "megatools"


def resolve_to_mega(url, timeout=15):
    """Nếu là shortlink của sachiepvien.net, theo redirect tới mega.nz. Giữ nguyên nếu đã là mega."""
    if "mega.nz" in url or "mega.co.nz" in url:
        return url
    if "link.sachiepvien.net" not in url:
        return url
    import requests
    try:
        r = requests.get(url, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                          "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }, allow_redirects=True, timeout=timeout)
        if r.url and "mega.nz/file/" in r.url:
            return r.url
    except Exception:
        pass
    return None


def main():
    parser = argparse.ArgumentParser(description="Download MEGA via megatools")
    parser.add_argument("url", help="mega.nz URL hoặc shortlink")
    parser.add_argument("--out", help="Tên file output (mặc định dùng id trong URL)")
    args = parser.parse_args()

    mega_url = resolve_to_mega(args.url)
    if not mega_url:
        logger.error("Không resolve được tới mega.nz")
        sys.exit(1)

    slug = args.out or mega_url.split("file/")[-1].split("#")[0]
    STORIES_DIR.mkdir(parents=True, exist_ok=True)
    out = STORIES_DIR / f"{slug}_full.txt"

    megatools = find_megatools()
    try:
        result = subprocess.run(
            [megatools, "dl", "--no-progress", "--path", str(out), mega_url],
            capture_output=True, text=True, timeout=300
        )
    except subprocess.TimeoutExpired:
        logger.error("Timeout")
        sys.exit(1)
    except FileNotFoundError:
        logger.error(f"megatools not found: {megatools}")
        sys.exit(1)

    if result.returncode != 0:
        logger.error(result.stderr.strip())
        sys.exit(1)
    if out.exists() and out.stat().st_size > 50000:
        logger.info(f"SUCCESS: {out} ({out.stat().st_size} bytes)")
    else:
        logger.error("File rỗng hoặc quá nhỏ")
        sys.exit(1)


if __name__ == "__main__":
    main()