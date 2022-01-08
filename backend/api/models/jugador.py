from django.db import models
from datetime import datetime
from .equipo import Equipo
from .rival import Rival
from django.conf import settings

class Jugador(models.Model):
	equipo = models.ForeignKey(
		Equipo, 
		on_delete=models.CASCADE, 
		related_name="jugadores",
		blank=True,
		null=True
	)
	rival = models.ForeignKey(
		Rival, 
		on_delete=models.CASCADE, 
		related_name="jugadores",
		blank=True,
		null=True
	)
	nombre = models.CharField(max_length=250)
	numero = models.IntegerField(null=True)
	rol = models.CharField(max_length=1, choices=settings.ROL_JUGADOR, default='J')
	fecha_creacion = models.DateTimeField(default=datetime.now)

	def __str__(self):
		return self.nombre