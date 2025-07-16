from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
# Register your models here.

admin.site.register(User)

# class CustomUserAdmin(BaseUserAdmin):
#     model = User
#     list_display = ('username', 'email', 'role', 'is_staff')
#     fieldsets = BaseUserAdmin.fieldsets + (
#         (None, {'fields': ('role', 'contact_num', 'address')}),
#     )

# admin.site.register(User, CustomUserAdmin)

