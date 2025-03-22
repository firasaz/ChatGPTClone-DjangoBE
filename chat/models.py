from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    creation_date = models.DateTimeField("Date Created", auto_now_add=True)
    modification_date = models.DateTimeField("Date Last Modified", auto_now=True)
