from django.contrib import admin

from .models import GrupoA, GrupoB


class GrupoAAdmin(admin.ModelAdmin):
    list_display = ('usuario',)
    
    list_display_links = (
        'usuario',
    )

class GrupoBAdmin(admin.ModelAdmin):
    list_display = ('usuario',)
    
    list_display_links = (
        'usuario',
    )
    
    
admin.site.register(GrupoA, GrupoAAdmin)
admin.site.register(GrupoB, GrupoBAdmin)