"""Mixins module for Phones application."""

from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated


class CRDRequestsMixins(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    """Get, Create and Delete methods to requests."""

    permission_classes = [IsAuthenticated]
