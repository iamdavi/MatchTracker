from rest_framework import serializers
from api.models import Jornada
from .equipo import EquipoSerializer
from .rival import RivalSerializer


class JornadaSerializer(serializers.ModelSerializer):
    creador = serializers.ReadOnlyField(source='creador.username')

    class Meta:
        model = Jornada
        fields = ["id", "numero", "fecha", "fecha_creacion", "creador"]