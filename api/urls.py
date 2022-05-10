from django.urls import path
from rest_framework import routers

router = routers.SimpleRouter()
from . import views

urlpatterns = [
    path('movies/', views.MovieList.as_view()),
    path('movies/<int:movie_id>',views.MovieDetail.as_view()),
    path('genres',views.GenreList.as_view()),
    path('users',views.UserList.as_view()),
    path('users/<int:user_id>',views.UserDetail.as_view()),
]