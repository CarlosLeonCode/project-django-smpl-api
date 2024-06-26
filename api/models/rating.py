from django.db import models

class Rating(models.Model):
    source = models.CharField(max_length=255)
    value = models.CharField(max_length=50)
