from django.db import models



class Car(models.Model):
    MAKE_MAX_LENGTH = 30
    make = models.CharField(
        max_length=MAKE_MAX_LENGTH,

    )

    def __str__(self):
        return self.make


class CarModel(models.Model):
    MODEL_MAX_LENGTH = 20
    model = models.CharField(
        max_length=MODEL_MAX_LENGTH,
    )
    make = models.ForeignKey(
        Car,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.model



