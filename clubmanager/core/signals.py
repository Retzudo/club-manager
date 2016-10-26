from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.utils.text import slugify

from core.models import Club, Role, Cash
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


@receiver(post_save, sender=Club)
def add_default_roles(instance, raw, created, using, update_fields, **kwargs):
    if created:
        # Add default roles
        admin_role = Role.new_admin_role(club=instance)
        member_role = Role.new_member_role(club=instance)

        admin_role.save()
        member_role.save()

        # Add cash object
        cash = Cash(club=instance)
        cash.save()