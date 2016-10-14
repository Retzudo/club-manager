from rest_framework import viewsets

from core.models import Club


class ClubViewSet(viewsets.ModelViewSet):
    queryset = Club.objects.all()
    model = Club
