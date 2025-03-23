from money import Money
from money_type import MoneyType

class Coins(Money):
    def __init__(self, value):
        super().__init__(MoneyType.COINS, value)