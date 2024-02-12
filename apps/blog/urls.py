from django.urls import path

from .views import BlogView, BlogDetailView

app_name = 'blog'

urlpatterns = [
    path('', BlogView.as_view(), name='blog'),
    path('detail/', BlogDetailView.as_view(), name='blog-detail')

]