from rest_framework import serializers
from api.models import Jugador


class JugadorSerializer(serializers.ModelSerializer):
    equipo = serializers.ReadOnlyField(source='equipo.nombre')

    class Meta:
        model = Jugador
        fields = ["nombre", "numero", "equipo"]