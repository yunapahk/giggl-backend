# Generated by Django 4.2.5 on 2023-10-14 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('podcasts', '0003_alter_podcast_youtube_video_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='podcast',
            name='podcast_title',
            field=models.CharField(default='Podcast title', max_length=200),
            preserve_default=False,
        ),
    ]
