from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_options = models.BooleanField(default=False, blank=True)
    option_title = models.CharField(max_length=254, null=True, blank=True)
    option_1 = models.CharField(max_length=254, null=True, blank=True)
    option_2 = models.CharField(max_length=254, null=True, blank=True)
    option_3 = models.CharField(max_length=254, null=True, blank=True)
    option_4 = models.CharField(max_length=254, null=True, blank=True)
    option_5 = models.CharField(max_length=254, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    class Meta:
        ordering = ["sku"]

    def __str__(self):
        return self.name
