from django.contrib import admin

from cars.oauth_app.models import AppUser


# Register your models here.

@admin.register(AppUser)
class AppUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_email_verified', 'is_staff', 'is_superuser')
    ordering = ['-is_superuser', '-is_staff', 'username', ]
    list_filter = ['is_staff', ]
    search_fields = ("username__icontains",)
