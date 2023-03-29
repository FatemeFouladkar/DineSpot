from django.template.loader import render_to_string

import folium
import branca 

from .models import Dining, Link, Image


def make_popup_data(dining, request):
    context = {
          'dining': dining,
          'request': request
    }
    return render_to_string('popup_data.html', context=context)


def make_markers_and_add_to_map(map, popup_data, dining):
        iframe = branca.element.IFrame(html=popup_data, width=300, height=400)
        popup = folium.Popup(iframe, max_width=300)
        
        folium.Marker(
            location = [dining.latitude, dining.longitude],
            popup=popup,
            tooltip = dining.name,
            icon = folium.Icon(icon='fa-coffee', prefix='fa')
        ).add_to(map)
