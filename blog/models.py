from django.db import models

from django.contrib.auth.models import User


class Entry(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    likes = models.TextField()
    likes_count = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
