# Generated by Django 5.0.1 on 2024-01-09 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0021_alter_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='productImages'),
        ),
    ]
