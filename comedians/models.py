from django.db import models

class Comedian(models.Model):
    name = models.CharField(max_length=200)
    profile_picture = models.ImageField(upload_to='comedian_pics/', null=True)
