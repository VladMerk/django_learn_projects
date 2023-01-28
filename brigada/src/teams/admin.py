from django.contrib import admin

from teams.models import Team


class TeamAdminForm(admin.ModelAdmin):
    # fields = (('city', 'name'), 'head')
    list_display = ('city', 'name')
    list_display_links = ('name', )
    list_filter = ('city', )


admin.site.register(Team, TeamAdminForm)
