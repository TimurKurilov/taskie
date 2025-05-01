from django.db import models

class Creation(models.Model):
    email = models.CharField(max_length=100)
    username = models.CharField(max_length=20, unique=True)