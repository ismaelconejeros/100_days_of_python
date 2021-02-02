import requests
from datetime import datetime

today = datetime.now().strftime("%Y%m%d")

PIXELA_ENDPOINT = "https://pixe.la/v1/users"

USER_PARAMS = {
    "token": "asdfhertynert356456gffgjsd233",
    "username": "ismael1990",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

USERNAME = USER_PARAMS["username"]
TOKEN = USER_PARAMS["token"]

# my_request = requests.post(url= PIXELA_ENDPOINT, json=USER_PARAMS)
# print(my_request.text)

PIXELA_GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
GRAPH_PARAMS = {
    "id": "graph1isma",
    "name": "Python projects isma",
    "unit": "projects",
    "type": "int",
    "color": "ajisai"
}
headers = {
    "X-USER-TOKEN": TOKEN
}
GRAPH_ID = GRAPH_PARAMS["id"]

# request = requests.post(url=PIXELA_GRAPH_ENDPOINT, json=GRAPH_PARAMS, headers=headers)
# print(request.text)

PIXELA_PIXEL_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"
PIXEL_PARAMS = {
    "date": today,
    "quantity": "1",
}

# pixel_request = requests.post(url=PIXELA_PIXEL_ENDPOINT, json=PIXEL_PARAMS, headers=headers)

PIXELA_UPDATEPIXEL_ENDPOINT = f"{PIXELA_PIXEL_ENDPOINT}/{today}"
UPDATEPIXEL_PARAMS = {
    "quantity": "5",
}

update_request = requests.put(url=PIXELA_UPDATEPIXEL_ENDPOINT, json=UPDATEPIXEL_PARAMS, headers=headers)