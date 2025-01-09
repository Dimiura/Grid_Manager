from django.contrib import admin
from pilots.models import Pilot, Team, Autodromo

class PilotAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'age', 'team')
    search_fields = ('name', 'team')


admin.site.register(Pilot, PilotAdmin)

class TeamAdmin(admin.ModelAdmin):
    list_display = ( 'namet', )
    search_fields = ('namet', )


class AutodromoAdmin(admin.ModelAdmin):
    list_display = ( 'name_autodromo', )
    search_fields = ('name_autodromo', )



admin.site.register(Autodromo, AutodromoAdmin)

admin.site.register(Team, TeamAdmin)