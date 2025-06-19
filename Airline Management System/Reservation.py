from Payment import Payment
from User import User
from Flight_Schedule import FlightSchedule
from datetime import datetime
class Reservation:
    def __init__(self, reservation_id, user: User, number_of_passengers, flight_schedule: FlightSchedule, payment_method: Payment):
        self.reservation_id = reservation_id
        self.user = user
        self.flight_schedule = flight_schedule
        self.number_of_passengers = number_of_passengers
        self.payment_method = payment_method
        self.booking_date = datetime.now()