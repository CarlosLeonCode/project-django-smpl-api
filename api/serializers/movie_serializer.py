from rest_framework import serializers
from api.models.movie import Movie
from api.serializers.rating_serializer import RatingSerializer

class MovieSerializer(serializers.ModelSerializer):
    ratings = RatingSerializer(many=True, read_only=True)

    class Meta:
      model = Movie
      fields = '__all__'
