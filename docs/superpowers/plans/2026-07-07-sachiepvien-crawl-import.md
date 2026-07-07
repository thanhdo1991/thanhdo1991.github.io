# Sắc Hiệp Viện — Crawl & Import Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Crawl category "Đề Cử" từ sachiepvien.net, set up WordPress local với XAMPP, import dữ liệu, custom theme đọc truyện.

**Architecture:** Python crawler lấy metadata + file .txt → WordPress import qua WP-CLI → Custom theme Underscores

**Tech Stack:** Python 3 + requests/bs4, WordPress 6.x, Underscores theme, XAMPP (Apache + MariaDB), WP-CLI

## Global Constraints

- Chỉ crawl category "Đề Cử" (28 pages)
- Rate limit: 1 request/giây
- Lưu trạng thái crawl để resume
- WordPress local tại D:\xampp\htdocs\sachiepvien
- PHP 8.2 compatible
- MariaDB 10.4 compatible
- Theme không dùng page builder
- No login/registration required

---

### Task 1: Crawl Script — Story Link Collector

**Files:**
- Create: `crawled_data/de-cu/links.json`
- Create: `crawled_data/de-cu/crawl_log.json`
- Create: `crawler/collect_links.py`

**Interfaces:**
- Consumes: Category URL `https://sachiepvien.net/category/de-cu/`
- Produces: `links.json` — mảng tất cả story URLs (string[]), `crawl_log.json` — trạng thái crawl

- [ ] **Step 1: Tạo virtualenv và cài dependencies**

```bash
cd /d/claude-sachiepvien
python -m venv .venv
source .venv/Scripts/activate
pip install requests beautifulsoup4
```

Expected output: `Successfully installed requests beautifulsoup4`

- [ ] **Step 2: Tạo thư mục và file script**

```bash
mkdir -p crawled_data/de-cu crawled_data/stories crawler
```

- [ ] **Step 3: Viết collect_links.py**

```python
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

def collect_page_links(page_num):
    url = f"{CATEGORY_URL}page/{page_num}/" if page_num > 1 else CATEGORY_URL
    print(f"  Fetching page {page_num}: {url}")
    resp = requests.get(url, headers=HEADERS, timeout=30)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")
    
    links = []
    for a_tag in soup.find_all("a", href=True):
        href = a_tag["href"]
        # Skip non-story links
        if any(x in href for x in ["/category/", "/page/", "/feed/", "/wp-", "#", "javascript", "xmlrpc"]):
            continue
        if href.startswith("https://sachiepvien.net/") and href.count("/") == 3:
            links.append(href.rstrip("/"))
    
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
    print(f"\n✅ Done! Collected {len(log['links'])} story links.")

if __name__ == "__main__":
    main()
```

- [ ] **Step 4: Chạy thử collector**

```bash
cd /d/claude-sachiepvien
.venv/Scripts/python crawler/collect_links.py
```

Expected: Crawl qua 28 pages, hiển thị tiến trình, output `links.json` với ~600-800 URLs

- [ ] **Step 5: Kiểm tra kết quả**

```bash
echo "Total links collected:"
python -c "import json; data=json.load(open('crawled_data/de-cu/links.json')); print(len(data)); print(data[0])"
```

---

### Task 2: Crawl Script — Story Detail + File Download

**Files:**
- Create: `crawler/download_stories.py`
- Modify: `crawled_data/de-cu/crawl_log.json` (thêm trạng thái download)
- Create: `crawled_data/metadata.json`

**Interfaces:**
- Consumes: `links.json` (mảng story URLs)
- Produces: `metadata.json` (mảng story metadata objects), file .txt trong `crawled_data/stories/`

- [ ] **Step 1: Viết download_stories.py**

```python
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
    
    print(f"\n✅ Done! Processed {log['processed']}/{len(links)} stories.")
    print(f"   Errors: {len(log['errors'])}")
    print(f"   Metadata saved to: {METADATA_FILE}")

if __name__ == "__main__":
    main()
```

- [ ] **Step 2: Chạy download script (test với 1 story trước)**

```bash
cd /d/claude-sachiepvien
# Test với 1 URL trước
python -c "
import json
links = json.load(open('crawled_data/de-cu/links.json'))
print(f'Total: {len(links)} links')
print(f'First: {links[0]}')
"
```

