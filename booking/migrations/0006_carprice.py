# Generated by Django 4.2.5 on 2024-03-02 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("booking", "0005_bookhistory"),
    ]

    operations = [
        migrations.CreateModel(
            name="carPrice",
            fields=[
                (
                    "car",
                    models.CharField(max_length=30, primary_key=True, serialize=False),
                ),
                ("perKmPrice", models.IntegerField()),
            ],
        ),
    ]
