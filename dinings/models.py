from django.db import models
from django.contrib.gis.db import models as gis_models
from django.utils.safestring import mark_safe

from .utils import dining_image_upload_path


class Dining(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    phone_number = models.CharField(max_length=100, null=True, blank=True)
    location = gis_models.PointField(srid=4326, null=True, blank=True)
    
    @property
    def latitude(self):
        return self.location.coords[1]

    @property
    def longitude(self):
        return self.location.coords[0]
    
    def __str__(self) -> str:
        return self.name
    


class Link(models.Model):
    key = models.CharField(max_length=100, null=True, blank=True)
    value = models.CharField(max_length=100, null=True, blank=True)
    dining = models.ForeignKey(Dining, on_delete=models.CASCADE, related_name='links')

    def __str__(self) -> str:
        return self.key


class Image(models.Model):
    image = models.ImageField(upload_to=dining_image_upload_path)
    dining = models.ForeignKey(Dining, on_delete=models.CASCADE, related_name='images')


    def image_tag(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" width="150" height="150" />')
        else:
            return "(No Image)"
        
    image_tag.short_description = "Image Preview"