from django.conf import settings
from django.db import models


class Club(models.Model):
    """A club."""
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Role(models.Model):
    """A role a member can have."""
    name = models.CharField(max_length=255)
    can_delete = models.BooleanField(default=True)
    club = models.ForeignKey(
        'Club',
        on_delete=models.CASCADE,
        related_name='roles',
    )

    @classmethod
    def new_admin_role(cls, club):
        role = cls(club=club)
        role.name = 'Administrator'
        role.can_delete = False
        return role

    @classmethod
    def new_member_role(cls, club):
        role = cls(club=club)
        role.name = 'Member'
        role.can_delete = False
        return role

    def __str__(self):
        return self.name


class Membership(models.Model):
    """A user-club relationship."""
    name = models.CharField(max_length=255, null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    bio = models.TextField()
    club = models.ForeignKey(
        'Club',
        on_delete=models.CASCADE,
        related_name='memberships',
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='memberships',
    )
    role = models.ForeignKey(
        'Role',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='memberships',
    )


class News(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    club = models.ForeignKey('Club')

    class Meta:
        ordering = ('-date',)


class Event(models.Model):
    """Events like festivals concerning the club."""
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True, blank=True)
    location = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()
    club = models.ForeignKey(
        'Club',
        related_name='events',
        on_delete=models.CASCADE,
    )


class Cash(models.Model):
    """The available cash of a club. Sum of transactions."""
    currency = models.CharField(max_length=3, default='EUR')
    club = models.OneToOneField('Club', related_name='cash')


class Transaction(models.Model):
    """A single transaction to or from a club's cash."""
    cash = models.ForeignKey('Cash', related_name='transactions')
    amount = models.FloatField()