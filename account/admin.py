from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import CustomUser

# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'role')
    add_fieldsets = (
        (None, {'fields': ('username', 'first_name', 'last_name', 'role', 'password1', 'password2')}),
    )