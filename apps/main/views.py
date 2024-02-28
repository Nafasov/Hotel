from django.shortcuts import render
from django.views.generic import View


from .models import HomeBanner, Service, AboutUs
from apps.blog.models import BlogPost, BlogNEWPost
from apps.rooms.models import Rooms, RoomComments
from .send_email import send_email


class HomeView(View):
    template_name = 'main/index.html'

    def get(self, request, *args, **kwargs):
        recipient_list = ['mirzonafasov20@gmail.com', ]
        # send_email.delay()
        send_email.apply_async((recipient_list, ))
        home_banner = HomeBanner.objects.all()
        service = Service.objects.all()
        blog_posts = BlogPost.objects.all()
        blog_new_posts = BlogNEWPost.objects.order_by('-id')[:3]
        rooms = Rooms.objects.all()
        rooms_comments = RoomComments.objects.all()[:4]
        context = {
            'home_banner': home_banner,
            'service': service,
            'blog_posts': blog_posts,
            'blog_new_posts': blog_new_posts,
            'rooms': rooms,
            'rooms_comments': rooms_comments,
        }
        return render(request, self.template_name, context)


class AboutView(View):
    template_name = 'main/about.html'

    def get(self, request, *args, **kwargs):
        about_us = AboutUs.objects.get()
        blog_new_posts = BlogNEWPost.objects.order_by('-id')[:3]
        context = {
            'about_us': about_us,
            'blog_new_posts': blog_new_posts
        }
        return render(request, self.template_name, context)

