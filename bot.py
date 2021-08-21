import websocket
import json
import config
import requests

API_KEY = config.API_KEY
SECRET_KEY = config.SECRET_KEY
BASE_URL = config.BASE_URL
HEADERS = {'APCA-PAPER-API-KEY-ID': API_KEY, 'APCA-PAPER-API-SECRET-KEY': SECRET_KEY}

ACCOUNT_URL = "{}/v2/account".format(BASE_URL)
r = requests.get(ACCOUNT_URL, HEADERS)
print(r.content)