- [ ] **Step 3: Chạy download toàn bộ**

```bash
cd /d/claude-sachiepvien
.venv/Scripts/python crawler/download_stories.py
```

---

### Task 3: WordPress Site Local Setup

**Files:**
- None (setup environment)

**Interfaces:**
- Consumes: XAMPP environment
- Produces: WordPress running at `http://localhost/sachiepvien`

- [ ] **Step 1: Kiểm tra XAMPP services**

```bash
# Start Apache
"/d/xampp/apache/bin/httpd.exe" -k start 2>/dev/null || echo "Apache may be running already"

# Start MySQL
"/d/xampp/mysql/bin/mysqld.exe" --console 2>/dev/null || echo "MySQL may be running already"
```

- [ ] **Step 2: Tạo database**

```bash
"/d/xampp/mysql/bin/mysql" -u root -e "CREATE DATABASE IF NOT EXISTS sachiepvien CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"
echo "Database created"
```

- [ ] **Step 3: Download & install WordPress mới nhất**

```bash
cd /d/xampp/htdocs
# Download WordPress
curl -L -o wp.zip https://wordpress.org/latest.zip
unzip -q wp.zip
mv wordpress sachiepvien
rm wp.zip
```

Expected: WordPress extracted to `D:\xampp\htdocs\sachiepvien\`

- [ ] **Step 4: Cấu hình wp-config.php**

```bash
cd /d/xampp/htdocs/sachiepvien
cp wp-config-sample.php wp-config.php
# Generate salts + update config
python -c "
import secrets, string
salts = ''
for name in ['AUTH_KEY','SECURE_AUTH_KEY','LOGGED_IN_KEY','NONCE_KEY','AUTH_SALT','SECURE_AUTH_SALT','LOGGED_IN_SALT','NONCE_SALT']:
    salt = ''.join(secrets.choice(string.ascii_letters + string.digits + '!@#$%^&*()') for _ in range(64))
    salts += f\"define('{name}', '{salt}');\n\"
print(salts)
" > /tmp/salts.txt
```

- [ ] **Step 5: Chỉnh sửa wp-config.php với thông tin database**

Edit `wp-config.php`:
- DB_NAME: `sachiepvien`
- DB_USER: `root`
- DB_PASSWORD: `''` (empty)
- DB_HOST: `localhost`
- WP_HOME: `'http://localhost/sachiepvien'`
- WP_SITEURL: `'http://localhost/sachiepvien'`

- [ ] **Step 6: Cài WP-CLI**

```bash
cd /d/xampp/htdocs/sachiepvien
curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar
php wp-cli.phar --info
```

- [ ] **Step 7: Install WordPress qua CLI**

```bash
cd /d/xampp/htdocs/sachiepvien
php wp-cli.phar core install \
  --url="http://localhost/sachiepvien" \
  --title="Sắc Hiệp Viện" \
  --admin_user="admin" \
  --admin_password="admin123" \
  --admin_email="admin@example.com"
```

Expected output: "Success: WordPress installed successfully."

- [ ] **Step 8: Verify site hoạt động**

```bash
curl -s http://localhost/sachiepvien | grep -o '<title>[^<]*</title>'
```

Expected: `<title>Sắc Hiệp Viện</title>`

---

### Task 4: WordPress Import Script

**Files:**
- Create: `import/import-stories.php`
- Create: `import/import.sh`
- Modify: crawled_data được import vào WordPress

**Interfaces:**
- Consumes: `crawled_data/metadata.json`, file .txt trong `crawled_data/stories/`
- Produces: WordPress posts với metadata + attachment files

- [ ] **Step 1: Tạo thư mục import**

```bash
mkdir -p /d/claude-sachiepvien/import
```

- [ ] **Step 2: Viết import.sh — WP-CLI import script**

```bash
#!/bin/bash
# import/import.sh
# Import crawled stories into WordPress

WP_CLI="php /d/xampp/htdocs/sachiepvien/wp-cli.phar"
WP_PATH="/d/xampp/htdocs/sachiepvien"
METADATA_FILE="/d/claude-sachiepvien/crawled_data/metadata.json"
STORIES_DIR="/d/claude-sachiepvien/crawled_data/stories"
UPLOADS_DIR="${WP_PATH}/wp-content/uploads/stories"

