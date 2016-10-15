from rest_framework import serializers

from core.models import Club


class ClubSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Club
        fields = ('id', 'name', 'slug')
        # Slug is not required because it will be generated
        # if left out.
        extra_kwargs = {'slug': {'required': False}}
