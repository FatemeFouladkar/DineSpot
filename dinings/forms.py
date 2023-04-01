from django import forms 

from .models import Dining, Link, Image


class DiningForm(forms.ModelForm):
    class Meta:
        model = Dining
        fields = ('name', 'address', 'phone_number', 'description')

    
ImageFormSet = forms.inlineformset_factory(Dining, Image, fields=('image', ), extra=1, can_delete=False)
LinkFormSet = forms.inlineformset_factory(Dining, Link, fields=('key','value'), extra=2, can_delete=False)


