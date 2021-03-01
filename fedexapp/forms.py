from django import forms

class NameForm(forms.Form):
    shipper_name = forms.CharField(label='shipper_name', max_length=35)