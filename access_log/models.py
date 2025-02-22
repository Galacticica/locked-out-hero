from django.db import models
from login.models import User
from building_access.models import Building


class UsageLog(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)


def __str__(self):
    return f"{self.user.username} accessed {self.building.name} at {self.time}"
