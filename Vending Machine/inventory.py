from chips import Chips
from candy_bars import CandyBars
from coins import Coins
from drinks import Drinks
from notes import Notes
from products import Products

class Inventory:
    def __init__(self):
        self.inventory = {}  

    def add_products(self, product: Products, quantity: int, name: str = ""):
        """Adds a specified quantity of a product to the inventory."""

        # Add product to inventory
        if product in self.inventory:
            self.inventory[product]["quantity"] += quantity
        else:
            self.inventory[product] = {"name": name, "quantity": quantity}
    

    def remove_products(self, product: Products, quantity: int):
        """Adds a specified quantity of a product to the inventory."""
        
        # Add product to inventory
        if product in self.inventory:
            self.inventory[product]["quantity"] -= quantity
        if self.inventory[product]["quantity"] <= 0:
            del self.inventory[product]
    

    def get_products(self, product: Products):
        if product in self.inventory:
            return self.inventory[product]["quantity"]
        else:
            return 0    
