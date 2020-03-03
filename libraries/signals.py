from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Library, Location


@receiver(post_save, sender=Library)
def create_location(sender, instance, created, **kwargs):
    if created:
        Location.objects.create(library=instance)

#
# @receiver(post_save, sender=models.Library)
# def save_location(sender, instance, **kwargs):
#     instance.add.save()

