from django.db import models
from datetime import datetime

class Jornada(models.Model):
	creador = models.ForeignKey('auth.user', related_name='jornadas', on_delete=models.CASCADE)
	numero = models.IntegerField()
	fecha = models.DateTimeField()
	fecha_creacion = models.DateTimeField(default=datetime.now)

	def __str__(self):
		return self.numero + ' - ' + self.fecha