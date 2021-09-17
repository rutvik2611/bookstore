from django.shortcuts import render
from rest_framework import viewsets

from storeapp import models, serializers

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
        This to manage user 
        creation, list, update and delete
    """
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer


class BookViewSet(viewsets.ModelViewSet):
    """
        This to manage books 
        creation, list, update and delete
    """
    queryset = models.Books.objects.all()
    serializer_class = serializers.BookSerializer