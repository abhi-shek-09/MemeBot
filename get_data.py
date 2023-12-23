import requests
BASE_URL = 'https://abhi091211.pythonanywhere.com'
import random

def send_link():
    payload = {'input': random.randint(1, 20)}
    response = requests.get(BASE_URL, params = payload)
    json_values = response.json()
    return json_values["link"]