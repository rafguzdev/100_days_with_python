import requests
from datetime import datetime
import time

my_lat = 53.121132
my_lng = 17.992970


def is_night():
    parameters = {'lat': my_lat, 'lng': my_lng, 'formatted': 0}
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data['results']['sunrise'].split('T')[1].split(':')[0])
    sunset = int(data['results']['sunset'].split('T')[1].split(':')[0])
    hour = datetime.now().hour
    return hour > sunset or hour < sunrise


def is_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    latitude = float(data['iss_position']['latitude'])
    longitude = float(data['iss_position']['longitude'])
    return my_lat - 5 <= latitude <= my_lat + 5 and my_lng - 5 <= longitude <= my_lng + 5


while True:
    if is_night():
        if is_overhead():
            print('ISS IS IN RANGE!')
    time.sleep(60)
