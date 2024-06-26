from rest_framework import viewsets
from api.models.rating import Rating
from api.serializers.rating_serializer import RatingSerializer

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
