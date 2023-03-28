from django.contrib import admin
from django.contrib.gis.admin import GISModelAdmin
from django.utils.safestring import mark_safe

from .models import Dining, Link, Image


class LinkInline(admin.TabularInline):
    model = Link
    extra = 1


class ImageInline(admin.TabularInline):
    model = Image
    extra = 1
    readonly_fields = ('image_tag', )
    
    def image_tag(self, obj):
        return mark_safe(f"<img width='100' height='100' src={obj.image.url}/>")
    
    image_tag.short_description = 'Image Preview'

        
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
