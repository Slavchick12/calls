"""Application config module."""

from django.apps import AppConfig


class PhonesConfig(AppConfig):
    """Config for Phones application."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'phones'
