from rest_framework import serializers

from core.models import Club


class ClubSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Club
        fields = ('name',)
