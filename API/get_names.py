import requests

import json

response = requests.get("https://api.github.com/users/mallikaravi/repos")

for data in response.json():

   print(data['name'])