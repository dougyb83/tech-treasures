# Generated by Django 3.2.23 on 2024-03-15 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0002_auto_20240310_1653'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutorials',
            name='youtube_embed_url',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
