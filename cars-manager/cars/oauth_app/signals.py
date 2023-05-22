from cloudinary import uploader
from django.db.models.signals import pre_delete, post_save
from django.dispatch import receiver

from cars.oauth_app.models import AppUser
from cars.profiles.models import Profile, DeleteCode


@receiver(pre_delete, sender=Profile)
def profile_pre_delete_images(sender, instance, *args, **kwargs):
    uploader.destroy(f'profiles/{instance.get_username}')


@receiver(post_save, sender=AppUser)
def create_profile_to_user(sender, instance, created, *args, **kwargs):
    if created:
        Profile.objects.create(user=instance).save()


@receiver(post_save, sender=Profile)
def create_empty_delete_code_model_to_profile(sender, instance, created, *args, **kwargs):
    if created:
        DeleteCode.objects.create(profile=instance).save()
