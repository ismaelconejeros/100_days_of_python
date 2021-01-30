import requests
import datetime as dt
import smtplib
import time

MY_LATITUDE = -33.4861900
MY_LONGITUDE = -70.5248500
GMT = -3
now = dt.datetime.now()

ISS_API = "http://api.open-notify.org/iss-now.json"
SUN_API = "https://api.sunrise-sunset.org/json"

SUN_API_PARAMS = {
    "lat" : MY_LATITUDE,
    "lng" : MY_LONGITUDE,
    "formatted": 0
}

#...........FUNCTIONS
def is_night():
    night_thisnight = [i for i in range(sunset_hour, 24)]
    night_next_morning = [i for i in range(sunrise_hour+1)]
    night_hours = night_thisnight + night_next_morning
    if my_hour in night_hours:
        return True

def is_near():
    lat_dif = iss_lat - MY_LATITUDE
    lng_dif = iss_lng - MY_LONGITUDE
    if -5 < lat_dif < 5 and -5 < lng_dif < 5:
        return True

def send_mail():
    my_email = "test.for.smtplib90@gmail.com"
    my_password = "smtplibtest01"
    to_adress = "isma.conejeros@gmail.com"
    msg_subject = "ISS is near"
    msg_body = "Go outside and look up"
    my_msg = f"Subject: {msg_subject}\n\n{msg_body}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs=to_adress, 
            msg=my_msg)

#.......API's
#ISS
my_request = requests.get(ISS_API)
iss_req = my_request.json()
iss_lat = float(iss_req['iss_position']['latitude'])
iss_lng = float(iss_req['iss_position']['longitude'])

#......MY PLACE
my_request = requests.get(SUN_API, params = SUN_API_PARAMS)
sun_req = my_request.json()
sunrise = sun_req['results']['sunrise']
sunset = sun_req['results']['sunset']

#........CONVERT TIME
my_hour = now.hour
my_min = now.min

sunrise_list = sunrise.split("T")[1].split(":")
sunrise_hour = int(sunrise.split("T")[1].split(":")[0]) + GMT

sunset_list = sunset.split("T")[1].split(":")
sunset_hour = int(sunset.split("T")[1].split(":")[0]) + GMT

if is_night() and is_near():
    send_mail()


