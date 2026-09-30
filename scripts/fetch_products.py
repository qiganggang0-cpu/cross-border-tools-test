import csv
import json
import os
import urllib.request
from datetime import datetime, timezone

url = "https://fakestoreapi.com/products"

with urllib.request.urlopen(url, timeout=10) as resp:
    products = json.loads(resp.read().decode())

now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

os.makedirs("data", exist_ok=True)
csv_path = "data/product_prices.csv"
file_exists = os.path.isfile(csv_path)

with open(csv_path, "a", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    if not file_exists:
        writer.writerow([
            "time_utc", "product_id", "title", "price",
            "category", "rating_rate", "rating_count"
        ])
    for p in products:
        writer.writerow([
            now,
            p["id"],
            p["title"],
            p["price"],
            p["category"],
            p["rating"]["rate"],
            p["rating"]["count"],
        ])

print(f"{now} 抓取到 {len(products)} 个商品，已写入 {csv_path}")
