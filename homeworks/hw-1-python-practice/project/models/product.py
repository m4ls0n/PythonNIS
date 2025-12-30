from __future__ import annotations


class Product:
    def __init__(self, name: str, category: str, price: float):
        self.name = name
        self.category = category
        self.price = price
        self.sale = 0

    def edit_category(self, new_category: str) -> None:
        self.category = new_category

    def edit_price(self, new_price: float) -> None:
        self.price = new_price

    def set_sale(self, sale: int) -> None:
        # скидка в процентах
        if sale < 0:
            sale = 0
        if sale > 100:
            sale = 100
        self.sale = sale

    def cancel_sale(self) -> None:
        self.sale = 0

    def get_price(self) -> float:
        # Это не тупо геттер - тут надо учесть скидку и еще то, что скидка указана в процентах
        if not self.sale:
            return float(self.price)
        return float(self.price) * (100 - self.sale) / 100

    def __repr__(self) -> str:
        return (
            f"Product(name={self.name!r}, category={self.category!r}, "
            f"price={self.price}, sale={self.sale})"
        )
