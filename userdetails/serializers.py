# serializers.py
from rest_framework import serializers
from .models import user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ['name', 'category', 'email', 'password']

class MarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ['name', 'mark1', 'mark2', 'mark3']
