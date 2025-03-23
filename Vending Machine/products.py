from product_type import ProductType

class Products:
    def __init__(self, product_type: ProductType, price):
        self.product_type = product_type
        self.price = price
    
    def get_product_type(self):
        return self.product_type

    def get_price(self):
        return self.price