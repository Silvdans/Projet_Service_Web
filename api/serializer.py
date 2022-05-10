from doctest import Example
from rest_framework import serializers

class MovieDetailSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=200)
    upvotes = serializers.IntegerField()
    users_voted = serializers.ListField(child=serializers.IntegerField())

    class Meta:
        pass

class MovieQueryParamsSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()

class recom_serializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    movie_id = serializers.IntegerField()

class UserUpdateQueryParamsSerializer(serializers.Serializer):
    favorites = serializers.ListField(child=serializers.IntegerField(), required=False)
    blacklist = serializers.ListField(child=serializers.IntegerField(), required=False)
    recom = recom_serializer(required=False)

class UserUpdateResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    favorites = serializers.ListField()
    blacklist = serializers.ListField()
    recom = recom_serializer()
