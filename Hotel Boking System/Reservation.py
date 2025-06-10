from Guest import Guest
from Payment import CreditCardPayment, Payment, PayPalPayment, CashPayment
from Room import Room

class Reservation:
    def __init__(self, reservation_id, reservation_date, room: Room, from_date, to_date, total_price, payment_method: Payment, guest: Guest):
        self.reservation_id = reservation_id
        self.reservation_date = reservation_date
        self.room = room
        self.from_date = from_date
        self.to_date = to_date
        self.total_price = total_price
        self.payment_method = payment_method
        self.guest = guest
        self.status = "Reservation"
        self.check_in_status = "Pending"