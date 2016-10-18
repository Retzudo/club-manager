from rest_framework import serializers

from core.models import Club, Cash, Transaction


class ClubSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Club
        fields = ('id', 'name', 'slug')
        # Slug is not required because it will be generated
        # if left out.
        extra_kwargs = {'slug': {'required': False}}


class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transaction
        fields = ('amount', 'description', 'date')


class CashSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cash
        fields = ('currency', 'total')
