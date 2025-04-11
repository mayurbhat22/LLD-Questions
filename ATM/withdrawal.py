from transaction_type import TransactionType
from transaction import Transaction

class Withdrawal(Transaction):
    def __init__(self):
        super().__init__(TransactionType.WITHDRAWAL)
    
    def deduct_money(self, account, amount):
        return account.deduct_money(amount)
    
