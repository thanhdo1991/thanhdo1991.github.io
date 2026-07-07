# crawler/collect_links.py
import requests
from bs4 import BeautifulSoup
import json
import time
import sys
import os
from urllib.robotparser import RobotFileParser
from urllib.parse import urlparse

CATEGORY_URL = "https://sachiepvien.net/category/de-cu/"
ROBOTS_URL = "https://sachiepvien.net/robots.txt"
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "crawled_data", "de-cu")
LINKS_FILE = os.path.join(OUTPUT_DIR, "links.json")
LOG_FILE = os.path.join(OUTPUT_DIR, "crawl_log.json")
RATE_LIMIT = 1.0  # seconds between requests
MAX_RETRIES = 3
RETRY_DELAY = 2.0  # initial backoff seconds

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def check_robots():
    """Check robots.txt permission before crawling."""
    rp = RobotFileParser()
    rp.set_url(ROBOTS_URL)
    rp.read()
    path = urlparse(CATEGORY_URL).path
    allowed = rp.can_fetch("*", CATEGORY_URL)
    if not allowed:
        print(f"ERROR: robots.txt disallows crawling {path}")
        sys.exit(1)
    print(f"robots.txt check: {path} allowed={allowed}")

def fetch_with_retry(url, max_retries=MAX_RETRIES, timeout=30):
    """Fetch URL with retry and exponential backoff."""
    last_exc = None
    for attempt in range(1, max_retries + 1):
        try:
            resp = requests.get(url, headers=HEADERS, timeout=timeout)
            resp.raise_for_status()
            return resp
        except (requests.ConnectionError, requests.Timeout, requests.HTTPError) as e:
            last_exc = e
            if attempt < max_retries:
                delay = RETRY_DELAY * (2 ** (attempt - 1))
                print(f"    Retry {attempt}/{max_retries} after {delay:.0f}s: {e}")
                time.sleep(delay)
    raise last_exc

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
    resp = fetch_with_retry(url)
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

def find_total_pages(soup_cache=None):
    """Find the last page number from pagination.

    Args:
        soup_cache: Optional BeautifulSoup object from page 1 (avoids duplicate fetch).

    Returns:
        Tuple of (max_page, soup_cache): max page number and the soup for page 1.
    """
    if soup_cache is None:
        print("Finding total pages...")
        resp = fetch_with_retry(CATEGORY_URL)
        soup = BeautifulSoup(resp.text, "html.parser")
    else:
        soup = soup_cache

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

    return max_page or 1, soup

def main():
    ensure_dir()
    log = load_progress()

    if log["completed"]:
        print(f"Crawl already completed! Found {len(log['links'])} links total.")
        return

    check_robots()

    if log["total_pages"] is None:
        total_pages, soup_cache = find_total_pages()
        log["total_pages"] = total_pages
        print(f"Total pages to crawl: {log['total_pages']}")
    else:
        soup_cache = None

    start_page = log["current_page"]
    print(f"Starting from page {start_page}")

    for page in range(start_page, log["total_pages"] + 1):
        print(f"\n--- Page {page}/{log['total_pages']} ---")
        try:
            # Use cached soup from find_total_pages for page 1 to avoid duplicate fetch
            if page == 1 and soup_cache is not None:
                print(f"  Using cached page 1 content")
                h2_links = []
                for h2 in soup_cache.find_all("h2"):
                    a = h2.find("a", href=True)
                    if a and is_story_url(a["href"]):
                        h2_links.append(a["href"].rstrip("/"))
                seen = set()
                page_links = []
                for link in h2_links:
                    if link not in seen:
                        seen.add(link)
                        page_links.append(link)
                print(f"    Found {len(page_links)} story links")
            else:
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
