from django.contrib import admin

from .models import Contact, ProfilePictures


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'created_date')
    search_fields = ('name', 'email', 'created_date')
    list_per_page = 20


@admin.register(ProfilePictures)
class ProfilePicturesAdmin(admin.ModelAdmin):
    list_display = ('id', )