# Generated by Django 5.0 on 2023-12-06 22:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("things", "0002_alter_thing_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="thing",
            name="description",
            field=models.TextField(
                blank=True,
                max_length=120,
                validators=[
                    django.core.validators.MaxLengthValidator(
                        limit_value=120,
                        message="Description must not have more than 120 characters",
                    )
                ],
            ),
        ),
    ]
