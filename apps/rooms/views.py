from django.shortcuts import render


from django.views.generic import TemplateView, DetailView


class RoomsView(TemplateView):
    template_name = 'rooms/room.html'


class RoomDetailView(TemplateView):
    template_name = 'rooms/single-room.html'
