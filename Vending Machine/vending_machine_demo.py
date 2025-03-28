from vending_machine import VendingMachine
from inventory import Inventory
from idle_state import IdleState
from ready_state import ReadyState
from dispense_state import DispenseState
from machine_state import MachineState
from products import Products
from money import Money
from chips import Chips
from drinks import Drinks
from candy_bars import CandyBars
from coins import Coins
from notes import Notes

class VendingMachineDemo:
    def run():
        vending_machine = VendingMachine.get_instance()

        #Create Money
        coin_quarter = Coins(0.25)
        coin_one_dollar = Coins(1)
        coin_five_dollar = Coins(5)

        note_one_dollar = Notes(1)
        note_five_dollar = Notes(5)
        note_ten_dollar = Notes(10)

    
        #Create the products
        lays = Chips("Lays", 10)
        coke = Drinks("Coke", 15)


        #Add the products to the Machine
        vending_machine.inventory.add_products(lays, 3, "Lays")
        vending_machine.inventory.add_products(coke, 2, "Coke")

        #Select a Product
        vending_machine.select_product(lays, 1)

        #Insert Money
        vending_machine.insert_money(note_five_dollar)
        vending_machine.insert_money(note_five_dollar)

        #DispenseProduct
        vending_machine.dispense_product()

        #Select a Product
        vending_machine.select_product(coke, 1)

        #Insert Money
        vending_machine.insert_money(note_five_dollar)
        vending_machine.insert_money(note_five_dollar)
        vending_machine.insert_money(note_five_dollar)


        #DispenseProduct
        vending_machine.dispense_product()

if __name__ == "__main__":
    VendingMachineDemo.run()




