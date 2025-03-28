from machine_state import MachineState
from products import Products
from money import Money
# from typing import override

class IdleState(MachineState):
    def __init__(self, vending_machine: MachineState):
        self.vending_machine = vending_machine
    
    def select_product(self, product: Products, quantity: str):
        if self.vending_machine.inventory.get_products(product) >= quantity:
            self.vending_machine.selected_product = product
            self.vending_machine.selected_quantity = quantity
            self.vending_machine.set_state(self.vending_machine.ready_state)
            print(f"Product {product.get_product_type().name} selected. Insert Money")
        else:
            print(f"There is no {product.get_product_type().name} available. Select another product")
    
    def insert_money(self, money: Money):
        print("Please select the Product first.")
    
    def dispense_product(self):
        print("Please select the Product first.")
