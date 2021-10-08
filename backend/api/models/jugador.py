from django.db import models
from datetime import datetime
from .equipo import Equipo

class Jugador(models.Model):
	equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name="jugadores")
	nombre = models.CharField(max_length=250)
	numero = models.IntegerField()
	fecha_creacion = models.DateTimeField(default=datetime.now)

	def __str__(self):
		return self.nombre