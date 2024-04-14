# Generated by Django 3.2.25 on 2024-04-13 08:40

import django.core.validators
from django.db import migrations, models
import plant_app_revision.web.validators


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_plant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='name',
            field=models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(2), plant_app_revision.web.validators.contains_only_letters]),
        ),
    ]
