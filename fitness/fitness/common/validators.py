from django.core.exceptions import ValidationError


def validate_only_letters(value):
    for ch in value:
        if not ch.isalpha():
            raise ValidationError('Value must contain only letters')


def validate_number_cannot_be_below_zero(value):
    if value < 0:
        raise ValidationError('Number cannot be below zero')


def validate_only_letters_number_underscore(value):
    for ch in value:
        if not ch.isalpha() and not ch.isnumeric() and not ch == '_':
            raise ValidationError('Value must contain only letters, numbers and underscore')


def validate_only_letters_numbers_space(value):
    for ch in value:
        if not ch.isalpha() and not ch.isnumeric() and not ch == ' ':
            raise ValidationError('Value must contain only letters, numbers and space')
