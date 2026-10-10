/**
 * background.js — service worker.
 *
 * Nhiệm vụ: nhận một href tải từ trang detail (content.js), phân loại
 * (mega trực tiếp hoặc shortlink link.sachiepvien.net), rồi mở link đó
 * trong TAB MỚI (chrome.tabs.create) — giữ nguyên tab trang truyện.
 *
 * Tại sao giải quyết bằng cách mở tab, không dùng fetch để "resolve":
 *   - fetch(redirect:'follow') của Chrome trả về resp.url bị BỎ fragment
 *     (#key). Nhiều shortlink của sachiepvien.net redirect bằng 307 và
 *     chỉ đem key nằm trong HTTP Location header:
 *       307  Location: https://mega.nz/file/o2wwhQLT#M5ZLEgzjfRNKqU6ITCRplJb...
 *     nếu resolve bằng fetch ta chỉ nhận được mega.nz/file/o2wwhQLT — mất
 *     key -> mega báo "Decryption key".
 *   - fetch(redirect:'manual') trả về response "opaque" (status 0), headers
 *     rỗng -> không đọc được Location dù muốn.
 *   - Điều hướng trình duyệt (chrome.tabs.create / location.assign) thì
 *     browser tự xử lý chuỗi 307 và GIỮ NGUYÊN fragment. Đã kiểm chứng
 *     trực tiếp: Chrome nhảy theo redirect -> mega.nz/file/o2wwhQLT#M5ZL...
 *     đủ key, không báo "Decryption key".
 */

'use strict';

/** Link mega.nz có đúng dạng tải file (có khoá sau dấu #) không. */
function isMegaFileUrl(url) {
  return /^https?:\/\/(?:www\.)?mega\.(?:nz|co\.nz)\/file\/[^#\s]+#[\w-]+/i.test(url || '');
}

/**
 * Xác định hành động cho một href tải:
 *  - {type:'mega', url}     : có sẵn mega.nz/file#key — mở thẳng.
 *  - {type:'shortlink', url}: shortlink — mở qua tab để browser giữ #key
 *                             (fetch làm mất key, không dùng).
 *  - null                   : không phải link tải.
 */
function classify(url) {
  if (!url) return null;
  let abs;
  try {
    abs = new URL(url, 'https://sachiepvien.net/');
  } catch {
    return null;
  }
  if (abs.hostname.endsWith('mega.nz') || abs.hostname.endsWith('mega.co.nz')) {
    return { type: 'mega', url: abs.href };
  }
  if (abs.pathname.includes('redirect.html') && abs.searchParams.has('url')) {
    const encoded = abs.searchParams.get('url');
    try {
      const s = encoded.replace(/-/g, '+').replace(/_/g, '/');
      const pad = s.length % 4 ? '='.repeat(4 - (s.length % 4)) : '';
      const bin = atob(s + pad);
      let decoded;
      try {
        decoded = decodeURIComponent(
          Array.prototype.map.call(bin, (c) => '%' + c.charCodeAt(0).toString(16).padStart(2, '0')).join('')
        );
      } catch {
        decoded = bin;
      }
      return classify(decoded); // có thể ra shortlink hoặc mega
    } catch {
      return null;
    }
  }
  if (abs.hostname === 'link.sachiepvien.net') {
    return { type: 'shortlink', url: abs.href };
  }
  return null;
}

/** Mở một URL trong TAB MỚI — giữ nguyên tab trang truyện đang xem. */
async function openInNewTab(url) {
  await chrome.tabs.create({ url });
  return true;
}

chrome.runtime.onMessage.addListener((msg, _sender, sendResponse) => {
  if (msg && msg.type === 'CLASSIFY_LINK') {
    const result = classify(msg.url);
    sendResponse({ ok: true, ...(result || { type: 'none' }) });
    return false;
  }
  if (msg && msg.type === 'NAVIGATE_TO') {
    openInNewTab(msg.url).then(() => sendResponse({ ok: true }));
    return true; // giữ kênh mở cho response bất đồng bộ
  }
  return false;
});
