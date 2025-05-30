from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount:float):
        pass

class CreditCardPayment(Payment):
    def __init__(self, card_number):
        self.card_number = card_number
    
    def pay(self, amount:float):
        print(f"Paid {amount} with credit card ending with number {self.card_number[-4:]}")
    
class PayPalPayment(Payment):
    def __init__(self, email):
        self.email = email
    
    def pay(self, amount:float):
        print(f"Paid {amount} with PayPal ending with email {self.email}")

class ShoppingCart:
    def __init__(self):
        self.amount = 0.0
        self._payment_method = None
    
    def add_items(self, price:float):
        self.amount += price
    
    def select_payment_method(self, paymentmethod: Payment):
        self._payment_method = paymentmethod
    
    def checkout(self):
        if not self._payment_method:
            return "Payment method not set"
        self._payment_method.pay(self.amount)

credit_card = CreditCardPayment("12345678")
paypal = PayPalPayment("abc@xyz.com")

shopping_cart = ShoppingCart()
shopping_cart.add_items(14.99)
shopping_cart.add_items(9.99)

shopping_cart.select_payment_method(credit_card)
shopping_cart.checkout()

shopping_cart.select_payment_method(paypal)
shopping_cart.checkout()
