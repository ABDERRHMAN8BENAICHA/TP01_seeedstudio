import json
from dataclasses import asdict
from typing import List
from domain.product import Product


def save(products: List[Product], filename: str):
    with open(filename + ".json", "w", encoding="utf-8") as f:
        json.dump([asdict(p) for p in products], f, ensure_ascii=False, indent=2)
