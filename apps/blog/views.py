from django.shortcuts import render

from django.views.generic import TemplateView, ListView, DetailView, View


from .models import BlogNEWPost


class BlogView(View):
    template_name = 'blog/blog.html'

    def get(self, request, *args, **kwargs):
        blogs = BlogNEWPost.objects.order_by('id')

        context = {
            'blogs': blogs,
        }
        return render(request, self.template_name, context)


class BlogDetailView(TemplateView):
    template_name = 'blog/single-blog.html'
