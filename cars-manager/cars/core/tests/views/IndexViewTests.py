from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from cars.core.forms import CarSearchForm
from cars.profiles.forms import ProfileCreateForm


class ProfileDetailsViewTests(TestCase):
    _USER_MODEL = get_user_model()
    TEMPLATE = "main/index.html"
    URL = reverse("index")
    CREDENTIALS = {
        "username": "normal",
        "password": "Ytr351a2.",
    }
    PROFILE_DATA = {
        "first_name": "test",
        "last_name": "test",
        "age": '20',
        "phone_number": '+35932175213'
    }

    CAR_SEARCH_FORM = CarSearchForm

    def setUp(self) -> None:
        self.user = self._USER_MODEL.objects.create_user(**self.CREDENTIALS)
        self.user.save()
        self.client.login(**self.CREDENTIALS)

        self.user.profile.is_activated = True
        self.user.profile.save()

    def test_correct_template_used__expect_success(self):
        response = self.client.get(self.URL)

        self.assertTemplateUsed(response, self.TEMPLATE)

    def test_correct_form_used__expect_success(self):
        response = self.client.get(self.URL)
        self.assertTrue(isinstance(response.context_data.get("form"), self.CAR_SEARCH_FORM))

