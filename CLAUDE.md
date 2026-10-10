# claude-sachiepvien

## Dự án

Săn truyện từ `sachiepvien.net` về 2 hướng:
1. **Chrome extension** (MV3) — tự resolve shortlink tải truyện → mở thẳng mega.nz trong **tab mới**.
2. **Bộ Python crawler** (CLI) — tải truyện + import vào Drupal local (XAMPP).

## Cấu trúc

```
chrome-extension/
  manifest.json     MV3: storage + host(sachiepvien.net) + content script
  background.js     Phân loại link tải (classify) + mở tab mới (chrome.tabs.create)
  content.js        Tìm nút "Tải File Truyện Về Máy Ở Đây" trên trang detail
  content.css       Banner nổi (blocked/error/done)
  popup.html/js     Bật/tắt tự động (chrome.storage.local key "enabled")
crawler/            CLI Python: collect_links, crawl_one, dl_one, download_mega,
                    download_full, batch_download, mega_direct, mega_downloader,
                    download_stories
import/             Python import truyện vào Drupal (import.py, import_story.py, import.sh)
crawl_one.bat       Windows wrapper cho crawler/crawl_one.py
crawled_data/
  stories/          Các file .txt truyện đã tải (24 file — GIỮ LẠI)
  metadata.json     Dữ liệu metadata truyện (giữ)
  download_full_log.json
```

## Luồng hoạt động extension (đã kiểm chứng thực tế)

```
Trang truyện (sachiepvien.net/...)
  └─ <a href="sachiepvien.net/redirect.html?url=<base64>">  (nút "Tải File Truyện Về Máy Ở Đây")
       └─ base64 → link.sachiepvien.net/<id>
            └─ Mở tab mới → Chrome theo redirect 307 → mega.nz/file/<id>#<key>
```

**Quan trọng:** KHÔNG resolve bằng `fetch()`. Chrome `fetch(redirect:'follow')`
bỏ mất fragment `#key` (key chỉ nằm trong HTTP `Location` header của redirect
307), khiến mega báo "Decryption key". Giải pháp đúng: mở tab để browser tự
theo redirect và giữ nguyên `#key`.

## Cài đặt / dùng

**Extension:** `chrome://extensions` → bật *Developer mode* → *Load unpacked* →
chọn `chrome-extension/`. Mở trang truyện → tự mở mega.nz ở tab mới
(trừ khi tắt trong popup).

**Crawler CLI:** `python crawler/crawl_one.py <story_url> [slug] [--local]`
hoặc `crawl_one.bat`. `python crawler/collect_links.py` để lấy danh sách.
`python crawler/download_full.py [--resume|--test]` để tải batch từ metadata.json.

## Lịch sử gần đây

- 2026-10-10 xây extension; sửa lỗi "mất key" bằng cách mở tab thay vì fetch.
- 2026-10-10 xóa `docs/`, `.superpowers/`, `crawled_data/stories.zip`, `.venv/`
  (dọn dự án), sau đó khôi phục bộ crawler/import theo yêu cầu.