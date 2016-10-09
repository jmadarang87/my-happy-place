from django.db import models
from django.utils import timezone

class Map(models.Model):
    country = models.TextField()
    date_landed = models.DateTimeField(
        blank=True, null=True)
    date_departure = models.DateTimeField(
        blank=True, null=True)



# Create your models here.
