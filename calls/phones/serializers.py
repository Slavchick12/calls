"""Serializers for Phones application."""

from uuid import uuid4

from phones.models import Audio, Connection, Numbers
from phones.utils.functions.system import get_local_ip
from rest_framework import serializers
from users.serializers import CustomUserSerializer


class ConnectionSerializer(serializers.ModelSerializer):
    """Serilizer for Connection model."""

    class Meta(object):
        """Class Meta for ConnectionSerializer."""

        user = CustomUserSerializer(read_only=True)

        model = Connection
        fields = (
            'uuid',
            'server',
            'port',
            'username',
            'password',
            'local_ip',
            'user',
        )
        read_only_fields = ('uuid', 'local_ip', 'user')

    def create(self, validated_data: dict) -> Connection:
        """Create Connection object.

        Parameters:
            validated_data: valited data from request body

        Returns:
            Connection object

        Raises:
            ValidationError: if object already exists
        """
        if Connection.objects.filter(user=validated_data['user']).exists():
            raise serializers.ValidationError('Connction parameters already created. You can change or delete them.')

        return Connection.objects.create(**validated_data, uuid=uuid4(), local_ip=get_local_ip())


class AudioSerializer(serializers.ModelSerializer):
    """Serilizer for Audio model."""

    user = CustomUserSerializer(read_only=True)

    class Meta(object):
        """Class Meta for AudioSerializer."""

        model = Audio
        fields = ('uuid', 'audio_file', 'name', 'user')
        read_only_fields = ('uuid', 'name')

    def create(self, validated_data: dict) -> Audio:
        """Create Audio object.

        Parameters:
            validated_data: valited data from request body

        Returns:
            Audio object

        Raises:
            ValidationError: if object already exists
        """
        audio_name = validated_data['audio_file'].name

        if Audio.objects.filter(user=validated_data['user'], name=audio_name).exists():
            raise serializers.ValidationError(f'Audio with name "{audio_name}" already exists.')

        return Audio.objects.create(**validated_data, uuid=uuid4(), name=audio_name)


class NumbersSerializer(serializers.ModelSerializer):
    """Serilizer for Numbers model."""

    user = CustomUserSerializer(read_only=True)

    class Meta(object):
        """Class Meta for NumbersSerializer."""

        model = Numbers
        fields = ('uuid', 'numbers_file', 'name', 'user')
        read_only_fields = ('uuid', 'name')

    def create(self, validated_data: dict) -> Numbers:
        """Create Numbers object.

        Parameters:
            validated_data: valited data from request body

        Returns:
            Numbers object

        Raises:
            ValidationError: if object already exists
        """
        numbers_name = validated_data['numbers_file'].name

        if Numbers.objects.filter(user=validated_data['user'], name=numbers_name).exists():
            raise serializers.ValidationError(f'Audio with name "{numbers_name}" already exists.')

        return Numbers.objects.create(**validated_data, uuid=uuid4(), name=numbers_name)
