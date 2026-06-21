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

pattern = r"(vless://[^\s]+)"

all_configs = set()

for url in CHANNELS:
    try:
        r = requests.get(url, timeout=20, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(r.text, "html.parser")
        text = soup.get_text("\n")

        found = re.findall(pattern, text)

        # 🔥 مهم: اینجا flatten و مستقیم اضافه کن
        for f in found:
            all_configs.add(f)

    except Exception as e:
        print("Error:", e)

# 🔥 خیلی مهم: فقط یک لیست ساده
vless_list = sorted(list(all_configs))

# 🔥 JSON تمیز و یک‌دست
data = {
    "count": len(vless_list),
    "vless": vless_list
}

with open("vless.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

with open("vless.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(vless_list))

print("DONE:", len(vless_list))
