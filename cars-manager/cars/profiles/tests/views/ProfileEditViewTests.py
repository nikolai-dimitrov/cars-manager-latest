from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from cars.profiles.forms import ProfileEditForm


class ProfileUpdateViewTests(TestCase):
    _USER_MODEL = get_user_model()
    TEMPLATE = "profiles/edit.html"
    URL = reverse("edit profile")
    REDIRECT_URL = reverse("details profile")

    CREDENTIALS = {
        "username": "normal",
        "password": "Ytr351a2.",
    }

    PROFILE_NEW_DATA = {
        "first_name": "test",
        "last_name": "test",
        "age": '20',
        "phone_number": '+35932175213'
    }

    PROFILE_EDIT_FORM = ProfileEditForm

    def setUp(self) -> None:
        self.user = self._USER_MODEL.objects.create_user(**self.CREDENTIALS)
        self.user.save()
        self.client.login(**self.CREDENTIALS)

        self.user.profile.is_activated = True
        self.user.profile.save()

    def test_correct_template_used__expect_success(self):
        response = self.client.get(self.URL)
        self.assertTemplateUsed(response, self.TEMPLATE)

    def test_redirect_url__expect_success(self):
        response = self.client.post(self.URL, data=self.PROFILE_NEW_DATA)
        self.assertRedirects(response, self.REDIRECT_URL)

    def test_correct_form_used__expect_success(self):
        response = self.client.get(self.URL)
        self.assertTrue(isinstance(response.context_data.get("form"), self.PROFILE_EDIT_FORM))

    def test_profile_change_expect_profile_changed_success(self):
        self.assertEqual(self.user.profile.first_name, "")
        self.assertEqual(self.user.profile.last_name, "")
        self.assertEqual(self.user.profile.age, 18)
        self.assertEqual(self.user.profile.phone_number, 0)

        self.client.post(self.URL, data=self.PROFILE_NEW_DATA)
        self.user.profile.refresh_from_db()

        self.assertEqual('test', self.user.profile.first_name)
        self.assertEqual('test', self.user.profile.last_name)
        self.assertEqual(20, self.user.profile.age)
        self.assertEqual('+35932175213', self.user.profile.phone_number)
