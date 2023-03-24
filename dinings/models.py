from django.db import models
from .utils import dining_image_upload_path


class Dining(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    latitude = models.DecimalField(null=True, blank=True)
    longitude = models.DecimalField(null=True, blank=True)
    phone_number = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self) -> str:
        return self.name


class Links(models.Model):
    key = models.CharField(max_length=100, null=True, blank=True)
    value = models.CharField(max_length=100, null=True, blank=True)
    dining = models.ForeignKey(Dining, on_delete=models.CASCADE, related_name='links')

    def __str__(self) -> str:
        return self.key


class Images(models.Model):
    image = models.ImageField(upload_to=dining_image_upload_path)
    dining = models.ForeignKey(Dining, on_delete=models.CASCADE, related_name='images')
