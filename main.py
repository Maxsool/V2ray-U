import requests
import re
import json
from bs4 import BeautifulSoup

CHANNELS = [
    "https://t.me/s/FreakConfig",
    "https://t.me/s/v2line",
    "https://t.me/s/v2ray1_ng",
    "https://t.me/s/v2rayng_fast",
    "https://t.me/s/PrivateVPNs",
    "https://t.me/s/DirectVPN",
    "https://t.me/s/vlesskeys",
    "https://t.me/s/vpnfail_v2ray",
    "https://t.me/s/vlessrus",
    "https://t.me/s/ShadowSocks",
    "https://t.me/s/mehrosaboran"
]

PATTERN = r"(vless://[^\s]+)"

TAG = "🆔 @V2rayUBot @V2rayuir"

configs = set()

headers = {"User-Agent": "Mozilla/5.0"}

# ---------------- SCRAPE ----------------
for url in CHANNELS:
    try:
        r = requests.get(url, headers=headers, timeout=20)
        soup = BeautifulSoup(r.text, "html.parser")
        text = soup.get_text("\n")

        found = re.findall(PATTERN, text)

        for c in found:
            configs.add(c)

    except Exception as e:
        print("Error:", e)

# ---------------- CLEAN ----------------
vless_list = sorted(list(configs))

cleaned = []

for c in vless_list:

    # جدا کردن fragment از لینک
    if "#" in c:
        base, fragment = c.split("#", 1)

        # 🔥 فقط حذف آخرین هشتگ داخل fragment
        parts = fragment.split()

        # اگر هشتگ کانال هست حذف کن (مثل @FreakConfig یا 🇸🇪@xxx)
        filtered = [p for p in parts if not p.startswith("@") and "#" not in p]

        # تگ ثابت ما
        new_fragment = TAG

        final = base + "#" + new_fragment
    else:
        final = c + "#" + TAG

    cleaned.append(final)

# ---------------- SAVE TXT ----------------
with open("vless.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(cleaned))

# ---------------- SAVE JSON ----------------
data = {
    "count": len(cleaned),
    "vless": cleaned
}

with open("vless.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("DONE:", len(cleaned))
