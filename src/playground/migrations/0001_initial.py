# Generated by Django 3.2.20 on 2023-07-14 11:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Covering",
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
                ("covering_name", models.CharField(max_length=150)),
                (
                    "covering_slug",
                    models.SlugField(max_length=160, unique=True),
                ),
            ],
            options={
                "default_related_name": "coverings",
            },
        ),
        migrations.CreateModel(
            name="ImagePlayground",
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
                (
                    "description_image",
                    models.CharField(blank=True, max_length=100),
                ),
                ("image", models.ImageField(upload_to="playground_image/")),
                ("main_image", models.BooleanField(default=False)),
            ],
            options={
                "default_related_name": "playground_images",
            },
        ),
        migrations.CreateModel(
            name="Inventory",
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
                ("inventory_name", models.CharField(max_length=150)),
                (
                    "inventory_price",
                    models.DecimalField(
                        decimal_places=2, default=0, max_digits=5
                    ),
                ),
            ],
            options={
                "default_related_name": "inventories",
            },
        ),
        migrations.CreateModel(
            name="Sport",
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
                ("sport_name", models.CharField(max_length=150)),
                ("sport_slug", models.SlugField(max_length=160, unique=True)),
            ],
            options={
                "default_related_name": "sports",
            },
        ),
        migrations.CreateModel(
            name="Playground",
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
                ("playground_name", models.CharField(max_length=150)),
                (
                    "playground_type",
                    models.CharField(
                        choices=[("Indoor", "Indoor"), ("Outdoor", "Outdoor")],
                        max_length=10,
                    ),
                ),
                ("size", models.CharField(max_length=50)),
                (
                    "playground_price",
                    models.DecimalField(
                        decimal_places=2, default=0, max_digits=7
                    ),
                ),
                ("address", models.CharField(max_length=150)),
                ("description", models.TextField(blank=True)),
                ("shower", models.BooleanField(default=False)),
                ("changing_rooms", models.BooleanField(default=False)),
                ("lighting", models.BooleanField(default=False)),
                ("parking", models.BooleanField(default=False)),
                ("stands", models.PositiveIntegerField(default=0)),
                (
                    "playground_slug",
                    models.SlugField(max_length=160, unique=True),
                ),
                ("draft", models.BooleanField(default=False)),
                (
                    "covering",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.SET_DEFAULT,
                        related_name="playgrounds",
                        to="playground.covering",
                    ),
                ),
            ],
            options={
                "default_related_name": "playgrounds",
            },
        ),
    ]
