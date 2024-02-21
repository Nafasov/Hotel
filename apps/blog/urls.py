from django.urls import path

from .views import BlogNewView, BlogDetailView

app_name = 'blog'

urlpatterns = [
    path('', BlogNewView.as_view(), name='blog'),
    path('detail/<slug:slug>/', BlogDetailView.as_view(), name='single-blog')

]