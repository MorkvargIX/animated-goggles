from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm


# Register your models here.


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ['email', 'username', 'age']
    model = CustomUser


admin.site.register(CustomUser, CustomUserAdmin)
