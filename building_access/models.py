from django.db import models


class Buildings(models.Model):
    """Create a model for the different buildings and their information."""

    name = models.CharField(max_length=30)
    hours = models.DateTimeField()
    building_type = models.CharField(max_length=6)
    latitude = models.FloatField(max_length=100)
    longitude = models.FloatField(max_length=100)
