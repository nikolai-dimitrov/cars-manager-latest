# Generated by Django 4.1.4 on 2022-12-21 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ad', '0008_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ad',
            name='image1',
        ),
        migrations.RemoveField(
            model_name='ad',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='ad',
            name='image3',
        ),
        migrations.RemoveField(
            model_name='ad',
            name='image_main',
        ),
    ]
