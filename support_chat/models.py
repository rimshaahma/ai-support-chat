from django.db import models

class ChatMessage(models.Model):
    user_name = models.CharField(max_length=255)  # Added this line
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_name}: {self.message[:50]}"  # Show first 50 chars in admin
