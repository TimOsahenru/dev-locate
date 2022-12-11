from django.db import models
from accounts.models import Engineer


class Inbox(models.Model):
    engineer = models.ForeignKey(Engineer, null=True, on_delete=models.CASCADE, related_name='engineer')
    sender = models.ForeignKey(Engineer, null=True, on_delete=models.CASCADE, related_name='mail_sender')
    # receiver = models.ForeignKey(Engineer, null=True, on_delete=models.CASCADE, related_name="mail_receiver")
    receiver = models.ManyToManyField(Engineer, related_name="mail_receiver")
    body = models.CharField(max_length=500)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.sender.username
