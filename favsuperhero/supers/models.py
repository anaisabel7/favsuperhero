from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Superhero(models.Model):

    name = models.CharField(max_length=60)
    player = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
