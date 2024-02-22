from django.shortcuts import render, redirect, reverse
from django.core.paginator import Paginator
from django.views.generic import TemplateView, View
from django.urls import reverse_lazy


from .models import BlogNEWPost, Tag, ContentNewBlog, SendBlogNEW
from .forms import SendBlogNEWForm


def email_new(email):
    SendBlogNEW.objects.create(email=email)


class BlogNewView(View):
    template_name = 'blog/blog.html'

    def get(self, request, *args, **kwargs):
        form = SendBlogNEWForm()
        blogs = BlogNEWPost.objects.order_by('-id')
        tags = Tag.objects.all()
        blog4 = blogs[:4]
        tag = request.GET.get('tag')
        if tag:
            blogs = blogs.filter(tags__title__exact=tag)
        paginator = Paginator(blogs, 6)
        page = request.GET.get('page')
        blogs = paginator.get_page(page)

        ctx = {
            'blogs': blogs,
            'tags': tags,
            'blog4': blog4,
            'form': form,
        }
        return render(request, self.template_name, ctx)

    def post(self, request, *args, **kwargs):
        form = SendBlogNEWForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('blog:blog'))


class BlogDetailView(TemplateView):
    template_name = 'blog/single-blog.html'

