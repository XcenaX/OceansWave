from django.urls import path, include
from django.conf.urls import url
from api import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
import os
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import *

from rest_framework_simplejwt import views as jwt_views

router = routers.SimpleRouter()
router.register(r'cities', CityViewSet)
router.register(r'countries', CountryViewSet)
router.register(r'specialists', SpecialistViewSet)

from rest_framework.authtoken import views as api_views

urlpatterns = [
    url(r'^', include(router.urls)),
]

urlpatterns = format_suffix_patterns(urlpatterns)