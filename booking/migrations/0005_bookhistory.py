# Generated by Django 4.2.5 on 2024-03-02 19:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("booking", "0004_alter_from_to_date"),
    ]

    operations = [
        migrations.CreateModel(
            name="bookHistory",
            fields=[
                (
                    "book_id",
                    models.CharField(max_length=30, primary_key=True, serialize=False),
                ),
                ("book_from", models.CharField(max_length=30)),
                ("book_to", models.CharField(max_length=30)),
                ("car", models.CharField(max_length=30)),
                ("price", models.IntegerField()),
                (
                    "username",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="booking.user"
                    ),
                ),
            ],
        ),
    ]