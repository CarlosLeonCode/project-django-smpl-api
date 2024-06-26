from django.db import models
from .movie import Movie

class Rating(models.Model):
    source = models.CharField(max_length=255)
    value = models.CharField(max_length=50)
    movie = models.ForeignKey(Movie, related_name='ratings', on_delete=models.CASCADE, null=True, blank=True)
