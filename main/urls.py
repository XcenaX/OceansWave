from django.urls import path
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name= "main"
urlpatterns = [
    path('', views.Index.as_view(), name='index'), 
    path('specialists', views.Specialists.as_view(), name='specialists'), 
    path('events', views.Events.as_view(), name='events'), 
    path('download/(?P<path>.*)$', views.DownloadFile.as_view(), name="download"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#