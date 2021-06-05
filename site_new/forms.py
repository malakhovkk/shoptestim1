from django import forms
from django.db.models import fields
from .models import Products
class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['id','origname','code','uid']
    #origname = forms.CharField(label='origname', max_length=100)
    #code = forms.CharField(label='code', max_length=100)
    #uid = forms.CharField(label='uid', max_length=100)