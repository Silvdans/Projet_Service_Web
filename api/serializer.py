from rest_framework import serializers

class MovieDetailSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=200)
    upvotes = serializers.IntegerField()
    users_voted = serializers.ListField(child=serializers.IntegerField())

class MovieFromAPI(serializers.Serializer):
    class Meta:
        example = [
        {
            "adult": False,
            "backdrop_path": "/egoyMDLqCxzjnSrWOz50uLlJWmD.jpg",
            "genre_ids": [
                28,
                878,
                35,
                10751,
                12
            ],
            "id": 675353,
            "original_language": "en",
            "original_title": "Sonic the Hedgehog 2",
            "overview": "After settling in Green Hills, Sonic is eager to prove he has what it takes to be a true hero. His test comes when Dr. Robotnik returns, this time with a new partner, Knuckles, in search for an emerald that has the power to destroy civilizations. Sonic teams up with his own sidekick, Tails, and together they embark on a globe-trotting journey to find the emerald before it falls into the wrong hands.",
            "popularity": 14361.939,
            "poster_path": "/6DrHO1jr3qVrViUO6s6kFiAGM7.jpg",
            "release_date": "2022-03-30",
            "title": "Sonic the Hedgehog 2",
            "video": False,
            "vote_average": 7.7,
            "vote_count": 1111
        },
        {
            "adult": False,
            "backdrop_path": "/5P8SmMzSNYikXpxil6BYzJ16611.jpg",
            "genre_ids": [
                80,
                9648,
                53
            ],
            "id": 414906,
            "original_language": "en",
            "original_title": "The Batman",
            "overview": "In his second year of fighting crime, Batman uncovers corruption in Gotham City that connects to his own family while facing a serial killer known as the Riddler.",
            "popularity": 5400.092,
            "poster_path": "/74xTEgt7R36Fpooo50r9T25onhq.jpg",
            "release_date": "2022-03-01",
            "title": "The Batman",
            "video": False,
            "vote_average": 7.8,
            "vote_count": 4379
        },
        {
            "adult": False,
            "backdrop_path": "/aEGiJJP91HsKVTEPy1HhmN0wRLm.jpg",
            "genre_ids": [
                28,
                12
            ],
            "id": 335787,
            "original_language": "en",
            "original_title": "Uncharted",
            "overview": "A young street-smart, Nathan Drake and his wisecracking partner Victor “Sully” Sullivan embark on a dangerous pursuit of “the greatest treasure never found” while also tracking clues that may lead to Nathan’s long-lost brother.",
            "popularity": 5195.721,
            "poster_path": "/tlZpSxYuBRoVJBOpUrPdQe9FmFq.jpg",
            "release_date": "2022-02-10",
            "title": "Uncharted",
            "video": False,
            "vote_average": 7.2,
            "vote_count": 1774
        },
        {
            "adult": False,
            "backdrop_path": "/AdyJH8kDm8xT8IKTlgpEC15ny4u.jpg",
            "genre_ids": [
                14,
                28,
                12
            ],
            "id": 453395,
            "original_language": "en",
            "original_title": "Doctor Strange in the Multiverse of Madness",
            "overview": "Doctor Strange, with the help of mystical allies both old and new, traverses the mind-bending and dangerous alternate realities of the Multiverse to confront a mysterious new adversary.",
            "popularity": 5846.845,
            "poster_path": "/wRnbWt44nKjsFPrqSmwYki5vZtF.jpg",
            "release_date": "2022-05-04",
            "title": "Doctor Strange in the Multiverse of Madness",
            "video": False,
            "vote_average": 7.5,
            "vote_count": 1048
        },
        {
            "adult": False,
            "backdrop_path": "/fEe5fe82qHzjO4yej0o79etqsWV.jpg",
            "genre_ids": [
                16,
                35,
                28,
                10751,
                80
            ],
            "id": 629542,
            "original_language": "en",
            "original_title": "The Bad Guys",
            "overview": "When the infamous Bad Guys are finally caught after years of countless heists and being the world’s most-wanted villains, Mr. Wolf brokers a deal to save them all from prison.",
            "popularity": 5100.406,
            "poster_path": "/7qop80YfuO0BwJa1uXk1DXUUEwv.jpg",
            "release_date": "2022-03-17",
            "title": "The Bad Guys",
            "video": False,
            "vote_average": 7.7,
            "vote_count": 287
        },
    ]
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
