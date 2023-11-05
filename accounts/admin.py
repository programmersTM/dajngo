from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_staff')
    list_per_page = 20
    # fieldsets = (
    #     ('User data', {'fields': ['username', 'email', 'password']}),
    # )
    ordering = ('username',)
    add_fieldsets = UserAdmin.add_fieldsets + (('Other fields', {'fields':['email']}),)


# admin.site.register(CustomUser, CustomUserAdmin)