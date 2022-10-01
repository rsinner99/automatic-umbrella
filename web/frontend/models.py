from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    task_id = models.CharField(max_length=100)
    task_name = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=20, default="unknown")


class Notification(models.Model):
    user_sender = models.ForeignKey(
        User, 
        null=True, 
        blank=True, 
        related_name='user_sender',
        on_delete=models.CASCADE
    )
    user_revoker = models.ForeignKey(
        User, 
        null=True, 
        blank=True, 
        related_name='user_revoker',
        on_delete=models.CASCADE
    )
    status = models.CharField(max_length=264, null=True, blank=True, default="unread")
    type_of_notification = models.CharField(max_length=264, null=True, blank=True)