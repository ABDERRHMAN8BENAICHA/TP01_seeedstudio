import csv
from dataclasses import asdict
from typing import List
from domain.product import Product


def save(products: List[Product], filename: str):
    with open(filename + ".csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "sku",
                "title",
                "description",
                "price",
                "product_url",
                "image_url",
            ],
        )
        writer.writeheader()
        for p in products:
            writer.writerow(asdict(p))
