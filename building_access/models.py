from django.db import models


class Building(models.Model):
    """Create a model for the different buildings and their information."""

    name = models.CharField(max_length=30)
    start_time = models.TimeField(default="00:00:00")
    end_time = models.TimeField(default="23:59:59")
    building_type = models.CharField(max_length=6)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name
