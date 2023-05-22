from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from cars.profiles.forms import ProfileDeleteCodeInputForm




class UserDeleteViewTests(TestCase):
    _USER_MODEL = get_user_model()
    TEMPLATE = "profiles/delete-profile.html"
    NO_PERMISION_TEMPLATE = "main/forbidden-403.html"
    URL = reverse("Delete user")
    REDIRECT_URL = reverse("Log in")
    CREATE_PROFILE_URL = reverse('create profile')
    CREDENTIALS = {
        "username": "normal",
        "password": "Ytr351a2.",
    }
    PROFILE_CREDENTIALS = {
        'first_name': 'test',
        'last_name': 'test',
        'age': '20',
        'phone_number': '+35912348765',
    }
    FORM = ProfileDeleteCodeInputForm

    def setUp(self) -> None:
        self.user = self._USER_MODEL.objects.create_user(**self.CREDENTIALS)
        self.user.save()
        self.client.login(**self.CREDENTIALS)

    def test_used_template__delete__not_activated_profile_expect_fail(self):
        response = self.client.get(self.URL)
        self.assertTemplateUsed(response, self.NO_PERMISION_TEMPLATE)

    def test_used_template___delete__activated_profile_expect_success(self):
        self.client.post(self.CREATE_PROFILE_URL, data=self.PROFILE_CREDENTIALS)
        response = self.client.get(self.URL)
        self.assertTemplateUsed(response, self.TEMPLATE)

    def test_user_delete_profile_expect_success(self):
        self.client.post(self.CREATE_PROFILE_URL, data=self.PROFILE_CREDENTIALS)
        self.client.post(self.URL)
        user_obj_collection = self._USER_MODEL.objects.filter(pk=self.user.pk)
        self.assertEqual(0, len(user_obj_collection))

    def test_correct_context_data(self):
        self.client.post(self.CREATE_PROFILE_URL, data=self.PROFILE_CREDENTIALS)
        response = self.client.get(self.URL)
        self.assertTrue(isinstance(response.context_data['form'], self.FORM))
        self.assertEqual(self.user.profile, response.context_data.get("profile"))

    def test_user_delete__expect_to_redirect(self):
        self.client.post(self.CREATE_PROFILE_URL, data=self.PROFILE_CREDENTIALS)
        response = self.client.post(self.URL)
        self.assertRedirects(response, self.REDIRECT_URL)
