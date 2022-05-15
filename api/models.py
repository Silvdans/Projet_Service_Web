from django.db import models
from api.connector.TBMB import get_movies

from api.connector.database import get_favorites_movies, get_user, get_users, update_movie, update_user, get_movie


# Create your models here.

class User(models.Model):
    
    def get_users():
        return get_users()

    def get_user(user_id : int):
        return get_user(user_id)

    def update_user(user_id : int, data : dict):
        return update_user(user_id, data)

class Movie(models.Model):
    def get_movies(params : dict):
        return get_movies(params)

    def get_favorites_movies(user_id: int):
        return get_favorites_movies(user_id)
        
    def get_movie(movid_id):
        return get_movie(movid_id)
        
    def update_movie(data : dict, movie_id :int):
        return update_movie(data, movie_id)
    
