from django.conf import settings
from django.db import models


class Club(models.Model):
    name = models.CharField(max_length=255)
    admin = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='admin_clubs'
    )
    members = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through='Membership',
        related_name='member_clubs',
    )

    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=255)
    club = models.ForeignKey(
        'Club',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name


class Membership(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    club = models.ForeignKey(
        'Club',
        on_delete=models.CASCADE,
    )
    role = models.ForeignKey(
        'Role',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
