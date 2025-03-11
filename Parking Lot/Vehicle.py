from Vehicle_Type import VehicleType

class Vehicle:
    def __init__(self, liscense_plate, vehicle_type: VehicleType):
        self.liscense_plate = liscense_plate
        self.vehicle_type = vehicle_type
    
    def get_liscense_plate(self) -> str: 
        return self.liscense_plate
    
    def get_vehicle_type(self) -> VehicleType:
        return self.vehicle_type
    