from rest_framework import viewsets
from api.models.movie import Movie
from api.serializers.movie_serializer import MovieSerializer

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
