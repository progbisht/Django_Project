from django.db import models

# Create your models here.
class About(models.Model):
    heading = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.TextField()
