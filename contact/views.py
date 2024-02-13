from django.shortcuts import render
from .forms import ContactForm


def contact(request):
    """ returns the contact page """
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            print("form is valid")
            # Process the form data (e.g., send an email)
            # Add your logic here
    else:
        contact_form = ContactForm()

    return render(request, 'contact/contact.html', {
        'contact_form': contact_form})
