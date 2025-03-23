from products import Products
from product_type import ProductType

class Chips(Products):
    def __init__(self, name, price):
        self.name = name
        super().__init__(ProductType.CHIPS, price)