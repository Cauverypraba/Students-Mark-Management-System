import re
from rest_framework import serializers
from .models import user

CATEGORIES = ["student", "faculty"]

class UserSerializer(serializers.ModelSerializer):
    def validate_name(self, name: str):
        # Define a regular expression pattern for a valid username
        pattern = r'^[a-zA-Z\s]+$'
        
        if re.match(pattern, name):
            return name
        raise serializers.ValidationError("Enter a valid name, must contain only alphabets")

    class Meta:
        model = user
        fields = ['name', 'category', 'email', 'password']

class MarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ['name', 'mark1', 'mark2', 'mark3']
