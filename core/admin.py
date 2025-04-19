from django.contrib import admin
from .models import Sector, Startup



class SectorAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)
    

admin.site.register(Sector, SectorAdmin)
admin.site.register(Startup)
