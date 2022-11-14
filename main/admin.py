from django.contrib import admin

from .models import *


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

class GrupoCAdmin(admin.ModelAdmin):
    list_display = ('usuario',)
    
    list_display_links = (
        'usuario',
    )

class GrupoDAdmin(admin.ModelAdmin):
    list_display = ('usuario',)
    
    list_display_links = (
        'usuario',
    )

class GrupoEAdmin(admin.ModelAdmin):
    list_display = ('usuario',)
    
    list_display_links = (
        'usuario',
    )
    
class GrupoFAdmin(admin.ModelAdmin):
    list_display = ('usuario',)
    
    list_display_links = (
        'usuario',
    )
    
class GrupoGAdmin(admin.ModelAdmin):
    list_display = ('usuario',)
    
    list_display_links = (
        'usuario',
    )

class GrupoHAdmin(admin.ModelAdmin):
    list_display = ('usuario',)
    
    list_display_links = (
        'usuario',
    )

class EliminatoriasAdmin(admin.ModelAdmin):
    list_display = ('usuario',)
    
    list_display_links = (
        'usuario',
    )
    
class PremioIndividualAdmin(admin.ModelAdmin):
    list_display = ('usuario',)
    
    list_display_links = (
        'usuario',
    )

class PontuacaoUsuariosAdmin(admin.ModelAdmin):
    list_display = ('usuario',)
    
    list_display_links = (
        'usuario',
    )

admin.site.register(GrupoA, GrupoAAdmin)
admin.site.register(GrupoB, GrupoBAdmin)
admin.site.register(GrupoC, GrupoCAdmin)
admin.site.register(GrupoD, GrupoDAdmin)
admin.site.register(GrupoE, GrupoEAdmin)
admin.site.register(GrupoF, GrupoFAdmin)
admin.site.register(GrupoG, GrupoGAdmin)
admin.site.register(GrupoH, GrupoHAdmin)
admin.site.register(Eliminatorias, EliminatoriasAdmin)
admin.site.register(PremioIndividual, PremioIndividualAdmin)
admin.site.register(PontuacaoUsuarios, PontuacaoUsuariosAdmin)