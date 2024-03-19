from django.urls import path

from . import views

urlpatterns = [
    path('room/', views.RoomCreateView.as_view(), name = 'room-create'),
    path('room/<str:title>/', views.RoomDetailView.as_view(), name = 'room-detail'),
    path('room/<str:title>/messages/', views.MessageListCreateView.as_view(), name = 'message')
]