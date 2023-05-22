from django.core.validators import RegexValidator
from django.db import models

from cars.core.validators import validate_name_is_alpha, validate_age_gte_18, phone_number_validator
from cars.oauth_app.models import AppUser
from cloudinary import models as cloudinary_models


# Create your models here.
class Profile(models.Model):
    FIRST_NAME_MAX_LENGTH = 20
    LAST_NAME_MAX_LENGTH = 20
    PHONE_NUMBER_MAX_LENGTH = 18
    AGE_DEFAULT_VALUE = 18

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        default='',
        validators=[
            validate_name_is_alpha,
        ],
    )
    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        default='',
        validators=[
            validate_name_is_alpha,
        ],
    )
    age = models.IntegerField(
        default=AGE_DEFAULT_VALUE,
        validators=[validate_age_gte_18, ],
    )
    user = models.OneToOneField(
        AppUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    phone_number = models.CharField(
        max_length=PHONE_NUMBER_MAX_LENGTH,
        # unique=True,
        default=0,
        validators=[
            RegexValidator(
                regex=r'^(\+\d{1,3})?,?\s?\d{8,13}',
                message="Phone number must not consist of space and requires country code. eg : +3591258565",
            ),
        ],
    )

    image = cloudinary_models.CloudinaryField(
        "Image",
        overwrite=True,
        resource_type="image",
        transformation={"quality": "auto:eco"},
        default='https://res.cloudinary.com/dltjy2gzz/image/upload/v1669752042/profiles/default/profile_qmzvir.jpg',

    )

    is_banned = models.BooleanField(
        default=False,
    )
    is_activated = models.BooleanField(
        default=False
    )


    def __str__(self):
        return self.first_name


    @property
    def get_username(self):
        return self.user.username


class DeleteCode(models.Model):
    generated_code = models.IntegerField(
        null=True,
        blank=True,
    )
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, primary_key=True)
