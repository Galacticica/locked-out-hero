from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (
            None,
            {
                "fields": (
                    "j_number",
                    "gender",
                    "dorm",
                    "accessible_buildings",
                    "times_used",
                )
            },
        ),
    )


# Register your models here.
admin.site.register(User, CustomUserAdmin)
