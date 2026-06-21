import requests
import re
import json
from bs4 import BeautifulSoup

CHANNELS = [
    "https://t.me/s/FreakConfig",
    "https://t.me/s/v2line",
    "https://t.me/s/v2rayng_fast",
    "https://t.me/s/mehrosaboran"
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
        last_5 = found[-5:]

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
