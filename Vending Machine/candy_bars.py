from products import Products
from product_type import ProductType

class CandyBars(Products):
    def __init__(self, name, price):
        self.name = name
        super().__init__(ProductType.Candy_BARS, price)
    