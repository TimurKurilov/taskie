from django.db import models
from django.contrib.auth.models import User

from upload.models import UploadModel

class Tasks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField()
    is_completed = models.BooleanField(default=False)
    in_pending = models.BooleanField(default=False)
    taken_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='taken_tasks')

    def __str__(self):
        return self.title

class Messages(models.Model):
    task = models.ForeignKey(Tasks, on_delete=models.CASCADE, related_name="messages")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    context = models.TextField(blank=True, null=True)
    uploaded_file = models.ForeignKey(UploadModel, on_delete=models.SET_NULL, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}: {self.context or (self.uploaded_file.name if self.uploaded_file else '')}"
    def __str__(self):
        return self.context
    