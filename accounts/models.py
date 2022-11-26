from django.db import models
from django.contrib.auth.models import AbstractUser


class Engineer(AbstractUser):
    username = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(default='little about you...')
    # avatar =
    country = models.CharField(max_length=200)
    years_of_experience = models.PositiveIntegerField(null=True, blank=True)
    tech_stack = models.CharField(null=True, blank=True, max_length=300, default='stack_one | stack_two | stack_three')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username


# class HiringManager(AbstractUser):
#     name = models.ForeignKey(User, on_delete=models.CASCADE)
#     # avatar =
#
#     def __str__(self):
#         return self.name



