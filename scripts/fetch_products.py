import csv
import json
import os
import urllib.request
from datetime import datetime, timezone

url = "https://dummyjson.com/products?limit=100"

req = urllib.request.Request(
    url,
    headers={
        "User-Agent": "Mozilla/5.0 (compatible; cross-border-tools/1.0)",
        "Accept": "application/json",
    },
)

with urllib.request.urlopen(req, timeout=15) as resp:
    data = json.loads(resp.read().decode())

products = data["products"]
now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

os.makedirs("docs/data", exist_ok=True)
csv_path = "docs/data/product_prices.csv"
file_exists = os.path.isfile(csv_path)

with open(csv_path, "a", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    if not file_exists:
        writer.writerow([
            "time_utc", "product_id", "title", "price",
            "category", "rating_rate", "stock"
        ])
    for p in products:
        writer.writerow([
            now,
            p["id"],
            p["title"],
            p["price"],
            p["category"],
            p.get("rating", ""),
            p.get("stock", ""),
        ])

print(f"{now} 抓取到 {len(products)} 个商品，已写入 {csv_path}")
