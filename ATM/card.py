class Card:
    def __init__(self, number, pin):
        self._number = number
        self._pin = pin
    
    def get_number(self):
        return self._number

    def get_pin(self):
        return self._pin
    