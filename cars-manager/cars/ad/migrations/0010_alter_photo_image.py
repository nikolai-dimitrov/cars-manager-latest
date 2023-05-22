# Generated by Django 4.1.4 on 2022-12-21 21:02

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ad', '0009_remove_ad_image1_remove_ad_image2_remove_ad_image3_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, default='https://res.cloudinary.com/dltjy2gzz/image/upload/v1669814122/cars/default/no-image-icon-15_p4ng0f.png', max_length=255, null=True, verbose_name='Image'),
        ),
    ]