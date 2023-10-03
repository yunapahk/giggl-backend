from django.db import models

# Create your models here.
class Tourdate(models.Model):
    comedians = models.CharField(max_length=200)
    tour = models.CharField(max_length=200)
    dates = models.CharField(max_length=200)
    link = models.CharField(max_length=200)