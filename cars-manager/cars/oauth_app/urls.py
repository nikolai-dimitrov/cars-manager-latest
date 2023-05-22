from django.contrib.auth.views import LogoutView
from django.urls import path
from .signals import *
from cars.oauth_app.views import UserRegisterView, UserLogInView, UserDeleteView, UserChangePassword, \
    AdminControlView, BanUnbanView
from ..core.emails import activate_account

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='Register'),
    path('log-in-folder/', UserLogInView.as_view(), name='Log in'),
    path('log-out/', LogoutView.as_view(), name='Log out'),
    path('delete/', UserDeleteView.as_view(), name='Delete user'),
    path('password/change/', UserChangePassword.as_view(), name='Change password'),
    path('activate/<uidb64>/<token>/', activate_account, name='activate account'),
    path('admin/panel/', AdminControlView.as_view(), name='admin panel'),
    path('ban/<int:pk>/<int:page>', BanUnbanView.as_view(), name='profile ban'),
]
