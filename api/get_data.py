import requests
BASE_URL = 'https://abhi091211.pythonanywhere.com'
import random

payload = {'input': random.randint(1, 20)}
response = requests.get(BASE_URL, params = payload)
json_values = response.json()
print(json_values["link"])