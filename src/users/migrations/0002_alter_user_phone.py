# Generated by Django 4.2.4 on 2023-09-02 13:00

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="phone",
            field=phonenumber_field.modelfields.PhoneNumberField(
                max_length=16, region=None, unique=True
            ),
        ),
    ]
