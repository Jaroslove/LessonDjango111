from django import forms
from .models import Restorant


class RestoranCreateForm(forms.Form):
    name = forms.CharField(required=True)
    location = forms.CharField(required=False)
    category = forms.CharField(required=False)


class RestoranCreateFromTwo(forms.ModelForm):
    class Meta:
        model = Restorant
        fields = [
            'name',
            'location',
            'category'
        ]
