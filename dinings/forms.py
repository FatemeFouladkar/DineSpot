from django import forms 

from .models import Dining, Link, Image


class DiningForm(forms.ModelForm):
    class Meta:
        model = Dining
        fields = ('name', 'address', 'phone_number', 'description')

    
class LinkFormSet(forms.BaseInlineFormSet):
    class Meta:
        model = Link
        fields = ('key', 'value')
        widgets = {
            'key': forms.HiddenInput(),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i, form in enumerate(self.forms):
            if i == 0:
                form.fields['key'].initial = 'Website' 
                form.fields['value'].label = 'Website' 
            else: 
                form.fields['key'].initial = 'Instagram' 
                form.fields['value'].label = 'Instagram' 

ImageFormSet = forms.inlineformset_factory(Dining, Image, fields=('image', ), extra=1, can_delete=False)
LinkFormSet = forms.inlineformset_factory(Dining, Link, formset=LinkFormSet, fields=('key', 'value' ), extra=2, can_delete=False, widgets={ 'key': forms.HiddenInput()})


