# Generated by Django 4.1.4 on 2022-12-20 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0013_alter_profile_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='is_activated',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='is_banned',
        ),
    ]