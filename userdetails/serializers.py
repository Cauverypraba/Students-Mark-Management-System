import re
from rest_framework import serializers
from .models import user

CATEGORIES = ["student", "faculty"]

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer to validate username and email address
    """
    def validate_name(self, name: str):
        # Define a regular expression pattern for a valid username
        pattern = r'^[a-zA-Z\s]+$'
        
        if re.match(pattern, name):
            return name
        raise serializers.ValidationError("Enter a valid name, must contain only alphabets")

    def validate_email(self, email: str):
        # Basic email validation logic
        if "@" not in email:
            raise serializers.ValidationError("Invalid email address. Must contain '@'.")
        
        local_part, domain_part = email.rsplit("@", 1)
        
        if "." not in domain_part or len(domain_part.split(".")[-1]) < 2:
            raise serializers.ValidationError("Invalid domain name.")
        
        if not local_part or not domain_part:
            raise serializers.ValidationError("Invalid email address format.")
        
        return email

    class Meta:
        model = user
        fields = ['name', 'category', 'email', 'password']

class MarkSerializer(serializers.ModelSerializer):
    """
    Serializer to validate student marks
    """
    class Meta:
        model = user
        fields = ['name', 'mark1', 'mark2', 'mark3']
