from Car import Car
from Customer import Customer
from Reservation import Reservation
from Payment import CreditCardPayment, PayPalPayment

class CarService:
    cars = []

    def add_car(self, make, model, year, license_number, price_per_day, availability):
        car = Car(make, model, year, license_number, price_per_day, availability)
        self.cars.append(car)
        return car

    def remove_car(self, car):
        self.cars.remove(car)
    
class PaymentService:

    def make_payment(amount, payment_method):
        if payment_method.get_balance() >= amount:
            payment_method.pay(amount)
            return True
        else:
            return False
    
class ReservationService:
    reservations = []
    reservation_id = 0

    def make_reservation(self, customer: Customer, car: Car, booking_date, from_date, to_date, payment_method):
        
        if self.is_car_available(car, from_date, to_date):
            total_price = ((to_date - from_date).days) * car.price_per_day
            if PaymentService.make_payment(total_price, payment_method):
                self.reservation_id += 1
                reservation = Reservation(self.reservation_id, customer, car, booking_date, from_date, to_date, total_price, payment_method)
                car.availability = False
                self.reservations.append(reservation)
                print(f"Car {car.make}-{car.model} reserved from {from_date} - to {to_date}")
                return reservation
            else:
                print("Insufficient balance to make a reservation")
        else:
            print("Car selected is not available")
    
    def is_car_available(self, car, from_date, to_date):
        for res in self.reservations:
            if res.car.license_number == car.license_number and res.status == "Booked":
                # Check for any overlap
                if not (to_date <= res.from_date or from_date >= res.to_date):
                    return False
        return True


    
    def modify_reservation(self, reservation, car, from_date, to_date):
        total_price = (to_date - from_date) * car.price_per_day
        for res in self.reservations:
            if res.reservation_id == reservation.reservation_id:
                if car:
                    res.car = car
                if from_date:
                    res.from_date = from_date
                if to_date:
                    res.to_date = to_date
                if total_price:
                    if total_price > res.total_price:
                        if PaymentService.make_payment(total_price - res.total_price, res.payment_method):
                            print("Extra amount has been deducted")
                    else:
                        print("Extra balance will be credited back to th original mode of payment")
    
                
                
        

    