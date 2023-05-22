from django.contrib import admin

from cars.profiles.models import Profile


# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'age', 'phone_number', 'user',)
    ordering = ['user_id', ]
    list_filter = ['first_name', ]
    search_fields = ("first_name__icontains",)

    def user(self, obj):
        return obj.profile.user.username
