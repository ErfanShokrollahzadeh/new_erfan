from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'created_at', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'created_at')
    search_fields = ('username', 'email')
    ordering = ('-created_at',)

admin.site.register(User, CustomUserAdmin)
