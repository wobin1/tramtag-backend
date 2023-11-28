from django.db import models
from django.utils.timezone import now
from django.contrib.postgres.fields import ArrayField
import uuid


class Startup(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    startup_name= models.CharField(max_length=200)
    startup_email= models.CharField(max_length=200, unique=True)
    startup_location = models.CharField(max_length=200)
    startup_industry = models.CharField(max_length=200)
    startup_description = models.CharField(max_length=400)
    startup_website_url = models.CharField(default="", max_length=200)
    startup_linkedin_profile = models.CharField(max_length=200)
    startup_phone_number = models.CharField(max_length=200)
    founded_in = models.DateField()
    founders = ArrayField(models.CharField(max_length=255), null=True, blank=True)
    additional_info = ArrayField(models.CharField(max_length=255), null=True, blank=True)
    def __str__(self):
        return f"{self.startup_name}"


