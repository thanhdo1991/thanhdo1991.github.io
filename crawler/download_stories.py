# crawler/download_stories.py
import requests
from bs4 import BeautifulSoup
import json
import time
import os
import re
import sys

LINKS_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "crawled_data", "de-cu", "links.json")
METADATA_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "crawled_data", "metadata.json")
LOG_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "crawled_data", "download_log.json")
STORIES_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "crawled_data", "stories")
RATE_LIMIT = 1.0

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def ensure_dir():
    os.makedirs(STORIES_DIR, exist_ok=True)

def load_links():
    with open(LINKS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def load_progress():
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"processed": 0, "total": None, "completed": [], "errors": []}

def save_progress(log):
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        json.dump(log, f, ensure_ascii=False, indent=2)

def save_metadata(metadata_list):
    with open(METADATA_FILE, "w", encoding="utf-8") as f:
        json.dump(metadata_list, f, ensure_ascii=False, indent=2)

def parse_story_page(url):
    print(f"  Fetching: {url}")
    resp = requests.get(url, headers=HEADERS, timeout=30)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    # Title
    title_tag = soup.find("h1") or soup.find("title")
    title = title_tag.get_text(strip=True) if title_tag else ""
    # Remove site name from title
    title = re.sub(r'\s*[-–|]\s*Sắc Hiệp Viện.*$', '', title).strip()

    # Description - try meta description
    desc = ""
    meta_desc = soup.find("meta", attrs={"name": "description"})
    if meta_desc:
        desc = meta_desc.get("content", "")

    # Category and tags
    categories = []
    tags = []
    for link in soup.find_all("a", href=True):
        href = link["href"]
        text = link.get_text(strip=True)
        if "/category/" in href:
            cat = href.split("/category/")[1].strip("/")
            if cat not in categories:
                categories.append(cat)
        elif "/tag/" in href:
            tag = href.split("/tag/")[1].strip("/")
            if tag not in tags:
                tags.append(tag)

    # Find download links (.txt files)
    download_links = []
    for a_tag in soup.find_all("a", href=True):
        href = a_tag["href"]
        if href.endswith(".txt") or "download" in href.lower() or "file" in href.lower():
            download_links.append(href)

    # Also search in iframes or embedded content for google drive or direct links
    for iframe in soup.find_all("iframe", src=True):
        src = iframe["src"]
        if "drive.google.com" in src:
            download_links.append(src)

    # Extract article content for description fallback
    article = soup.find("article") or soup.find("div", class_="post-content") or soup.find("div", class_="entry-content")
    if article:
        paragraphs = article.find_all("p")
        article_text = "\n".join(p.get_text(strip=True) for p in paragraphs[:3] if p.get_text(strip=True))
        if not desc:
            desc = article_text[:500] if len(article_text) > 500 else article_text

    # Generate slug from url
    slug = url.rstrip("/").split("/")[-1]

    return {
        "slug": slug,
        "title": title,
        "url": url,
        "categories": categories,
        "tags": tags,
        "description": desc,
        "download_links": download_links
    }

def download_file(url, filename):
    """Download a file from url and save to stories dir."""
    filepath = os.path.join(STORIES_DIR, filename)
    if os.path.exists(filepath) and os.path.getsize(filepath) > 0:
        print(f"    File already exists: {filename} ({os.path.getsize(filepath)} bytes)")
        return filepath

    try:
        resp = requests.get(url, headers=HEADERS, timeout=60)
        resp.raise_for_status()
        with open(filepath, "wb") as f:
            f.write(resp.content)
        print(f"    Downloaded: {filename} ({len(resp.content)} bytes)")
        return filepath
    except Exception as e:
        print(f"    ERROR downloading {url}: {e}")
        return None

def main():
    ensure_dir()
    links = load_links()
    log = load_progress()

    log["total"] = len(links)
    save_progress(log)

    metadata_list = []
    if os.path.exists(METADATA_FILE):
        with open(METADATA_FILE, "r", encoding="utf-8") as f:
            metadata_list = json.load(f)

    start_from = log["processed"]

    for i, url in enumerate(links):
        if i < start_from:
            continue

        slug = url.rstrip("/").split("/")[-1]
        if slug in log["completed"]:
            print(f"  Skipping (already done): {slug}")
            continue

        print(f"\n[{i+1}/{len(links)}] {slug}")

        try:
            story = parse_story_page(url)

            # Try to download first txt link
            txt_filename = f"{slug}.txt"
            local_path = None
            for dl_url in story["download_links"]:
                local_path = download_file(dl_url, txt_filename)
                if local_path:
                    story["txt_file"] = txt_filename
                    story["txt_size_bytes"] = os.path.getsize(local_path) if local_path else 0
                    break

            metadata_list.append(story)
            log["completed"].append(slug)
            log["processed"] = i + 1
            save_progress(log)
            save_metadata(metadata_list)

        except Exception as e:
            print(f"  ERROR processing {url}: {e}")
            log["errors"].append({"url": url, "error": str(e)})
            log["processed"] = i + 1
            save_progress(log)
            save_metadata(metadata_list)

        time.sleep(RATE_LIMIT)

    print(f"\nDone! Processed {log['processed']}/{len(links)} stories.")
    print(f"   Errors: {len(log['errors'])}")
    print(f"   Metadata saved to: {METADATA_FILE}")

if __name__ == "__main__":
    main()
