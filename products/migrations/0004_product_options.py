# Generated by Django 3.2.23 on 2024-01-20 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_remove_product_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='options',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
