/**
 * popup.js — cửa sổ bật lên của extension.
 *
 * Bật/tắt cờ `enabled` trong chrome.storage.local.
 * content.js đọc cờ này khi trang truyện load xong.
 */

'use strict';

const DEFAULTS = { enabled: true };
const checkbox = document.getElementById('enabled');
const statusEl = document.getElementById('status');

async function init() {
  const { enabled = DEFAULTS.enabled } = await chrome.storage.local.get(DEFAULTS);
  checkbox.checked = enabled;
  statusEl.textContent = '';
}

checkbox.addEventListener('change', async () => {
  const enabled = checkbox.checked;
  await chrome.storage.local.set({ enabled });
  statusEl.textContent = enabled ? 'Đã bật tự động resolve.' : 'Đã tắt.';
  setTimeout(() => (statusEl.textContent = ''), 2000);
});

init();