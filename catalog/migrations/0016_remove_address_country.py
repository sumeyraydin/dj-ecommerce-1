# Generated by Django 5.0.1 on 2024-01-08 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0015_item_country'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='country',
        ),
    ]
