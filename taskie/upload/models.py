from django.db import models

class UploadModel(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='uploads/')

    def is_image(self):
        return self.file.name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp'))

    def is_video(self):
        return self.file.name.lower().endswith(('.mp4', '.avi', '.mov', '.webm'))

    def is_audio(self):
        return self.file.name.lower().endswith(('.mp3', '.wav', '.ogg'))

    def __str__(self):
        return self.name
