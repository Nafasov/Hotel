from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.core.paginator import Paginator
from django.views.generic import TemplateView, View
from django.urls import reverse_lazy


from .models import BlogNEWPost, Tag, SendBlogNEW, CommentNewBlog
from .forms import SendBlogNEWForm, CommentNewBlogForm


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


class BlogDetailView(View):
    template_name = 'blog/single-blog.html'

    def get(self, request, *args, **kwargs):
        form = CommentNewBlogForm()
        blog = get_object_or_404(BlogNEWPost, slug=kwargs['slug'])
        blogs = BlogNEWPost.objects.order_by('-id')[:4]
        tags = Tag.objects.all()
        comments = CommentNewBlog.objects.filter(blog_post_id=blog.id, top_level_comment_id__isnull=True).order_by('-id')
        context = {
            'blog': blog,
            'blogs': blogs,
            'tags': tags,
            'comments': comments,
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, 'You should login first!')
            return redirect('contact:login')
        blog = get_object_or_404(BlogNEWPost, slug=kwargs['slug'])
        form = CommentNewBlogForm(request.POST)
        cid = request.GET.get('cid')
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.blog_post_id = blog.id
            form.parent_id = cid
            form.save()
            messages.success(request, 'Comment sent successfully!')
            return redirect('.#comment-list')

        return self.get(request, *args, **kwargs)

