# Generated by Django 3.2.23 on 2024-01-20 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['sku']},
        ),
        migrations.RenameField(
            model_name='product',
            old_name='has_sizes',
            new_name='has_options',
        ),
        migrations.AddField(
            model_name='product',
            name='option_title',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='options',
            field=models.TextField(blank=True, null=True),
        ),
    ]
