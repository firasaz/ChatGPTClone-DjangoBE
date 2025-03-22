from django.db import models
from chat.models import Chat


# Create your models here.
class Messages(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    message = models.TextField("message text")
    is_message_artificial = models.BooleanField(
        help_text="Is the message a user prompt or AI generated"
    )
    creation_date = models.DateTimeField("Date Created", auto_now_add=True)
    modification_date = models.DateTimeField("Date Last Modified", auto_now=True)
