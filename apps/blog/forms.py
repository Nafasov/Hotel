from django import forms

from .models import SendBlogNEW, CommentNewBlog


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


class CommentNewBlogForm(forms.ModelForm):
    class Meta:
        model = CommentNewBlog
        fields = ['author', 'message', ]
        exclude = ['author', ]

    def __init__(self, *args, **kwargs):
        super(CommentNewBlogForm, self).__init__(*args, **kwargs)
        self.fields['message'].widget.attrs.update({
            'class': 'form-control mb-30',
            'placeholder': "Start the discussion...",
            'name': "message",

        })