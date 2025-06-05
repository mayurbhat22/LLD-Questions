from Car import Car
from Customer import Customer
from Customer import Customer
from Reservation import Reservation
from Payment import CreditCardPayment, PayPalPayment
from RentalService import CarService, PaymentService, ReservationService
from datetime import datetime

class CarRentalDemo:
    def run():
        mayur = Customer("Mayur", "mayur@email.com", "812777777", "ABCD87IN")
        shreyas = Customer("Shreyas", "shreyas@email.com", "1111111122", "ERFE34CA")

        honda_civic = CarService().add_car("Honda", "Civic", 2020, "AZW12IN", 29.99, "Available")
        toyota_camry = CarService().add_car("Toyota", "Camry", 2022, "AZW12CA", 34.99, "Available")

        credit_card = CreditCardPayment("123456789123")
        pay_pal = PayPalPayment("mayur@email.com")

        reservation_1 = ReservationService().make_reservation(mayur, honda_civic, datetime.now(), datetime(2025, 6, 7), datetime(2025, 6, 10), credit_card)
        reservation_2 = ReservationService().make_reservation(shreyas, honda_civic, datetime.now(), datetime(2025, 6, 9), datetime(2025, 6, 11), credit_card)    

if __name__ == "__main__":
    CarRentalDemo.run()
