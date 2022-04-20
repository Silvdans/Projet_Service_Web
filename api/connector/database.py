from pymongo import MongoClient
from django.conf import settings

HOST = settings.HOST
PORT = settings.PORT
USERNAME = settings.USERNAME
PASSWORD = settings.PASSWORD 
def get_db(db_name):
    client = MongoClient(host=HOST,
                         port=PORT,
                         username=USERNAME,
                         password=PASSWORD
                        )
    db = client[db_name]
    return db

def get_collection(db,collection_name):
    return db[collection_name]
    
def set_favorite(data : dict):
    collection = get_collection(get_db('apidb'),'Users')
    
    user = collection.find_one({"id":data["id"]})
    favorites = user["favorites"]
    for item in data["favorites"]:
        favorites.append(item)
    result = collection.update_one({"id":data["id"]}, {'$set':{'favorite':favorites}})
    return result
    


