# crawler/collect_links.py
import requests
from bs4 import BeautifulSoup
import json
import time
import sys
import os

CATEGORY_URL = "https://sachiepvien.net/category/de-cu/"
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "crawled_data", "de-cu")
LINKS_FILE = os.path.join(OUTPUT_DIR, "links.json")
LOG_FILE = os.path.join(OUTPUT_DIR, "crawl_log.json")
RATE_LIMIT = 1.0  # seconds between requests

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

# Known non-story single-path pages on this domain
SKIP_PATHS = {
    "kho-truyen-v2", "series-lau-thap-cam", "vuc-sau-van-truong",
    "bang-xep-hang", "danh-sach-tac-gia", "blog-tin-tuc", "group-social",
}

def ensure_dir():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

def load_progress():
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"current_page": 1, "total_pages": None, "completed": False, "links": []}

def save_progress(log):
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        json.dump(log, f, ensure_ascii=False, indent=2)
    # Also save links separately for convenience
    with open(LINKS_FILE, "w", encoding="utf-8") as f:
        json.dump(log["links"], f, ensure_ascii=False, indent=2)

def is_story_url(href):
    """Check if a URL looks like a WordPress story/post URL."""
    if not href.startswith("https://sachiepvien.net/"):
        return False
    path = href.replace("https://sachiepvien.net/", "").rstrip("/")
    # Skip empty (homepage), multi-segment (dates like 2026/07/01), and known non-story paths
    if not path or "/" in path:
        return False
    if path in SKIP_PATHS:
        return False
    # Skip URLs with unwanted fragments/patterns
    if any(x in href for x in ["/category/", "/page/", "/feed/", "/wp-", "#", "javascript", "xmlrpc"]):
        return False
    return True

def collect_page_links(page_num):
    url = f"{CATEGORY_URL}page/{page_num}/" if page_num > 1 else CATEGORY_URL
    print(f"  Fetching page {page_num}: {url}")
    resp = requests.get(url, headers=HEADERS, timeout=30)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    # WordPress post titles are consistently inside <h2> tags
    links = []
    for h2 in soup.find_all("h2"):
        a = h2.find("a", href=True)
        if a and is_story_url(a["href"]):
            links.append(a["href"].rstrip("/"))

    # De-duplicate while preserving order
    seen = set()
    unique = []
    for link in links:
        if link not in seen:
            seen.add(link)
            unique.append(link)

    print(f"    Found {len(unique)} story links")
    return unique

def find_total_pages():
    """Find the last page number from pagination."""
    print("Finding total pages...")
    resp = requests.get(CATEGORY_URL, headers=HEADERS, timeout=30)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    max_page = 0
    for a_tag in soup.find_all("a", href=True):
        href = a_tag["href"]
        if "/category/de-cu/page/" in href:
            try:
                page_num = int(href.split("/page/")[1].split("/")[0])
                if page_num > max_page:
                    max_page = page_num
            except ValueError:
                pass

    if max_page == 0:
        # Check if there's a page 2 link
        for a_tag in soup.find_all("a", href=True):
            if "/category/de-cu/page/2/" in a_tag.get("href", ""):
                max_page = 1  # will be updated as we go
                break

    return max_page or 1

def main():
    ensure_dir()
    log = load_progress()

    if log["completed"]:
        print(f"Crawl already completed! Found {len(log['links'])} links total.")
        return

    if log["total_pages"] is None:
        log["total_pages"] = find_total_pages()
        print(f"Total pages to crawl: {log['total_pages']}")

    start_page = log["current_page"]
    print(f"Starting from page {start_page}")

    for page in range(start_page, log["total_pages"] + 1):
        print(f"\n--- Page {page}/{log['total_pages']} ---")
        try:
            page_links = collect_page_links(page)
            log["links"].extend(page_links)
            log["current_page"] = page + 1
            save_progress(log)
            print(f"  Total links so far: {len(log['links'])}")
        except Exception as e:
            print(f"  ERROR on page {page}: {e}")
            save_progress(log)
            print("Progress saved. Will resume next run.")
            sys.exit(1)

        if page < log["total_pages"]:
            time.sleep(RATE_LIMIT)

    log["completed"] = True
    save_progress(log)
    print(f"\nDone! Collected {len(log['links'])} story links.")

if __name__ == "__main__":
    main()
