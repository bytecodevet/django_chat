from django.db import models


class Room(models.Model):
    title = models.CharField(max_length = 100)

class Message(models.Model):
    text = models.TextField()
    user = models.CharField(max_length = 100)
    room = models.ForeignKey(Room, on_delete = models.CASCADE, related_name = 'messages')
    date = models.DateTimeField(auto_now_add = True, blank = True)
    