# Generated by Django 3.2 on 2022-03-22 06:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('health_worker', '0002_auto_20220321_2141'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='healthworker',
            options={'permissions': (('can_crud_for_healthworkers', 'To perform crud operations for health workers'),)},
        ),
    ]
