from rest_framework import serializers
from .models import Bicycle, Rental


class BicycleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bicycle
        fields = '__all__'


class RentalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rental
        fields = '__all__'
