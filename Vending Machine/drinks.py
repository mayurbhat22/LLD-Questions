from products import Products
from product_type import ProductType

class Drinks(Products):
    def __init__(self, name, price):
        self.name = name
        super().__init__(ProductType.DRINKS, price)
    
