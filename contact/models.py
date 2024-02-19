from django.db import models


class Contact(models.Model):
    """ Contact form fields """

    full_name = models.CharField(max_length=75, blank=False, null=False)
    email = models.EmailField(max_length=256, blank=False, null=False)
    message = models.TextField(blank=False, null=False)
    have_read = models.BooleanField(default=False)
    have_replied = models.BooleanField(default=False)
    date_sent = models.DateTimeField(auto_now_add=True, blank=False, null=False)

    def __str__(self):
        return self.email
