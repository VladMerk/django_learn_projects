from django.contrib import admin

from cities.models import City


class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name', )

admin.site.register(City, CityAdmin)
