from django.core.exceptions import ValidationError


def starts_with_capital_letter(value):
    if not value[0].isupper():
        raise ValidationError('Your name must start with a capital letter!')


def contains_only_letters(value):
    for ch in value:
        if not ch.isalpha():
            raise ValidationError('Plant name should contain only letters!')