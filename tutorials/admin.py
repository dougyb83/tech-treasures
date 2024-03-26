from django.contrib import admin
from .models import Tutorials


class TutorialAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'youtube_url',
        'youtube_embed_url',
        'additional_link',
    )

    ordering = ('title',)


admin.site.register(Tutorials, TutorialAdmin)
