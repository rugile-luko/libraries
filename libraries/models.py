from django.conf import settings
from django.db import models
from django.utils import timezone
import requests
from math import radians, cos, sin, asin, sqrt


class Library(models.Model):
    OPEN_DAYS = (
        ('Mon', 'Monday'),
        ('Tue', 'Tuesday'),
        ('Wed', 'Wednesday'),
        ('Thu', 'Thursday'),
        ('Fri', 'Friday'),
        ('Sat', 'Saturday'),
        ('Sun', 'Sunday')
    )

    WORKING_HOURS = [(i, str(i)) for i in range(1, 25)]

    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True, default=0)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True, default=0)
    picture = models.ImageField(null=True, blank=True, upload_to='gallery')
    description = models.TextField(max_length=5000)
    phone = models.CharField(max_length=100)
    fax = models.CharField(max_length=100, null=True, blank=True)
    website = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100)
    weekday_from = models.CharField(choices=OPEN_DAYS, max_length=100, null=True, blank=True)
    weekday_to = models.CharField(choices=OPEN_DAYS, max_length=100, null=True, blank=True)
    open_from = models.IntegerField(choices=WORKING_HOURS)
    open_to = models.IntegerField(choices=WORKING_HOURS)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "%s in %s" % (self.name, self.address) or ''

    def save(self, **kwargs):
        api_response = requests.get(
            'https://maps.googleapis.com/maps/api/geocode/json?address={0}&key={1}'.format(self.address, settings.MAPS_API_KEY))
        api_response_dict = api_response.json()
        if api_response_dict['status'] == 'OK':
            self.latitude = api_response_dict['results'][0]['geometry']['location']['lat']
            self.longitude = api_response_dict['results'][0]['geometry']['location']['lng']

        super().save(**kwargs)

    def measure_distance(self, lon1, lat1):
        lon1, lat1, lon2, lat2 = map(radians, [self.longitude, self.latitude, lon1, lat1])
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        c = 2 * asin(sqrt(a))
        km = 6371 * c
        return km

    @property
    def picture_url(self):
        if self.picture and hasattr(self.picture, 'url'):
            return self.picture_url

    class Meta:
        verbose_name_plural = 'Libraries'








