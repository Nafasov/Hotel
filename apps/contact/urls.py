from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views

from .forms import PasswordChangeForm1
from .views import ContactView, LoginView, LogoutView, RegisterView

app_name = 'contact'

urlpatterns = [
    path('contact/', ContactView.as_view(), name='contact'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),

    path('password/change/', auth_views.PasswordChangeView.as_view(
        form_class=PasswordChangeForm1,
        success_url=reverse_lazy("contact:change_done_password"),
        template_name='contact/password_change.html'
    ), name='change_password'),
    path('password/change/done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='contact/change_done_password.html'), name='change_done_password')
]
