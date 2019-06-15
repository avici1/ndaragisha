from django.db import models


# Create your models here.

class LostItems(models.Model):
    owner_name = models.CharField(default="empty", max_length=120)
    owner_phone = models.CharField(default="empty", max_length=20)
    doc_name = models.CharField(default="empty", max_length=120)
    real_doc_id = models.CharField(default="empty", max_length=120)
    fake_doc_id = models.CharField(default="empty", max_length=120)
    status = models.CharField(default="Not Found", max_length=120)
    img_path = models.CharField(default="Not found", max_length=100)
    lost_desc = models.TextField(default="Empty", null=True)
    found_desc = models.TextField(default="Empty", null=True)
    found_person_name = models.CharField(default="empty", max_length=120)
    found_person_phone = models.CharField(default="empty", max_length=120)


class FoundItems(models.Model):
    img_path = models.ImageField(upload_to='image/%Y/%m/%d')
    found_desc = models.TextField()
    found_person_name = models.CharField(default="empty", max_length=120)
    found_person_phone = models.CharField(default="empty", max_length=120)


class IncomingMessage(models.Model):
    names = models.CharField(default="empty", max_length=120)
    subject = models.CharField(default="empty", max_length=120)
    email = models.CharField(default="empty", max_length=120)
    message = models.TextField(null=True)
    status = models.CharField(default="Not Responded", max_length=40)
