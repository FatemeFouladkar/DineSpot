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
                form.fields['key'].initial = 'Email' 
                form.fields['value'].label = 'Email' 
                form.fields['value'].help_text = 'Fill out this field to be informed when your dining spot in confirmed'
            elif i == 1: 
                form.fields['key'].initial = 'Instagram' 
                form.fields['value'].label = 'Instagram' 
            else: 
                form.fields['key'].initial = 'Website' 
                form.fields['value'].label = 'Website' 


ImageFormSet = forms.inlineformset_factory(Dining, Image, fields=('image', ), extra=1, can_delete=False)
LinkFormSet = forms.inlineformset_factory(Dining, Link, formset=LinkFormSet, fields=('key', 'value' ), extra=3, can_delete=False, widgets={ 'key': forms.HiddenInput()})


