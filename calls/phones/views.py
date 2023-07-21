"""Views for Phones application."""

from django.db.models import QuerySet
from phones.mixins import CRDRequestsMixins
from phones.models import Audio, Connection, Numbers
from phones.serializers import AudioSerializer, ConnectionSerializer, NumbersSerializer
from phones.utils.functions.calls import make_calls
from phones.utils.functions.reformats import get_uuid_from_string
from rest_framework import status, viewsets
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

MESSAGE_KEY = 'message'


class ConnectionViewSet(viewsets.ModelViewSet):
    """ViewSet for Connection model."""

    serializer_class = ConnectionSerializer

    def get_queryset(self) -> QuerySet[Connection]:
        """Get Connection objects per user.

        Returns:
            Queryset of Connection objects
        """
        return Connection.objects.filter(user=self.request.user)

    def perform_create(self, serializer: ConnectionSerializer) -> Connection:
        """Save user in serializer.

        Parameters:
            serializer: serializer for object

        Returns:
            Connection object
        """
        return serializer.save(user=self.request.user)


class NumbersViewSet(CRDRequestsMixins):
    """ViewSet for Numbers model."""

    serializer_class = NumbersSerializer

    def get_queryset(self) -> QuerySet[Numbers]:
        """Get Numbers objects per user.

        Returns:
            Queryset of Numbers objects
        """
        return Numbers.objects.filter(user=self.request.user)

    def perform_create(self, serializer: NumbersSerializer) -> Numbers:
        """Save user in serializer.

        Parameters:
            serializer: serializer for object

        Returns:
            Numbers object
        """
        return serializer.save(user=self.request.user)


class AudioViewSet(CRDRequestsMixins):
    """ViewSet for Audio model."""

    serializer_class = AudioSerializer

    def get_queryset(self) -> QuerySet[Audio]:
        """Get Audio objects per user.

        Returns:
            Queryset of Audio objects
        """
        return Audio.objects.filter(user=self.request.user)

    def perform_create(self, serializer: AudioSerializer) -> Audio:
        """Save user in serializer.

        Parameters:
            serializer: serializer for object

        Returns:
            Audio object
        """
        return serializer.save(user=self.request.user)


class Calls(APIView):
    """Call to user numbers list."""

    def get(self, request: Request) -> Response:
        """Get request for calls.

        Parameters:
            request: Request object

        Returns:
            Response: 200 the calls were successful and
            400 if the parameters are incorrect or there are none
        """
        numbers_str = request.GET.get('numbers_uuid')
        audio_str = request.GET.get('audio_uuid')

        if not numbers_str or not audio_str:
            return Response(
                {MESSAGE_KEY: 'Invalid one or more request parameters: "numbers_uuid", "audio_uuid".'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        numbers_uuid = get_uuid_from_string(numbers_str)
        audio_uuid = get_uuid_from_string(audio_str)

        if not numbers_uuid or not audio_uuid:
            return Response(
                {MESSAGE_KEY: 'One or more parameters have incorrect values.'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        make_calls(
            connection=Connection.objects.filter(user=self.request.user).first(),
            numbers_file=Numbers.objects.filter(uuid=numbers_uuid).first(),
            audio_file=Audio.objects.filter(uuid=audio_uuid).first(),
        )

        return Response(status=status.HTTP_200_OK)
