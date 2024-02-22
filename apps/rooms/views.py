from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, View, DetailView
from django.core.paginator import Paginator

from .models import Rooms, RoomComments


class RoomsView(View):
    template_name = 'rooms/room.html'

    def get(self, request, *args, **kwargs):
        rooms = Rooms.objects.all().order_by('-id')
        paginator = Paginator(rooms, 6)
        page = request.GET.get('page')
        rooms = paginator.get_page(page)

        context = {
            'rooms': rooms,
        }
        return render(request, self.template_name, context)


class RoomDetailView(View):
    template_name = 'rooms/single-room.html'

    def get(self, request, *args, **kwargs):
        room = get_object_or_404(Rooms, id=kwargs['pk'])
        context = {
            'room': room,
        }
        return render(request, self.template_name, context)

