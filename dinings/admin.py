from django.contrib import admin
from django.contrib.gis.admin import GISModelAdmin

from .models import Dining, Link, Image


class LinkInline(admin.TabularInline):
    model = Link
    extra = 1


class ImageInline(admin.TabularInline):
    model = Image
    extra = 1
    readonly_fields = ('image_tag', )
        
        
@admin.register(Dining)
class DiningAdmin(GISModelAdmin):
    list_display = [field.name for field in Dining._meta.fields]
    inlines = [LinkInline, ImageInline]


    gis_widget_kwargs = {
            'attrs': {
                'default_zoom': 11,
                'default_lat': 36.2971,
                'default_lon': 59.5953,
            },
        }
