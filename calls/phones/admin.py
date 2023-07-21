"""Admin panels for phones application."""

from django.contrib import admin
from phones.models import Audio, Connection, Numbers


@admin.register(Connection)
class ConnectionAdmin(admin.ModelAdmin):
    """Admin panel for Connection model."""

    list_display = (
        'uuid',
        'server',
        'port',
        'username',
        'password',
        'local_ip',
        'user',
    )
    search_fields = ('username', 'user')
    list_filter = ('server', 'username')
    empty_value_display = '-empty-'


@admin.register(Audio)
class AudioAdmin(admin.ModelAdmin):
    """Admin panel for Audio model."""

    list_display = (
        'uuid',
        'audio_file',
        'user',
    )
    search_fields = ('audio_file',)
    list_filter = ('user',)
    empty_value_display = '-empty-'


@admin.register(Numbers)
class NumbersAdmin(admin.ModelAdmin):
    """Admin panel for Numbers model."""

    list_display = (
        'uuid',
        'numbers_file',
        'user',
    )
    search_fields = ('numbers_file',)
    list_filter = ('user',)
    empty_value_display = '-empty-'
