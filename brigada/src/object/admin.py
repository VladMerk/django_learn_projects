from django.contrib import admin

from object.models import Object


class ObjectAdmin(admin.ModelAdmin):
    list_display = ('city', 'team', 'name')
    list_display_links = ('name',)
    list_filter = ('city', 'team')


admin.site.register(Object, ObjectAdmin)
