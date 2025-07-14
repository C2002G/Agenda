from django.db import models
from django.contrib.auth.models import User

# Create your models here.

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