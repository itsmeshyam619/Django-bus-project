# Generated by Django 4.0.3 on 2025-04-24 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('busapp', '0004_alter_bus_schedule_departure_place_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bus_schedule',
            name='available_seats',
            field=models.IntegerField(default=40),
        ),
    ]
