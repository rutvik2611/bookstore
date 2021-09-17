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

class Transaction(base_model.TimeStampMixin):
    rented_by = models.ForeignKey(User, related_name='rented_by', on_delete=models.CASCADE)
    book = models.ForeignKey(Books, related_name='rented_book', on_delete=models.CASCADE)
    rented_on = models.DateField()
    due_date = models.DateField(null=True)
    is_returned = models.BooleanField(default=False)

    class Meta:
        ordering = ['due_date']
    
    def save(self, *args, **kwargs):
        if self.due_date is None:
            self.due_date = self.rented_on + dt.timedelta(days=7)
        super(Transaction, self).save(*args, **kwargs)


class Library(base_model.TimeStampMixin):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Books)