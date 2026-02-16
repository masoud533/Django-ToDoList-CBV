from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('email', "is_superuser", "is_active")
    list_filter = ('email', "is_superuser", "is_active")
    search_fields = ('email',)
    ordering = ('email',)
    fieldsets = (
        (None, {
            "fields": (
                'email', 'password'
            ),
        }),
        ('permissions', {
            "fields": (
                "is_staff", 'is_active', 'is_superuser'
            ),
        }),
        ('group permissions', {
            "fields": (
                "groups", 'user_permissions',
            ),
        }),
        ('important date', {
            "fields": (
                "last_login",
            ),
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_superuser', 'is_active')
        }),
    )

admin.site.register(User,CustomUserAdmin)