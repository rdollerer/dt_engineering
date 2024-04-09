from datetime import datetime
import os 
import requests
from pymongo import MongoClient

KEY = 'f05952544078999252619507fc14b64f'
CITY = "COURBEVOIE"

r = requests.get(
    url="https://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(
        CITY, KEY
    )
)

data = r.json()

clean_data = {}
keys_to_extract = ["weather", "main"]

for key in keys_to_extract:
    clean_data[key] = data[key]

clean_data['time'] = datetime.now()
clean_data['city'] = CITY

client = MongoClient(host = '127.0.0.1', port = 27017)
sample = client['sample']
db_collection = sample.create_collection(name = 'weather')
db_collection.insert_one(clean_data)