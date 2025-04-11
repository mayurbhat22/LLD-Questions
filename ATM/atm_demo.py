from user import User
from card import Card
from account import Account
from atm import ATM
class ATMDemo:
    def run():
        account = Account(1, 12345, 1000)
        card = Card(4211, "1234")
        mayur = User("Mayur", "abc@gmail.com", account, card)
        
        atm = ATM("Chase Bank ATM", 1)

        #Assuming, user inserts the card
        atm.set_user(mayur)
        atm.authorize_pin("1234")

        atm.withdraw_amount(600)
        atm.get_balance()


if __name__ == "__main__":
    ATMDemo.run()