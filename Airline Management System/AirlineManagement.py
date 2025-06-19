from Payment import Payment
from User import User
from Flight_Schedule import FlightSchedule
from Reservation import Reservation
from Flight import Flight
class UserService:
    def __init__(self):
        self.users = []
        self.user_id = 0
    
    def create_user(self, name, email, phone, dob):
        self.user_id += 1
        user = User(self.user_id, name, email, phone, dob)
        self.users.append(user)
        return user
    
class PaymentService:
    def make_payment(self, amount, payment_method):
        if payment_method.balance >= amount:
            payment_method.pay(amount)
            return True
        return False

class FlightService:
    def __init__(self):
        self.flight_service = []
    
    def create_flights(self, name, model, capacity):
        flight = Flight(name, model, capacity)
        return flight
    
    def create_flight_schedule(self, source, destination, from_date, to_date, price, flight):
        flight_schedule = FlightSchedule(source, destination, from_date, to_date, price, flight)
        self.flight_service.append(flight_schedule)
        return flight_schedule
        print(self.flight_service)
    
    def search_flight(self, source="", destination="", from_date=None, to_date=None):
        self.flights = set()
        for flight_schedule in self.flight_service:
            print(flight_schedule.source)
            if flight_schedule.source == source:
                self.flights.add(flight_schedule)
            if flight_schedule.destination == destination:
                self.flights.add(flight_schedule)
            if flight_schedule.from_date == from_date:
                self.flights.add(flight_schedule)
            if flight_schedule.to_date == to_date:
                self.flights.add(flight_schedule)
            if source=="" and destination == "" and from_date==None and to_date==None:
                self.flights.add(flight_schedule)
        return list(self.flights)
    
class ReservationService:
    def __init__(self):
        self.reservations = []
        self.reservation_id = 0
    
    def make_booking(self, user: User, number_of_passengers, flight_schedule: FlightSchedule, payment_method: Payment):
        total_price = number_of_passengers * flight_schedule.price
        if PaymentService().make_payment(total_price, payment_method):
            self.reservation_id += 1
            reservation = Reservation(self.reservation_id, user, number_of_passengers, flight_schedule, payment_method)
            self.reservations.append(reservation)
            return reservation
        else:
            print("No sufficient Balance")
    