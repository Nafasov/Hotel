from django.urls import path

from .views import BlogNewView, BlogDetailView, BlogDetail

app_name = 'blog'

urlpatterns = [
    path('', BlogNewView.as_view(), name='blog'),
    path('detail/<slug:slug>/', BlogDetailView.as_view(), name='single-blog'),
    path('detail-blog/<int:pk>/', BlogDetail.as_view(), name='detail')
]