from django.db import models

# Create your models here.
class Contacts(models.Model):
    contact_name = models.CharField(max_length=50)
    contact_email = models.CharField(max_length=50)
    contact_subject = models.CharField(max_length=50)
    contact_message = models.TextField()