# Ensure uploads directory
mkdir -p "$UPLOADS_DIR"

# Read metadata
echo "Reading metadata..."
cat "$METADATA_FILE" | python -c "
import json, sys
data = json.load(sys.stdin)
for item in data:
    print(json.dumps(item))
" > /tmp/stories_stream.jsonl

TOTAL=$(wc -l < /tmp/stories_stream.jsonl)
COUNT=0

while IFS= read -r line; do
    COUNT=$((COUNT + 1))
    echo "[${COUNT}/${TOTAL}] Importing..."
    
    # Parse JSON
    SLUG=$(echo "$line" | python -c "import json,sys; print(json.load(sys.stdin).get('slug',''))")
    TITLE=$(echo "$line" | python -c "import json,sys; print(json.load(sys.stdin).get('title',''))")
    DESC=$(echo "$line" | python -c "import json,sys; print(json.load(sys.stdin).get('description',''))")
    CATS=$(echo "$line" | python -c "import json,sys; print(','.join(json.load(sys.stdin).get('categories',[])))")
    TAGS=$(echo "$line" | python -c "import json,sys; print(','.join(json.load(sys.stdin).get('tags',[])))")
    TXT_FILE=$(echo "$line" | python -c "import json,sys; print(json.load(sys.stdin).get('txt_file','') or '')")
    TXT_SIZE=$(echo "$line" | python -c "import json,sys; print(json.load(sys.stdin).get('txt_size_bytes',0))")
    SOURCE_URL=$(echo "$line" | python -c "import json,sys; print(json.load(sys.stdin).get('url',''))")
    
    # Skip if no title
    if [ -z "$TITLE" ]; then
        echo "  Skipping (no title): $SLUG"
        continue
    fi
    
    # Copy txt file to WordPress uploads
    ATTACHMENT_ID=""
    if [ -n "$TXT_FILE" ] && [ -f "${STORIES_DIR}/${TXT_FILE}" ]; then
        cp "${STORIES_DIR}/${TXT_FILE}" "${UPLOADS_DIR}/${TXT_FILE}"
        
        # Import as attachment
        ATTACHMENT_ID=$($WP_CLI --path="$WP_PATH" media import "${UPLOADS_DIR}/${TXT_FILE}" --porcelain 2>/dev/null)
        echo "  Attachment ID: $ATTACHMENT_ID"
    fi
    
    # Create post with categories
    CAT_ARGS=""
    IFS=',' read -ra CAT_ARRAY <<< "$CATS"
    for CAT in "${CAT_ARRAY[@]}"; do
        # Create category if doesn't exist
        CAT_ID=$($WP_CLI --path="$WP_PATH" term create category "$CAT" --porcelain 2>/dev/null)
        CAT_ARGS="$CAT_ARGS --categories=\"$CAT\""
    done
    
    # Create post
    POST_ARGS=(
        --path="$WP_PATH"
        --post_type="post"
        --post_title="$TITLE"
        --post_content="$DESC"
        --post_status="publish"
        --post_name="$SLUG"
    )
    
    # Add categories and tags
    if [ -n "$CATS" ]; then
        POST_ARGS+=(--categories="$CATS")
    fi
    if [ -n "$TAGS" ]; then
        POST_ARGS+=(--tags="$TAGS")
    fi
    
    POST_ID=$($WP_CLI "${POST_ARGS[@]}" --porcelain 2>/dev/null)
    
    if [ -n "$POST_ID" ]; then
        echo "  Post created: ID=$POST_ID slug=$SLUG"
        
        # Set custom fields
        $WP_CLI --path="$WP_PATH" post meta update "$POST_ID" "_story_source_url" "$SOURCE_URL" 2>/dev/null
        $WP_CLI --path="$WP_PATH" post meta update "$POST_ID" "_story_txt_size" "$TXT_SIZE" 2>/dev/null
        
        if [ -n "$TXT_FILE" ]; then
            $WP_CLI --path="$WP_PATH" post meta update "$POST_ID" "_story_txt_file" "$TXT_FILE" 2>/dev/null
        fi
        
        if [ -n "$ATTACHMENT_ID" ]; then
            $WP_CLI --path="$WP_PATH" post meta update "$POST_ID" "_story_txt_attachment" "$ATTACHMENT_ID" 2>/dev/null
        fi
    else
        echo "  ERROR: Failed to create post for $SLUG"
    fi
    
