import requests
import re
import json
from bs4 import BeautifulSoup

CHANNELS = [
    "https://t.me/s/FreakConfig",
    "https://t.me/s/v2rayng_fast",
    "https://t.me/s/mehrosaboran"
    "https://t.me/s/FarazV2ray"
]

PATTERN = r"(vless://[^\s]+)"

# 🔥 تگ دلخواه تو
TAG = "🆔 @V2rayUBot @V2rayuir"

configs = set()

headers = {
    "User-Agent": "Mozilla/5.0"
}

# ------------------ SCRAPE ------------------
for url in CHANNELS:
    try:
        r = requests.get(url, headers=headers, timeout=20)
        soup = BeautifulSoup(r.text, "html.parser")
        text = soup.get_text("\n")

        found = re.findall(PATTERN, text)

        for c in found:
            configs.add(c)

        print(f"[+] {url} -> {len(found)}")

    except Exception as e:
        print(f"[!] Error {url}: {e}")

# ------------------ CLEAN DATA ------------------
vless_list = sorted(list(configs))

# ------------------ ADD TAG ------------------
vless_tagged = [c + " " + TAG for c in vless_list]

# ------------------ SAVE TXT ------------------
with open("vless.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(vless_tagged))

# ------------------ SAVE JSON ------------------
data = {
    "count": len(vless_list),
    "vless": vless_tagged
}

with open("vless.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("DONE:", len(vless_list))
