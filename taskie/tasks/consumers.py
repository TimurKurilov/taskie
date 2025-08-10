import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .history import chathistory
from asgiref.sync import sync_to_async
from tasks.models import Messages

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.task_id = self.scope['url_route']['kwargs']['task_id']
        self.room_group_name = f'chat_{self.task_id}'

        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

        message_exists = await sync_to_async(
            lambda: Messages.objects.filter(task_id=self.task_id, context="Чат начался").exists()
        )()

        if not message_exists:
            await chathistory("Чат начался", self.task_id)

            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': 'Чат начался'
                }
            )


    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        task_id = data.get('task_id', self.task_id)

        await chathistory(message, task_id)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    async def chat_message(self, event):
        await self.send(text_data=json.dumps({
            'message': event['message']
        }))
