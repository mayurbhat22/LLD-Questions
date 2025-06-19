from Payment import Payment, CreditCardPayment, PayPalPayment
from User import User
from Flight import Flight
from Flight_Schedule import FlightSchedule
from Reservation import Reservation
from AirlineManagement import UserService, FlightService, ReservationService
from datetime import datetime
class Demo:
    def run(self):
        mayur = UserService().create_user("Mayur", "mayu@xyz.com", "812999999", "07-11-2005")
        vishakh = UserService().create_user("Vishakh", "vishakh@xyz.com", "812999999", "07-11-2005")

        #Create Flights
        qatar_airways = FlightService().create_flights("Qatar", "AirBus380", 350)
        emirates_airways = FlightService().create_flights("Emirates", "AirBus380", 250)
        delta_ailines = FlightService().create_flights("Delta", "AirBus380", 350)

        #Create Flight Schedule
        flight_schedule1 = FlightService().create_flight_schedule("San Francisco", "New York", datetime(2025, 7, 1), datetime(2025, 7, 2), 129.99, qatar_airways)
        flight_schedule2 = FlightService().create_flight_schedule("San Francisco", "New York", datetime(2025, 7, 1), datetime(2025, 7, 2), 119.99, emirates_airways)
        flight_schedule3 = FlightService().create_flight_schedule("Atlanta", "New York", datetime(2025, 7, 11), datetime(2025, 7, 12), 89.99, delta_ailines)

        print("Here")
        #Search Flight
        flights = FlightService().search_flight("San Francisco", "New York", None, None)
        for flight_schedule in flights:
            print(flight_schedule.flight.name)
        
        credir_card_payment = CreditCardPayment("123456789011")
        reservation = ReservationService().make_booking(mayur, 1, flight_schedule1, credir_card_payment)

if __name__ == "__main__":
    Demo().run()
