from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    description = models.TextField()
    twitter_icon = models.CharField(max_length=50)
    insta_icon = models.CharField(max_length=50)
    facebook_icon = models.CharField(max_length=50)
    linkedin_icon = models.CharField(max_length=50)
    image = models.FileField(upload_to='images/',max_length=250,null=True, default=None)