from machine_state import MachineState
from products import Products
from money import Money
# from typing import override
from money_type import MoneyType
class ReadyState(MachineState):
    def __init__(self, vending_machine: MachineState):
        self.vending_machine = vending_machine
    
    def select_product(self, product: Products, quantity: str):
        print("Product already selected. Insert Money to get that product.")
    
    def insert_money(self, money: Money):
        print(f"{money.get_money_type().name} of value {money.value} inserted")
        self.vending_machine.total_payment += money.value
        if self.vending_machine.total_payment >= (self.vending_machine.selected_product.get_price() * self.vending_machine.selected_quantity):
            self.vending_machine.set_state(self.vending_machine.dispense_state)
            print("Product is being dispensed.")
    
    def dispense_product(self):
        print("Insert Money to get that product.")
