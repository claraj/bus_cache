import get_bus_locations
from datetime import datetime

while True:

    input('press enter to get bus time ')
    print('The current date/time is', datetime.now())

    locations = get_bus_locations.get_bus_locations('17940')

    print('The next bus will depart:', locations.next_bus_depart())

