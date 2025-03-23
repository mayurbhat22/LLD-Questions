from money_type import MoneyType

class Money:
    def __init__(self, money_type : MoneyType, value):
        self.money_type = money_type
        self.value = value
