from coffee_machine import CoffeeMachine
from espresso import Espresso
from cappuccino import Cappuccino
from latte import Latte

class CoffeeMachineDemo:
    def run():
        coffee_machine = CoffeeMachine.get_instance()
        coffee_machine.display_menu()

        coffee_machine.inventory.display_ingredients()
        #Select a Coffee
        espresso = coffee_machine.select_coffee("Espresso")
        #Dispense the selected coffee
        coffee_machine.dispense_coffee(espresso, 5.00)

        coffee_machine.inventory.display_ingredients()
        #Select a Coffee
        latte = coffee_machine.select_coffee("Latte")
        #Dispense the selected coffee
        coffee_machine.dispense_coffee(latte, 8.00)
        coffee_machine.inventory.display_ingredients()

    
if __name__ == "__main__":
    CoffeeMachineDemo.run()