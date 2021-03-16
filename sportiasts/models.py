from django.db import models
from django.contrib.auth.models import User




class Events(models.Model):
    id = models.AutoField(primary_key=True)
    eventt = models.CharField(max_length=500, default="Sportiasts Event")
    slug = models.SlugField(unique=True)
    date = models.DateTimeField()
    location = models.CharField(max_length=40)
    organizer = models.ForeignKey(User,on_delete=models.CASCADE, null=True, related_name='Organizer')
    player = models.ManyToManyField(to=User)

    def __str__(self):
        return self.eventt
    