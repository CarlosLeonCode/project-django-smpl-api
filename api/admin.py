from django.contrib import admin
from .models import Movie, Rating

# Models register
admin.site.register(Movie)
admin.site.register(Rating)
