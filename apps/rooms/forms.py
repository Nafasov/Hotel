from django import forms

from .models import RoomComments, Booking


class RoomCommentsForm(forms.ModelForm):
    class Meta:
        model = RoomComments
        fields = ['room', 'author', 'comment', 'room_star1', 'room_star2', 'room_star3', 'room_star4', 'room_star5']
        exclude = ['room', 'author']

    def __init__(self, *args, **kwargs):
        super(RoomCommentsForm, self).__init__(*args, **kwargs)
        self.fields['comment'].widget.attrs.update({
            'class': 'form-control mb-30',
            'placeholder': 'Your comment',
            'name': 'Your comment'
        })
        self.fields['room_star1'].widget.attrs.update({
            'class': 'fa fa-star',
        })
        self.fields['room_star2'].widget.attrs.update({
            'class': 'fa fa-star',

        })
        self.fields['room_star3'].widget.attrs.update({
            'class': 'fa fa-star',

        })
        self.fields['room_star4'].widget.attrs.update({
            'class': 'fa fa-star',

        })
        self.fields['room_star5'].widget.attrs.update({
            'class': 'fa fa-star',

        })


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['room', 'author', 'check_out', 'check_in', 'children', 'adults']
    #     exclude = ['room', 'author']
    #
    # def __init__(self, *args, **kwargs):
    #     super(BookingForm, self).__init__(*args, **kwargs)
    #     self.fields['check_out'].widget.attrs.update({
    #         'class': 'form-control mb-30',
    #         'name': 'check_out'
    #     })
    #     self.fields['check_in'].widget.attrs.update({
    #         'class': 'form-control mb-30',
    #         'name': 'check_in'
    #     })
    #     self.fields['children'].widget.attrs.update({
    #         'class': 'form-control mb-30',
    #         'name': 'children'
    #     })
    #     self.fields['adults'].widget.attrs.update({
    #         'class': 'form-control mb-30',
    #         'name': 'adults'
    #     })
