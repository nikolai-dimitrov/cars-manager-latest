# from django.test import TestCase
# from django.urls import reverse
# from django.contrib.auth import get_user_model
#
# from cars.profiles.models import Profile
#
#
# class BanUnbanViewTests(TestCase):
#     _USER_MODEL = get_user_model()
#     TEMPLATE = "oauth_app/change-password.html"
#     # URL = reverse("profile ban")
#     CREDENTIALS = {
#         "username": "superuser",
#         "password": "Ydsa3al.",
#     }
#     USER_TO_BAN_CREDENTIALS = {
#         "username": "staffuser",
#         "email": "asdas",
#         "password": "Ydsa3al.",
#     }
#     PROFILE_CREDENTIALS = {
#         'first_name': 'test',
#         'last_name': 'test',
#         'age': '20',
#         'phone_number': '+35912348765',
#     }
#
#     def setUp(self) -> None:
#         self.user = self._USER_MODEL.objects.create_user(**self.CREDENTIALS)
#         self.user.is_staff = True
#         self.user.save()
#         self.user.profile.is_activated = True
#         self.user.profile.phone_number = "+3598786252"
#         self.user.profile.save()
#         self.client.login(**self.CREDENTIALS)
#
#     def test_ban_staff_user__expect_fail(self):
#         user_to_ban = self._USER_MODEL.objects.create_user(**self.USER_TO_BAN_CREDENTIALS)
#         url = reverse("profile ban", kwargs={"pk": user_to_ban.profile.pk})
#         self.client.get(url)
#         self.assertEqual(True, user_to_ban.profile.is_banned)
