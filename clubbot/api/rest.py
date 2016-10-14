from rest_framework import viewsets

from api import serializers
from core.models import Club


class ClubViewSet(viewsets.ModelViewSet):
    queryset = Club.objects.all()
    serializer_class = serializers.ClubSerializer
