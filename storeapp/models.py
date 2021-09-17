from django.db import models
from django.contrib.auth.models import AbstractUser
from storeapp.model_managers import StoreUserManager
from base import base_model
import datetime as dt
# Create your models here.


class User(AbstractUser):
    username = None
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=False, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = StoreUserManager()

class Books(base_model.TimeStampMixin):
    title = models.CharField(max_length=200, null=False)
    author = models.ManyToManyField(User)
    isbn = models.CharField(max_length=13)