import requests
import os
from twilio.rest import Client

appid = '********************'
lon = '18.0383'
lat = '53.1297'
url = 'https://api.openweathermap.org/data/2.5/onecall'

params = {
    'lat': lat,
    'lon': lon,
    'exclude': 'current,minutely,daily',
    'appid': appid
}
data = requests.get(url=url, params=params)
data.raise_for_status()
hourly = data.json()['hourly'][:12]
is_rain = False
for hour in hourly:
    if hour['weather'][0]['id'] < 700:
        print('Take umbrella!')
        is_rain = True
        break

twilio_sid = '*******************'
twilio_token = '*************************'
client = Client(twilio_sid, twilio_token)

if is_rain:
    message = client.messages.create(
                                  body='Hello there!, Take umbrella...',
                                  from_='+14023474766',
                                  media_url=['https://demo.twilio.com/owl.png'],
                                  to='my number'
                              )

    print(message.status)
