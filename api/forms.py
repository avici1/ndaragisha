from django import forms

from .models import *


class FoundItemsForms(forms.ModelForm):
    class Meta:
        model = FoundItems
        fields = ('img_path', 'found_desc', 'found_person_name', 'found_person_phone')