done < /tmp/stories_stream.jsonl

echo ""
echo "✅ Import complete! Imported $COUNT stories."
```

- [ ] **Step 3: Chạy import script**

```bash
cd /d/claude-sachiepvien
bash import/import.sh
```

---

### Task 5: Custom WordPress Theme

**Files:**
- Create: `wp-content/themes/sachiepvien/style.css`
- Create: `wp-content/themes/sachiepvien/index.php`
- Create: `wp-content/themes/sachiepvien/functions.php`
- Create: `wp-content/themes/sachiepvien/header.php`
- Create: `wp-content/themes/sachiepvien/footer.php`
- Create: `wp-content/themes/sachiepvien/single.php`
- Create: `wp-content/themes/sachiepvien/archive.php`
- Create: `wp-content/themes/sachiepvien/search.php`
- Create: `wp-content/themes/sachiepvien/page.php`

**Interfaces:**
- Consumes: WordPress post data, custom fields (`_story_txt_file`, `_story_txt_size`, `_story_txt_attachment`)
- Produces: Front-end HTML

- [ ] **Step 1: Tạo theme directory**

```bash
mkdir -p /d/xampp/htdocs/sachiepvien/wp-content/themes/sachiepvien
```

- [ ] **Step 2: Viết style.css**

```css
/*
Theme Name: Sắc Hiệp Viện Reader
Theme URI: https://localhost/sachiepvien
Author: Custom
Description: Theme nhẹ cho đọc truyện, focus vào text và download
Version: 1.0
*/

:root {
  --primary: #ba3838;
  --primary-dark: #8a2a2a;
  --accent: #00a86b;
  --bg: #f5f5f5;
  --card-bg: #ffffff;
  --text: #333333;
  --text-light: #666666;
  --border: #e0e0e0;
  --radius: 8px;
}

* { box-sizing: border-box; margin: 0; padding: 0; }

body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  background: var(--bg);
  color: var(--text);
  line-height: 1.6;
}

a { color: var(--primary); text-decoration: none; }
a:hover { color: var(--primary-dark); }

/* Header */
.site-header {
  background: var(--primary);
  color: #fff;
  padding: 16px 0;
  position: sticky;
  top: 0;
  z-index: 100;
  box-shadow: 0 2px 8px rgba(0,0,0,0.15);
}

.header-inner {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 16px;
  display: flex;
  align-items: center;
  gap: 24px;
  flex-wrap: wrap;
}

