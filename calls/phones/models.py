"""Models for Phones application."""

from django.core.validators import FileExtensionValidator
from django.db import models
from phones.utils.functions.reformats import get_user_audio_path, get_user_numbers_path
from users.models import User

USERNAME_LENGTH = 50


class Connection(models.Model):
    """Phone connection model."""

    uuid = models.UUIDField(verbose_name='uuid', primary_key=True, help_text='connection uuid')
    server = models.CharField(verbose_name='server', max_length=100, help_text='server host name')
    port = models.PositiveIntegerField(verbose_name='port', help_text='connection port')
    username = models.CharField(verbose_name='username', max_length=USERNAME_LENGTH, help_text='connection username')
    password = models.CharField(verbose_name='password', max_length=100, help_text='connection password')
    local_ip = models.CharField(verbose_name='local_ip', max_length=100, help_text='local IP')
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name='user_connection', verbose_name='user')

    class Meta(object):
        """Meta class for Connection model."""

        ordering = ('server',)
        verbose_name = 'Connection'
        verbose_name_plural = 'Connections'

    def __str__(self):
        """Get string field.

        Returns:
            Username field
        """
        return self.username


class Numbers(models.Model):
    """Phone model."""

    numbers_file = models.FileField(
        verbose_name='numbers',
        help_text='phone numbers file',
        unique=True,
        upload_to=get_user_numbers_path,
        validators=[
            FileExtensionValidator(
                allowed_extensions=[
                    'txt',
                ],
            ),
        ],
    )
    uuid = models.UUIDField(verbose_name='uuid', primary_key=True, help_text='connection uuid')
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='user_numbers', verbose_name='user')
    name = models.CharField(verbose_name='name', max_length=100, help_text='file name', unique=True)


class Audio(models.Model):
    """Audio model."""

    audio_file = models.FileField(
        verbose_name='audio',
        help_text='audio file',
        unique=True,
        upload_to=get_user_audio_path,
        validators=[
            FileExtensionValidator(
                allowed_extensions=[
                    'mp3',
                    'aac',
                    'midi',
                    'm4a',
                    'ogg',
                    'flac',
                    'wav',
                    'amr',
                    'aiff',
                ],
            ),
        ],
    )
    uuid = models.UUIDField(verbose_name='uuid', primary_key=True, help_text='connection uuid')
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='user_audio', verbose_name='user')
    name = models.CharField(verbose_name='name', max_length=100, help_text='file name', unique=True)
