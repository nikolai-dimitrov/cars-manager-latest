from django.contrib import admin

from cars.ad.models import Ad, City, Bookmark


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ('car_make', 'price', 'publication_date', 'user', 'year_of_manufacture')
    ordering = ['publication_date', ]
    list_filter = ['publication_date', ]
    search_fields = ('price__gt',)

    def car_make(self, obj):
        name = obj.car
        return name

    def user(self, obj):
        return obj.profile.user.username


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    pass


@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    pass
