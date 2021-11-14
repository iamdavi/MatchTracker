from api.models.equipo import Equipo
from rest_framework import serializers
from api.serializers.jugador import JugadorSerializer


class EquipoSerializer(serializers.ModelSerializer):
    creador = serializers.ReadOnlyField(source='creador.username')
    jugadores = JugadorSerializer(many=True, read_only=True)

    class Meta:
        model = Equipo
        fields = ['id', 'nombre', 'descripcion', 'fecha_creacion', 'color', 'creador', 'jugadores']