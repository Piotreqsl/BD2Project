# Generated by Django 3.2.12 on 2023-06-20 18:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Airplanes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
