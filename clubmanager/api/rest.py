from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet

from api import serializers
from core.models import Membership, Club, Role


class ClubViewSet(viewsets.ModelViewSet):
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


class TransactionsViewSet(ViewSet):
    def list(self, request, club_pk=None):
        club = get_object_or_404(Club, pk=club_pk)
        serializer = serializers.TransactionSerializer(club.cash.transactions.all(), many=True)

        return Response(serializer.data)

    def create(self, request, club_pk=None):
        club = get_object_or_404(Club, pk=club_pk)
        serializer = serializers.TransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(cash=club.cash)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
