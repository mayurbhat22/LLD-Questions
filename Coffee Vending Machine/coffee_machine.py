from inventory import Inventory
from espresso import Espresso
from latte import Latte
from cappuccino import Cappuccino

class CoffeeMachine:
    _instance = None
    def __init__(self):
        if CoffeeMachine._instance is not None:
            raise Exception("This class is a singleton!")
        else:
            CoffeeMachine._instance = self
            self.coffee_menu = []
            self.inventory = Inventory()
            self._create_recipes()
            self._add_products()
    
    def get_instance():
        if CoffeeMachine._instance is None:
            CoffeeMachine()
        return CoffeeMachine._instance 

    def _add_products(self):
        self.inventory.add_ingredients("Water", 10)
        self.inventory.add_ingredients("Coffee", 10)
        self.inventory.add_ingredients("Milk", 10)

    def _create_recipes(self):
        espresso_recipe = {
            "Coffee" : 1,
            "Water" : 1
        }
        self.coffee_menu.append(Espresso("Espresso", 4.99, espresso_recipe))

        cappuccino_recipe = {
            "Coffee" : 1,
            "Water" : 1,
            "Milk" : 1
        }
        self.coffee_menu.append(Cappuccino("Cappuccino", 6.99, cappuccino_recipe))

        latte_recipe = {
            "Coffee" : 1,
            "Water" : 1,
            "Milk" : 2.5
        }
        self.coffee_menu.append(Latte("Latte", 7.99, latte_recipe))
    
    def display_menu(self):
        for coffee in self.coffee_menu:
            print(f"{coffee.get_name()} - {coffee.get_price()}$")

    def select_coffee(self, coffee_name):
        for coffee in self.coffee_menu:
            if coffee.get_name().lower() == coffee_name.lower():
                return coffee

    def dispense_coffee(self, coffee, amount):
        recipe = coffee.get_recipe()
        for ingredient, quantity in recipe.items():
            if self.inventory.get_ingredients(ingredient) >= quantity:
                continue
            else:
                print(f"Not enough ingredients to make {coffee.get_name()}!")

        if amount >= coffee.get_price():
            print(f"Dispensing {coffee.get_name()}")
            self._update_inventory(recipe)
        else:
            print(f"Not enough amount to dispense {coffee.get_name()}.")

    def _update_inventory(self, recipe):
        for ingredient, quantity in recipe.items():
            self.inventory.update_ingredients(ingredient, -quantity)