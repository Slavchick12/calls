"""Serializers for Users application."""

from rest_framework import serializers
from users.models import User


class CustomUserSerializer(serializers.ModelSerializer):
    """Serilizer for User model."""

    class Meta(object):
        """Class Meta for CustomUserSerializer."""

        model = User
        fields = (
            'email',
            'username',
        )
