from django import forms

from cars.core.mixins import FormControlsMixin
from cars.profiles.models import Profile


class ProfileCreateForm(forms.ModelForm, FormControlsMixin):
    placeholders = {'first_name': 'First Name',
                    'last_name': 'Last Name',
                    'age': 'Age',
                    'phone_number': 'Phone Number',
                    }
    classes = {
        'first_name': 'create-profile-fields',
        'last_name': 'create-profile-fields',
        'age': 'create-profile-fields',
        'phone_number': 'create-profile-fields',
    }

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'age', 'phone_number',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_place_holders()
        self.add_classes()


class ProfileEditForm(forms.ModelForm, FormControlsMixin):
    classes = {
        'first_name': 'edit-profile-form-field char-field',
        'last_name': 'edit-profile-form-field char-field',
        'age': 'edit-profile-form-field char-field',
        'phone_number': 'edit-profile-form-field char-field',
    }

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'age', 'phone_number', 'image',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_classes()
        for name, field in self.fields.items():
            if 'image' in name:
                field.widget.attrs.update({
                    "onchange": "profileImageHasChanged(event)",
                    "id": name,
                })


class ProfileDeleteCodeInputForm(forms.Form):
    confirm_delete_code = forms.IntegerField(
    )
