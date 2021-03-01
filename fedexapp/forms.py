from django import forms

class ShipperForm(forms.Form):
    country = forms.CharField(label='Country', max_length=35)
    city = forms.CharField(label='City', max_length=35)
    state = forms.CharField(label='State', max_length=35)
    zipcode = forms.IntegerField(label='Zip Code')

    company = forms.CharField(label='Company', max_length=35, required=False)   
    address1 = forms.CharField(label='Address 1', max_length=35)
    address2 = forms.CharField(label='Address 2', max_length=35, required=False)
    phone = forms.CharField(label='Phone no.', max_length=10)