from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from cars.profiles.models import Profile


class LogInViewTests(TestCase):
    _USER_MODEL = get_user_model()
    TEMPLATE = "oauth_app/log-in-folder.html"
    URL = reverse("Log in")
    REDIRECT_URL = reverse("index")
    REDIRECT_URL_CREATE_PROFILE = reverse('create profile')
    CREDENTIALS = {
        "username": "normaluser",
        "password": "Ytr351a2.",
    }

    def test_used_template__expect_success(self):
        response = self.client.get(self.URL)
        self.assertTemplateUsed(response, self.TEMPLATE)

    def test_user_logged_in__with_activated_profile__expect_redirect_url_success(self):
        user = self._USER_MODEL.objects.create_user(**self.CREDENTIALS)
        user.is_email_verified = True
        user.save()

        profile = Profile.objects.get(user_id=user.pk)
        profile.is_activated = True
        profile.save()

        response = self.client.post(self.URL, data=self.CREDENTIALS)
        self.assertRedirects(response, self.REDIRECT_URL)

    def test_user_logged_in__with_not_activated_profile__expect_redirect_create_profile(self):
        user = self._USER_MODEL.objects.create_user(**self.CREDENTIALS)
        user.is_email_verified = True
        user.save()

        profile = Profile.objects.get(user_id=user.pk)
        profile.is_activated = False
        profile.save()

        response = self.client.post(self.URL, data=self.CREDENTIALS)
        self.assertRedirects(response, self.REDIRECT_URL_CREATE_PROFILE)

    def test_user_logged_in__with_not_verified_email__expect_fail__and_redirect_log_in(self):
        user = self._USER_MODEL.objects.create_user(**self.CREDENTIALS)
        user.is_email_verified = False
        user.save()

        profile = Profile.objects.get(user_id=user.pk)
        profile.is_activated = False
        profile.save()

        response = self.client.post(self.URL, data=self.CREDENTIALS)
        self.assertRedirects(response, self.URL)


    def test_user_log_in__banned_profile__expect_fail__and_redirect_login(self):
        user = self._USER_MODEL.objects.create_user(**self.CREDENTIALS)
        user.is_email_verified = True
        user.save()

        profile = Profile.objects.get(user_id=user.pk)
        profile.is_banned = True
        profile.is_activated = True
        profile.save()

        response = self.client.post(self.URL, data=self.CREDENTIALS)
        self.assertRedirects(response, self.URL)
