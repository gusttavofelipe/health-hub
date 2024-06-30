# Generated by Django 5.0.6 on 2024-06-30 17:36

import utils.base_model
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Professional",
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
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        unique=True,
                        verbose_name="UUID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created at"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated at"),
                ),
                (
                    "full_name",
                    models.CharField(max_length=255, verbose_name="Full Name"),
                ),
                (
                    "picture",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to=utils.base_model.get_upload_path,
                        verbose_name="Picture",
                    ),
                ),
                ("age", models.IntegerField(verbose_name="Age")),
                (
                    "phone_number",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="Phone Number",
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True,
                        max_length=254,
                        null=True,
                        unique=True,
                        verbose_name="E-mail",
                    ),
                ),
            ],
            options={
                "verbose_name": "Professional",
                "verbose_name_plural": "Professionals",
                "ordering": ["-created_at"],
            },
        ),
    ]
