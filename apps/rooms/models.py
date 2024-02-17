from django.db import models

from apps.blog.models import BaseModel


class RoomServices(BaseModel):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title


class Rooms(BaseModel):
    title = models.CharField(max_length=221)
    author = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True)
    services = models.ManyToManyField(RoomServices)
    bed = models.CharField(max_length=221)
    cost = models.CharField(max_length=25)
    size = models.CharField(max_length=25)
    adults = models.IntegerField()
    children = models.IntegerField()
    capacity = models.CharField(max_length=40)

    def __str__(self):
        return self.bed


class RoomContent(models.Model):
    content = models.TextField(null=True, blank=True)
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE, related_name='contents')
    is_check = models.BooleanField(default=False)


class RoomImages(models.Model):
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images/')


class Booking(models.Model):
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE, related_name='datas')
    author = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()
    adults = models.IntegerField()
    children = models.IntegerField()

    def __str__(self):
        return self.check_out


class RoomComments(BaseModel):
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()
    room_star1 = models.BooleanField(default=False)
    room_star2 = models.BooleanField(default=False)
    room_star3 = models.BooleanField(default=False)
    room_star4 = models.BooleanField(default=False)
    room_star5 = models.BooleanField(default=False)






