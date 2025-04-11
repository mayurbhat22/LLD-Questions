class Account:
    def __init__(self, id, number, balance):
        self._id = id
        self._account_number = number
        self._balance = balance
    
    def get_id(self):
        return self._id
    
    def get_account_number(self):
        return self._account_number
    
    def get_balance(self):
        return self._balance
    
    def deduct_money(self, amount):
        if amount <= self.get_balance():
            self._balance -= amount
            return True
        else:
            print("Insufficient Balance")