from django.views.generic import TemplateView

import folium
from folium.plugins import LocateControl, Search

from .models import Dining
from .map_utils import make_markers_and_add_to_map, make_popup_data


class MapView(TemplateView):
    template_name = 'map.html'    

    def get_context_data(self, **kwargs):
        figure = folium.Figure()
        map = folium.Map(
            location = [36.2971, 59.5953],
            zoom_start = 13,
            tiles = 'OpenStreetMap',
            control_scale=True,
            height='90%',
            max_bounds=True
        )
        map.add_to(figure)
        
        for dining in Dining.objects.all():
            popup_data = make_popup_data(dining, self.request)
            make_markers_and_add_to_map(map, popup_data, dining)

        LocateControl().add_to(map)

        figure.render()
        return {"map": figure}
    
