from api.models.rival import Rival
from api.models.jugador import Jugador
from rest_framework import serializers
from api.serializers.jugador import JugadorSerializer


class RivalSerializer(serializers.ModelSerializer):
    # creador = serializers.ReadOnlyField(source='creador.username')
    jugadores = JugadorSerializer(many=True, read_only=False)

    class Meta:
        model = Rival
        fields = ['id', 'nombre', 'descripcion', 'jugadores']

    def create(self, validated_data):
        jugadores_data = validated_data.pop('jugadores')
        rival = Rival.objects.create(**validated_data)
        for jugador in jugadores_data:
            Jugador.objects.create(rival=rival, **jugador)
        return rival

    def update(self, rival, validated_data):
        jugadores_data = validated_data.pop('jugadores')
        rival.nombre = validated_data.get('nombre', rival.nombre)
        rival.descripcion = validated_data.get('descripcion', rival.descripcion)
        rival.save()
        return rival