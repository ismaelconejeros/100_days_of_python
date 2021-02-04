import pandas as pd
import requests
from datetime import datetime

today = datetime.now().strftime("%d/%m/%Y")

class App:
    def __init__(self):
        self.from_city = input("City of origin? (ex: SCL) \n")
        self.date_from = input("Date of init? (ex: 01/06/2021) \n")
        self.date_to = input("Date max? (ex: 31/12/2021) \n")
        self.endpoint_flights = "https://tequila-api.kiwi.com/v2/search"
        self.request_data = {}
        self.df = ""
        self.min_df = ""

    def get_data(self):
        parameters = {
            "apikey": "Qw601LDY5Cxlukken-bsPuWKpy6sbJ0s",
            "fly_from" : self.from_city,
            "date_from" : self.date_from,
            "date_to" : self.date_to
        }
        my_request = requests.get(url=self.endpoint_flights, params=parameters)
        request_data = my_request.json()
        print(my_request)
        self.request_data = request_data
        self.build_df(self.request_data)

    def build_df(self, request_data):
        dict_df = {
            "fromCity" : [request_data["data"][i]["cityFrom"] for i in range(len(self.request_data["data"]))],
            "fromCountry" : [request_data["data"][i]["countryFrom"]["name"] for i in range(len(self.request_data["data"]))],
            "fromAirport" : [request_data["data"][i]["flyFrom"] for i in range(len(self.request_data["data"]))],
            "toCity" : [request_data["data"][i]["cityTo"] for i in range(len(self.request_data["data"]))],
            "toCountry": [request_data["data"][i]["countryTo"]["name"] for i in range(len(self.request_data["data"]))],
            "toAirport": [request_data["data"][i]["flyTo"] for i in range(len(self.request_data["data"]))],
            "price": [request_data["data"][i]["price"] for i in range(len(self.request_data["data"]))],
            "airline": [request_data["data"][i]["airlines"][0] for i in range(len(self.request_data["data"]))],
            "fromHour": [request_data["data"][i]["local_departure"] for i in range(len(self.request_data["data"]))],
            "fromUtc": [request_data["data"][i]["utc_departure"] for i in range(len(self.request_data["data"]))], 
            "toUtc": [request_data["data"][i]["utc_departure"] for i in range(len(self.request_data["data"]))],
            "airportChange": [request_data["data"][i]["has_airport_change"] for i in range(len(self.request_data["data"]))],
            "link": [request_data["data"][i]["deep_link"] for i in range(len(self.request_data["data"]))]
        }
        self.df = pd.DataFrame(dict_df)
        self.df.to_csv(f"{self.from_city}_all_data.csv", mode = "w")

    def cheap_per_city(self):
        self.min_df = self.df.iloc[self.df.groupby("toCity").agg(min_ = ("price", lambda data: data.idxmin())).min_]
        self.min_df.to_csv(f"{self.from_city}_cheap_data.csv", mode = "w")