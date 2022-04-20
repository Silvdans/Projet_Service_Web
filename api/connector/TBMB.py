import json
import requests
from django.conf import settings

def get_movies():
    """
    Return a list of films
    """
    url = f'https://api.themoviedb.org/3/discover/movie?api_key={settings.API_KEY}'
    response = requests.get(url)
    json_data = response.content
    raw_datas = json.loads(json_data)
    results = raw_datas["results"]
    movies = []
    for movie in results:
        film = {}
        film["id"] = movie["id"]
        film["title"] = movie["title"]
        movies.append(film)
    return movies

def get_genres():
    """
    Return a list of genres
    """
    url = f'https://api.themoviedb.org/3/genre/movie/list?api_key={settings.API_KEY}'
    response = requests.get(url)
    json_data = response.content
    raw_datas = json.loads(json_data)
    results = raw_datas["genres"]
    genres = []
    for genre in results:
        genres.append(genre["name"])
    return genres

