from django.urls import path

from cars.core.views import IndexView, AboutUsView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about', AboutUsView.as_view(), name='about'),
]
