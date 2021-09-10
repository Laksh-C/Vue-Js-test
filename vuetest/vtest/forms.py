from django import forms

from .models import testmodel

class ProductCreateForm(forms.ModelForm):
    name = forms.CharField(widget = forms.TextInput())
    description = forms.CharField(max_length = 200)
    price = forms.FloatField(widget = forms.NumberInput())

    class Meta:
        model = testmodel
        fields = ['name', 'description', 'price']