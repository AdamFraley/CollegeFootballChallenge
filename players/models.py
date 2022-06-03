from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    draft_order = models.IntegerField(default=7)
