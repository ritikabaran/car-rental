# Generated by Django 4.2.5 on 2024-03-02 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("booking", "0003_from_to_km"),
    ]

    operations = [
        migrations.AlterField(
            model_name="from_to",
            name="date",
            field=models.CharField(max_length=30),
        ),
    ]
