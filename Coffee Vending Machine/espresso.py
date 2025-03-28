from coffee import Coffee
class Espresso(Coffee):
    def __init__(self, name, price, recipe):
        super().__init__(name, price, recipe)