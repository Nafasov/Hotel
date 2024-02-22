from django.urls import path

from .views import RoomsView, RoomDetailView

app_name = 'rooms'

urlpatterns = [
    path('', RoomsView.as_view(), name='rooms'),
    path('detail/<int:pk>/', RoomDetailView.as_view(), name='room_detail')

]