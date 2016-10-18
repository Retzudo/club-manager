from rest_framework import viewsets

from api import serializers
from core.models import Membership, Role


class ClubViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ClubSerializer

    def get_queryset(self):
        return self.request.user.memberships.all()

    def perform_create(self, serializer):
        club = serializer.save()
        admin_role = club.roles.filter(name='Administrator').first()
        default_membership = Membership(
            club=club,
            user=self.request.user,
            role=admin_role,
        )

        default_membership.save()
