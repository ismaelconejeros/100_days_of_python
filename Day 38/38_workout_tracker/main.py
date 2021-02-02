import requests
from datetime import datetime

new_data = input("What did you do today?\n").lower()

EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
EXERCISE_PARAMS = {
    "query": new_data,
    "gender": "male",
    "weight_kg": 120,
    "height_cm":173,
    "age":30
}
headers_nutri = {
    "x-app-id": "7921cee3",
    "x-app-key": "a00e8f2ac0b310c99247e18a51228bd1",
}

my_request = requests.post(url=EXERCISE_ENDPOINT, json=EXERCISE_PARAMS, headers = headers_nutri)
data = my_request.json()

SHEETY_ENDPOINT = "https://api.sheety.co/6f67598029c8e14eed5d9716c40a4e1b/workoutTracker/hoja1"
SHEETY_PARAMS = {
	"hoja1": {
        "date" : datetime.now().strftime("%d-%m-%Y"),
        "time" : datetime.now().strftime("%H:%M"),
        "exercise" : data["exercises"][0]["name"],
        "duration" : data["exercises"][0]["duration_min"],
        "calories" : data["exercises"][0]["nf_calories"]
    }
}
headers_google = {
    "Authorization": "Bearer ajkdndsjkdfhdsdfjffjd"
}

google_post = requests.post(url=SHEETY_ENDPOINT, json=SHEETY_PARAMS, headers=headers_google)
print(google_post.text)