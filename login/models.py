from django.contrib.auth.models import AbstractUser
from django.db import models


class Users(AbstractUser):
    """Create a model for the different users and their information."""

    j_number = models.IntegerField(max_length=9)
    # username = models.CharField(max_length=15)
    # password = models.CharField(max_length=15)
    gender = models.CharField(max_length=1)
    # dorm = models.CharField(max_length=15)
    # # accessible_buildings = models.ManyToManyField(Buildings)
    # Number_of_times_used = models.IntegerField(max_length=100)
