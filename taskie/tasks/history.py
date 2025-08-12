import os
import django
from channels.db import database_sync_to_async

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'taskie.settings')
django.setup()

from tasks.models import Messages

@database_sync_to_async
def chathistory(message, task_id, user_id):
    return Messages.objects.create(context=message, task_id=task_id, user_id=user_id)