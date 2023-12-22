from django import forms


class AddProduct(forms.Form):
    objects = None
    title = forms.CharField(max_length=20)
    price = forms.IntegerField(min_value=0)
