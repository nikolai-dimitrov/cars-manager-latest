# Generated by Django 4.1.3 on 2022-12-12 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0011_deletecode_remove_profile_delete_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deletecode',
            name='confirm_delete_code',
        ),
    ]
