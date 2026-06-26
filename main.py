import requests
import re
import json
from bs4 import BeautifulSoup

CHANNELS = [
    
    "https://t.me/s/bigAVPN",
    "https://t.me/s/oneclickvpnkeys",
    "https://t.me/s/nitruStore",
    "https://t.me/s/freenettir",
    "https://t.me/s/V2All",
    "https://t.me/s/appsooner",
    "https://t.me/s/v2rayngvpn",
    "https://t.me/s/vistav2ray",
    "https://t.me/s/mtmvpn",
    "https://t.me/s/V2rayng_Fast",
    "https://t.me/s/FarazV2ray",
    "https://t.me/s/FreakConfig",
    "https://t.me/s/v2rayng_fast",
    "https://t.me/s/meliproxyy",
    "https://t.me/s/chillguy_vpn",
    "https://t.me/s/configV2rayNG",
    "https://t.me/s/anotherme_night",
    "https://t.me/s/V2dogs_n",
    "https://t.me/s/erfanandroid",
    "https://t.me/s/filembad",
    "https://t.me/s/mehrosaboran"
    "https://t.me/s/AR14N24B",
    "https://t.me/s/ShadowProxy66",
    "https://t.me/s/V2dogs_n"
    
]

PATTERN = r"(vless://[^\s]+)"
TAG = "🆔 @V2rayUBot @V2rayuir"

headers = {"User-Agent": "Mozilla/5.0"}

configs = set()

# ---------------- SCRAPE ----------------
for url in CHANNELS:
    try:
        r = requests.get(url, headers=headers, timeout=20)
        soup = BeautifulSoup(r.text, "html.parser")
        text = soup.get_text("\n")

        found = re.findall(PATTERN, text)

        # 🔥 فقط 5 تای آخر هر کانال
        last_5 = found[-3:]

        for c in last_5:
            configs.add(c)

    except Exception as e:
        print("Error:", e)

# ---------------- CLEAN ----------------
vless_list = sorted(list(configs))

cleaned = []

for c in vless_list:
    base = c.split("#")[0]   # حذف fragment قبلی
    final = base + "#" + TAG
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
