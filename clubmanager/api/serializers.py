from rest_framework import serializers

from core.models import Club, Cash, Transaction, Event


class ClubSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(required=False)

    class Meta:
        model = Club
        fields = ('id', 'name', 'slug')


class TransactionSerializer(serializers.ModelSerializer):
    amount = serializers.FloatField()
    id = serializers.ReadOnlyField()

    class Meta:
        model = Transaction
        fields = ('id', 'amount', 'description', 'club_id')

    def get_field_names(self, declared_fields, info):
        return ['id', 'amount', 'description']


class CashSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cash
        fields = ('currency', 'total')


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
        read_only_fields = ('club',)
