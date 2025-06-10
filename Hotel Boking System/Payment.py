from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(Payment):
    def __init__(self, credit_card_number):
        self.credit_card_number = credit_card_number
        self.limit = 100
    
    def get_balance(self):
        return self.limit

    def pay(self, amount):
        print(f"Paid amount {amount} ending with credit card number {self.credit_card_number[-4:]}")

class PayPalPayment(Payment):
    def __init__(self, email):
        self.email = email
        self.limit = 100
    
    def get_balance(self):
        return self.limit

    def pay(self, amount):
        print(f"Paid amount {amount} associated with email {self.email}")

class CashPayment(Payment):
    def __init__(self):
        self.limit = 100
    
    def get_balance(self):
        return self.limit

    def pay(self, amount):
        print(f"Paid amount {amount} with cash")