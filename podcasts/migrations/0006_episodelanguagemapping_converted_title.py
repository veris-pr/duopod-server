# Generated by Django 2.1.1 on 2020-04-12 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('podcasts', '0005_subscription_subscriber'),
    ]

    operations = [
        migrations.AddField(
            model_name='episodelanguagemapping',
            name='converted_title',
            field=models.TextField(blank=True, null=True, verbose_name='Converted Title'),
        ),
    ]
