# Generated by Django 3.2 on 2022-03-24 02:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('health_worker', '0004_auto_20220324_0830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='healthworker',
            name='district',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='health_worker.district'),
        ),
    ]