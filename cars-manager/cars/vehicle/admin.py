from django.contrib import admin
from cars.ad.models import Car, CarModel


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    ordering = ['make']


@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ['model', 'make']
