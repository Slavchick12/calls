"""Application config module."""

from django.apps import AppConfig


class UsersConfig(AppConfig):
    """Config for Users application."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
