from django.db import models

class Comedian(models.Model):
    name = models.CharField(max_length=200)
    profile_picture = models.TextField()
