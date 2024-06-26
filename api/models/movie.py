from django.db import models
from .rating import Rating

class Movie(models.Model):
    title = models.CharField(max_length=255)
    year = models.CharField(max_length=4)
    rated = models.CharField(max_length=10)
    released = models.DateField()
    runtime = models.CharField(max_length=50)
    genre = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    writer = models.CharField(max_length=255)
    actors = models.TextField()
    plot = models.TextField()
    language = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    awards = models.TextField()
    poster = models.URLField()
    metascore = models.CharField(max_length=10)
    imdb_rating = models.CharField(max_length=10)
    imdb_votes = models.CharField(max_length=20)
    imdb_id = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    dvd = models.CharField(max_length=50, null=True, blank=True)
    box_office = models.CharField(max_length=50, null=True, blank=True)
    production = models.CharField(max_length=255, null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    response = models.CharField(max_length=10)

    # Relationships
    ratings = models.ManyToManyField(Rating)
