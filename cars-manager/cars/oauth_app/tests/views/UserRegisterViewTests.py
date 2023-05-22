from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


class RegisterViewTests(TestCase):
    _USER_MODEL = get_user_model()
    TEMPLATE = "oauth_app/register.html"
    URL = reverse("Register")
    REDIRECT_URL_LOG_IN = reverse("Log in")
    CREDENTIALS = {
        "username": "normal",
        "email": "pythonproject771@abv.bg",
        "password1": "Ytr351a2.",
        "password2": "Ytr351a2.",
    }
    INVALID_CREDENTIALS = {
        "username": "normal",
        "email": "pythonproject771",
        "password1": "asd12e.",
        "password2": "Ytr351a2.",
    }

    def test_used_template__expect_success(self):
        response = self.client.get(self.URL)
        self.assertTemplateUsed(response, self.TEMPLATE)

    def test_register_user__successful__expect_to_redirect(self):
        response = self.client.post(self.URL, data=self.CREDENTIALS)
        self.assertRedirects(response, self.REDIRECT_URL_LOG_IN)

    def test_registered_user_created_sucessfully__expect_success(self):
        self.client.post(self.URL, data=self.CREDENTIALS)
        self.assertTrue(len(self._USER_MODEL.objects.all()) > 0)

    def test_register_user__with_invalid_credentials__expect_fail(self):
        response = self.client.post(self.URL, data=self.INVALID_CREDENTIALS)
        self.assertTrue(len(self._USER_MODEL.objects.all()) == 0)
        self.assertTemplateUsed(response, self.TEMPLATE)
