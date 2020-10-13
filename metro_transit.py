import requests
from model import BusLocation


def get_bus_locations(stop_number):
    url = f'https://svc.metrotransit.org/NexTrip/{stop_number}?format=json'
    response = requests.get(url)
    data = response.json()
    locations = [ BusLocation(**bus) for bus in data ]
    return locations
