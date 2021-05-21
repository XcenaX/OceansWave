from django.contrib import admin
from .models import Assistant, New, Specialist, Event, City, Country
# Register your models here.
admin.site.register(New)
admin.site.register(Specialist)
admin.site.register(Event)
admin.site.register(City)
admin.site.register(Country)
admin.site.register(Assistant)