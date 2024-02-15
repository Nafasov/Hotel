from django.contrib import admin


from .models import (
                        BlogPost,
                        SendBlogNEW,
                        Tag,
                        BlogNEWPost,
                        ContentNewBlog,
                        CommentNewBlog,
                        BlogNewLike,
                                        )


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("id", 'author', 'title', 'created_date', )
    list_filter = ("created_date", )
    search_fields = ('title', 'author', )
    date_hierarchy = 'created_date'
    ordering = ('-id', )
    list_per_page = 10


@admin.register(SendBlogNEW)
class SendBlogNEWAdmin(admin.ModelAdmin):
    list_display = ("id", "email", 'created_date', )


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("id", 'title', 'created_date', )


class ContentNewBlogAdmin(admin.TabularInline):
    model = ContentNewBlog


class BlogNewLikeAdmin(admin.TabularInline):
    model = BlogNewLike


@admin.register(BlogNEWPost)
class BlogNEWPostAdmin(admin.ModelAdmin):
    inlines = [ContentNewBlogAdmin, BlogNewLikeAdmin]
    list_display = ("id", 'author', 'title', 'created_date', )
    list_filter = ("created_date", )
    search_fields = ('title', 'author', 'id')
    date_hierarchy = 'created_date'
    ordering = ('id', )
    list_per_page = 10


@admin.register(CommentNewBlog)
class CommentNewBlogAdmin(admin.ModelAdmin):
    list_display = ("id", 'author', 'title', 'created_date', )
    list_filter = ("created_date", )
    search_fields = ('title', 'author', )
    date_hierarchy = 'created_date'
    list_per_page = 15





