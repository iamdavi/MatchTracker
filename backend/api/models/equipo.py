from django.db import models
from datetime import datetime
from django.conf import settings

class Equipo(models.Model):
	nombre = models.CharField(max_length=250)
	descripcion = models.CharField(max_length=250)
	fecha_creacion = models.DateTimeField(default=datetime.now)
	creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

	def __str__(self):
		return self.nombre