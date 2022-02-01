from django.contrib.admin import register
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


@register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email',)
    list_filter = ('first_name', 'email')
