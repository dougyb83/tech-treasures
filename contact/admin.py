from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'date_sent',
        'full_name',
        'email',
        'message',
        'have_read',
        'have_replied',
    )

    ordering = ('date_sent',)


admin.site.register(Contact, ContactAdmin)
