from user import User
from card import Card
from account import Account
from transaction_type import TransactionType
class ATM:
    def __init__(self, name, id):
        self._name = name
        self._id = id
        self._user = None
        self._is_authorized = False
    
    def display_menu(self):
        print(
            """
            Withdrawal : 1
            Balance Enquiry : 2
            """
        )   
    
    def set_user(self, user: User):
        self._user = user
        print("Insert PIN")
    
    def authorize_pin(self, pin: str):
        card = self._user.get_card()
        if card.get_pin() == pin:
            self._is_authorized = True
            self.display_menu()
        else:
            print("Invalid Pin, try again.")
    
    def withdraw_amount(self, amount):
        if self._is_authorized:
            self._user.make_transaction(TransactionType.WITHDRAWAL, amount)
        else:
            print("Insert Pin and Try Again")
    
    def get_balance(self):
        if self._is_authorized:
            self._user.make_transaction(TransactionType.BALANCE_ENQUIRY)
        else:
            print("Insert Pin and Try Again")
    