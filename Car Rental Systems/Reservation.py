from Customer import Customer
from Car import Car

class Reservation:
    def __init__(self, reservation_id, customer: Customer, car: Car, booking_date, from_date, to_date, total_price, payment_method):
        self.reservation_id = reservation_id
        self.customer = customer
        self.car = car
        self.booking_date = booking_date
        self.from_date = from_date
        self.to_date = to_date
        self.total_price = total_price
        self.payment_method = payment_method
        self.status = "Booked"
