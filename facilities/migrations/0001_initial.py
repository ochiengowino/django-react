# Generated by Django 4.2.5 on 2023-10-26 13:46

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="HealthFacilities",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=80)),
                ("healthcare", models.CharField(max_length=80)),
                ("amenity", models.CharField(max_length=80)),
                ("operatory", models.CharField(max_length=80)),
                ("geom", django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
        ),
    ]
