"""
Pure Python MEGA.nz downloader - sử dụng MEGA REST API + AES decryption.
Không cần browser, không cần megatools. Chạy trực tiếp với requests + pycryptodome.

Tài liệu tham khảo: https://github.com/meganz/sdk (MEGA API protocol)
"""

import base64
import json
import os
import re
import struct
import sys
import time
from pathlib import Path
from urllib.parse import urlparse, parse_qs

import requests

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

try:
    from Crypto.Cipher import AES
except ImportError:
    AES = None

STORIES_DIR = Path(__file__).resolve().parent.parent / "crawled_data" / "stories"
METADATA_FILE = Path(__file__).resolve().parent.parent / "crawled_data" / "metadata.json"

API_URL = "https://g.api.mega.co.nz"


def base64_url_decode(data):
    """MEGA uses base64-url encoding with different padding rules."""
    data = data.replace("-", "+").replace("_", "/")
    # Add padding
    remainder = len(data) % 4
    if remainder:
        data += "=" * (4 - remainder)
    return base64.b64decode(data)


def base64_url_encode(data):
    """Encode to MEGA base64-url format."""
    return base64.b64encode(data).decode("utf-8").replace("+", "-").replace("/", "_").rstrip("=")


def a32_to_str(a):
    """Convert array of 32-bit integers to bytes."""
    return struct.pack(">%dI" % len(a), *a)


