from pymongo import MongoClient
from django.conf import settings
from api.connector.exceptions import MovieAlreadyFavorites, MovieAlreadyRecommendedForThisUser, UserDoNotExist, UserHasAlreadyVotedException

from api.connector.TBMB import get_movie_api

HOST = settings.HOST
PORT = settings.PORT
USERNAME = settings.USERNAME
PASSWORD = settings.PASSWORD 
def get_db(db_name):
    """Get database provided"""
    client = MongoClient(host=HOST,
                         port=PORT,
                         username=USERNAME,
                         password=PASSWORD
                        )
    db = client[db_name]
    return db

def get_collection(db,collection_name):
    """Get the collection wanted"""
    return db[collection_name]

def get_users():
    """Retrieve users"""
    collection = get_collection(get_db('apidb'),'Users')
    all_users = list(collection.find({}))
    for user in all_users:
        del user['_id']
    return all_users

def get_user(user_id : int):
    """Retrive the user provided"""
    collection = get_collection(get_db('apidb'),'Users')
    user = collection.find_one({"id":user_id})
    if(not user):
        raise UserDoNotExist()
    del user['_id']
    return user

def update_user(user_id: int, data : dict):
    """Update the user with given properties"""
    collection = get_collection(get_db('apidb'),'Users')
    user = collection.find_one({"id":user_id})
    if(not user):
        raise UserDoNotExist()
    if 'favorites' in data:
        for movie in data['favorites']:
            if movie in collection.find_one({"id":user_id})['favorites']:
                raise MovieAlreadyFavorites()
            collection.update_one({"id":user_id}, {'$push': {'favorites': movie}})
    if 'blacklist' in data:
        for movie in data['blacklist']:
            if movie in collection.find_one({"id":user_id})['blacklist']:
                raise MovieAlreadyFavorites()
            collection.update_one({"id":user_id}, {'$push': {'blacklist': movie}})
    if 'recom' in data:
        recom = data['recom']
        recoms = collection.find_one({"id":user_id})['recom']
        for value in recoms:
            if value['user_id'] == recom['user_id'] and value['movie_id'] == recom['movie_id']:
                raise MovieAlreadyRecommendedForThisUser()
        collection.update_one({"id":user_id}, {'$push': {'recom': {'user_id':recom['user_id'], 'movie_id':recom['movie_id']}}})
    
    updated_user = collection.find_one({"id":user_id})
    del updated_user['_id']
    return updated_user

def get_movie(movie_id : int):
    """Retrieve the movie details with upvotes and users_voted informations"""
    collection = get_collection(get_db('apidb'),'Movies')
    movie_from_db = collection.find_one({"id": movie_id})
    movie_from_api = get_movie_api(movie_id)
    if not movie_from_db:
        collection.insert_one({"id":movie_id,"upvotes":0,"title":movie_from_api["title"],"users_voted":[]})
    else:
        fields = ['upvotes', 'users_voted']
        for key in fields:
            movie_from_api[key] = movie_from_db[key]
    return movie_from_api
    
def get_favorites_movies(user_id : int):
    favorites_list = []
    collection = get_collection(get_db('apidb'),'Users')
    favorites = collection.find_one({"id":user_id})['favorites']
    for movie in favorites:
        favorites_list.append(get_movie_api(movie))
    return favorites_list


def update_movie(data : dict, movie_id : int):
    """Update the movie with given properties"""
    collection = get_collection(get_db('apidb'),'Movies')
    movie = collection.find_one({"id":movie_id})
    if(not movie):
        new_movie = get_movie_api(movie_id)
        collection.insert_one({"id":movie_id,"upvotes":1,"title":new_movie["title"],"users_voted":[data['user_id']]})
    else:
        check_user_has_already_vote(data['user_id'],movie_id)
        collection.update_one({"id":movie_id}, {'$inc': {'upvotes': 1}, '$push': {'users_voted': data['user_id']}})
    movie_from_api = get_movie_api(movie_id)
    updated_movie = collection.find_one({"id":movie_id})
    fields = ['upvotes','users_voted']
    for key in fields:
        movie_from_api[key]= updated_movie[key]
    return movie_from_api

def check_user_has_already_vote(user_id : int, movie_id):
    """Method that check if user provided have already voted"""
    collection = get_collection(get_db('apidb'),'Movies')
    movie = collection.find_one({"id":movie_id})
    if(user_id in movie['users_voted']):
        raise UserHasAlreadyVotedException()
    return True