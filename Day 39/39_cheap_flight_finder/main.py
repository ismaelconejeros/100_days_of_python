import requests
from pprint import pprint

class FlightSearch:
    def __init__(self, city):
        self.from_city = city
        self.endpoint = "https://tequila-api.kiwi.com/v2/search"

    def get_all(self):
        parameters = {
            "apikey": "Qw601LDY5Cxlukken-bsPuWKpy6sbJ0s",
            "fly_from" : "TLL",
            "date_from" : "01/04/2021",
            "date_to" : "05/04/2021"
        }
        my_request = requests.get(url=self.endpoint, params=parameters)
        print(my_request)
        return my_request.json()

class DataManager:
    def __init__(self, data_dict):
        self.request_data = data_dict
        self.endpoint = "https://api.sheety.co/6f67598029c8e14eed5d9716c40a4e1b/flighttracker/hoja1"
        self.headers = {"Authorization": "Bearer abcd1234"}

    def update(self):
        for i in range(len(self.request_data["data"])):
            parameters = {
                "hoja 1" : {
                    "fromCity" : self.request_data["data"][i]["cityFrom"],
                    "fromCountry" : self.request_data["data"][i]["countryFrom"]["name"],
                    "fromAirport" : self.request_data["data"][i]["flyFrom"],
                    "toCity" : self.request_data["data"][i]["cityTo"],
                    "toCountry": self.request_data["data"][i]["countryTo"]["name"],
                    "toAirport": self.request_data["data"][i]["flyTo"],
                    "price": self.request_data["data"][i]["price"],
                    "airline": self.request_data["data"][i]["airlines"][0],
                    "fromHour": self.request_data["data"][i]["local_departure"],
                    "fromUtc": self.request_data["data"][i]["utc_departure"], 
                    "toUtc": self.request_data["data"][i]["utc_departure"],
                    "airportChange": self.request_data["data"][i]["has_airport_change"],
                    "link": self.request_data["data"][i]["deep_link"]
                }
            }
            post_request = requests.post(url=self.endpoint, json=parameters, headers=self.headers)

tallinn = FlightSearch("tallinn")
get_all = tallinn.get_all()

datamanager = DataManager(get_all)
datamanager.update()