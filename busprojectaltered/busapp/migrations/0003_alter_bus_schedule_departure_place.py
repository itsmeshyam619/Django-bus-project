# Generated by Django 5.1.3 on 2025-04-04 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("busapp", "0002_rename_time_bus_schedule_start_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bus_schedule",
            name="departure_place",
            field=models.CharField(max_length=50),
        ),
    ]
