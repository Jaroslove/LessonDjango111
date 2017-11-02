from django import forms
from .models import Restorant
from .validation import valid_email, valid_even, valid_location


class RestoranCreateForm(forms.Form):
    name = forms.CharField(required=True)
    location = forms.CharField(required=False)
    category = forms.CharField(required=False)


class RestoranCreateFromTwo(forms.ModelForm):
    location = forms.CharField(required=False, validators=[valid_location])

    class Meta:
        model = Restorant
        fields = [
            'name',
            'location',
            'category'
        ]
