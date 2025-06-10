from RoomType import RoomType

class Room:
    def __init__(self, room_number, capacity_of_guests, price_per_day, room_type: RoomType):
        self.room_number = room_number
        self.capacity_of_guests = capacity_of_guests
        self.price_per_day = price_per_day
        self.room_type = room_type
        self.is_available = True
    
    def get_room_number(self):
        return self.room_number

    def get_capacity(self):
        return self.capacity_of_guests

    def get_room_type(self):
        return self.room_type