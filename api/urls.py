from xml.etree.ElementInclude import include
from django.urls import path
from rest_framework import routers

router = routers.SimpleRouter()
from . import views

urlpatterns = [
    path('movies', views.MovieList.as_view()),
    path('genres',views.GenreList.as_view()),
    path('favorite',views.Favorite.as_view())
]