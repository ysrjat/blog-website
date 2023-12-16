from django.db import models
from datetime import datetime


class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=10000000)
    created_At=models.DateTimeField(default=datetime.now, blank=True)

# Create your models here.
