from django import forms
from .models import Resource

class ResourceFilterForm(forms.ModelForm):

    class Meta:
        model = Resource
        fields = ('aspiration', 'group', 'level')
        