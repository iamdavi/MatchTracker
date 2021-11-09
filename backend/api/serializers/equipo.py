from api.models.equipo import Equipo
from rest_framework import serializers


class EquipoSerializer(serializers.ModelSerializer):
    creador = serializers.ReadOnlyField(source='creador.username')

    class Meta:
        model = Equipo
        fields = ['id', 'nombre', 'descripcion', 'fecha_creacion', 'color', 'creador']