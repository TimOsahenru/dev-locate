from django.db import models
from django.contrib.auth.models import AbstractUser


class Message(models.Model):
    sender = models.ForeignKey("Engineer", null=True, on_delete=models.CASCADE, related_name='mail_sender')
    receiver = models.ForeignKey("Engineer", null=True, on_delete=models.CASCADE, related_name="mail_receiver")
    message = models.CharField(max_length=500)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.sender.username


class Engineer(AbstractUser):
    username = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField()
    avatar = models.ImageField(default="profile.png")
    country = models.CharField(max_length=200)
    years_of_experience = models.PositiveIntegerField(null=True, blank=True)
    tech_stack = models.CharField(null=True, blank=True, max_length=300)
    inbox = models.ForeignKey(Message, null=True, on_delete=models.CASCADE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.username


# class HiringManager(AbstractUser):
#     name = models.ForeignKey(User, on_delete=models.CASCADE)
#     # avatar =
#
#     def __str__(self):
#         return self.name
