from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, View, DetailView
from django.core.paginator import Paginator

from .models import Rooms, RoomComments, Booking
from .forms import RoomCommentsForm, BookingForm


class RoomsView(View):
    template_name = 'rooms/room.html'

    def get(self, request, *args, **kwargs):
        print(request.GET)
        rooms = Rooms.objects.all().order_by('-id')
        chick_in = request.GET.get('check_in')
        chick_out = request.GET.get('check_out')
        adults = request.GET.get('adults')
        children = request.GET.get('children')
        print(chick_in, chick_out, adults, children)
        if chick_in and chick_out:
            print(chick_in, chick_out)
            rooms = rooms.filter(~Q(datas__check_in__lte=chick_out) | ~Q(datas__check_out__gte=chick_in))
        if children or adults:
            adults = int(adults)
            children = int(children)
            rooms = rooms.filter(Q(children__gte=children))
            rooms = rooms.filter(Q(adults__gte=adults))
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
        if request.user.is_authenticated:
            check_in = request.POST.get('check_in')
            adults = request.POST.get('adults')
            children = request.POST.get('children')
            check_out = request.POST.get('check_out')
            user = request.user
            if (type(adults)) == str:
                adults = 0
            if (type(children)) == str:
                children = 0
            adults = int(adults)
            children = int(children)
            ctx = {
                'check_in': check_in,
                'adults': adults,
                'children': children,
                'check_out': check_out
            }
            print(check_in, check_out, adults, children)
            if check_in and check_out:
                Booking.objects.create(
                    author=user,
                    check_in=check_in,
                    adults=adults,
                    children=children,
                    check_out=check_out,
                    room_id=kwargs['pk'],
                    )
                messages.success(request, 'The room has been successfully booked!')
                return redirect('.')

            form = RoomCommentsForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                form.author = request.user
                form.room_id = kwargs['pk']
                form.save()
                messages.success(request, f'Your comment saved successfully!')
                return redirect('.#comment-list')
            return self.get(request, *args, **kwargs)
        messages.error(request, 'Please login first!')
        return redirect('contact:login')




