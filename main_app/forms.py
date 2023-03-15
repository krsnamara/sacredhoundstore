from django.forms import ModelForm
from django import forms

class ContactForm(forms.Form):
    yourname = forms.CharField(max_length=100, label='Your Name')
    email = forms.EmailField(label='Your email address', required=False)
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)