"""Admin panels for Users application."""

from django.contrib import admin
from django.contrib.auth.models import Group
from users.models import User

admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Admin panel for Connection model."""

    list_display = (
        'id',
        'username',
        'password',
    )
    search_fields = ('username',)
    list_filter = ('username',)
    empty_value_display = '-empty-'
