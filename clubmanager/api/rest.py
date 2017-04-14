from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from api import serializers
from core.models import Membership, Club, Role, Event, Transaction


class ClubModelViewSet(viewsets.ModelViewSet):
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

    @detail_route()
    def cash(self, request, pk=None):
        club = self.get_object()
        serializer = serializers.CashSerializer(club.cash)

        return Response(serializer.data)

    @detail_route()
    def transactions(self, request, pk=None):
        club = self.get_object()
        serializer = serializers.TransactionSerializer(club.cash.transactions.all(), many=True)

        return Response(serializer.data)


class TransactionsModelViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TransactionSerializer
    queryset = Transaction.objects.all()
    http_method_names = ['post', 'put', 'patch', 'delete', 'head']

    def perform_create(self, serializer):
        try:
            club = Club.objects.get()
        except Club.DoesNotExist:
            raise ValidationError()

        serializer.save(cash=club.cash)


class EventsViewSet(viewsets.ViewSet):
    def list(self, request, club_pk=None):
        club = get_object_or_404(Club, pk=club_pk)
        serializer = serializers.EventSerializer(club.events.all(), many=True)

        return Response(serializer.data)

    def create(self, request, club_pk=None):
        club = get_object_or_404(Club, pk=club_pk)
        serializer = serializers.EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(club=club)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def destroy(self, request, club_pk=None, pk=None):
        club = get_object_or_404(Club, pk=club_pk)

        try:
            event = club.events.get(pk=pk)
        except Event.DoesNotExist:
            raise Http404

        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)