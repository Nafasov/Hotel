from django.shortcuts import render

from django.views.generic import TemplateView


class ContactView(TemplateView):
    template_name = 'contact/contact.html'


class LoginView(TemplateView):
    template_name = 'contact/login.html'


class RegisterView(TemplateView):
    template_name = 'contact/registration.html'


class LogoutView(TemplateView):
    template_name = 'contact/logout.html'
