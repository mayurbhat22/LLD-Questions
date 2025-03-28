class Inventory:
    def __init__(self):
        self.ingredients = {}

    def add_ingredients(self, product, quantity):
        if product in self.ingredients:
            self.ingredients[product] += quantity
        else:
            self.ingredients[product] = quantity
    
    def update_ingredients(self, product, quantity):
        if product in self.ingredients:
            self.ingredients[product] += quantity
        else:
            self.ingredients[product] = quantity
        if self.ingredients[product] == 0:
            del self.ingredients[product]

    def remove_ingredients(self, product):
        if product in self.ingredients:
            del self.ingredients[product]
        
    def get_ingredients(self, product):
        return self.ingredients[product]
    
    def display_ingredients(self):
        for product, quantity in self.ingredients.items():
            print(product, quantity)