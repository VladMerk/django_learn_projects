from django.contrib import admin

from trains.models import Trains

class TrainAdmin(admin.ModelAdmin):
    list_display = ('name', 'from_city', 'to_city', 'travel_time')
    list_editable = ('travel_time', )
    list_filter = ('from_city', 'to_city')

    class Meta:
        model = Trains


admin.site.register(Trains, TrainAdmin)
