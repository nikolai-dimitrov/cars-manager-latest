from django.urls import path

from cars.vehicle.views import ListCreateCarModelView

urlpatterns = [
    path(
        'api/',
        ListCreateCarModelView().as_view()
    )
]
