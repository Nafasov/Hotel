from django.db import models

from apps.blog.models import BaseModel


class RoomServices(BaseModel):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')


class Rooms(BaseModel):
    services = models.ManyToManyField(RoomServices)
    bed = models.CharField(max_length=221)
    cost = models.CharField(max_length=25)
    size = models.CharField(max_length=25)
    capacity = models.CharField(max_length=40)

    def __str__(self):
        return self.bed






