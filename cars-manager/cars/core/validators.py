from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


def validate_name_is_alpha(value):
    if not value.isalpha():
        raise ValidationError('Name must contain only letters.')


def validate_age_gte_18(value):
    if value < 18:
        raise ValidationError('Age must be more than 18')


phone_number_validator = RegexValidator(
    regex=r'^(\+\d{1,3})?,?\s?\d{8,13}',
    message="Phone number must not consist of space and requires country code. eg : +3591258565"
)
