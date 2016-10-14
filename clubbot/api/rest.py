from rest_framework import viewsets

from api import serializers


class ClubViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ClubSerializer

    def get_queryset(self):
        return self.request.user.admin_clubs.all()

    def perform_create(self, serializer):
        serializer.save(admin=self.request.user)
