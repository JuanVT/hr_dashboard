from django.contrib.auth.models import AbstractUser
from django.db import models


class HRUser(AbstractUser):

    bio = models.TextField(max_length=700, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
