from datetime import datetime
from cloudinary import models as cloudinary_models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from cars.ad.enums import Fuel, BodyType, Transmission
from cars.oauth_app.models import AppUser
from cars.profiles.models import Profile
from cars.vehicle.models import Car, CarModel

# Create your models here.
current_year = int(datetime.now().year)


class City(models.Model):
    CITY_MAX_LENGTH = 20
    name = models.CharField(
        max_length=CITY_MAX_LENGTH,
    )

    def __str__(self):
        return self.name


class Ad(models.Model):
    TITLE_MAX_LENGTH = 70
    YEAR_OF_MANUFACTURE_MIN = 1930
    FUEL_MAX_LENGTH = 15
    BODY_TYPE_MAX_LENGTH = 10
    TRANSMISSION_MAX_LENGTH = 10
    MODEL_MAX_LENGTH = 20

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
        null=False,
        blank=False,
        unique=True,
    )

    year_of_manufacture = models.IntegerField(
        validators=(MinValueValidator(YEAR_OF_MANUFACTURE_MIN),
                    MaxValueValidator(current_year),
                    ),

    )
    fuel = models.CharField(
        max_length=FUEL_MAX_LENGTH,
        choices=Fuel.choices(),
    )
    body_type = models.CharField(
        max_length=BODY_TYPE_MAX_LENGTH,
        choices=BodyType.choices(),
    )
    transmission = models.CharField(
        max_length=TRANSMISSION_MAX_LENGTH,
        choices=Transmission.choices(),
    )
    horse_power = models.PositiveIntegerField(

    )
    mileage = models.PositiveIntegerField(

    )
    price = models.IntegerField(

    )
    description = models.TextField(
        null=True,
        blank=True, )
    publication_date = models.DateField(
        auto_now_add=True,
    )
    car = models.ForeignKey(
        Car,
        on_delete=models.CASCADE,
    )
    model = models.ForeignKey(
        CarModel,
        on_delete=models.CASCADE,
    )
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )
    city = models.ForeignKey(
        City,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return self.title

    @property
    def get_title(self):
        return self.title

    @property
    def get_main_photo(self):
        try:
            return self.photo_set.all()[0].image.url
        except IndexError:
            return None
        # return self.photo_set.all()[0].image.url



class Bookmark(models.Model):
    ad = models.ForeignKey(
        Ad,
        on_delete=models.CASCADE,
    )
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE,
    )


class Photo(models.Model):  # TODO: RECENTLY ADDED
    image = cloudinary_models.CloudinaryField(
        "Image",
        overwrite=True,
        resource_type="image",
        transformation={"quality": "auto:eco"},
        blank=True,
        null=True,
        default='https://res.cloudinary.com/dltjy2gzz/image/upload/v1672068988/cars/default/no-image-icon-15_jm4w3b.png',
    )
    ad = models.ForeignKey(
        Ad,
        on_delete=models.CASCADE
    )
