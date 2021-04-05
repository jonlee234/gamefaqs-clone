from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser
# import auth forms

class CustomUserAdmin(UserAdmin):
    # add auth forms
    model = CustomUser
    list_display = [
        "username",
        "email",
        "bio",
        "platform_choice_field",
        "avatar",
    ]


admin.site.register(CustomUser, CustomUserAdmin)