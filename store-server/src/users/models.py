from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
