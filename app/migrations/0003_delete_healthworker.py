# Generated by Django 3.2 on 2022-03-21 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_profile_healthworker'),
    ]

    operations = [
        migrations.DeleteModel(
            name='HealthWorker',
        ),
    ]