import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Custom User model extending Django's AbstractUser.
    Uses UUID as the primary key and adds additional fields.
    """
    # 1. Replace AbstractUser's default "id" instead of adding "user_id"
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # 2. AbstractUser already includes: username, first_name, last_name, email, password
    email = models.EmailField(unique=True, null=False)

    phone_number = models.CharField(max_length=25, null=True, blank=True)

    GUEST_ROLE = 'guest'
    HOST_ROLE = 'host'
    ADMIN_ROLE = 'admin'

    ROLE_CHOICES = [
        (GUEST_ROLE, 'guest'),
        (HOST_ROLE, 'host'),
        (ADMIN_ROLE, 'admin'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default=GUEST_ROLE)

    # 3. created_at should use auto_now_add=True, not auto_now
    created_at = models.DateTimeField(auto_now_add=True)

    # 4. Make email the login field
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]   # still required by Django

    def __str__(self):
        return f"{self.email} ({self.role})"


class Message(models.Model):
    """
    Message model containing sender, conversation, and message body.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sender = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='sent messages')
    message_body = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message {self.id} from {self.sender.email}"

   
class Conversation(models.Model):
    """
    Conversation model tracking which users are part of the chat.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    participants = models.ManyToManyField('users.User', on_delete=models.CASCADE, related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"conversation {self.id}"