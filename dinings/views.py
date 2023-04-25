from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from django.db import transaction
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

import folium
from folium.plugins import LocateControl, Search

from .models import Dining
from .forms import DiningForm, ImageFormSet, LinkFormSet
from .map_utils import make_markers_and_add_to_map, make_popup_data



class CreateDining(SuccessMessageMixin, CreateView):
    template_name = 'add_new_dining_form.html'
    model = Dining
    form_class = DiningForm
    success_url = reverse_lazy('dinings:add-dining')
    success_message = "Your request was sent successfully! We'll let you know when it's confirmed"
   
    def get_success_message(self, cleaned_data):
        return messages.success(self.request, self.success_message, extra_tags='alert-success')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['formset1'] = ImageFormSet(self.request.POST, self.request.FILES, instance=self.object)
            context['formset2'] = LinkFormSet(self.request.POST, instance=self.object)       
        else:
            context['formset1'] = ImageFormSet(instance=self.object)
            context['formset2'] = LinkFormSet(instance=self.object)
        return context
    
    def form_valid(self, form, formset1, formset2):

        with transaction.atomic():
            self.object = form.save()

        if formset1.is_valid():
            formset1.instance = self.object
            formset1.save()
        if formset2.is_valid():
            formset2.instance = self.object
            formset2.save()

        return super().form_valid(form)

    def form_invalid(self, form, formset1, formset2):

        return self.render_to_response(self.get_context_data(form=form, formset1=formset1, formset2=formset2))

    def post(self, request, *args, **kwargs):

        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        formset1 = ImageFormSet(self.request.POST, self.request.FILES)
        formset2 = LinkFormSet(self.request.POST)
        
        if form.is_valid() and formset1.is_valid() and formset2.is_valid():
            
            return self.form_valid(form, formset1, formset2)
        else:
            return self.form_invalid(form, formset1, formset2)


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
    
