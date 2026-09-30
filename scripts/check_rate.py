import csv
import json
import os
import urllib.request
from datetime import datetime, timezone

api_key = os.environ.get("DEMO_API_KEY", "未设置")
print(f"读取到的 API Key: {api_key[:8]}...")

url = "https://open.er-api.com/v6/latest/USD"

with urllib.request.urlopen(url, timeout=10) as resp:
    data = json.loads(resp.read().decode())

rate = data["rates"]["CNY"]
now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

print(f"{now} USD/CNY = {rate}")

os.makedirs("docs/data", exist_ok=True)
csv_path = "docs/data/exchange_rate.csv"
file_exists = os.path.isfile(csv_path)

with open(csv_path, "a", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    if not file_exists:
        writer.writerow(["time_utc", "base", "quote", "rate"])
    writer.writerow([now, "USD", "CNY", rate])
