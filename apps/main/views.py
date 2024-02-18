from django.shortcuts import render

from django.views.generic import TemplateView, ListView, DetailView, View


from .models import HomeBanner, Service
from apps.blog.models import BlogPost, BlogNEWPost
from apps.rooms.models import Rooms, RoomComments


class HomeView(View):
    template_name = 'main/index.html'

    def get(self, request, *args, **kwargs):
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


class AboutView(TemplateView):
    template_name = 'main/about.html'
