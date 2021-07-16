import requests
import os
from twilio.rest import Client

appid = '4e14df082f831b3e6b6c7158fb648445'
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

twilio_sid = 'AC7b2eef5ad5e82d670439c2fe4b6f9cb6'
twilio_token = 'b2c63883764a8aed544f2b741e51d930'
client = Client(twilio_sid, twilio_token)

if is_rain:
    message = client.messages.create(
                                  body='Hello there!, Take umbrella...',
                                  from_='+14023474766',
                                  media_url=['https://demo.twilio.com/owl.png'],
                                  to='+48 783 044 067'
                              )

    print(message.status)
