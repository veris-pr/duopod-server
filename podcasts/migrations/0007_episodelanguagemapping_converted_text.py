# Generated by Django 2.1.1 on 2020-04-12 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('podcasts', '0006_episodelanguagemapping_converted_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='episodelanguagemapping',
            name='converted_text',
            field=models.TextField(blank=True, null=True, verbose_name='Converted Text'),
        ),
    ]
