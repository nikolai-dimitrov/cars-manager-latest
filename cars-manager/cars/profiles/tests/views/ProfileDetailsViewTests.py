from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from cars.profiles.models import Profile


class ProfileDetailsViewTests(TestCase):
    _USER_MODEL = get_user_model()
    TEMPLATE = "profiles/details.html"
    URL = reverse("details profile")
    CREDENTIALS = {
        "username": "normal",
        "password": "Ytr351a2.",
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

    def test_correct_profile_data__expect_success(self):
        self.user.profile.first_name = 'test'
        self.user.profile.last_name = 'test'
        self.user.profile.age = '20'
        self.user.profile.phone_number = '+35932175213'
        self.user.profile.save()

        self.assertTrue(True, isinstance(self.user.profile, Profile))
        self.assertEqual('test', self.user.profile.first_name)
        self.assertEqual('test', self.user.profile.last_name)
        self.assertEqual('20', self.user.profile.age)
        self.assertEqual('+35932175213', self.user.profile.phone_number)

    def test_correct_ad_set_number__expect_success(self):
        self.user.profile.ad_set.count()
        self.assertEqual(0, self.user.profile.ad_set.count())
