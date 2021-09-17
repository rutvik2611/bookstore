from django.db import models
from django.contrib.auth.models import AbstractUser
from storeapp.model_managers import StoreUserManager
import datetime as dt

class User(AbstractUser):
    username = None
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=False, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = StoreUserManager()