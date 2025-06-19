from Flight import Flight
class FlightSchedule:
    def __init__(self, source, destination, from_date, to_date, price, flight:Flight=None):
        self.source = source
        self.destination = destination
        self.from_date = from_date
        self.to_date = to_date
        self.price = price
        self.flight = flight
