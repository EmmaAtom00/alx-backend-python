# users/serializers.py

from rest_framework import serializers
from .models import User, Message, Conversation


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "user_id",
            "username",
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "role",
            "created_at",
        ]
        read_only_fields = ["user_id", "created_at"]

class MessageSerializer(serializers.ModelSerializer):

    sender = UserSerializer(read_only=True) # nested sender details

    class Meta:
        Model = Message
        fields = [
            "message_id",
            "conversation",
            "sender",
            "message_body",
            "sent_at",
        ]
        read_only_fields = ["message_id", "sent_at", "sender"]

class ConversationSerializer(serializers.ModelSerializer):

    participants = UserSerializer(many=True, read_only=True)
    
    class Meta:
        Model = Conversation
        fields = [
            "conversation_id",
            "participants",
            "created_at"
        ]
        read_only_fields = ["conversation_id, created_at"]