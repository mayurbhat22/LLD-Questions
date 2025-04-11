from account import Account
from card import Card
from transaction import Transaction
from withdrawal import Withdrawal
from balance import Balance
from transaction_type import TransactionType
class User:
    def __init__(self, name, email, account: Account, card: Card):
        self._name = name
        self._email = email
        self._account = account
        self._card = card

    def make_transaction(self, transaction_type, amount = 0):
        if transaction_type == TransactionType.WITHDRAWAL:
            Withdrawal().deduct_money(self._account, amount)
            print(f"Amount {amount} deducted from your account")
        elif transaction_type == TransactionType.BALANCE_ENQUIRY:
            print(f"Your account balance is:  {Balance().get_balance(self._account)} ")
    
    def get_card(self):
        return self._card

    def get_account(self):
        return self._account