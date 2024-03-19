from django.shortcuts import render
from rest_framework import generics

from .models import Room
from .serializers import MessageSerializer, RoomSerializer


class RoomDetailView(generics.RetrieveAPIView):
    serializer_class = RoomSerializer
    lookup_field = 'title'
    queryset = Room.objects.all()

class RoomCreateView(generics.CreateAPIView):
    serializer_class = RoomSerializer

class MessageListCreateView(generics.ListCreateAPIView):
    serializer_class = MessageSerializer

    def get_queryset(self):
        room = Room.objects.get(title = self.kwargs.get('title'))
        return room.messages.all()