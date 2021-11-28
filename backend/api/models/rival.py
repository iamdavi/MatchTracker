from django.db import models
from datetime import datetime
from api.models.equipo import Equipo as EquipoModel

class Rival(models.Model):
	nombre = models.CharField(max_length=250)
	descripcion = models.CharField(max_length=250)
	fecha_creacion = models.DateTimeField(default=datetime.now)
	color = models.CharField(max_length=250, null=True)

	def __str__(self):
		return self.nombre

		# TODO: eliminar BD y generar una nueva