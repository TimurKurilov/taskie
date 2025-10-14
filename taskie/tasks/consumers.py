import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from tasks.models import Messages
from .history import chathistory


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope["user"]
        self.task_id = self.scope["url_route"]["kwargs"]["task_id"]
        self.room_group_name = f"chat_{self.task_id}"

        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

        message_exists = await sync_to_async(
            lambda: Messages.objects.filter(task_id=self.task_id, context="Чат начался").exists()
        )()
        
        if not message_exists:
            await chathistory("Чат начался", self.task_id, self.user.id)
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    "type": "chat_message",
                    "message": "Чат начался!",
                    "username": "Система",
                    "file_url": None,
                    "file_name": None,
                    "file_type": None,
                },
            )

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data.get("message")
        file_url = data.get("file_url")
        file_name = data.get("file_name")
        file_type = data.get("file_type")

        if not message and not file_url:
            return

        username = self.user.username if self.user.is_authenticated else "Аноним"

        content_to_save = message if message else file_url or "[Файл]"
        await chathistory(content_to_save, self.task_id, self.user.id)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat_message",
                "message": message,
                "username": username,
                "file_url": file_url,
                "file_name": file_name,
                "file_type": file_type,
            },
        )

    async def chat_message(self, event):
        await self.send(text_data=json.dumps({
            "message": event.get("message"),
            "username": event.get("username"),
            "file_url": event.get("file_url"),
            "file_name": event.get("file_name"),
            "file_type": event.get("file_type"),
        }))
