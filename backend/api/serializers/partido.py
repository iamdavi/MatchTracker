from rest_framework import serializers
from api.models import Partido
from .equipo import EquipoSerializer
from .rival import RivalSerializer


class PartidoSerializer(serializers.ModelSerializer):
    creador = serializers.ReadOnlyField(source='creador.username')
    equipo = EquipoSerializer()
    rival = RivalSerializer()

    class Meta:
        model = Partido
        fields = ["id", "equipo", "rival", "fecha_creacion", "creador"]