import requests
import re
import json
from bs4 import BeautifulSoup
from pathlib import Path

# Telegram channels
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

# Save files next to this script
BASE_DIR = Path(__file__).resolve().parent

TXT_FILE = BASE_DIR / "vless.txt"
JSON_FILE = BASE_DIR / "vless.json"

# VLESS regex
PATTERN = r"(vless://[^\s]+)"

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

vless_configs = set()

for url in CHANNELS:
    try:
        print(f"[+] Fetching: {url}")

        response = requests.get(
            url,
            headers=HEADERS,
            timeout=20
        )
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        text = soup.get_text("\n")

        found = re.findall(PATTERN, text)

        if found:
            print(f"    Found {len(found)} VLESS configs")

        vless_configs.update(found)

    except Exception as e:
        print(f"[!] Error fetching {url}: {e}")

# Remove duplicates and sort
vless_configs = sorted(vless_configs)

# Save TXT
with open(TXT_FILE, "w", encoding="utf-8") as f:
    f.write("\n".join(vless_configs))

# Save JSON
with open(JSON_FILE, "w", encoding="utf-8") as f:
    json.dump(
        {
            "count": len(vless_configs),
            "vless": vless_configs
        },
        f,
        ensure_ascii=False,
        indent=2
    )

print("\n================================")
print(f"Total unique VLESS configs: {len(vless_configs)}")
print(f"TXT saved to : {TXT_FILE}")
print(f"JSON saved to: {JSON_FILE}")
print("Done.")
