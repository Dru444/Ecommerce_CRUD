from django import forms
from .models import Product,OFFERS,WARRANTY


class ProductForm(forms.ModelForm):
    offers = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(
         attrs={
                'class': 'list-unstyled'
               
            }
    ),choices= OFFERS,required = False,)

    warranty = forms.ChoiceField(widget=forms.RadioSelect(),choices=WARRANTY)
    class Meta:
        model = Product
        fields = '__all__'

        