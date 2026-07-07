---
id: init-project
version: 1.0.0
confidence: 0.80
success_rate: 0.75
last_updated: 2026-06-29
tags: [process, init, project-setup, junction, flexible]
---

# Init Project

> Flexible skill. Tự động tạo folder dự án mới + junction link `.ai/` đến framework gốc, không cần copy files.

## Overview
Tạo một dự án mới kết nối đến framework self-improving mà không tốn dung lượng. Dùng junction link để nhiều project dùng chung 1 bộ `.ai/`.

## Step-by-Step Process

### Phase 1: Parse Path
1. User nói: "khởi tạo trên D:\path" hoặc "init D:\path"
2. Trích xuất đường dẫn từ câu nói
3. Normalize path (Windows: backslashes, absolute path)

### Phase 2: Create Folder
```powershell
if (-not (Test-Path "$PROJECT_PATH")) {
    New-Item -ItemType Directory -Path "$PROJECT_PATH" -Force
}
```

### Phase 3: Create Junction
```powershell
cmd /c mklink /J "$PROJECT_PATH\.ai" "D:\claude-aerolink\.ai"
```

### Phase 4: Report
```
✅ Đã khởi tạo tại: <path>
📁 .ai/ → 🔗 junction: D:\claude-aerolink\.ai\ (139 files)
```

## Common Mistakes
- **Quên Admin quyền**: Junction cần Admin hoặc Developer Mode. Nếu lỗi → báo user bật Developer Mode.
- **Đã có .ai/ rồi**: Kiểm tra trước. Nếu có → hỏi user trước khi ghi đè.
- **Nhầm source/target**: Source = project mới, target = D:\claude-aerolink\.ai

## Quality Gates
- [ ] Folder đã được tạo
- [ ] Junction đã được tạo (check ReparsePoint attribute)
- [ ] File count qua junction = file count ở gốc
- [ ] Không có lỗi permission
