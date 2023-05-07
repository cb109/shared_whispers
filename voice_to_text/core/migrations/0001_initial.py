# Generated by Django 4.1.3 on 2023-05-07 13:34

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AudioFile",
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
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                ("filepath", models.CharField(blank=True, default="", max_length=512)),
                ("duration", models.FloatField(default=0.0)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="AudioFileChunk",
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
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                ("filepath", models.CharField(blank=True, default="", max_length=512)),
                ("duration", models.FloatField(default=0.0)),
                ("index", models.PositiveIntegerField(default=0)),
                ("transcribed_text", models.TextField(blank=True, default="")),
                (
                    "original_parent_file",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="chunks",
                        to="core.audiofile",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
