from abc import ABC, abstractmethod
from products import Products
from money import Money
class MachineState(ABC):
    @abstractmethod
    def select_product(self, product: Products, quantity: str):
        pass
    
    def insert_money(self, money: Money):
        pass

    def dispense_product(self):
        pass
