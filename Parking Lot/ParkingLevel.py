from ParkingSpot import ParkingSpot
from Vehicle import Vehicle
from typing import List
from Vehicle_Type import VehicleType
from math import ceil

class ParkingLevel:
    def __init__(self, level: int, number_of_spots: int):
        self.number_of_spots = number_of_spots
        self.level = level
        self.parking_spots : List[ParkingSpot] = self.create_parking_spots()
        print(self.parking_spots)
    
    def create_parking_spots(self) -> List[ParkingSpot]:
        parking_spots : List[ParkingSpot] = []
        vehicle_types = [ VehicleType.CAR, VehicleType.TRUCK, VehicleType.MOTORBIKE ]
        
        count = 0
        num_spot_count = 0
        while count < ceil((self.number_of_spots / 3)):
            i = 0
            while i < len(vehicle_types) and num_spot_count < self.number_of_spots:
                parking_spots.append(ParkingSpot(num_spot_count, vehicle_types[i]))
                num_spot_count += 1
                i += 1
            
            count += 1
        return parking_spots
    
    def park_vehicle(self, vehicle: Vehicle) -> bool:
        for spot in self.parking_spots:
            print(f"Trying to park in spot {spot.parking_spot_number}")
            if spot.is_available and spot.vehicle_type == vehicle.get_vehicle_type():
                spot.park_vehicle(vehicle)
                self.number_of_spots -= 1
                return True
        return False
    
    def unpark_vehicle(self, vehicle: Vehicle) -> bool:
        for spot in self.parking_spots:
            if spot.get_vehicle() == vehicle:
                spot.unpark_vehicle()
                self.number_of_spots += 1
                return True
        return False

    def print_available_spots(self) -> int:
        for spot in self.parking_spots:
            print(f"Spot {spot.parking_spot_number}: {'is available' if spot.is_available else 'is not available'}")
        