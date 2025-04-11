from transaction_type import TransactionType
from transaction import Transaction

class Balance(Transaction):
    def __init__(self):
        super().__init__(TransactionType.BALANCE_ENQUIRY)
    
    def get_balance(self, account):
        return account.get_balance()
    