import json
from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from asgiref.sync import async_to_sync, sync_to_async
from channels.layers import get_channel_layer
from django.db.models import signals
from django.dispatch import receiver

from .models import Notification, Task

@database_sync_to_async
def create_notification(receiver, typeof="task_created", status="unread"):
    notification_to_create = Notification.objects.create(
        user_revoker=receiver,
        type_of_notification=typeof
    )
    print('I am here to help')
    return (notification_to_create.user_revoker.username, notification_to_create.type_of_notification)


class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        #user = self.scope["user"]
        #self.group_name = 'tasks-user-{}'.format(user.username)
        self.group_name = 'tasks'
        print(self.group_name)

        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )

        await self.accept()


    async def disconnect(self, code):
        self.group_name = 'tasks'

        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

        await self.close()

    async def receive(self, text_data):
        await self.channel_layer.group_send(
            "tasks",
            {
                "type": "task_data",
                "text": text_data,
            },
        )

    async def task_data(self, text_data):
        await self.send(json.dumps({
            'type':'websocket.send',
            'text': text_data
        }))


    
    @staticmethod
    @receiver(signals.post_save, sender=Task)
    def tasks_observer(sender, instance, **kwargs):
        layer = get_channel_layer()
        print("Database event for instance" + str(instance.task_id))
       
        group_name = 'tasks'
        async_to_sync(layer.group_send)(group_name, {
            'type': 'task_data',
            'data': {
                'task_id': instance.task_id,
                'user': instance.pk,
                'task_name': instance.task_name,
                'state': instance.state
            }
        })
        # data = {
        #     'task_id': instance.task_id,
        #     'user': instance.pk,
        #     'task_name': instance.task_name,
        #     'state': instance.state
        # }
        # layer.send({
        #     "type": "websocket.send",
        #     "data": json.dumps(data),
        # })