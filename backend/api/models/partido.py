from django.db import models
from datetime import datetime

from .equipo import Equipo
from .jornada import Jornada
from .rival import Rival

class Partido(models.Model):
	equipo = models.ForeignKey(Equipo, related_name="partidos", on_delete=models.CASCADE)
	rival = models.ForeignKey(Rival, related_name="partidos", on_delete=models.CASCADE)
	jornada = models.ForeignKey(Jornada, related_name="partidos", on_delete=models.CASCADE)
	creador = models.ForeignKey('auth.user', related_name='partidos', on_delete=models.CASCADE)
	fecha_partido = models.DateTimeField()
	hora_partido = models.CharField(max_length=5) # Str que representa la hora: HH:MM
	local = models.CharField(max_length=255)
	visitante = models.CharField(max_length=255)
	fecha_creacion = models.DateTimeField(default=datetime.now)

	def __str__(self):
		return self.equipo + ' - ' + self.rival