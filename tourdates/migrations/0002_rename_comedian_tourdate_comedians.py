# Generated by Django 4.2.5 on 2023-10-02 23:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tourdates', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tourdate',
            old_name='comedian',
            new_name='comedians',
        ),
    ]
