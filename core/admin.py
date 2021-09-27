from core.models import Categoria,Perdido,Achado
from django.contrib import admin

# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    ordering =['nome']
    search_fields = ['nome']
    list_filter = ['nome']

class PerdidoAdmin(admin.ModelAdmin):
    ordering = ['data_perdido']
    lis_display_link = ['data_perdido']
    search_fields = ['nomecompleto','numero','declarante']
    list_filter = ['tipo_item']

class AchadoAdmin(admin.ModelAdmin):
    ordering = ['data_registro']
    lis_display_link = ['data_registro']
    search_fields = ['nomecompleto','numero','declarante']
    list_filter = ['tipo_item']

admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Achado,AchadoAdmin)
admin.site.register(Perdido,PerdidoAdmin)

