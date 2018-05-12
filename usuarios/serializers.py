from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.serializers import ModelSerializer
from .models import Client

class CustomLoginSerializer(AuthTokenSerializer):
    device_token = serializers.CharField(label="token")

class ClientRegisterSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = ('username', 'email', 'password', 'first_name',
                  'last_name')
