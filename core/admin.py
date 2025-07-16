from django.contrib import admin

from core.models import Evento

# Register your models here.
class Exbicao(admin.ModelAdmin):
    list_display = ('id','titulo', 'usuario', 'descricao', 'data_evento', 'data_criacao')
    list_filter = ('usuario', 'data_evento',)


admin.site.register(Evento, Exbicao)