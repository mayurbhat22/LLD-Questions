from coffee import Coffee
class Latte(Coffee):
    def __init__(self, name, price, recipe):
        super().__init__(name, price, recipe)