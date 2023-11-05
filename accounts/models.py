from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = models.EmailField(blank=False, help_text='Input your email.',)


    def __str__(self):
        return self.username
