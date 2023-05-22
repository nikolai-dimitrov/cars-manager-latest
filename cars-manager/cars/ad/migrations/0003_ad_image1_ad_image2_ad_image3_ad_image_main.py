# Generated by Django 4.1.3 on 2022-11-30 13:17

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ad', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='image1',
            field=cloudinary.models.CloudinaryField(default='https://res.cloudinary.com/dltjy2gzz/image/upload/v1669814122/cars/default/no-image-icon-15_p4ng0f.png', max_length=255, verbose_name='Image'),
        ),
        migrations.AddField(
            model_name='ad',
            name='image2',
            field=cloudinary.models.CloudinaryField(default='https://res.cloudinary.com/dltjy2gzz/image/upload/v1669814122/cars/default/no-image-icon-15_p4ng0f.png', max_length=255, verbose_name='Image'),
        ),
        migrations.AddField(
            model_name='ad',
            name='image3',
            field=cloudinary.models.CloudinaryField(default='https://res.cloudinary.com/dltjy2gzz/image/upload/v1669814122/cars/default/no-image-icon-15_p4ng0f.png', max_length=255, verbose_name='Image'),
        ),
        migrations.AddField(
            model_name='ad',
            name='image_main',
            field=cloudinary.models.CloudinaryField(default='https://res.cloudinary.com/dltjy2gzz/image/upload/v1669814122/cars/default/no-image-icon-15_p4ng0f.png', max_length=255, verbose_name='Image'),
        ),
    ]