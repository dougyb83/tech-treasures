# Generated by Django 3.2.23 on 2024-03-10 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20240310_0847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='has_options',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
