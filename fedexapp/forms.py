from django import forms

class NameForm(forms.Form):
    shipper_name = forms.CharField(label='shipper_name', max_length=35)

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea, default='foo')
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)