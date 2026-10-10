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

MIN_FILE_SIZE = 50000  # 50KB - stories should be larger than this


def find_megatools():
    """Find megatools executable."""
    common_paths = [
        r"C:\ProgramData\chocolatey\bin\megatools.exe",
        "megatools",
    ]
    for path in common_paths:
        if os.path.exists(path):
            return path
    return "megatools"


def main():
    parser = argparse.ArgumentParser(description="Download a MEGA file using megatools")
    parser.add_argument("mega_url", help="MEGA.nz file URL")
    parser.add_argument("-s", "--slug", help="Output filename slug (default: extracted from URL)")
    parser.add_argument("-o", "--output-dir", default="crawled_data/stories", help="Output directory")
    parser.add_argument("-t", "--timeout", type=int, default=120, help="Download timeout in seconds")
    parser.add_argument("--min-size", type=int, default=MIN_FILE_SIZE, help="Minimum file size in bytes")
    args = parser.parse_args()

    if args.slug:
        slug = args.slug
    else:
        slug = args.mega_url.split("/")[-1].split("#")[0]

    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / f"{slug}_full.txt"

    megatools = find_megatools()
    logger.info(f"Downloading to: {out}")

    try:
        result = subprocess.run(
            [megatools, "dl", "--no-progress", "--path", str(out), args.mega_url],
            capture_output=True, text=True, timeout=args.timeout
        )
    except subprocess.TimeoutExpired:
        logger.error(f"Download timed out after {args.timeout}s")
        sys.exit(1)
    except FileNotFoundError:
        logger.error(f"megatools not found at: {megatools}")
        sys.exit(1)

    if result.returncode != 0:
        logger.error(f"megatools failed (exit code {result.returncode})")
        if result.stderr:
            logger.error(f"STDERR: {result.stderr.strip()}")
        sys.exit(1)

    if not out.exists():
        logger.error("File not found after download")
        sys.exit(1)

    file_size = out.stat().st_size
    if file_size < args.min_size:
        logger.warning(f"File too small ({file_size:,} bytes < {args.min_size:,}), might be error page")
        out.unlink()
        sys.exit(1)

    logger.info(f"SUCCESS: {out} ({file_size:,} bytes)")


if __name__ == "__main__":
    main()