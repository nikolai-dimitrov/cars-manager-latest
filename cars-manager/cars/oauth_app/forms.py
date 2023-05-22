from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm

from cars.core.mixins import FormControlsMixin

UserModel = get_user_model()


class UserRegisterForm(UserCreationForm, FormControlsMixin):
    placeholders = {'username': 'Username',
                    'email': 'Email',
                    'password1': 'Password',
                    'password2': 'Confirm password',
                    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_form_control_class()
        self.add_place_holders()

    class Meta:
        model = UserModel
        fields = ('username', 'email')


class CustomAuthenticationForm(AuthenticationForm, FormControlsMixin):
    placeholders = {'username': 'Username',
                    'password': 'Password',
                    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.add_form_control_class()
        self.add_place_holders()


class CustomChangePasswordForm(PasswordChangeForm, FormControlsMixin):
    placeholders = {'old_password': 'Old Password',
                    'new_password1': 'New Password',
                    'new_password2': 'Confirm New Password'
                    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_form_control_class()
        self.add_place_holders()
