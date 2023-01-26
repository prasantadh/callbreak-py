import requests
from time import sleep
import os

os.system( 'cls' if os.name == 'nt' else 'clear' )

baseurl = 'http://127.0.0.1:5000/'

resp = requests.get(baseurl + '/new/prasant')
print(resp.text)

resp = requests.get(baseurl + '/status')
print(resp.text)
import json
hand = json.loads(resp.text)['data']['hand']
print(hand)
