from rest_framework import serializers
from django.core.serializers import serialize
from django.http import Http404, JsonResponse
import json
from main.models import *

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ("id", "name")


class CountrySerializer(serializers.ModelSerializer):    
    cities = CitySerializer(many=True, read_only=False, required=False)
    class Meta:
        model = Country
        fields = ("id", "country", "cities")


class SpecialistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialist
        fields = ("id", "name", "whatsapp", "telegram")