# Generated by Django 4.2.5 on 2024-03-02 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("booking", "0002_from_to"),
    ]

    operations = [
        migrations.AddField(
            model_name="from_to",
            name="km",
            field=models.IntegerField(default=0),
        ),
    ]