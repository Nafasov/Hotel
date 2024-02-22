from django import forms

from .models import SendBlogNEW


class SendBlogNEWForm(forms.ModelForm):
    class Meta:
        model = SendBlogNEW
        fields = ['email']

    def __init__(self, *args, **kwargs):
        super(SendBlogNEWForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': "Enter your email...",
            'name': "nl-email",
        })
