from rest_framework import serializers
from storeapp import models


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = ('id', 'email', 'name')


class BookSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = models.Books
        fields = '__all__'

