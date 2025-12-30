from __future__ import annotations

from typing import Sequence

from models.product import Product


def extract_prices(products: Sequence[Product]) -> list[float]:
    """Преобразовать список продуктов в список их цен."""
    return [float(p.price) for p in products]
