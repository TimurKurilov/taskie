from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    TYPE_CHOICES = [
        ("Заказчик", "Заказчик"),
        ("Исполнитель", "Исполнитель")
    ]
    type = models.CharField(choices=TYPE_CHOICES, null=False)
    
    def __str__(self):
        return self.user.username