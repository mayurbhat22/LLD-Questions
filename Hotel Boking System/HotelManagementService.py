from Guest import Guest
from Payment import CreditCardPayment, Payment, PayPalPayment, CashPayment
from Room import Room
from Reservation import Reservation
from RoomType import RoomType
from datetime import datetime
class RoomService:
    def __init__(self):
        self.rooms = []
        self.room_number = 0
    
    def add_room(self, room_number, capacity_of_guests, price_per_day, room_type):
        self.room_number += 1
        room = Room(self.room_number, capacity_of_guests, price_per_day, room_type)
        self.rooms.append(room)
        return room

class PaymentService:
    def make_payment(self, payment_method: Payment, amount):
        if payment_method.get_balance() >= amount:
            payment_method.pay(amount)
            return True
        return False
    
class ReservationService:
    reservations = []
    reservation_id = 0
    
    def is_room_available(self, room, from_date, to_date):
        for reservation in self.reservations:
            if room.room_number == reservation.room.room_number:
                if reservation.from_date < from_date < reservation.to_date or reservation.from_date < to_date < reservation.to_date:
                    return False
        return True

    def make_reservation(self, room: Room, from_date, to_date, payment_method: Payment, guest: Guest):
        #Check if the room is available
        if self.is_room_available(room, from_date, to_date):
            #If the payment went through
            total_price = (to_date - from_date).days * room.price_per_day
            if PaymentService().make_payment(payment_method, total_price):
                ReservationService.reservation_id += 1
                reservation = Reservation(ReservationService.reservation_id, datetime.now(), room, from_date, to_date, total_price, payment_method, guest)
                ReservationService.reservations.append(reservation)
                room.is_available = False
                return reservation
            else:
                print("Insufficient balance to make the payment")
        else:
            print("Selected room is not available for the selected dates")

class CheckInService:
    def check_in(self, reservation):
        for res in ReservationService().reservations:
            if res.reservation_id == reservation.reservation_id:
                if res.from_date == datetime.now():
                    if res.check_in_status != "CheckedIn":
                        res.check_in_status = "CheckedIn"
                else:
                    print("Reservation date is not today")
    
    def check_out(self, reservation):
        for res in ReservationService().reservations:
            if res.reservation_id == reservation.reservation_id:
                if res.to_date >= datetime.now():
                    if res.check_in_status != "CheckedOut":
                        res.check_in_status = "CheckedOut"

