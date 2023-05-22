# Generated by Django 4.1.4 on 2022-12-26 15:40

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ad', '0010_alter_photo_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, default='https://res.cloudinary.com/dltjy2gzz/image/upload/v1672068988/cars/default/no-image-icon-15_jm4w3b.png', max_length=255, null=True, verbose_name='Image'),
        ),
    ]
