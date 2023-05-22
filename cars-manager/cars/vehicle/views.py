from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from cars.vehicle.models import CarModel, Car
from cars.vehicle.serializers import CarModelSerializer


class ListCreateCarModelView(APIView):
    model = CarModel

    def get(self, request, *args, **kwargs):
        car = request.GET.get('car')

        if car is None:
            car_models = self.model.objects.all()
        else:
            car_obj = Car.objects.get(make=car)
            car_models = self.model.objects.filter(make=car_obj.id)

        car_models_serializer = CarModelSerializer(car_models, many=True)
        return Response(car_models_serializer.data, status=status.HTTP_200_OK)
