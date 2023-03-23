from pymongo import *
import json

connection = "mongodb+srv://melih:1234@weatherapp.6zi3pge.mongodb.net/Configurations?retryWrites=true&w=majority"
client = MongoClient(connection)
db = client['WeatherApp'] # veritabanı adı
collection = db['countries_data'] # koleksiyon adı
with open('belgium_data.json') as f:
    belgium_data = json.load(f)
with open('germany_data.json') as f:
    germany_data = json.load(f)
with open('usa_data.json') as f:
    usa_data = json.load(f)

collection.insert_many(belgium_data)
collection.insert_many(germany_data)
collection.insert_many(usa_data)