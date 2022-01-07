from api.models.equipo import Equipo
from api.models.jugador import Jugador
from rest_framework import serializers
from api.serializers.jugador import JugadorSerializer


class EquipoSerializer(serializers.ModelSerializer):
    creador = serializers.ReadOnlyField(source='creador.username')
    jugadores = JugadorSerializer(many=True, read_only=False)

    class Meta:
        model = Equipo
        fields = ['id', 'nombre', 'descripcion', 'fecha_creacion', 'creador', 'jugadores', 'liga']

    def create(self, validated_data):
        jugadores_data = validated_data.pop('jugadores')
        equipo = Equipo.objects.create(**validated_data)
        for jugador in jugadores_data:
            Jugador.objects.create(equipo=equipo, **jugador)
        return equipo

    def update(self, equipo, validated_data):
        jugadores_data = validated_data.pop('jugadores')
        equipo.nombre = validated_data.get('nombre', equipo.nombre)
        equipo.descripcion = validated_data.get('descripcion', equipo.descripcion)
        equipo.save()
        return equipo