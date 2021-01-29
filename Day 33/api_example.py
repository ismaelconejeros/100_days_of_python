import requests
import json
import datetime

penalolen_long = -70.5248500
penalolen_lat = -33.4861900

my_request = requests.get('http://api.open-notify.org/iss-now.json')
data = my_request.json()

latitude = data['iss_position']['latitude']
longitude = data['iss_position']['longitude']

iss_position = (longitude, latitude)

print(iss_position)

time_now = datetime.datetime.now()

parameters = {
    "lat" : penalolen_lat,
    "lng" : penalolen_long,
    "date": "2021-01-29",
    "formatted": 0
}

my_request = requests.get("https://api.sunrise-sunset.org/json", params = parameters)
data = my_request.json()
sunrise = data['results']['sunrise'].split("T")[1].split(":")
sunset = data['results']['sunset'].split("T")[1].split(":")

print(time_now)
print(sunrise)
print(sunset)