import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .history import chathistory

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.task_id = self.scope["url_route"]["kwargs"]["task_id"]
        self.room_group_name = f"chat_{self.task_id}"

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        try:
            data = json.loads(text_data)
            message = data.get("message")
            file_url = data.get("file_url")
            file_name = data.get("file_name")
            file_type = data.get("file_type")

            user = self.scope["user"] if self.scope["user"].is_authenticated else None
            username = self.scope["user"].username if self.scope["user"].is_authenticated else "Аноним"

            if not message and not file_url:
                return

            if message:
                await chathistory(message, self.task_id, user)

            if file_url:
                file_message = f"[Файл: {file_name}]"
                await chathistory(file_message, self.task_id, user)

            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    "type": "chat_message",
                    "message": message,
                    "username": username,
                    "file_url": file_url,
                    "file_name": file_name,
                    "file_type": file_type,
                }
            )

        except Exception as e:
            print(f"Error in receive: {e}")

    async def chat_message(self, event):
        await self.send(text_data=json.dumps({
            "message": event.get("message"),
            "username": event.get("username"),
            "file_url": event.get("file_url"),
            "file_name": event.get("file_name"),
            "file_type": event.get("file_type"),
        }))
