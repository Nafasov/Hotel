from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, View, DetailView
from django.core.paginator import Paginator

from .models import Rooms, RoomComments
from .forms import RoomCommentsForm


class RoomsView(View):
    template_name = 'rooms/room.html'

    def get(self, request, *args, **kwargs):
        rooms = Rooms.objects.all().order_by('-id')
        chick_in = request.GET.get('check_in')
        chick_out = request.GET.get('check_out')
        adults = request.GET.get('adults')
        children = request.GET.get('children')
        print(chick_in, chick_out, adults, children)
        if chick_in or chick_out:
            print(chick_in, chick_out)
            rooms = rooms.filter(~Q(datas__check_in__lte=chick_out) |~Q(datas__check_out__gte=chick_in))
        if adults or children:
            print(adults, children)
            rooms = rooms.filter(Q(children__gte=children) or Q(adults__gte=adults))
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
        form = RoomCommentsForm()
        room = get_object_or_404(Rooms, id=kwargs['pk'])
        comments = RoomComments.objects.filter(room_id=room.id).order_by('-id')
        context = {
            'room': room,
            'form': form,
            'comments': comments,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = RoomCommentsForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.room_id = kwargs['pk']
            form.save()
            messages.success(request, f'Your comment saved successfully!')
            return redirect('.#comment-list')




