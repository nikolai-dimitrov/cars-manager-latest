from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from cars.oauth_app.manger import AppUserManger


# Create your models here.
class AppUser(AbstractBaseUser, PermissionsMixin):
    USERNAME_MAX_LENGTH = 50
    username = models.CharField(
        max_length=USERNAME_MAX_LENGTH,
        unique=True,
    )
    email = models.EmailField(
        unique=True,
    )
    is_staff = models.BooleanField(
        default=False,
    )
    date_joined = models.DateTimeField(
        auto_now_add=True,
    )
    is_email_verified = models.BooleanField(
        default=False)

    objects = AppUserManger()
    USERNAME_FIELD = 'username'
