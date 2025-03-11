from ParkingLot import ParkingLot
from Car import Car
from Truck import Truck
from Motorbike import Motorbike
from ParkingLevel import ParkingLevel
from Vehicle_Type import VehicleType


class System:
    def run():
        parking_lot = ParkingLot()

        car = Car("123")
        truck = Truck("456")
        motorbike = Motorbike("789")

        parking_lot.add_level(ParkingLevel(1, 2))
        # parking_lot.add_level(ParkingLevel(2, 2))
        parking_lot.park_vehicle(car)
        parking_lot.park_vehicle(truck)
        parking_lot.park_vehicle(motorbike)

        parking_lot.print_available_spots()

        parking_lot.unpark_vehicle(car)

        parking_lot.print_available_spots()

if __name__ == "__main__":
    System.run()
    

