from django.contrib import admin
from core.models import Club
from core.models import Role
from core.models import Membership

admin.site.register(Club)
admin.site.register(Role)
admin.site.register(Membership)
