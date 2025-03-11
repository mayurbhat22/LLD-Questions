from ParkingLevel import ParkingLevel
from typing import List

class ParkingLot:
    def __init__(self):
        self.levels : List[ParkingLevel] = []
    
    def add_level(self, level: ParkingLevel):
        self.levels.append(level)
    
    def park_vehicle(self, vehicle) -> bool:
        for level in self.levels:
            print(f"Trying to park in level {level.level}")
            if level.park_vehicle(vehicle):
                return True
        return False

    def unpark_vehicle(self, vehicle) -> bool:
        for level in self.levels:
            if level.unpark_vehicle(vehicle):
                return True
        return False

    def print_available_spots(self):
        for level in self.levels:
            print(f"Level {level.level}:")
            level.print_available_spots()
    
