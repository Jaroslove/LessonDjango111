from django import forms


class RestoranCreateForm(forms.Form):
    name = forms.CharField(required=True)
    location = forms.CharField(required=False)
    category = forms.CharField(required=False)
