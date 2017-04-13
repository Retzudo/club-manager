from rest_framework import serializers

from core.models import Club, Cash, Transaction


class ClubSerializer(serializers.HyperlinkedModelSerializer):
    slug = serializers.SlugField(required=False)

    class Meta:
        model = Club
        fields = ('id', 'name', 'slug')


class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    amount = serializers.FloatField()

    class Meta:
        model = Transaction
        fields = ('amount', 'description', 'date')


class CashSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cash
        fields = ('currency', 'total')
