from django.db import models

class Podcast(models.Model):
    name = models.CharField(max_length=200)
    comedians = models.CharField(max_length=200)
    podcast_title = models.CharField(max_length=200)
    youtube_video_id = models.CharField(max_length=80, blank=True, null=True) # new field
