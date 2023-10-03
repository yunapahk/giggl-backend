from django.db import models

# Create your models here.
class Bit(models.Model):
    comedian = models.CharField(max_length=200)
    description = models.CharField(max_length=200)