.site-title { font-size: 24px; font-weight: 700; color: #fff; }
.site-title:hover { color: #ffd700; }

.header-nav { display: flex; gap: 16px; }
.header-nav a { color: #fff; font-size: 15px; padding: 4px 8px; border-radius: 4px; }
.header-nav a:hover { background: rgba(255,255,255,0.15); }

.search-form {
  display: flex;
  margin-left: auto;
  gap: 0;
}

.search-form input[type="text"] {
  padding: 8px 12px;
  border: none;
  border-radius: var(--radius) 0 0 var(--radius);
  width: 200px;
  font-size: 14px;
}

.search-form button {
  padding: 8px 16px;
  background: var(--accent);
  color: #fff;
  border: none;
  border-radius: 0 var(--radius) var(--radius) 0;
  cursor: pointer;
  font-size: 14px;
}

/* Container */
.container {
  max-width: 1200px;
  margin: 24px auto;
  padding: 0 16px;
}

/* Story Grid */
.story-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 16px;
}

.story-card {
  background: var(--card-bg);
  border-radius: var(--radius);
  padding: 20px;
  box-shadow: 0 1px 4px rgba(0,0,0,0.08);
  transition: box-shadow 0.2s;
  display: flex;
  flex-direction: column;
}

.story-card:hover { box-shadow: 0 4px 16px rgba(0,0,0,0.12); }

.story-card h2 {
  font-size: 17px;
  line-height: 1.4;
  margin-bottom: 8px;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.story-card h2 a { color: var(--text); }
.story-card h2 a:hover { color: var(--primary); }

.story-meta {
  font-size: 13px;
  color: var(--text-light);
  margin-bottom: 8px;
}

.story-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 4px;
  margin-bottom: 12px;
}

.story-tags .tag {
  background: #f0f0f0;
  padding: 2px 8px;
  border-radius: 4px;
  font-size: 12px;
  color: var(--text-light);
}

.story-excerpt {
  font-size: 14px;
  color: var(--text-light);
  margin-bottom: 12px;
  flex-grow: 1;
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.story-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-top: 12px;
  border-top: 1px solid var(--border);
  font-size: 13px;
  color: var(--text-light);
}

.download-btn {
  display: inline-block;
  padding: 8px 20px;
  background: var(--accent);
  color: #fff !important;
  border-radius: var(--radius);
  font-weight: 600;
  font-size: 14px;
  transition: background 0.2s;
}

.download-btn:hover { background: #008f5a; }

/* Single Post */
.single-story {
  background: var(--card-bg);
  border-radius: var(--radius);
  padding: 32px;
  max-width: 800px;
  margin: 0 auto;
}

.single-story h1 {
  font-size: 28px;
  line-height: 1.3;
  margin-bottom: 16px;
}

.single-meta { margin-bottom: 20px; }

.single-meta .label {
  font-size: 14px;
  color: var(--text-light);
  margin-right: 16px;
}

.single-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  margin-bottom: 24px;
}

.single-tags .tag {
  background: #f0f0f0;
  padding: 4px 12px;
  border-radius: 4px;
  font-size: 13px;
  color: var(--text-light);
}

.download-section {
  background: #f8fff8;
  border: 1px solid #c8e6c9;
  border-radius: var(--radius);
  padding: 20px;
  margin-bottom: 24px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 12px;
}

.download-info { font-size: 14px; color: var(--text-light); }
.download-info strong { color: var(--text); }

.download-btn-large {
  padding: 12px 32px;
  background: var(--accent);
  color: #fff !important;
  border-radius: var(--radius);
  font-weight: 700;
  font-size: 16px;
  transition: background 0.2s;
}

.download-btn-large:hover { background: #008f5a; }

.story-description {
  font-size: 15px;
  line-height: 1.8;
  color: var(--text);
}

/* Pagination */
.pagination {
  display: flex;
  justify-content: center;
  gap: 8px;
  margin: 32px 0;
}

.pagination a, .pagination span {
  padding: 8px 14px;
  background: var(--card-bg);
  border-radius: var(--radius);
  font-size: 14px;
  color: var(--text);
}

.pagination .current {
  background: var(--primary);
  color: #fff;
}

/* Footer */
.site-footer {
  background: #222;
  color: #999;
  padding: 24px 0;
  margin-top: 48px;
  text-align: center;
  font-size: 14px;
}

/* Category Filter */
.category-filter {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-bottom: 24px;
}

.category-filter a {
  padding: 6px 16px;
  background: var(--card-bg);
  border-radius: 20px;
  font-size: 14px;
  color: var(--text);
  border: 1px solid var(--border);
  transition: all 0.2s;
}

.category-filter a:hover, .category-filter a.active {
  background: var(--primary);
  color: #fff;
  border-color: var(--primary);
}

/* Responsive */
@media (max-width: 768px) {
  .header-inner { flex-direction: column; align-items: stretch; }
  .search-form { margin-left: 0; }
  .search-form input[type="text"] { width: 100%; }
  .story-grid { grid-template-columns: 1fr; }
  .single-story { padding: 16px; }
  .single-story h1 { font-size: 22px; }
  .download-section { flex-direction: column; text-align: center; }
}
```

- [ ] **Step 3: Viết header.php**

```php
<!DOCTYPE html>
<html <?php language_attributes(); ?>>
<head>
<meta charset="<?php bloginfo( 'charset' ); ?>">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<?php wp_head(); ?>
</head>
<body <?php body_class(); ?>>
<header class="site-header">
  <div class="header-inner">
    <a href="<?php echo home_url(); ?>" class="site-title"><?php bloginfo('name'); ?></a>
    <nav class="header-nav">
      <a href="<?php echo home_url(); ?>">Trang Chủ</a>
      <a href="<?php echo home_url('/category/de-cu/'); ?>">Đề Cử</a>
      <a href="<?php echo home_url('/category/dich-edit/'); ?>">Dịch/Edit</a>
      <a href="<?php echo home_url('/category/sang-tac/'); ?>">Sáng Tác</a>
    </nav>
    <form role="search" method="get" class="search-form" action="<?php echo home_url('/'); ?>">
      <input type="text" name="s" placeholder="Tìm truyện..." value="<?php echo get_search_query(); ?>">
      <button type="submit">🔍</button>
    </form>
  </div>
</header>
```

- [ ] **Step 4: Viết footer.php**

```php
<footer class="site-footer">
  <div class="container">
    <p>&copy; <?php echo date('Y'); ?> <?php bloginfo('name'); ?>. Crawled từ <a href="https://sachiepvien.net" target="_blank" rel="noopener">sachiepvien.net</a></p>
  </div>
</footer>
<?php wp_footer(); ?>
</body>
</html>
```

- [ ] **Step 5: Viết functions.php**

```php
<?php
// Theme setup
function sachiepvien_setup() {
    add_theme_support('title-tag');
    add_theme_support('post-thumbnails');
    register_nav_menu('primary', __('Primary Menu', 'sachiepvien'));
}
add_action('after_setup_theme', 'sachiepvien_setup');

// Enqueue styles
function sachiepvien_scripts() {
    wp_enqueue_style('sachiepvien-style', get_stylesheet_uri(), [], '1.0');
}
add_action('wp_enqueue_scripts', 'sachiepvien_scripts');

// Custom meta boxes for story data
function sachiepvien_display_txt_info($content) {
    if (is_singular('post')) {
        $txt_file = get_post_meta(get_the_ID(), '_story_txt_file', true);
        $txt_size = get_post_meta(get_the_ID(), '_story_txt_size', true);
        $txt_attachment = get_post_meta(get_the_ID(), '_story_txt_attachment', true);
        $source_url = get_post_meta(get_the_ID(), '_story_source_url', true);
        
        if ($txt_file) {
            $download_url = $txt_attachment 
                ? wp_get_attachment_url($txt_attachment) 
                : home_url('/wp-content/uploads/stories/' . $txt_file);
            
            $size_display = $txt_size ? size_format($txt_size) : 'Unknown';
            
            $download_html = '<div class="download-section">';
            $download_html .= '<div class="download-info">';
            $download_html .= '<strong>📄 File:</strong> ' . esc_html($txt_file) . '<br>';
            $download_html .= '<strong>📦 Dung lượng:</strong> ' . esc_html($size_display);
            $download_html .= '</div>';
            $download_html .= '<a href="' . esc_url($download_url) . '" class="download-btn-large" download>⬇️ Tải File</a>';
            $download_html .= '</div>';
            
            if ($source_url) {
                $download_html .= '<p style="font-size:13px;color:#999;">Nguồn: <a href="' . esc_url($source_url) . '" target="_blank" rel="noopener">sachiepvien.net</a></p>';
            }
            
            $content = $download_html . $content;
        }
    }
    return $content;
}
add_filter('the_content', 'sachiepvien_display_txt_info');

// Custom excerpt length
function sachiepvien_excerpt_length($length) {
    return 30;
}
add_filter('excerpt_length', 'sachiepvien_excerpt_length');
```

- [ ] **Step 6: Viết index.php**

```php
<?php get_header(); ?>
<div class="container">
  <?php if (is_home()): ?>
    <h1 style="font-size:22px;margin-bottom:16px;">📚 Truyện Mới Cập Nhật</h1>
  <?php endif; ?>
  
  <div class="story-grid">
    <?php if (have_posts()) : while (have_posts()) : the_post(); ?>
      <article class="story-card">
        <h2><a href="<?php the_permalink(); ?>"><?php the_title(); ?></a></h2>
        <div class="story-meta">
          📅 <?php echo get_the_date(); ?>
        </div>
        <?php
        $tags = get_the_tags();
        if ($tags): ?>
        <div class="story-tags">
          <?php foreach ($tags as $tag): ?>
            <span class="tag">#<?php echo esc_html($tag->name); ?></span>
          <?php endforeach; ?>
        </div>
        <?php endif; ?>
        <div class="story-excerpt"><?php echo get_the_excerpt(); ?></div>
        <div class="story-footer">
          <span>
            <?php
            $txt_size = get_post_meta(get_the_ID(), '_story_txt_size', true);
            echo $txt_size ? '📦 ' . size_format($txt_size) : '';
            ?>
          </span>
          <a href="<?php the_permalink(); ?>" class="download-btn">Xem & Tải</a>
        </div>
      </article>
    <?php endwhile; endif; ?>
  </div>
  
  <div class="pagination">
    <?php echo paginate_links(); ?>
  </div>
</div>
<?php get_footer(); ?>
```

- [ ] **Step 7: Viết single.php**

```php
<?php get_header(); ?>
<div class="container">
  <div class="single-story">
    <?php while (have_posts()) : the_post(); ?>
      <h1><?php the_title(); ?></h1>
      <div class="single-meta">
        <span class="label">📅 <?php echo get_the_date(); ?></span>
        <?php
        $categories = get_the_category();
        if ($categories): ?>
          <span class="label">📂 
            <?php foreach ($categories as $cat): ?>
              <a href="<?php echo get_category_link($cat->term_id); ?>"><?php echo esc_html($cat->name); ?></a>
            <?php endforeach; ?>
          </span>
        <?php endif; ?>
      </div>
      
      <?php
      $tags = get_the_tags();
      if ($tags): ?>
      <div class="single-tags">
        <?php foreach ($tags as $tag): ?>
          <span class="tag">#<?php echo esc_html($tag->name); ?></span>
        <?php endforeach; ?>
      </div>
      <?php endif; ?>
      
      <div class="story-description">
        <?php the_content(); ?>
      </div>
    <?php endwhile; ?>
  </div>
</div>
<?php get_footer(); ?>
```

- [ ] **Step 8: Viết archive.php**

```php
<?php get_header(); ?>
<div class="container">
  <h1 style="font-size:22px;margin-bottom:8px;">
    📂 <?php single_cat_title(); ?>
  </h1>
  <p style="color:#666;margin-bottom:24px;">
    <?php echo category_description(); ?>
  </p>
  
  <div class="story-grid">
    <?php if (have_posts()) : while (have_posts()) : the_post(); ?>
      <article class="story-card">
        <h2><a href="<?php the_permalink(); ?>"><?php the_title(); ?></a></h2>
        <div class="story-meta">
          📅 <?php echo get_the_date(); ?>
        </div>
        <?php
        $tags = get_the_tags();
        if ($tags): ?>
        <div class="story-tags">
          <?php foreach ($tags as $tag): ?>
            <span class="tag">#<?php echo esc_html($tag->name); ?></span>
          <?php endforeach; ?>
        </div>
        <?php endif; ?>
        <div class="story-excerpt"><?php echo get_the_excerpt(); ?></div>
        <div class="story-footer">
          <span>
            <?php
            $txt_size = get_post_meta(get_the_ID(), '_story_txt_size', true);
            echo $txt_size ? '📦 ' . size_format($txt_size) : '';
            ?>
          </span>
          <a href="<?php the_permalink(); ?>" class="download-btn">Xem & Tải</a>
        </div>
      </article>
    <?php endwhile; endif; ?>
  </div>
  
  <div class="pagination">
    <?php echo paginate_links(); ?>
  </div>
</div>
<?php get_footer(); ?>
```

- [ ] **Step 9: Viết search.php**

```php
<?php get_header(); ?>
<div class="container">
  <h1 style="font-size:22px;margin-bottom:16px;">
    🔍 Kết quả tìm kiếm: "<?php echo get_search_query(); ?>"
  </h1>
  
  <div class="story-grid">
    <?php if (have_posts()) : while (have_posts()) : the_post(); ?>
      <article class="story-card">
        <h2><a href="<?php the_permalink(); ?>"><?php the_title(); ?></a></h2>
        <div class="story-meta">
          📅 <?php echo get_the_date(); ?>
        </div>
        <?php
        $tags = get_the_tags();
        if ($tags): ?>
        <div class="story-tags">
          <?php foreach ($tags as $tag): ?>
            <span class="tag">#<?php echo esc_html($tag->name); ?></span>
          <?php endforeach; ?>
        </div>
        <?php endif; ?>
        <div class="story-excerpt"><?php echo get_the_excerpt(); ?></div>
        <div class="story-footer">
          <span>
            <?php
            $txt_size = get_post_meta(get_the_ID(), '_story_txt_size', true);
            echo $txt_size ? '📦 ' . size_format($txt_size) : '';
            ?>
          </span>
          <a href="<?php the_permalink(); ?>" class="download-btn">Xem & Tải</a>
        </div>
      </article>
    <?php endwhile; else: ?>
      <p style="grid-column:1/-1;text-align:center;padding:48px;color:#999;">
        Không tìm thấy truyện nào phù hợp.
      </p>
    <?php endif; ?>
  </div>
  
  <div class="pagination">
    <?php echo paginate_links(); ?>
  </div>
</div>
<?php get_footer(); ?>
```

- [ ] **Step 10: Viết page.php**

```php
<?php get_header(); ?>
<div class="container">
  <div class="single-story">
    <?php while (have_posts()) : the_post(); ?>
      <h1><?php the_title(); ?></h1>
      <div class="story-description">
        <?php the_content(); ?>
      </div>
    <?php endwhile; ?>
  </div>
</div>
<?php get_footer(); ?>
```

- [ ] **Step 11: Kích hoạt theme**

```bash
cd /d/xampp/htdocs/sachiepvien
php wp-cli.phar theme activate sachiepvien
```

Expected: "Success: Switched to 'Sắc Hiệp Viện Reader' theme."

- [ ] **Step 12: Tạo menu và home page**

```bash
cd /d/xampp/htdocs/sachiepvien
# Set home page to show latest posts
php wp-cli.phar option update show_on_front 'posts'
php wp-cli.phar option update posts_per_page 24
```

---

### Task 6: Verify & Test

**Files:**
- None (testing)

- [ ] **Step 1: Test home page**

```bash
curl -s http://localhost/sachiepvien | grep -c 'story-card'
```

Expected: > 0 (shows story cards)

- [ ] **Step 2: Test single story page**

```bash
STORY_SLUG=$(python -c "
import json
data = json.load(open('crawled_data/metadata.json'))
for item in data:
    if item.get('slug'):
        print(item['slug'])
        break
")
curl -s "http://localhost/sachiepvien/$STORY_SLUG/" | grep -c 'download-btn-large'
```

Expected: 1 (download button appears)

- [ ] **Step 3: Test download link works**

```bash
STORY_SLUG=$(python -c "
import json
data = json.load(open('crawled_data/metadata.json'))
for item in data:
    if item.get('slug'):
        print(item['slug'])
        break
")
curl -s "http://localhost/sachiepvien/$STORY_SLUG/" | grep -oP 'href="[^"]*\.txt"' | head -1
```

Expected: Shows link to .txt file

- [ ] **Step 4: Test search**

```bash
curl -s "http://localhost/sachiepvien/?s=truyen" | grep -c 'story-card'
```

Expected: > 0

- [ ] **Step 5: Test category archive**

```bash
curl -s "http://localhost/sachiepvien/category/de-cu/" | grep -c 'story-card'
```

Expected: > 0

- [ ] **Step 6: Test mobile responsive**

```bash
curl -s -A "Mozilla/5.0 (Linux; Android 12)" http://localhost/sachiepvien/ | grep -c 'story-card'
```

Expected: > 0

---

## Tổng quan task dependencies

```
Task 1 (Collect links)
    │
    ▼
Task 2 (Download stories) ← cần links từ Task 1
    │
    ▼
Task 3 (WordPress local) ← độc lập, chạy song song với Task 1-2
    │
    ▼
Task 4 (Import script) ← cần data từ Task 2 + WordPress từ Task 3
    │
    ▼
Task 5 (Custom theme) ← cần WordPress từ Task 3
    │
    ▼
Task 6 (Verify) ← cần tất cả các task trên
```
