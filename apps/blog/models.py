from django.db import models
from django.utils import timezone
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from ckeditor.fields import RichTextField


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class BlogPost(BaseModel):
    author = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=221)
    image = models.ImageField(upload_to='blog/post')
    description = models.TextField()


class SendBlogNEW(BaseModel):
    email = models.EmailField()


class Tag(BaseModel):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class BlogNEWPost(BaseModel):
    author = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    image = models.ImageField(upload_to='blog/new')
    tags = models.ManyToManyField(Tag)


class ContentNewBlog(BaseModel):
    blog_post = models.ForeignKey(BlogNEWPost, on_delete=models.CASCADE, related_name='contents', null=True)
    content = models.TextField()
    is_quote = models.BooleanField(default=False)


class CommentNewBlog(BaseModel):
    blog_post = models.ForeignKey(BlogNEWPost, on_delete=models.CASCADE, related_name='comments', null=True)
    author = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True)
    message = models.TextField()
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, related_name="blog_children")
    top_level_comment_id = models.IntegerField(null=True, blank=True)

    def blog_children(self):
        model = self.__class__
        return model.objects.filter(top_level_comment_id=self.id)


class BlogNewLike(BaseModel):
    blog_post = models.ForeignKey(BlogNEWPost, on_delete=models.CASCADE, related_name='likes', null=True)
    author = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True)


@receiver(pre_save, sender=CommentNewBlog)
def comment_pre_save(sender, instance, **kwargs):
    if instance.parent:
        if not instance.parent.top_level_comment_id:
            instance.parent.top_level_comment_id = instance.parent.id
        else:
            instance.top_level_comment_id = instance.parent.top_level_comment_id


@receiver(pre_save, sender=BlogNEWPost)
def blog_post_pre_save(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title + ' - ' + str(timezone.now().date()))


