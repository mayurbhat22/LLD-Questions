from chips import Chips
from candy_bars import CandyBars
from coins import Coins
from drinks import Drinks
from notes import Notes
from product_type import ProductType

class Machine:
    def __init__(self, name, total_items):
        self.name = name
        self.total_items = total_items
        self.inventory = {}  

    def add_products(self, product_type: ProductType, name: str, price: float, quantity: int):
        """Adds a specified quantity of a product to the inventory."""
        
        # Factory method to create product instances dynamically
        product_class = {
            ProductType.CHIPS: Chips,
            ProductType.DRINKS: Drinks,
            ProductType.Candy_BARS: CandyBars
        }.get(product_type)  # Get the correct class

        if product_class is None:
            print(f"Unknown product type: {product_type}")
            return
        
        # Create an instance of the product
        product = product_class(name, price)

        # Add product to inventory
        if product_type in self.inventory:
            self.inventory[product_type]["quantity"] += quantity
        else:
            self.inventory[product_type] = {"product": product, "quantity": quantity}

        
