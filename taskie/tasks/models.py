from django.db import models
from django.contrib.auth.models import User

class Tasks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField()
    is_completed = models.BooleanField(default=False)
    taken_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='taken_tasks')

    def __str__(self):
        return self.title
