from django.urls import path
from cars.profiles.views import ProfileEditView, ProfileCreateView, ProfileDetailsView, DeleteCodeView

urlpatterns = [
    path('edit/', ProfileEditView.as_view(), name='edit profile'),
    path('create/', ProfileCreateView.as_view(), name='create profile'),
    path('details/', ProfileDetailsView.as_view(), name='details profile'),
    path('code/<int:pk>/', DeleteCodeView.as_view(), name='send delete code'),
]
