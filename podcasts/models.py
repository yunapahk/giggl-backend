from django.db import models

# Create your models here.
class Podcast(models.Model):
    name = models.CharField(max_length=200)
    comedians = models.CharField(max_length=200)