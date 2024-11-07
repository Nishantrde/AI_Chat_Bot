# api/serializers.py

from rest_framework import serializers
from .models import User, Chat

# For return User feilds 
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'tokens']

# For returning Chat feilds
class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ['id', 'user', 'message', 'response', 'timestamp']
