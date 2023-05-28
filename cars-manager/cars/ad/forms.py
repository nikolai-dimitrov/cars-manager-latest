from datetime import datetime

from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator
from django.forms import inlineformset_factory

from cars.ad.enums import Transmission, BodyType, Fuel
from cars.ad.models import Ad, Photo
from cars.core.mixins import FormControlsMixin

current_year = int(datetime.now().year)


class AdSearchForm(forms.Form, FormControlsMixin):
    classes = {
        'title': 'ad-form-field char-field',
        # 'price': 'ad-form-field float-field',
        'car': 'ad-form-field choice-field',
        'year_of_manufacture': 'ad-form-field integer-field',
        'model': 'ad-form-field choice-field',
        'transmission': 'ad-form-field choice-field',
        'body_type': 'ad-form-field choice-field',
        'city': 'ad-form-field choice-field',
        'fuel': 'ad-form-field choice-field',
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_classes()
        self.add_place_holders()
        for name, field in self.fields.items():
            if name == 'car':
                field.widget.attrs.update({
                    'onchange': 'setModel()'
                })

            field.widget.attrs['class'] += f' {name}'

    TITLE_MAX_LENGTH = 70
    YEAR_OF_MANUFACTURE_MIN = 1930

    title = forms.CharField(
        max_length=TITLE_MAX_LENGTH,
        label='',
    )
    car = forms.ChoiceField()
    model = forms.ChoiceField()
    year_of_manufacture = forms.IntegerField(
        validators=(
            MinValueValidator(YEAR_OF_MANUFACTURE_MIN),
            MaxValueValidator(current_year),
        ), label='',
    )

    fuel = forms.ChoiceField(
        choices=Fuel.choices(),
        label='',
    )
    body_type = forms.ChoiceField(
        choices=BodyType.choices(),
        label='',
    )
    transmission = forms.ChoiceField(
        choices=Transmission.choices(),
        label='',
    )
    # price = forms.FloatField()
    city = forms.ChoiceField()


class AdCreateForm(forms.ModelForm, FormControlsMixin):
    classes = {
        'title': 'ad-form-field char-field',
        'price': 'ad-form-field integer-field',
        'car': 'ad-form-field choice-field',
        'year_of_manufacture': 'ad-form-field integer-field',
        'model': 'ad-form-field choice-field',
        'transmission': 'ad-form-field choice-field',
        'body_type': 'ad-form-field choice-field',
        'city': 'ad-form-field choice-field',
        'horse_power': 'ad-form-field integer-field',
        'mileage': 'ad-form-field integer-field',
        'fuel': 'ad-form-field choice-field',
        'description': 'ad-form-field text-area',

    }
    placeholders = {
        # 'title': 'Title',
        # 'price': 'Price',
        # 'description': 'Description',
        # 'year_of_manufacture':'Year'
    }

    class Meta:
        model = Ad
        fields = (
            'title', 'car', 'model', 'price', 'year_of_manufacture',
            'fuel', 'body_type', 'transmission', 'city', 'horse_power', 'mileage', 'description'
        )  # 'image_main', 'image1', 'image2', 'image3'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_classes()
        self.add_place_holders()
        for name, field in self.fields.items():
            if name == 'car':
                field.widget.attrs.update({
                    'onchange': 'setModel()'
                })
            field.widget.attrs['class'] += f' {name}'

            # if 'image' in name:
            #     field.widget.attrs.update({
            #         "onchange": "imageHasChanged(event)",
            #         # "id": name,
            #     })


class AdEditForm(AdCreateForm):
    pass


class AdImageForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('image',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if 'image' in name:
                field.widget.attrs.update({
                    "onchange": "imageHasChanged(event)",
                    # "id": name,
                })


AdImageFormSetCreate = inlineformset_factory(
    Ad, Photo, form=AdImageForm,
    fields=['image'], extra=4, can_delete=True, max_num=4, min_num=4,
)
