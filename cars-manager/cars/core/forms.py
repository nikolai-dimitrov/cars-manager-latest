from django import forms

from cars.ad.enums import Cylinders, Fuel
from cars.core.mixins import FormControlsMixin


class CarSearchForm(forms.Form, FormControlsMixin):
    classes = {
        'make': 'car-search-form-field',
        'model': 'car-search-form-field',
        'year': 'car-search-form-field',
        'transmission': 'car-search-form-field',
        'fuel_type': 'car-search-form-field',
        'cylinders': 'car-search-form-field',
    }
    placeholders = {
        'make': 'Brand',
        'model': 'Model',
        'year': 'Year',
    }
    TRANSMISSION_CHOICES = (
        ('all', 'All'),
        ('m', 'Manual'),
        ('a', 'Automatic'),
    )
    FUEL_TYPE = (
        Fuel.car_api_search_choices()
    )
    CYLINDERS_CHOICES = (
        Cylinders.fuel_choices()
    )

    make = forms.CharField(
        required=True
    )
    model = forms.CharField(
        required=False
    )
    year = forms.DateField(
        required=False
    )
    transmission = forms.ChoiceField(
        choices=TRANSMISSION_CHOICES

    )
    fuel_type = forms.ChoiceField(
        choices=FUEL_TYPE
    )
    cylinders = forms.ChoiceField(
        choices=CYLINDERS_CHOICES
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_classes()
        self.add_place_holders()
