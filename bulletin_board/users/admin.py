from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, UserProfile


@admin.register(UserProfile)
class UserProfileInline(admin.ModelAdmin):
    pass


@admin.register(User)
class UserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'phone_number',)}),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Statuses', {'fields': ('following', 'is_banned',)}),
    )
    filter_horizontal = ('following',)
