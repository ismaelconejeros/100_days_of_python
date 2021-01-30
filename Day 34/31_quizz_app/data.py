import requests
import random

parameters = {
    'amount': 10,
    'type': 'boolean'
}

my_request = requests.get('https://opentdb.com/api.php', params = parameters)
data = my_request.json()
question_data = data['results']