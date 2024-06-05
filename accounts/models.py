from django.db import models
from django.contrib.auth.models import AbstractUser # firstanme , lastname , pass, email


class CustomUser(AbstractUser):
    # add 'age' to the model
    age = models.PositiveIntegerField(null=True, blank=True)