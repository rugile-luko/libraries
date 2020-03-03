from django.db import models
from django.utils import timezone
import requests


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
    picture = models.ImageField(null=True, blank=True, upload_to='gallery')
    description = models.TextField(max_length=2000, null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    fax = models.CharField(max_length=100, null=True, blank=True)
    website = models.CharField(max_length=100, null=True, blank=True)
    weekday_from = models.CharField(choices=OPEN_DAYS, max_length=100, null=True, blank=True)
    weekday_to = models.CharField(choices=OPEN_DAYS, max_length=100, null=True, blank=True)
    open_from = models.IntegerField(choices=WORKING_HOURS)
    open_to = models.IntegerField(choices=WORKING_HOURS)
    review = models.TextField(max_length=3000, blank=True, null=True)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "%s in %s" % (self.name, self.address) or ''

    # def save(self, force_insert=False, force_update=False, using=None,
    #          update_fields=None):
    #     super().save()
    #
    #     img = Image.open(self.picture.path)
    #
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.picture.path)

    @property
    def picture_url(self):
        if self.picture and hasattr(self.picture, 'url'):
            return self.picture_url

    class Meta:
        verbose_name_plural = 'Libraries'


class Location(models.Model):
    library = models.OneToOneField(Library, on_delete=models.CASCADE)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, default=0)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, default=0)

    def __str__(self):
        return '%s' % self.library

    def save(self, **kwargs):
        super().save(**kwargs)
        address = " ".join(self.library.address)
        api_key = "AIzaSyDHmd_dI3EZ7JwL6xSHYGJnsFMZe5zBYW4"
        api_response = requests.get(
            'https://maps.googleapis.com/maps/api/geocode/json?address={0}&key={1}'.format(address, api_key))
        api_response_dict = api_response.json()
        print(api_response_dict)
        if api_response_dict['status'] == 'OK':
            self.latitude = api_response_dict['results'][0]['geometry']['location']['lat']
            self.longitude = api_response_dict['results'][0]['geometry']['location']['lng']
            # self.save()







