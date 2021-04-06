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
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            None,
            {
                "fields": (
                    "email",
                    "first_name",
                    "last_name",
                    "avatar",
                    "platform_choice_field",
                )
            },
        ),
    )
    fieldsets = UserAdmin.fieldsets


admin.site.register(CustomUser, CustomUserAdmin)