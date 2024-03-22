from django.db import models


class Tutorials(models.Model):
    title = models.CharField(max_length=254)
    description = models.TextField()
    youtube_url = models.CharField(max_length=500)
    youtube_embed_url = models.CharField(max_length=500, null=True, blank=True)
    additional_link = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.title
