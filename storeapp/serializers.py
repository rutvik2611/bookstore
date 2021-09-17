from rest_framework import serializers
from storeapp import models


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = ('id', 'email', 'name')
        #fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = models.Books
        fields = '__all__'


class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Transaction
        fields = '__all__'

