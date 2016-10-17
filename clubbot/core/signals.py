from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify

from core.models import Club
from core.utils.names import get_random_slug


@receiver(pre_save, sender=Club)
def slugify_club_name(sender, instance, raw, using, update_fields, **kwargs):
    if not instance.slug:
        slug = slugify(instance.name)

        # Check if slug already exists
        if not Club.objects.filter(slug=slug):
            instance.slug = slug
            return

        slug = get_random_slug()
        while Club.objects.filter(slug=slug):
            # Create new slugs if the last one exists already
            slug = get_random_slug()

        instance.slug = slug
