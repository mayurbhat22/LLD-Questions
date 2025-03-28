from machine_state import MachineState
from products import Products
from money import Money
# from typing import override
from money_type import MoneyType

class DispenseState(MachineState):
    def __init__(self, vending_machine: MachineState):
        self.vending_machine = vending_machine
    
    def select_product(self, product: Products, quantity: str):
        print("Product already selected. Money inserted. Wait for the product to get dispensed.")
    
    def insert_money(self, money: Money):
        print("Money inserted. Wait for the product to get dispensed.")
    
    def dispense_product(self):
        product = self.vending_machine.selected_product
        quantity = self.vending_machine.selected_quantity
        print(f"{quantity} quantities of {product.get_product_type().name} dispensed.")
        self.vending_machine.inventory.add_products(product, -quantity)
        self.vending_machine.reset_selected_product()
        self.vending_machine.reset_payment()
        self.vending_machine.set_state(self.vending_machine.idle_state)




