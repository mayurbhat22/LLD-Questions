from money import Money
from money_type import MoneyType

class Notes(Money):
    def __init__(self, value):
        super().__init__(MoneyType.NOTE, value)
    
    def get_money_type(self):
        return MoneyType.NOTE