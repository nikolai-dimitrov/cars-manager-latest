from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model



class UserChangePasswordViewTests(TestCase):
    _USER_MODEL = get_user_model()
    TEMPLATE = "oauth_app/change-password.html"
    URL = reverse("Change password")
    REDIRECT_URL = reverse("Log in")
    CREDENTIALS = {
        "username": "normaluser",
        "password": "Ydsa3al.",
    }
    PASSOWRD_CHANGE_CREDENTIALS = {
        "old_password": "Ydsa3al.",
        'new_password1': "Ads3al.",
        'new_password2': "Ads3al.",
    }

    def setUp(self) -> None:
        self.user = self._USER_MODEL.objects.create_user(**self.CREDENTIALS)
        self.user.save()
        self.client.login(**self.CREDENTIALS)
        self.user.profile.is_activated = True
        self.user.profile.save()

    def test_correct_template_used__expect_success(self):
        response = self.client.get(self.URL)

        self.assertTemplateUsed(response, self.TEMPLATE)

    def test_change_password_redirect_url__expect_success(self):
        response = self.client.post(self.URL, data=self.PASSOWRD_CHANGE_CREDENTIALS)
        self.assertRedirects(response, self.REDIRECT_URL)

    def test_change_password__try_login_old_credentials(self):
        self.client.post(self.URL, data=self.PASSOWRD_CHANGE_CREDENTIALS)
        response = self.client.post(self.REDIRECT_URL, data=self.CREDENTIALS)
        err = len(response.context_data['form'].errors)
        self.assertEqual(1, err)
