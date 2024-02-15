from django.contrib import admin

from .models import (
                    RoomServices,
                    Rooms,
                    RoomContent,
                    RoomImages,
                    RoomData,
                    RoomComments,
                                    )


@admin.register(RoomServices)
class RoomsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_date')


class RoomContentAdmin(admin.TabularInline):
    model = RoomContent


class RoomImagesAdmin(admin.TabularInline):
    model = RoomImages


class RoomDataAdmin(admin.TabularInline):
    model = RoomData


@admin.register(Rooms)
class RoomAdmin(admin.ModelAdmin):
    inlines = (RoomContentAdmin, RoomImagesAdmin, RoomDataAdmin)
    list_display = ('id', 'title', 'created_date')
    search_fields = ('id', 'title')
    date_hierarchy = 'created_date'
    list_per_page = 10
    filter_horizontal = ('services', )


@admin.register(RoomComments)
class RoomCommentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'room', 'author', 'created_date')
    search_fields = ('id', 'author', 'room')
    date_hierarchy = 'created_date'
    list_per_page = 20


