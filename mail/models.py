from django.db import models
from accounts.models import Engineer


class Inbox(models.Model):
    sender = models.ForeignKey(Engineer, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.sender.username
