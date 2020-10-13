from dataclasses import dataclass
from cachable import Cachable
import json


class BusEncoder(json.JSONEncoder):
    def default(self, obj):
        # obj is a BusLocation
        return obj.__dict__   # return something JSON-serializable


@dataclass
class BusLocation():
    Actual: bool
    BlockNumber: int
    DepartureText: str
    DepartureTime: str
    Description: str
    Gate: str
    Route: int
    RouteDirection: str
    Terminal: str
    VehicleHeading: int
    VehicleLatitude: float
    VehicleLongitude: float


class BusLocationList(Cachable):

    def __init__(self, bus_location_list, identifier, expiration):
        self.bus_location_list = bus_location_list
        self.identifier = identifier
        self.expiration = expiration


    def next_bus_depart(self):
        if self.bus_location_list:
            return self.bus_location_list[0].DepartureText   # A string like "8 Min or "15:45"
            

    def to_json(self):
        return json.dumps(self.bus_location_list, cls=BusEncoder)


    @staticmethod
    def load_from_cache(json_str, identifier, expiration):
        json_list = json.loads(json_str)
        bus_list = [ BusLocation(**bus) for bus in json_list ]   # or make a JSONDecoder
        return BusLocationList(bus_list, identifier, expiration)

