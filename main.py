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

vless_configs = set()

for url in CHANNELS:
    try:
        r = requests.get(url, timeout=20, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(r.text, "html.parser")
        text = soup.get_text("\n")

        vless_configs.update(re.findall(pattern, text))

    except Exception as e:
        print("Error:", e)

# مرتب + یکدست
vless_configs = sorted(vless_configs)

# JSON استاندارد
data = {
    "count": len(vless_configs),
    "vless": vless_configs
}

with open("vless.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# TXT
with open("vless.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(vless_configs))

print("Done:", len(vless_configs))
