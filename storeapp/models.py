from django.db import models
from django.contrib.auth.models import AbstractUser
from storeapp.model_managers import StoreUserManager
# Create your models here.


class User(AbstractUser):
    username = None
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=False, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = StoreUserManager()