/**
 * content.js — chạy trên mọi trang sachiepvien.net.
 *
 * Với trang detail của truyện, tìm đúng nút tải chính:
 *   <a href="https://sachiepvien.net/redirect.html?url=<base64>">
 * base64 đó decode ra shortlink (link.sachiepvien.net/<id>), rồi
 * background mở thẳng bằng cách điều hướng tab — để CHROME tự xử lý
 * chuỗi 307 và GIỮ fragment (#key) của link mega.nz.
 * (fetch làm mất #key -> mega báo "Decryption key"; đã kiểm chứng.)
 */

'use strict';

const DEFAULTS = { enabled: true };

/** Trang này có phải trang detail truyện không? */
function isStoryPage() {
  return location.hostname === 'sachiepvien.net' || location.hostname.endsWith('.sachiepvien.net');
}

/** Tìm nút tải chính. Chỉ nhận redirect.html?url= hoặc shortlink trực tiếp. */
function findPrimaryDownload() {
  const anchors = Array.from(document.querySelectorAll('a[href]'));

  // Ưu tiên nút có chữ "tải ... về máy" như trên trang.
  const byText = anchors.filter((a) =>
    /tải\s+file|tải\s+truyện|về\s+máy/i.test(a.textContent || '')
  );
  const byHref = anchors.filter((a) => {
    const h = a.getAttribute('href') || '';
    return h.includes('redirect.html?url=') || h.includes('link.sachiepvien.net');
  });

  const ordered = [...byText, ...byHref];
  for (const a of ordered) {
    const h = a.getAttribute('href');
    if (h) return { anchor: a, href: h };
  }
  return null;
}

/* ------------------------------------------------------------------ */
/* Banner UI                                                           */
/* ------------------------------------------------------------------ */

const BANNER_ID = 'siepv-mega-banner';

function getBanner() {
  let el = document.getElementById(BANNER_ID);
  if (!el) {
    el = document.createElement('div');
    el.id = BANNER_ID;
    el.setAttribute('role', 'status');
    document.documentElement.appendChild(el);
  }
  return el;
}

function removeBanner() {
  document.getElementById(BANNER_ID)?.remove();
}

/** render(state, payload) — state: blocked | error | done */
function render(state, payload = {}) {
  const el = getBanner();
  el.dataset.state = state;
  el.replaceChildren();

  const icon = document.createElement('span');
  icon.className = 'siepv-icon';
  icon.textContent = state === 'done' ? '✅' : state === 'error' ? '⚠️' : '🔒';

  const text = document.createElement('span');
  text.className = 'siepv-text';

  const actions = document.createElement('span');
  actions.className = 'siepv-actions';
  actions.append(closeButton());

  if (state === 'blocked') {
    text.textContent = 'Tự động tìm link mega đang TẮT — bấm để mở ở tab mới.';
    const go = document.createElement('button');
    go.type = 'button';
    go.className = 'siepv-primary';
    go.textContent = 'Mở mega.nz (tab mới)';
    go.addEventListener('click', () => navigate());
    actions.prepend(go);
  } else if (state === 'error') {
    text.textContent = payload.reason || 'Không tìm thấy nút tải truyện.';
    const retry = document.createElement('button');
    retry.type = 'button';
    retry.textContent = 'Thử lại';
    retry.addEventListener('click', () => navigate());
    actions.prepend(retry);
  } else if (state === 'done') {
    text.textContent = 'Đã chuyển sang mega.nz.';
  }

  el.append(icon, text, actions);

  // Tự ẩn sau 4s trừ state 'blocked' (cần người dùng quyết định).
  if (state !== 'blocked') {
    setTimeout(() => {
      if (document.getElementById(BANNER_ID)?.dataset.state === state) removeBanner();
    }, 4000);
  }
}

function closeButton() {
  const close = document.createElement('button');
  close.type = 'button';
  close.className = 'siepv-close';
  close.textContent = '✕';
  close.title = 'Đóng';
  close.addEventListener('click', removeBanner);
  return close;
}

/* ------------------------------------------------------------------ */
/* Luồng chính                                                         */
/* ------------------------------------------------------------------ */

let running = false;

async function navigate() {
  if (running) return;
  running = true;
  try {
    const found = findPrimaryDownload();
    if (!found) {
      render('error', { reason: 'Không tìm thấy nút tải truyện trên trang này.' });
      return;
    }

    const res = await chrome.runtime.sendMessage({
      type: 'CLASSIFY_LINK',
      url: found.href,
    });

    if (!res || !res.ok) {
      render('error', { reason: 'Lỗi liên lạc với background.' });
      return;
    }

    if (res.type === 'none') {
      render('error', { reason: 'Trang này không có link tải hợp lệ.' });
      return;
    }

    // Mở target bằng cách điều hướng tab: browser giữ nguyên #key.
    await chrome.runtime.sendMessage({ type: 'NAVIGATE_TO', url: res.url });
    render('done');
  } catch (err) {
    render('error', { reason: 'Lỗi: ' + (err?.message || String(err)) });
  } finally {
    running = false;
  }
}

if (isStoryPage()) {
  const start = async () => {
    const { enabled = DEFAULTS.enabled } = await chrome.storage.local.get(DEFAULTS);
    const found = findPrimaryDownload();
    if (!found) return; // trang không có nút tải -> không làm gì
    if (!enabled) {
      render('blocked');
      return;
    }
    navigate();
  };

  // Cho DOM ổn định rồi mới chạy (một số theme chèn nút tải muộn).
  if (document.readyState === 'complete') {
    start();
  } else {
    window.addEventListener('load', () => start(), { once: true });
  }
}