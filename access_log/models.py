from django.db import models
from login.models import User
from building_access.models import Building
from django.utils import timezone


class UsageLog(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.time:
            self.time = timezone.localtime()
        super().save(*args, **kwargs)

    def __str__(self):
        local_time = self.time - timezone.timedelta(hours=6)
        formatted_time = local_time.strftime("%Y-%m-%d %H:%M:%S")
        return f"{self.user.username} accessed {self.building.name} at {formatted_time}"
