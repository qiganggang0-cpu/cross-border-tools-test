import json
import urllib.request
from datetime import datetime, timezone

url = "https://open.er-api.com/v6/latest/USD"

with urllib.request.urlopen(url, timeout=10) as resp:
    data = json.loads(resp.read().decode())

rate = data["rates"]["CNY"]
now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

print(f"{now} USD/CNY = {rate}")
