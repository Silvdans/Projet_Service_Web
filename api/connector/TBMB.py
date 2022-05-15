import json
import requests
from django.conf import settings
def get_movie_api(id : int):
    """Retrieve wanted movie from TBMB api"""
    url = f'https://api.themoviedb.org/3/movie/{id}?api_key={settings.API_KEY}'
    movie = json.loads(requests.get(url).content)
    return movie

def get_movies(params : dict):
    """
    Return a list of films from TBMB api
    """
    if('genres' in params):
        genres = params['genres'].split(',')
        query_string = ""
        for genre in genres:
            query_string += genre + '&'
        url = f'https://api.themoviedb.org/3/discover/movie?with_genres={query_string}api_key={settings.API_KEY}'
    else:
        url = f'https://api.themoviedb.org/3/discover/movie?api_key={settings.API_KEY}'
            
    response = requests.get(url)
    json_data = response.content
    raw_datas = json.loads(json_data)
    results = raw_datas["results"]
    movies = []
    for movie in results:
        movies.append(movie)
    return movies

def get_genres():
    """
    Return a list of genres from TBMB api
    """
    url = f'https://api.themoviedb.org/3/genre/movie/list?api_key={settings.API_KEY}'
    response = requests.get(url)
    json_data = response.content
    raw_datas = json.loads(json_data)
    results = raw_datas["genres"]
    return results

