from threading import Lock
from inventory import Inventory
from idle_state import IdleState
from ready_state import ReadyState
from dispense_state import DispenseState
from machine_state import MachineState
from products import Products
from money import Money

class VendingMachine:
    _instance = None
    _lock = Lock()

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
                cls._instance.inventory = Inventory()
                cls._instance.idle_state = IdleState(cls._instance)
                cls._instance.ready_state = ReadyState(cls._instance)
                cls._instance.dispense_state = DispenseState(cls._instance)
                cls._instance.current_state = cls._instance.idle_state
                cls._instance.selected_product = None
                cls._instance.selected_quantity = 0
                cls._instance.total_payment = 0.0
        return cls._instance

    @classmethod
    def get_instance(cls):
        return cls()

    def select_product(self, product: Products, quantity: str):
        self.current_state.select_product(product, quantity)
    
    def insert_money(self, money: Money):
        self.current_state.insert_money(money)
    
    def dispense_product(self):
        self.current_state.dispense_product()
    
    def set_state(self, state: MachineState):
        self.current_state = state
    
    def reset_payment(self):
        self.total_payment = 0.0

    def reset_selected_product(self):
        self.selected_product = None    
    
    
