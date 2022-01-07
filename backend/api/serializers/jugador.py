from rest_framework import serializers
from api.models import Jugador
from django.conf import settings


class JugadorSerializer(serializers.ModelSerializer):
    equipo = serializers.ReadOnlyField(source='equipo.nombre')
    rol = serializers.ChoiceField(choices=settings.ROL_JUGADOR, required=False, allow_blank=True)

    class Meta:
        model = Jugador
        fields = ["id", "nombre", "numero", "equipo", "rol"]