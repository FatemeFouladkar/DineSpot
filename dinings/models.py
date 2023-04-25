from django.db import models
from django.contrib.gis.db import models as gis_models
from django.contrib.gis.geos import Point
from .utils import dining_image_upload_path


class Dining(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    phone_number = models.CharField(max_length=100, null=True, blank=True)
    location = gis_models.PointField(srid=4326, null=True, blank=True, default=Point(36.2971, 59.5953))
    
    @property
    def latitude(self):
        return self.location.coords[1] if self.location else 36.2971

    @property
    def longitude(self):
        return self.location.coords[0] if self.location else 59.5953
    
    def __str__(self) -> str:
        return str(self.name) if str(self.name) else int(self.pk)
    


class Link(models.Model):
    key = models.CharField(max_length=100, null=True, blank=True)
    value = models.CharField(max_length=100, null=True, blank=True)
    dining = models.ForeignKey(Dining, on_delete=models.CASCADE, related_name='links')

    def __str__(self) -> str:
        return self.key if self.key else int(self.pk)


class Image(models.Model):
    image = models.ImageField(upload_to=dining_image_upload_path)
    dining = models.ForeignKey(Dining, on_delete=models.CASCADE, related_name='images')
