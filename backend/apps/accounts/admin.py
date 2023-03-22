from django.contrib import admin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin
from .models import Customer, CustomerAddress
from django.contrib.auth import get_user_model
Account = get_user_model()


@admin.register(Account)
class AccountAdmin(UserAdmin):

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "phone_numbers", "is_customer", )}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "first_name", "last_name", "is_customer", "is_staff", "password1", "password2"),
            },
        ),
    )
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ("email", "first_name", "last_name", "is_staff")
    list_filter = ("is_staff", "is_superuser", "is_active", "groups")
    search_fields = ("first_name", "last_name", "email")
    ordering = ("id",)
    filter_horizontal = (
        "groups",
        "user_permissions",
    )

    readonly_fields = ['last_login', 'date_joined', ]


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):

    readonly_fields = ['device', ]


@admin.register(CustomerAddress)
class CustomerAddressAdmin(admin.ModelAdmin):
    pass
