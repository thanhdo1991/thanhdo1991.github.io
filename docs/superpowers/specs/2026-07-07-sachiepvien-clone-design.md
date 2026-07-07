# Sắc Hiệp Viện — Clone Design Spec

**Ngày:** 2026-07-07
**Dự án:** claude-sachiepvien
**Mục tiêu:** Crawl category "Đề Cử" từ sachiepvien.net, import vào WordPress site trên Pantheon, frontend sạch dễ đọc.

---

## 1. Kiến trúc tổng thể

```
┌─────────────────────────┐
│   Crawler (Python)       │
│   requests + bs4         │
│   → .txt + metadata.json │
└──────────┬──────────────┘
           │ crawled data
           ▼
┌─────────────────────────┐
│   Import script          │
│   WP-CLI wp post create  │
│   + import attachment    │
└──────────┬──────────────┘
           │ WordPress posts
           ▼
┌─────────────────────────┐
│   Custom Theme           │
│   Underscores-based      │
│   lightweight, text      │
│   -first                  │
└─────────────────────────┘
           │
           ▼
      Hosting: Pantheon (sau) / Local (trước)
```

## 2. Crawl Pipeline

### Nguồn
- Category: `sachiepvien.net/category/de-cu/`
- Pages: 28 trang, mỗi trang ~30-40 truyện
- Dữ liệu mỗi truyện: title, tác giả, tags, mô tả, category, download link (.txt)

### Output Format — metadata.json

```json
[
  {
    "slug": "phan-dien-mau-than-cua-ta-la-dai-de",
    "title": "Phản diện: Mẫu thân của ta là đại đế",
    "author": "",
    "categories": ["Đề cử"],
    "tags": ["xuyên không", "hệ thống", "loạn luân", "hậu cung"],
    "description": "1-147 chương kết thúc + đồng nhân phiên ngoại...",
    "txt_file": "crawled_data/stories/phan-dien-mau-than-cua-ta-la-dai-de.txt",
    "txt_size_bytes": 14000000,
    "source_url": "https://sachiepvien.net/phan-dien-mau-than-cua-ta-la-dai-de/"
  }
]
```

### Thư mục output
```
crawled_data/
├── metadata.json
├── stories/
│   ├── story-1.txt
│   └── story-2.txt
└── crawl_log.json
```

## 3. WordPress Import

### Custom Post Type
- Sử dụng `post` type mặc định (tận dụng category/tag có sẵn)
- Hoặc tạo CPT `story` nếu cần tách biệt

### Import workflow
1. WordPress site sạch (Local → Pantheon)
2. Đăng ký categories, tags trong metadata
3. `wp post create` — title, content (description), categories, tags
4. `wp post meta update <id> txt_file <path>` — lưu đường dẫn file
5. File .txt upload lên thư mục `/wp-content/uploads/stories/`

### Custom Fields
- `_story_txt_path`: đường dẫn file .txt
- `_story_author`: tác giả
- `_story_txt_size`: dung lượng

## 4. Theme Front-end

### Yêu cầu
- Text-first, load nhanh, responsive
- Không cần hình ảnh cover
- Ai cũng download được (không auth)
- Category/tag filters

### Pages/Views
| View | Mô tả |
|------|-------|
| Home | Grid truyện mới nhất, search bar, category filter |
| Category archive | Grid truyện theo category |
| Single story | Title, tác giả, tags, description, download button |
| Search | Kết quả tìm kiếm full-text |

### Layout — Home
```
[Header: logo + nav + search]
[Story Grid: 3-4 cột]
  ┌─────────┬─────────┬─────────┐
  │Title    │Title    │Title    │
  │Tác giả  │Tác giả  │Tác giả  │
  │[tags]   │[tags]   │[tags]   │
  │DL: 1.2MB│DL: 3.4MB│DL: 0.8MB│
  └─────────┴─────────┴─────────┘
[Pagination]
[Footer: đơn giản]
```

### Layout — Single Story
```
[Header]
[Title - H1]
[Tác giả] [Category] [Tags]
[Download button — nổi bật]
[Mô tả truyện]
[File info: .txt, 3.4MB, 147 chương]
[Related stories]
[Footer]
```

### Tech
- Theme từ Underscores (`_s`) hoặc Block theme
- CSS: custom minimal, không dùng page builder
- JS: tối thiểu (chỉ cho search, filter)
- Responsive breakpoints: mobile-first

## 5. Hosting

### Local (trước)
- XAMPP / Laragon / Local WP
- WordPress + theme + imported data

### Production (sau)
- Pantheon Basic Plan
- Git-based deploy
- CDN có sẵn (Pantheon + Fastly)

## 6. Non-goals

- ❌ Trang chủ phức tạp như bản gốc
- ❌ User registration / Login
- ❌ Bình luận
- ❌ Wishlist / Favorites
- ❌ Ranking / leaderboard
- ❌ Admin crawl từ Pantheon web UI

## 7. Tech Stack

| Component | Công nghệ |
|-----------|-----------|
| Crawler | Python 3 + requests + beautifulsoup4 |
| CMS | WordPress 6.x |
| Theme | Custom Underscores |
| Local dev | XAMPP |
| Production | Pantheon |
| Import | WP-CLI + custom PHP script |

## 8. Crawl Ethics

- Respect `robots.txt`
- Rate limiting: 1 request/giây
- Chỉ crawl category Đề Cử (public)
- Không vượt quá 1 request/giây
- Lưu crawl_log.json để resume nếu bị gián đoạn
