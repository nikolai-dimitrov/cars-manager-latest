from cloudinary import uploader
from django.db.models.signals import pre_delete, pre_save, post_save
from django.dispatch import receiver

from cars.ad.models import Ad, Photo


@receiver(pre_delete, sender=Ad)
def ad_pre_delete_images(sender, instance, *args, **kwargs):
    image_set = instance.photo_set.all()
    for i in range(len(image_set)):
        current_image = image_set[i]
        uploader.destroy(f'{current_image.image}')

