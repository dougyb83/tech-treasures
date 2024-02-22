from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail, send_mass_mail
from django.template.loader import render_to_string
from .models import Contact
from .forms import ContactForm


def contact(request):
    """ returns the contact page """
    contact_form = ContactForm(request.POST or None)
    if request.method == 'POST':
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, 'Your message has been sent!')

            # form data collection
            form_context = {
                "full_name": request.POST.get("full_name"),
                "email": request.POST.get("email"),
                "message": request.POST.get("message"),
            }

            # create email to customer
            customer_email = (
                "Tech Treasures has recieved your message",
                render_to_string(
                    "contact/emails/contact-email-notifiaction.txt",
                    {"form_context": form_context}
                ),
                settings.DEFAULT_FROM_EMAIL,
                [form_context["email"]],
            )

            # create email to admin
            admin_email = (
                "New message from Customer",
                render_to_string(
                    "contact/emails/admin-contact-notifiaction.txt",
                    {"form_context": form_context}
                ),
                settings.DEFAULT_FROM_EMAIL,
                [settings.DEFAULT_FROM_EMAIL],
            )

            # send emails
            send_mass_mail((customer_email, admin_email))

            # take the user back to home page
            return redirect(reverse('home'))

        # error on form
        messages.error(request, 'Error, please try again.')

    template = 'contact/contact.html'
    context = {
        'contact_form': contact_form,
    }
    return render(request, template, context)


def admin_contact_page(request, email_id=None):
    """ returns the admin contact page """
    if not request.user.is_superuser:
        # user is not superuser; take them to home page
        messages.error(request, "Access denied. Invalid permissions.")
        return redirect(reverse("home"))

    # is superuser; can proceed
    emails = Contact.objects.all()

    template = 'contact/admin-contact.html'
    context = {
        'emails': emails,
    }

    return render(request, template, context)


def admin_contact_reply(request, email_id=None):
    """ returns the admin contact page """
    if not request.user.is_superuser:
        # user is not superuser; take them to home page
        messages.error(request, "Access denied. Invalid permissions.")
        return redirect(reverse("home"))

    # is superuser; can proceed
    email = get_object_or_404(Contact, id=email_id)

    email.have_read = True
    email.save()

    template = 'contact/admin-contact-reply.html'
    context = {
        'email': email,
    }

    return render(request, template, context)


def reply_email(request, email_id):
    """Handles replying to an email."""
    if request.method == 'POST':
        email = get_object_or_404(Contact, id=email_id)
        reply_text = request.POST.get('reply')

        if reply_text:
            # Update the database to set have_replied to True
            email.have_replied = True
            email.save()

            # form data collection
            form_context = {
                "reply": request.POST.get("reply"),
                "original_message": email.message,
                "email": email.email
            }

            send_mail(
                "New Message from Tech Treasures",
                render_to_string(
                    "contact/emails/customer-email-reply.txt",
                    {"form_context": form_context}
                ),
                settings.DEFAULT_FROM_EMAIL,
                [form_context["email"]]
            )

            messages.success(request, 'Reply sent successfully!')
            return redirect(reverse('admin-contact'))
        else:
            messages.error(request, 'Reply cannot be empty.')
            
    template = 'contact/admin-contact-reply.html'
    context = {
        'email': email,
    }

    return render(request, template, context)


def delete_email(request, email_id):
    email = get_object_or_404(Contact, id=email_id)
    email.delete()

    messages.success(request, 'Message deleted successfully!')
    return redirect(reverse('admin-contact'))
