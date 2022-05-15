from drf_spectacular.utils import  OpenApiExample

from api.serializer import MovieFromAPI
EXAMPLE_API_MOVIES = [
    OpenApiExample(
        name="a",
        status_codes=['200'],
        description='Movies from api',
        value=MovieFromAPI.Meta.example
    ),
]