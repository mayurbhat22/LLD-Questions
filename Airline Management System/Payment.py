from abc import ABC, abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(Payment):
    def __init__(self, card_number):
        self.card_number = card_number
        self.balance = 200
    
    def pay(self, amount):
        print(f"Paid amount {amount} with credit card ending {self.card_number[-4:]}")

class PayPalPayment(Payment):
    def __init__(self, email):
        self.email = email
        self.balance = 200
    
    def pay(self, amount):
        print(f"Paid amount {amount} with email {self.email}")