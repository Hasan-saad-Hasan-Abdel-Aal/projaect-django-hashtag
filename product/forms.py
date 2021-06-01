from django import forms
# from django.forms.models import ModelForm
from . models import Product

class ProductForm(forms.ModelForm):
    """Form definition for Product."""

    class Meta:
        """Meta definition for Productform."""

        model = Product
        fields = ('ProCtegory','ProBrand','ProBrand')
