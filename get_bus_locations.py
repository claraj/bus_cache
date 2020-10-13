import metro_transit
import cache 
from model import BusLocationList
from datetime import datetime
import time

cached_time = 60  # 60 seconds 

def get_bus_locations(stop_number):

    if cached_bus_locations_list := cache.fetch(stop_number, BusLocationList):
        print('RETURN FROM CACHE')
        return cached_bus_locations_list
    else:
        print('RETURN FROM API CALL')
        bus_locations = metro_transit.get_bus_locations(stop_number)
        bus_locations_list = BusLocationList(bus_locations, stop_number, now_plus_expiry())
        cache.add(bus_locations_list)
        return bus_locations_list


def now_plus_expiry():
    now = time.time()
    return now + cached_time



