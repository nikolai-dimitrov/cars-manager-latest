from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


class AdminControlPanelTests(TestCase):
    _USER_MODEL = get_user_model()
    TEMPLATE = "profiles/show-profiles.html"
    ERROR_TEMPLATE = "main/forbidden-403.html"
    URL = reverse("admin panel")
    CREDENTIALS_USER = {
        "username": "normaluser",
        "password": "Ydsa3al.",
    }

    def setUp(self) -> None:
        self.user = self._USER_MODEL.objects.create_user(**self.CREDENTIALS_USER)
        self.user.save()
        self.client.login(**self.CREDENTIALS_USER)
        self.user.profile.is_activated = True
        self.user.profile.save()

    def test_correct_template_used__when_user_is_not_staff_expect_success(self):
        self.user.is_staff = False
        self.user.save()
        response = self.client.get(self.URL)
        self.assertTemplateUsed(response, self.ERROR_TEMPLATE)

    def test_correct_template_used__when_user_is_staff__expect_success(self):
        self.user.is_staff = True
        self.user.save()
        response = self.client.get(self.URL)
        self.assertTemplateUsed(response, self.TEMPLATE)
