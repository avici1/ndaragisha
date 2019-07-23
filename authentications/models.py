from django.db import models

# Create your models here.

class ClientUsers(models.Model):
    first_name = models.CharField(max_length=120,default="empty")
    last_name = models.CharField(max_length=120, default="empty")
    phone = models.CharField(max_length=120,default="empty")
    password = models.CharField(max_length=240,default="empty")
