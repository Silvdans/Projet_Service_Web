from rest_framework.response import Response
from rest_framework.views import APIView
from api.models import Movie, User
from api.serializer import MovieFromAPI, UserUpdateQueryParamsSerializer, UserUpdateResponseSerializer
from api.connector.TBMB import get_genres
from drf_spectacular.utils import extend_schema

from api.swagger_schemas import EXAMPLE_API_MOVIES

class MovieList(APIView):
    """Manage movies list"""
    @extend_schema(
        responses={200: MovieFromAPI},
        examples=EXAMPLE_API_MOVIES
    )   
    def get(self, request):
        """
        Return a list of discovered movies.
        """
        params = request.query_params
        data = Movie.get_movies(params)
        return Response(data)

class MovieListFavorites(APIView):
    """Manage movies list"""
    @extend_schema(
        responses={200: MovieFromAPI},
        examples=EXAMPLE_API_MOVIES
    )   
    def get(self, request, user_id : int):
        """
        Return a list of discovered movies.
        """
        data = Movie.get_favorites_movies(user_id)
        return Response(data)

class MovieDetail(APIView):
    """
    Manage recommandation
    """
    def get(self, request, movie_id : int):
        """Retrieve movie detail"""
        movie = Movie.get_movie(movie_id)
        return Response(movie)

    def put(self, request,movie_id : int):
        """Update movies informations"""
        data = request.data
        update_data = Movie.update_movie(data, movie_id)
        return Response(update_data)   

class GenreList(APIView):
    """List of genres"""
    def get(self, request):
        """
        Retrieve the list of all genres.
        """
        data = get_genres()
        return Response(data)

class UserList(APIView):
    """Manage user list"""
    def get(self, request):
        """Retrieve the list of users"""
        users = User.get_users()
        return Response(users)

class UserDetail(APIView):
    """Manage user details"""
    def get(self, request, user_id : int):
        """Retrieve the user's details"""
        user = User.get_user(user_id)
        return Response(user)

    def put(self, request, user_id: int):
        """Update user informations"""
        serializer = UserUpdateQueryParamsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        updated_user = User.update_user(user_id ,serializer.validated_data)
        response = UserUpdateResponseSerializer(data=updated_user)
        response.is_valid()
        return Response(response.data)