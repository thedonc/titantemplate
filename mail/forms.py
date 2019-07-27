from django import forms

class ContactForm(forms.Form):
    your_email = forms.EmailField(max_length=100, required=True)
    subject = forms.CharField(max_length=50, required=True)
    message = forms.CharField(max_length=50, required=True)