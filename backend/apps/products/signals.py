from django.template.defaultfilters import slugify

from .models import Category
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver


@receiver(pre_save, sender=Category)
def slugify_category(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.name)
