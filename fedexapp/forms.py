from django import forms

class ShipmentForm(forms.Form):
    # Shipper information.
    shipper_country = forms.CharField(label='* Country', max_length=35)
    shipper_city = forms.CharField(label='* City', max_length=35)
    shipper_state = forms.CharField(label='* State', max_length=35)
    shipper_zipcode = forms.IntegerField(label='* Zip Code')

    shipper_company = forms.CharField(label='Company', max_length=35, required=False)   
    shipper_address1 = forms.CharField(label='* Address 1', max_length=35)
    shipper_address2 = forms.CharField(label='Address 2', max_length=35, required=False)
    shipper_phone = forms.CharField(label='* Phone no.', max_length=10)

    # Recipient information.
    recipient_country = forms.CharField(label='* Country', max_length=35)
    recipient_city = forms.CharField(label='* City', max_length=35)
    recipient_state = forms.CharField(label='* State', max_length=35)
    recipient_zipcode = forms.IntegerField(label='* Zip Code')
    
    recipient_company = forms.CharField(label='Company', max_length=35, required=False)   
    recipient_address1 = forms.CharField(label='* Address 1', max_length=35)
    recipient_address2 = forms.CharField(label='Address 2', max_length=35, required=False)
    recipient_phone = forms.CharField(label='* Phone no.', max_length=10)

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()