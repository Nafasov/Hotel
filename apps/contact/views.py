from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, reverse
from django.views.generic import TemplateView, View
from django.contrib.auth import views as auth_views, logout

from .forms import ContactForm, UserForm


class ContactView(View):
    template_name = 'contact/contact.html'

    def get(self, request):
        form = ContactForm
        context = {
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Message sent successfully!')
            return redirect(reverse_lazy('contact:contact'))
        return redirect(reverse_lazy('contact:contact'))


class LoginView(auth_views.LoginView):
    # form = UserForm
    next_page = reverse_lazy('main:home')
    template_name = 'contact/login.html'

    def get(self, request, *args, **kwargs):
        form = UserForm()
        context = {
            'form': form
        }
        return render(request, self.template_name, context)


class RegisterView(TemplateView):
    template_name = 'contact/registration.html'


class LogoutView(View):
    template_name = 'contact/logout.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        logout(request)
        messages.success(request, 'Siz muoffiqayatli chiqdingiz!')
        return redirect(reverse_lazy('main:home'))


