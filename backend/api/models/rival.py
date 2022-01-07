from django.db import models
from datetime import datetime

class Rival(models.Model):
	nombre = models.CharField(max_length=250)
	descripcion = models.CharField(max_length=250, blank=True, null=True)
	fecha_creacion = models.DateTimeField(default=datetime.now)
	creador = models.ForeignKey('auth.user', related_name='rivales', on_delete=models.CASCADE)

	def __str__(self):
		return self.nombre