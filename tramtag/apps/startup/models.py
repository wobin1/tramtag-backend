from django.db import models
from django.utils.timezone import now
import uuid


class Startup(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    startup_name = models.CharField(max_length=200)
    startup_email = models.CharField(max_length=200, unique=True)
    startup_location = models.CharField(max_length=200)
    startup_industry = models.CharField(max_length=200)
    startup_description = models.CharField(max_length=400)
    founded_in = models.DateField(default=now)

    # def __str__(self):
    #     return startup_name

class Founders(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    startup_id = models.ForeignKey(Startup, related_name="Founders_startup", on_delete=models.CASCADE)
    founder_first_name = models.CharField(max_length=200)
    founder_last_name = models.CharField(max_length=200)
    founder_email = models.CharField(max_length=200)

    def __str__(self):
        return f"{founder_first_name} {founder_last_name}"

