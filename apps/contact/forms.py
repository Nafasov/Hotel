from django import forms

from .models import Contact
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'class': 'form-control mb-30',
            'placeholder': 'Your Name',
            'name': "message-name"

        })
        self.fields['email'].widget.attrs.update({
            'class': 'form-control mb-30',
            'placeholder': 'Your Email',
            'name': "message-email",

        })
        self.fields['message'].widget.attrs.update({
            'class': 'form-control mb-30',
            'placeholder': 'Your message',
            'name': "message"

        })


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control mb-30',
            'placeholder': 'Your Username',
            'name': "username"
        })
        self.fields['password'].widget.attrs.update({
            'class': 'form-control mb-30',
            'placeholder': 'Your Password',
            'name': "password",
        })


class UserRegisterForm(UserCreationForm):
    image = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['username', 'image', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control mb-30',
            'placeholder': 'Your Username',
            'name': "username"
        })
        self.fields['image'].widget.attrs.update({
            'class': 'form-control mb-30',
            'placeholder': 'Your image',
            'name': "image"
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control mb-30',
            'placeholder': 'Password',
            'name': "password1",
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control mb-30',
            'placeholder': 'Confirm Password',
            'name': "password2",
        })


