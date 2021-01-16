import requests
import json

def get_questions():
    my_request = requests.get('https://opentdb.com/api.php?amount=10&type=boolean')
    json_body = my_request.json()
    return json_body['results']