# Generated by Django 3.2.23 on 2024-01-20 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='option_title',
        ),
        migrations.RemoveField(
            model_name='product',
            name='options',
        ),
        migrations.AddField(
            model_name='product',
            name='option_details',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
