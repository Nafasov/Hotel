from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import TemplateView, View


from .models import BlogNEWPost, Tag, ContentNewBlog


class BlogNewView(View):
    template_name = 'blog/blog.html'

    def get(self, request, *args, **kwargs):
        blogs = BlogNEWPost.objects.order_by('-id')
        tags = Tag.objects.all()
        blog4 = blogs[:4]
        tag = request.GET.get('tag')
        if tag:
            blogs = blogs.filter(tags__title__exact=tag)
        paginator = Paginator(blogs, 2)
        page = request.GET.get('page')
        blogs = paginator.get_page(page)

        ctx = {
            'blogs': blogs,
            'tags': tags,
            'blog4': blog4
        }
        return render(request, self.template_name, ctx)


class BlogDetailView(TemplateView):
    template_name = 'blog/single-blog.html'

