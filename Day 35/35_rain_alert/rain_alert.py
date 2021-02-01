import requests
import os
from twilio.rest import Client

OWM_ENDPOINT = 'https://api.openweathermap.org/data/2.5/onecall?'
MY_API_KEY = '3f89bc9f9532fffb81336beee8b5d411'
parameters = {
    'lat' : 59.43829873373069,
    'lon' : 24.746360638037682,
    'units': 'metric',
    'exclude': 'current,minutely,daily',
    'appid': MY_API_KEY
}

# account_sid = os.environ['account_sid']
# auth_token = os.environ['auth_token']
# client = Client(account_sid, auth_token)


my_request = requests.get(OWM_ENDPOINT, params=parameters)
data = my_request.json()

rain_hours_nextday = [i+1 for i in range(24) if data['hourly'][i]['weather'][0]['id'] < 700]

if len(rain_hours_nextday) > 0:
    print(f"It will rain, you'll need an umbrella on hours {rain_hours_nextday}")
#     message = client.messages \
#                 .create(
#                      body=f"It will rain, you'll need an umbrella on hours {rain_hours_nextday}",
#                      from_='+12084151811',
#                      to='+569'
#                  )

#     print(message.status)