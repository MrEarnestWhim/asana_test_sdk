from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    gid = models.CharField(max_length=100, blank=True, null=True)
    name = models.TextField(max_length=255, blank=True, null=True)
