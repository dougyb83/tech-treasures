from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """ Form to allow users to submit a contact to site admins. """

    class Meta:
        model = Contact
        fields = ["full_name", "email", "message"]
