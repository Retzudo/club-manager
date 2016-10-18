from rest_framework import viewsets

from api import serializers
from core.models import Membership, Club, Role


class ClubViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ClubSerializer

    def get_queryset(self):
        return Club.objects.filter(memberships__user=self.request.user).all()

    def perform_create(self, serializer):
        club = serializer.save()
        admin_role = club.roles.get(name=Role.ADMIN_ROLE)
        default_membership = Membership(
            club=club,
            user=self.request.user,
            role=admin_role,
        )

        default_membership.save()
