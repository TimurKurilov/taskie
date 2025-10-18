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
            await self.send(text_data=json.dumps({
                "message": "Чат начался!",
                "username": "Система",
            }))

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        try:
            data = json.loads(text_data)
        except json.JSONDecodeError:
            return

        message = data.get("message", "").strip()
        file_url = data.get("file_url", "")
        file_name = data.get("file_name", "")
        file_type = data.get("file_type", "")

        if not message and not file_url:
            return

        username = self.user.username if self.user.is_authenticated else "Аноним"

        content_to_save = message if message else file_url
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
        payload = {
            "username": event.get("username", ""),
        }
        
        if event.get("message"):
            payload["message"] = event["message"]
        if event.get("file_url"):
            payload["file_url"] = event["file_url"]
        if event.get("file_name"):
            payload["file_name"] = event["file_name"]
        if event.get("file_type"):
            payload["file_type"] = event["file_type"]
            
        await self.send(text_data=json.dumps(payload))