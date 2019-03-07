from django import forms
from .models import ContactModelForm



class ContactForm(forms.ModelForm):
    class Meta():
        fields = '__all__'
        model = ContactModelForm
