# Generated by Django 5.0.1 on 2024-01-09 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0019_alter_item_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(upload_to='productImages'),
        ),
    ]
