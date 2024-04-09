from datetime import datetime
import os 
import requests
from pymongo import MongoClient

key = 'f05952544078999252619507fc14b64f'
client = MongoClient(host = '127.0.0.1', port = 27017)
sample = client['sample']
db_collection = sample['weather']

cities = []
for city in cities:
    clean_data = {}
    data = {}
    r = requests.get(
        url="https://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(
            city, key
        )
    )
    data = r.json()

    if data:
        clean_data['weather'] = data['weather']
        clean_data['main'] = data['main']
        clean_data['time'] = datetime.now()
        clean_data['city'] = city
        db_collection.insert_one(clean_data)


for i in list(db_collection.find({"weather.main": "Clear"}, {"_id": 0, "city": 1})):
    print(i)


print(
    db_collection.count_documents(
        {
            '$and': [
                {'main.temp_min': {'$gte': 287}},
                {'main.temp_max': {'$lte': 291}},
            ]
        }
    )
)

for i in list(db_collection.aggregate([{"$group": {"_id": "$weather.main", "nb": {"$sum": 1}}}])):
    print(i)