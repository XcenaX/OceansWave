from api.serializers import *
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from main.models import *

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer

    def retrieve(self, request, pk=None):
        queryset = City.objects.all()
        try:
            item = City.objects.get(id=pk)
            serializer = CitySerializer(item)
            return Response(serializer.data)
        except:
            raise Http404

    def get_queryset(self):
        country = self.request.query_params.get('country', None)

        queryset = self.queryset
        
        if country:
            country = Country.objects.get(id=country)
            queryset = country.cities.all()
        return queryset

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

    def retrieve(self, request, pk=None):
        queryset = Country.objects.all()
        try:
            item = Country.objects.get(id=pk)
            serializer = CountrySerializer(item)
            return Response(serializer.data)
        except:
            raise Http404

    def get_queryset(self):
        return self.queryset

class SpecialistViewSet(viewsets.ModelViewSet):
    queryset = Specialist.objects.all()
    serializer_class = SpecialistSerializer

    def retrieve(self, request, pk=None):
        queryset = Specialist.objects.all()
        try:
            item = Specialist.objects.get(id=pk)
            serializer = SpecialistSerializer(item)
            return Response(serializer.data)
        except:
            raise Http404

    def get_queryset(self):
        city = self.request.query_params.get('city', None)

        queryset = self.queryset
        
        if city:
            city = City.objects.get(id=city)
            queryset = Specialist.objects.filter(city=city)
        return queryset
