from django.db import models
from oceanswave.yandex_s3_storage import ClientDocsStorage
from datetime import date


class New(models.Model):
    title = models.TextField(default="")
    description = models.TextField(default="")
    image = models.FileField(storage=ClientDocsStorage(), blank=True, null=True)
    source_link = models.TextField(default="")
    def __str__(self):
        return self.title



class City(models.Model):
    name = models.TextField(default="")

    def __str__(self):
        return self.name

class Country(models.Model):
    country = models.TextField(default="")
    flag = models.FileField(storage=ClientDocsStorage(), blank=True, null=True)
    cities = models.ManyToManyField(City, null=True, blank=True)
    def __str__(self):
        return self.country

class Specialist(models.Model):
    name = models.TextField(default="")
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField(default="")
    count_of_lections = models.IntegerField(default=0)
    image = models.FileField(storage=ClientDocsStorage(), blank=True, null=True)
    whatsapp = models.TextField(default="")
    telegram = models.TextField(default="")
    
    def get_rating_range(self):
        return range(0, int(self.rating))

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.TextField(default="")
    image = models.FileField(storage=ClientDocsStorage(), blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    start_time = models.TimeField(blank=True, null=True)    
    end_time = models.TimeField(blank=True, null=True)    
    teacher = models.TextField(default="")
    price = models.IntegerField(default=0)
    description = models.TextField(default="")
    places_left = models.IntegerField()
    pdf_file = models.FileField(storage=ClientDocsStorage(), blank=True, null=True)
    qr_image = models.FileField(storage=ClientDocsStorage(), blank=True, null=True)
    expired = models.BooleanField(default=False)
    location = models.TextField(default="")
    country = models.ForeignKey(Country, on_delete=models.CASCADE, blank=True, null=True)

    def get_expired(self):
        if self.start_date < date.today():
            self.expired = True
            self.save()
        return self.expired

    def __str__(self):
        return self.name