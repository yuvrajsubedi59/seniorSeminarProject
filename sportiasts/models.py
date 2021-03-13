from django.db import models

# Create your models here.

class Player(models.Model):
    username = models.CharField(unique=true , max_length=200);
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    dateob = models.DateField()
    home_place = models.ForeignKey(verbose_name='Home Place' related_name='Player')

class Location(models.Model):
    latitude = models.PositiveIntegerField()
    longitude = models.PositiveIntegerField()
    place_name = models.CharField(max_length=200)
    country_name = models.CharField(max_length=200)
    zone_name = models.CharField(max_length=200)
    postal_code = models.IntegerField()