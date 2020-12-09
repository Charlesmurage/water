from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

class Business(models.Model):
    name = models.CharField(max_length=40)
    logo = models.ImageField(upload_to='logo', blank=True)
    phone = models.CharField(max_length=10)
    
