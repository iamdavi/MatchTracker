from rest_framework.serializers import CurrentUserDefault, HiddenField, ModelSerializer
from api.models import Jugador, Equipo

from .jugador import JugadorSerializer


class EquipoSerializer(ModelSerializer):
    creador = HiddenField(default=CurrentUserDefault())
    jugadores = JugadorSerializer(many=True)

    class Meta:
        model = Equipo
        fields = ["id", "nombre", "fecha_creacion", "descripcion", "jugadores", "creador"]

    def create(self, validated_data):
        jugadores = validated_data.pop("jugadores")
        equipo = Equipo.objects.create(**validated_data)
        for jugador in jugadores:
            Jugador.objects.create(equipo=equipo, **jugador)
        return equipo

    def update(self, instance, validated_data):
        jugadores = validated_data.pop("jugadores")
        instance.nombre = validated_data.get("nombre", instance.nombre)
        instance.descripcion = validated_data.get("descripcion", instance.descripcion)
        instance.save()
        keep_jugadores = []
		# Se incremente el id de los jugadores
        for jugador in jugadores:
			# De donde se obtiene '.keys()'?
            if "id" in jugador.keys():
                if Jugador.objects.filter(id=jugador["id"]).exists():
                    j = Jugador.objects.get(id=jugador["id"])
                    j.nombre = jugador.get("jugador", j.jugador)
                    j.numero = jugador.get("numero", j.numero)
                    j.save()
                    keep_jugadores.append(j.id)
                else:
                    continue
            else:
                j = Jugador.objects.create(equipo=instance, **jugador)
                keep_jugadores.append(j.id)
        for jugador in instance.jugadores.all():
            if jugador.id not in keep_jugadores:
                jugador.delete()

        return instance