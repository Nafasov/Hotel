from django.urls import path

from .views import ContactView, LoginView, LogoutView, RegisterView

app_name = 'contact'

urlpatterns = [
    path('contact/', ContactView.as_view(), name='contact'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register')

]