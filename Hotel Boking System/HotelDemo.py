from Guest import Guest
from Payment import CreditCardPayment, Payment, PayPalPayment, CashPayment
from Room import Room
from Reservation import Reservation
from RoomType import RoomType
from datetime import datetime
from HotelManagementService import RoomService, PaymentService, ReservationService, CheckInService
from RoomType import RoomType
from datetime import datetime
class Demo:
    def run():
        room_1 = RoomService().add_room(101, 2, 29.99, RoomType.SINGLE)
        room_2 = RoomService().add_room(105, 2, 49.99, RoomType.DOUBLE)

        kirtan = Guest("Kirtan", "kirtan@gadhi.com", "1112223333")
        mayur = Guest("Mayur", "mayur@email.com", "1112223333")

        credit_card = CreditCardPayment("123456789123")
        pay_pal = PayPalPayment("kirtan@gadhi.com")

        reservation_1 = ReservationService().make_reservation(room_1, datetime(2025, 6, 10), datetime(2025, 6, 12), credit_card, kirtan)
        print(reservation_1.reservation_id)
        reservation_2 = ReservationService().make_reservation(room_2, datetime(2025, 6, 10), datetime(2025, 6, 12), pay_pal, mayur)
        print(reservation_2.reservation_id)
        #CheckIn
        CheckInService().check_in(reservation_1)

if __name__ == "__main__":
    Demo.run()