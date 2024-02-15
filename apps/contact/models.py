from django.db import models
from django.contrib.auth.models import User


from apps.blog.models import BaseModel


class Contact(BaseModel):
    name = models.CharField(max_length=221)
    email = models.EmailField(null=True, blank=True)
    message = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class ProfilePictures(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    picture = models.ImageField(upload_to='contact/profile', null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s photo"
