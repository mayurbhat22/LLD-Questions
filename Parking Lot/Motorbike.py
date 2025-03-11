from Vehicle import Vehicle
from Vehicle_Type import VehicleType

class Motorbike(Vehicle):
    def __init__(self, liscense_plate: str):
        super().__init__(liscense_plate, VehicleType.MOTORBIKE)