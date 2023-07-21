"""Models for Users application."""

from django.contrib.auth.models import AbstractUser

USERNAME_LENGTH = 50


class User(AbstractUser):
    """User model."""

    class Meta(object):
        """Meta class for User model."""

        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        """Get string field.

        Returns:
            Username field
        """
        return self.username
