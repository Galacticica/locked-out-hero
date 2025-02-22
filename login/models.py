from django.contrib.auth.models import AbstractUser
from django.db import models
from building_access.models import Building


class User(AbstractUser):
    """Create a model for the different users and their information."""

    j_number = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=1, null=True, blank=True)
    dorm = models.CharField(max_length=15, null=True, blank=True)
    accessible_buildings = models.ManyToManyField(
        Building, related_name="Accessible_Buildings"
    )
    times_used = models.IntegerField(default=0)
