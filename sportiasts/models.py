from django.db import models
from django.contrib.auth.models import User
from datetime import date


class EventType(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, default="Unknown")

    def __str__(self):
        return self.title
    


class Events(models.Model):
    id = models.AutoField(primary_key=True)
    eventt = models.CharField(max_length=500, default="Sportiasts Event")
    slug = models.SlugField(unique=True)
    date = models.DateField()
    time = models.TimeField(default="12:00:00")
    location = models.CharField(max_length=40)
    maps_url = models.URLField(null=True,max_length=1000)
    discord_link = models.URLField(null=True)
    EventType = models.ForeignKey(EventType, on_delete=models.CASCADE,null=True,related_name="EventType")
    organizer = models.ForeignKey(User,on_delete=models.CASCADE, null=True, related_name='Organizer',)
    player = models.ManyToManyField(to=User,related_name="players")

    def __str__(self):
        return self.eventt


    @property
    def is_today(self):
        return date.today() == self.date

    @property
    def is_due(self):
        return date.today()> self.date

    @property
    def diff(self):
        if date.today() > self.date:
            return (date.today() - self.date).days
        else:
            return (self.date - date.today()).days


