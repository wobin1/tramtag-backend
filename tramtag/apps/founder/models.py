from django.db import models
from apps.startup.models import Startup
import uuid

class Founder(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    startup_id = models.ForeignKey(Startup, related_name="Founders_startup", on_delete=models.CASCADE)
    founder_first_name = models.CharField(max_length=200)
    founder_last_name = models.CharField(max_length=200)
    founder_email = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.founder_first_name} {self.founder_last_name}"