def str_to_a32(s):
    """Convert bytes to array of 32-bit integers."""
    if isinstance(s, str):
        s = s.encode("utf-8")
    # Pad to multiple of 4
    if len(s) % 4:
        s += b"\0" * (4 - len(s) % 4)
    return struct.unpack(">%dI" % (len(s) // 4), s)


def decrypt_key(key_data, key):
    """Decrypt MEGA file key using AES.

    The file key is encrypted with the node key (AES-128).
    key_data is the raw key bytes from the master key.
    key is the node key (32 bytes for file, with file key and IV components).
    """
    if AES is None:
        raise ImportError("PyCryptodome is required. Install with: pip install pycryptodome")

    cipher = AES.new(key_data, AES.MODE_ECB)
    decrypted = cipher.decrypt(key)

    # MEGA uses a specific key structure for files
    # First 16 bytes = file key, last 16 bytes = IV
    return decrypted


def decrypt_attr(attr_data, key):
    """Decrypt MEGA file attributes (name, size, etc.)."""
    if AES is None:
        raise ImportError("PyCryptodome is required. Install with: pip install pycryptodome")

    attr_key = key[:16]
    iv = key[16:24] + b"\0" * 8

    try:
        cipher = AES.new(attr_key, AES.MODE_CBC, iv=iv)
        decrypted = cipher.decrypt(attr_data)

        pad_len = decrypted[-1]
        if 1 <= pad_len <= 16:
            decrypted = decrypted[:-pad_len]

        # MEGA attributes start with "MEGA" prefix
        text = decrypted.decode("utf-8", errors="replace")
        if text.startswith("MEGA"):
            text = text[4:]
        return json.loads(text)
    except Exception as e:
        print(f"    Attribute decryption error: {e}")
        return {"name": "unknown.txt"}


def mega_api_request(action, data=None, query_params=None):
    """Make a request to MEGA API."""
    params = {"ak": "", "domain": "meganode"}
    if query_params:
        params.update(query_params)

    url = f"{API_URL}/cs"
    # Add sequence number
    params.update({"id": str(int(time.time() * 1000))})

    # Build query string
    qs = "&".join(f"{k}={v}" for k, v in params.items())
    full_url = f"{url}?{qs}"

    payload = [{"a": action, **(data or {})}]

    resp = requests.post(
        full_url,
        json=payload,
        headers={"User-Agent": "Mozilla/5.0"},
        timeout=30,
    )
    resp.raise_for_status()
    result = resp.json()
    if isinstance(result, list):
        return result[0]
    return result


def get_file_info(file_id):
    """Get file information from MEGA."""
    result = mega_api_request("g", {"p": file_id})
    return result


def get_download_url(file_id, public_handle):
    """Get download URL from MEGA."""
    result = mega_api_request("g", {"p": file_id, "n": public_handle})
    if result and isinstance(result, dict):
        return result.get("g")
    return None


def parse_mega_url(url):
    """Parse mega.nz URL to extract file ID and key.

    Format: https://mega.nz/file/{file_id}#{key}
    """
    match = re.match(r"https://mega\.nz/file/([^#]+)#(.+)", url)
    if match:
        return match.group(1), match.group(2)
    return None, None


def download_file(file_id, key_b64, output_path):
    """Download and decrypt a file from MEGA."""
    # Parse the key
    key_data = base64_url_decode(key_b64)
    print(f"    Key length: {len(key_data)}, hex: {key_data.hex()[:64]}...")

    # Get file info
    print(f"    Getting file info...")
    info = get_file_info(file_id)
    if not info or isinstance(info, list):
        # Try alternative API call format
        info = mega_api_request("g", {"p": file_id})

    print(f"    File info received: type={type(info).__name__}")
    if isinstance(info, dict):
        print(f"    Keys available: {list(info.keys())[:10]}")
        print(f"    File name: {info.get('n', 'N/A')}")
        print(f"    File size: {info.get('s', 'N/A')}")

    # For public file downloads, MEGA uses a different approach
    # Get the download URL
    dl_url = mega_api_request("g", {"p": file_id})

    print(f"    Download URL result: {str(dl_url)[:200] if dl_url else 'None'}")

    if isinstance(dl_url, dict) and "g" in dl_url:
        actual_url = dl_url["g"]
        size = dl_url.get("s", 0)
        print(f"    Download URL: {actual_url[:100]}...")
        print(f"    File size: {size}")

        # Download encrypted file
        print(f"    Downloading encrypted file...")
        resp = requests.get(actual_url, stream=True, timeout=300)
        resp.raise_for_status()

        encrypted_data = resp.content
        print(f"    Downloaded {len(encrypted_data)} bytes")

        # Decrypt the file
        # MEGA uses AES-128-CTR with the file key
        file_key = key_data[:16]
        iv = key_data[16:32] if len(key_data) >= 32 else b"\0" * 16

        print(f"    File key (16 bytes): {file_key.hex()}")
        print(f"    IV (16 bytes): {iv.hex()}")

        # Try decryption
        try:
            # MEGA uses AES-128 in CTR mode (not CBC)
            from Crypto.Util import Counter
            ctr = Counter.new(128, initial_value=int.from_bytes(iv, 'big'))
            cipher = AES.new(file_key, AES.MODE_CTR, counter=ctr)
            decrypted = cipher.decrypt(encrypted_data)

            with open(output_path, "wb") as f:
                f.write(decrypted)

            print(f"    Decrypted and saved: {output_path} ({len(decrypted)} bytes)")
            return True
        except Exception as e:
            print(f"    Decryption error: {e}")

            # Try CBC fallback
            try:
                cipher = AES.new(file_key, AES.MODE_CBC, iv=iv)
                decrypted = cipher.decrypt(encrypted_data)
                if len(decrypted) > 16:
                    pad_len = decrypted[-1]
                    if 1 <= pad_len <= 16:
                        decrypted = decrypted[:-pad_len]
                with open(output_path, "wb") as f:
                    f.write(decrypted)
                print(f"    CBC fallback saved: {output_path} ({len(decrypted)} bytes)")
                return True
            except Exception as e2:
                print(f"    CBC fallback also failed: {e2}")

            # Try writing encrypted as-is (maybe not encrypted?)
            with open(str(output_path) + ".encrypted", "wb") as f:
                f.write(encrypted_data)
            print(f"    Saved encrypted version as fallback")
            return False

    return False


def main():
    # Test with the first MEGA URL
    mega_url = "https://mega.nz/file/hmhxTQaT#APPZ-ICOmRY-im87RQhmFkMj1Exb4U69f7cdXru2s1k"
    file_id, key_b64 = parse_mega_url(mega_url)

    if not file_id or not key_b64:
        print(f"Could not parse MEGA URL: {mega_url}")
        sys.exit(1)

    print(f"File ID: {file_id}")
    print(f"Key (base64): {key_b64}")

    output_path = STORIES_DIR / "dai-dam-hiep_mega.txt"
    success = download_file(file_id, key_b64, output_path)

    if success:
        size = output_path.stat().st_size if output_path.exists() else 0
        print(f"\nSUCCESS! File saved to: {output_path} ({size} bytes)")
    else:
        print(f"\nFAILED to download/decrypt file")


if __name__ == "__main__":
    main()