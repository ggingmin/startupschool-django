from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):

    name = models.CharField(max_length=10)
    gender = models.CharField(max_length=1)
    birth_date = models.DateField(auto_now=False, blank=True, null=True)
    phone_num = models.CharField(max_length=11)