from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime

# Create your models here.
#
class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_evento = models.DateTimeField(verbose_name="Data do Evento")
    data_criacao = models.DateTimeField(auto_now=True)

    # para usuario
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    # esse cascade é pra qnd for excluido o usario, apaga td q estava associado a ele

    class Meta:
        db_table = 'evento'




    def __str__(self):
        return self.titulo

    def get_data_evento(self):
        return  self.data_evento.strftime('%d/%m/%Y %H:%M')

    def get_data_input_evento(self):
        return self.data_evento.strftime('%Y-%m-%dT%H:%M')

    def get_evento_atrasado(self):
        if self.data_evento < datetime.now():
            return True
        else:
            return False