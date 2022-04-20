from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from api.connector.TBMB import get_movies, get_genres
from api.connector.database import get_collection,get_db, set_favorite

class MovieList(APIView):
    
    def get(self, request):
        """
        Return a list of discovered movies.
        """
        data = get_movies()
        db = get_db('service_web')
        print(db.list_collection_names())
        return Response(data)
    
class GenreList(APIView):
    def get(self, request):
        """
        Return a list of discovered movies.
        """
        data = get_genres()
        return Response(data)

class Favorite(APIView):
    """
    Favorite 
    """
    def post(self, request):

        data = request.data
        set_favorite(data)
        return Response(data)
        

