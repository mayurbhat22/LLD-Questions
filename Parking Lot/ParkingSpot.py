from Vehicle import Vehicle
from Vehicle_Type import VehicleType

class ParkingSpot:
    def __init__(self, num : int, vehicle_type = VehicleType.CAR):
        self.vehicle_type = vehicle_type
        self.vehicle = None
        self.is_available = True
        self.parking_spot_number = num
    
    def get_isavailable(self) -> bool:
        return self.is_available
    
    def get_vehicle(self) -> Vehicle:
        return self.vehicle
    
    def get_parking_spot_number(self) -> int:
        return self.parking_spot_number
    
    def park_vehicle(self, vehicle: Vehicle):
        if not self.is_available or vehicle.get_vehicle_type() != self.vehicle_type:
            print(f"Cannot park {vehicle.get_vehicle_type()} in {self.vehicle_type} spot")
            return False
        self.vehicle = vehicle
        self.is_available = False
        print(f"Parked {vehicle.get_vehicle_type()} in spot {self.parking_spot_number}")
    
    def unpark_vehicle(self):
        self.vehicle = None
        self.is_available = True
    