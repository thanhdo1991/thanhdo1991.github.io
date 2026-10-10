# crawler/crawl_one.py
# Crawl a single story from sachiepvien.net by URL and save its .txt file.
# Usage: python crawl_one.py <story_url> [slug]
# Prints the absolute path of the saved .txt file on success, or "ERROR: ..." on failure.

import sys
import os
import re
import base64
import requests
from bs4 import BeautifulSoup

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STORIES_DIR = os.path.join(BASE, "crawled_data", "stories")
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
SKIP_REDIRECT_DOMAINS = [
    "shrinkme.io", "shrink", "shortlink", "short-link",
    "redirect.html", "sachiepvien.net/redirect",
    "sachiepvien.net/wp-login",
]


def decode_redirect_url(url):
    if "redirect.html" in url and "url=" in url:
        encoded = url.split("url=")[1].split("&")[0]
        try:
            missing_padding = 4 - len(encoded) % 4
            if missing_padding != 4:
                encoded += "=" * missing_padding
            return base64.b64decode(encoded).decode("utf-8")
        except Exception:
            return url
    return url


def find_download_links(soup):
    links = []
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if href.endswith(".txt"):
            links.append(href)
        elif "redirect.html" in href and "url=" in href:
            links.append(href)
            decoded = decode_redirect_url(href)
            if decoded != href:
                links.append(decoded)
        elif "drive.google.com" in href or "docs.google.com" in href:
            links.append(href)
        elif "link.sachiepvien.net" in href:
            links.append(href)
        elif "download" in href.lower():
            links.append(href)
    for iframe in soup.find_all("iframe", src=True):
        if "drive.google.com" in iframe["src"]:
            links.append(iframe["src"])
    return list(dict.fromkeys(links))


def page_text_fallback(soup):
    accordion = soup.find("div", class_="wpsm-accordion")
    if accordion:
        content = accordion.find("div", class_="accordion-content")
        if content:
            paras = [p.get_text() for p in content.find_all("p") if p.get_text(strip=True)]
            if paras:
                return "\n\n".join(paras)
    article = soup.find("article") or soup.find("div", class_="post-content") or soup.find("div", class_="entry-content")
    if article:
        paras = [p.get_text() for p in article.find_all("p") if len(p.get_text(strip=True)) > 20]
        if paras:
            return "\n\n".join(paras)
    return ""


def download_mega(mega_url, path):
    """Download a mega.nz file using megatools (like dl_one.py)."""
    import subprocess
    megatools = r"C:\ProgramData\chocolatey\bin\megatools.exe"
    if not os.path.exists(megatools):
        megatools = "megatools"
    out_dir = os.path.dirname(path)
    try:
        result = subprocess.run(
            [megatools, "dl", "--no-progress", "--path", out_dir, mega_url],
            capture_output=True, timeout=300
        )
        # Find the downloaded file (mega keeps its own name)
        out_name = os.path.basename(path)
        for f in os.listdir(out_dir):
            fp = os.path.join(out_dir, f)
            if os.path.isfile(fp) and os.path.basename(fp) != out_name and os.path.getsize(fp) > 50000:
                if os.path.exists(path):
                    os.remove(path)
                os.rename(fp, path)
                return True
        if os.path.exists(path) and os.path.getsize(path) > 50000:
            return True
        return False
    except Exception:
        return False


def download(url, path):
    if os.path.exists(path) and os.path.getsize(path) > 0:
        return True
    try:
        resp = requests.get(url, headers=HEADERS, timeout=90, allow_redirects=True)
        resp.raise_for_status()
        if "text/html" in resp.headers.get("content-type", ""):
            return False
        with open(path, "wb") as f:
            f.write(resp.content)
        return os.path.getsize(path) > 0
    except Exception:
        return False


def main():
    if len(sys.argv) < 2:
        print("ERROR: missing story url")
        sys.exit(1)
    url = sys.argv[1].strip().rstrip("/")
    slug = sys.argv[2] if len(sys.argv) > 2 and not sys.argv[2].startswith("--") else url.split("/")[-1]
    use_local = "--local" in sys.argv

    os.makedirs(STORIES_DIR, exist_ok=True)
    out_path = os.path.join(STORIES_DIR, slug + ".txt")

    try:
        resp = requests.get(url, headers=HEADERS, timeout=30)
        resp.raise_for_status()
    except Exception as e:
        print("ERROR: fetch page failed: " + str(e))
        sys.exit(1)

    soup = BeautifulSoup(resp.text, "html.parser")
    links = find_download_links(soup)

    # 0) Optional: prefer already-crawled _full.txt only if --local flag is given
    if use_local:
        full_local = os.path.join(STORIES_DIR, slug + "_full.txt")
        if os.path.exists(full_local) and os.path.getsize(full_local) > 0:
            import shutil
            shutil.copyfile(full_local, out_path)
            print(os.path.abspath(out_path))
            # still report mega url if discoverable from page
            for l in links:
                if "link.sachiepvien.net" in l:
                    try:
                        r = requests.get(l, headers=HEADERS, timeout=15, allow_redirects=False)
                        if r.status_code in (301, 302, 303, 307, 308):
                            dest = r.headers.get("Location", "")
                            if "mega.nz" in dest or "mega.co.nz" in dest:
                                print("MEGA: " + dest)
                                break
                    except Exception:
                        pass
            sys.exit(0)

    # 1) Mega link -> use megatools (dl_one.py style)
    mega_found = ""
    mega_links = [l for l in links if "mega.nz" in l or "mega.co.nz" in l]
    for mega in mega_links:
        mega_found = mega
        if download_mega(mega, out_path):
            print(os.path.abspath(out_path))
            if mega_found:
                print("MEGA: " + mega_found)
            sys.exit(0)

    # 1b) shortlink (link.sachiepvien.net) -> follow redirect to find Mega
    for l in links:
        if "link.sachiepvien.net" in l:
            try:
                r = requests.get(l, headers=HEADERS, timeout=30, allow_redirects=False)
                if r.status_code in (301, 302, 303, 307, 308):
                    dest = r.headers.get("Location", "")
                    if "mega.nz" in dest or "mega.co.nz" in dest:
                        mega_found = dest
                        if download_mega(dest, out_path):
                            print(os.path.abspath(out_path))
                            if mega_found:
                                print("MEGA: " + mega_found)
                            sys.exit(0)
            except Exception:
                pass

    # 2) Direct/txt/shortlink download
    for dl in links:
        if any(s in dl for s in SKIP_REDIRECT_DOMAINS):
            continue
        if "mega.nz" in dl or "mega.co.nz" in dl:
            continue
        if download(dl, out_path):
            print(os.path.abspath(out_path))
            sys.exit(0)

    # 3) Fallback: page text
    text = page_text_fallback(soup)
    if text:
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(text)
        print(os.path.abspath(out_path))
        sys.exit(0)

    print("ERROR: no downloadable content found")
    sys.exit(1)


if __name__ == "__main__":
    main()