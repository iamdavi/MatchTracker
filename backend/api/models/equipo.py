from django.db import models
from datetime import datetime

class Equipo(models.Model):
	nombre = models.CharField(max_length=250)
	descripcion = models.CharField(max_length=250)
	liga = models.CharField(max_length=250)
	fecha_creacion = models.DateTimeField(default=datetime.now)
	creador = models.OneToOneField('auth.user', related_name='equipo', on_delete=models.CASCADE)

	def __str__(self):
		return self.nombre