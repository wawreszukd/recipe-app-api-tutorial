"""
Django admin customization
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from core import models


class UserAdmin(BaseUserAdmin):
    """Define the admin pages for users."""
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
        (_('Login data'), {'fields': ('email', 'password')}),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
            }
        ),
        (_('Importnat dates'), {'fields': ('last_login',)}),
    )
    readonly_fields = ['last_login']
    add_fieldsets = (
        (_('Login data'),
         {
             'classes': ('wide',),
             'fields': (
                 'email',
                 'password',
                 'password2',
                 'name',
                 'is_active',
                 'is_staff',
                 'is_superuser',
             )
        }),
    )


admin.site.register(models.User, UserAdmin)
