from rest_framework.serializers import ModelSerializer, IntegerField
from rest_framework.response import Response
from api.models import Jugador


class JugadorSerializer(ModelSerializer):
    class Meta:
        model = Jugador
        fields = ["id", "nombre", "numero", "equipo", "fecha_creacion"]
        read_only_fields = ("equipo",)