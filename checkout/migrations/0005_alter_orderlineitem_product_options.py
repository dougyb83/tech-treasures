# Generated by Django 3.2.23 on 2024-03-03 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_order_user_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderlineitem',
            name='product_options',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
