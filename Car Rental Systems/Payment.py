from abc import ABC, abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(Payment):
    def __init__(self, credit_card_number):
        self.credit_card_number = credit_card_number
        self.balance = 100
    
    def get_balance(self):
        return self.balance

    def pay(self, amount):
        print(f"Paid {amount} with credit card ending in {self.credit_card_number[-4:]}")

class PayPalPayment(Payment):
    def __init__(self, email):
        self.email = email
        self.balance = 100
    
    def get_balance(self):
        return self.balance
    
    def pay(self, amount):
        print(f"Paid {amount} with paypal with email {self.email}")
