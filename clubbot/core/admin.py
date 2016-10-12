from django.contrib import admin
from core.models import Club
from core.models import Role
from core.models import Membership


@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    pass


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    pass


@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    pass
