from chat.managers import ThreadManager
from django.db import models

class TrackingModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Thread(TrackingModel):
    THREAD_TYPE = (
        ('personal', 'Personal'),
        ('group', 'Group')
    )

    name = models.CharField(max_length=50, null=True, blank=True)
    thread_type = models.CharField(max_length=15, choices=THREAD_TYPE, default='group')
    users = models.ManyToManyField('auth.User')

    objects = ThreadManager()

    def __str__(self):
        return f'{self.name}'

class ChatModel(models.Model):
    room_no = models.CharField(max_length=128)
    message = models.TextField()

class Message(TrackingModel):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    sender = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    text = models.TextField(blank=False, null=False)

    def __str__(self) -> str:
        return f'From <Thread - {self.thread}>'



