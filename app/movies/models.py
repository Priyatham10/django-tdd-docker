from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# Creating the CustomUser that's defined in AUTH_USER_MODEL in settings.py
class CustomUser(AbstractUser):
    pass