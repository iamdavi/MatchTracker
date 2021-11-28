from rest_framework import serializers
from api.models import Jugador
import api.constants as constants


class JugadorSerializer(serializers.ModelSerializer):
    equipo = serializers.ReadOnlyField(source='equipo.nombre')
    rol = serializers.ChoiceField(choices=constants.ROL_JUGADOR, required=False, allow_blank=True)

    class Meta:
        model = Jugador
        fields = ["id", "nombre", "numero", "equipo", "rol"]