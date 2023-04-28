from django.db import models
from django.contrib.gis.db import models as gis_models
from django.contrib.gis.geos import Point
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.contrib.auth import get_user_model

from .utils import dining_image_upload_path


class Dining(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    phone_number = models.CharField(max_length=100, null=True, blank=True)
    location = gis_models.PointField(srid=4326, null=True, blank=True, default=Point(36.2971, 59.5953))
    confirmed = models.BooleanField(default=False)

    @property
    def latitude(self):
        return self.location.coords[1] if self.location else 36.2971

    @property
    def longitude(self):
        return self.location.coords[0] if self.location else 59.5953
    
    def __str__(self) -> str:
        return str(self.name) if str(self.name) else int(self.pk)
    

@receiver(post_save, sender=Dining)
def send_email_to_admin (sender, instance, created, **kwargs):
    if created and not instance.confirmed:
        subject = "New Dining Spot Requested"
        message = f"""A new dining spot was requested.\nTo confirm it, please checkout the admin panel.
                    Name: {instance.name}  
                    Address: {instance.address},
                    Phone Number: {instance.phone_number},
                    Description: {instance.description}"""
        
        admins = list(get_user_model().objects.filter(is_superuser=True).values_list('email', flat=True))
        send_mail(subject, message, recipient_list=admins, from_email=None)


class Link(models.Model):
    key = models.CharField(max_length=100, null=True, blank=True)
    value = models.CharField(max_length=100, null=True, blank=True)
    dining = models.ForeignKey(Dining, on_delete=models.CASCADE, related_name='links')

    def __str__(self) -> str:
        return self.key if self.key else int(self.pk)


class Image(models.Model):
    image = models.ImageField(upload_to=dining_image_upload_path)
    dining = models.ForeignKey(Dining, on_delete=models.CASCADE, related_name='images')
