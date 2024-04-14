from django.core.validators import MinLengthValidator
from django.db import models

from plant_app_revision.web.validators import starts_with_capital_letter, contains_only_letters


class Profile(models.Model):
    USERNAME_MIN_LEN = 2
    USERNAME_MAX_LEN = 10
    FIRST_NAME_MAX_LEN = 20
    LAST_NAME_MAX_LEN = 20

    username = models.CharField(
        max_length=USERNAME_MAX_LEN,
        validators=(
            MinLengthValidator(USERNAME_MIN_LEN),
        ),
        null=False,
        blank=False,
    )
    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LEN,
        validators=(
            starts_with_capital_letter,
        ),
        null=False,
        blank=False,
    )
    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LEN,
        validators=(
            starts_with_capital_letter,
        ),
        null=False,
        blank=False,
    )
    profile_picture = models.URLField(
        null=True,
        blank=True,
    )


class Plant(models.Model):
    OUTDOOR_PLANTS = 'Outdoor Plants'
    INDOOR_PLANTS = 'Indoor Plants'
    PLANT_CHOICES = (
        (OUTDOOR_PLANTS, OUTDOOR_PLANTS),
        (INDOOR_PLANTS, INDOOR_PLANTS),
    )

    TYPE_MAX_LEN = 14
    NAME_MIN_LEN = 2
    NAME_MAX_LEN = 20

    type = models.CharField(
        max_length=TYPE_MAX_LEN,
        choices=PLANT_CHOICES,
        null=False,
        blank=False,
    )
    name = models.CharField(
        max_length=NAME_MAX_LEN,
        validators=(
            MinLengthValidator(NAME_MIN_LEN),
            contains_only_letters,
        ),
        null=False,
        blank=False,
    )
    image_url = models.URLField(
        null=False,
        blank=False,
    )
    description = models.TextField(
        null=False,
        blank=False,
    )
    price = models.FloatField(
        null=False,
        blank=False,
    )