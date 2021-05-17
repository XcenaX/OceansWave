from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.dispatch.dispatcher import receiver
from main.models import *
from main.modules.functions import margin_counter, get_paginated_blogs
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from start_bot import TELEGRAM_BOT
TELEGRAM_BOT.start_bot()

COUNT_SPECIALISTS_ON_PAGE = 9
COUNT_EVENTS_ON_PAGE = 9

class Index(View):
    def get(self, request):
        specialists = Specialist.objects.all()[0:3]
        closest_event = None
        try:
            closest_event = Event.objects.filter(start_date__gte=date.today()).order_by("start_date").first()
        except:
            pass
        news = New.objects.all()[0:4]
        return render(request, "index.html", {
            "specialists": specialists,
            "closest_event": closest_event,
            "news": news,
        })
    def post(self, request):
        return render(request, "index.html", {})

class Specialists(View):
    def get(self, request):
        specialists = Specialist.objects.all()
        fake_blocks_count = 0

        country = request.GET.get("country", "")
        city = request.GET.get("city", "")
        rating = request.GET.get("rating", "")

        country_obj = None
        city_obj = None
        cities = None

        if country:
            country_obj = Country.objects.filter(id=country).first()
            if country_obj:
                specialists = specialists.filter(country=country_obj)
        if city:
            city_obj = City.objects.filter(id=city).first()
            if city_obj:
                specialists = specialists.filter(city=city_obj)
        if rating:
            if rating == "true":
                specialists = specialists.order_by("rating")
            elif rating == "false":
                specialists = specialists.order_by("-rating")
        
        if country_obj:
            cities = country_obj.cities.all()

        paginator = Paginator(specialists, COUNT_SPECIALISTS_ON_PAGE)
        paginated_blocks, pages = get_paginated_blogs(request, paginator)

        length = len(paginated_blocks)
        if length % 3 != 0:
            if length % 2 == 0:
                fake_blocks_count = 2
            else:
                fake_blocks_count = 1

        river_count = 0
        river_mobile_count = range(0, length)

        if length > 6:
            river_count = range(0,3)
        elif length > 3:
            river_count = range(0,2)
        elif length > 0:
            river_count = range(0,1)
        else:
            river_count = range(0,0)


        return render(request, "specialists.html", {
            "specialists": paginated_blocks,
            "pages": pages,
            "margin_counter": margin_counter(-800, 700),
            "margin_counter_mobile": margin_counter(-750, 750),
            "river_count": river_count,
            "river_mobile_count": river_mobile_count,
            "fake_blocks_count": range(0, fake_blocks_count),
            "country": country_obj,
            "city": city_obj,
            "rating": rating,
            "countries": Country.objects.all(),
            "cities": cities,
        })
    def post(self, request):
        return render(request, "specialists.html", {})

class Events(View):
    def get(self, request):
        events = Event.objects.all()

        name = request.GET.get("name", "")
        price = request.GET.get("price", "")

        if name and name != "":
            events = events.filter(name__icontains=name)
        if price:
            if price == "true":
                events = events.order_by("price")
            elif price == "false":
                events = events.order_by("-price")

        paginator = Paginator(events, COUNT_EVENTS_ON_PAGE)
        paginated_blocks, pages = get_paginated_blogs(request, paginator)

        length = len(paginated_blocks)
        if length % 3 != 0:
            if length % 2 == 0:
                fake_blocks_count = 2
            else:
                fake_blocks_count = 1

        river_count = 0
        river_mobile_count = range(0, length)

        if length > 6:
            river_count = range(0,3)
        elif length > 3:
            river_count = range(0,2)
        elif length > 0:
            river_count = range(0,1)
        else:
            river_count = range(0,0)


        return render(request, "events.html", {
            "events": paginated_blocks,
            "pages": pages,
            "margin_counter": margin_counter(-1000, 900),
            "margin_counter_mobile": margin_counter(-750, 750),
            "river_count": river_count,
            "river_mobile_count": river_mobile_count,
            "name": name,
            "price": price,
        })
    def post(self, request):
        return render(request, "events.html", {})

class DownloadFile(View):
    def get(self, request):
        fl_path = '/file/path'
        filename = 'downloaded_file_name.extension'

        fl = open(fl_path, 'r')
        mime_type, _ = mimetypes.guess_type(fl_path)
        response = HttpResponse(fl, content_type=mime_type)
        response['Content-Disposition'] = "attachment; filename=%s" % filename
        return response

@receiver(models.signals.post_delete, sender=Specialists)
def specialist_avatar_delete_ondelete(sender, instance, using, **kwargs):
    instance.image.delete(save=False)

@receiver(models.signals.pre_save, sender=Specialists)
def specialist_avatar_delete_onsave(sender, instance, using, **kwargs):
    try:
        old_file = sender.objects.get(pk=instance.pk).image
    except sender.DoesNotExist:
        return False
    
    new_file = instance.image
    if not old_file == new_file:
        old_file.delete(save=False)

@receiver(models.signals.post_delete, sender=Country)
def country_avatar_delete_ondelete(sender, instance, using, **kwargs):
    instance.flag.delete(save=False)

@receiver(models.signals.pre_save, sender=Country)
def country_avatar_delete_onsave(sender, instance, using, **kwargs):
    try:
        old_file = sender.objects.get(pk=instance.pk).flag
    except sender.DoesNotExist:
        return False
    
    new_file = instance.flag
    if not old_file == new_file:
        old_file.delete(save=False)

@receiver(models.signals.post_delete, sender=Event)
def event_avatar_delete_ondelete(sender, instance, using, **kwargs):
    instance.image.delete(save=False)
    instance.qr_image.delete(save=False)
    instance.pdf_file.delete(save=False)

@receiver(models.signals.pre_save, sender=Event)
def event_avatar_delete_onsave(sender, instance, using, **kwargs):
    try:
        old_file = sender.objects.get(pk=instance.pk).image
    except sender.DoesNotExist:
        return False
    
    new_file = instance.image
    if not old_file == new_file:
        old_file.delete(save=False)

@receiver(models.signals.post_save, sender=Event) 
def when_init(sender, instance, created, **kwargs):
    if created:
        TELEGRAM_BOT.send_event(instance)
        

@receiver(models.signals.post_delete, sender=New)
def new_avatar_delete_ondelete(sender, instance, using, **kwargs):
    instance.image.delete(save=False)

@receiver(models.signals.pre_save, sender=New)
def new_avatar_delete_onsave(sender, instance, using, **kwargs):
    try:
        old_file = sender.objects.get(pk=instance.pk).image
    except sender.DoesNotExist:
        return False
    
    new_file = instance.image
    if not old_file == new_file:
        old_file.delete(save=False)