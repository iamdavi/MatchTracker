from django.http.response import Http404
from rest_framework.views import APIView
from api.models import Equipo
from rest_framework.decorators import api_view
from api.serializers import EquipoSerializer, RivalSerializer
from rest_framework import  status, permissions, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.conf import settings
import json


class EquipoList(APIView):
    """
    Obtiene la información del equipo. Solo se obtiene la información del que
    ha creado el equipo usuario, ya que solo puede tener uno
    Se encarga de crear el equipo del usuario
    """
    queryset = Equipo.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_object(self, user):
        try:
            return Equipo.objects.get(creador=user)
        except Equipo.DoesNotExist:
            raise Http404

    def guardar_rival(self, nombre_rival, jugadores_rival, usuario):
        arr_jugadores_rival = []
        for jugador in jugadores_rival:
            arr_jugadores_rival.append({
                'nombre': jugador[1],
                'numero': jugador[0]
            })
        obj_rival = {
            'nombre': nombre_rival,
            'jugadores': arr_jugadores_rival
        }
        serializer = RivalSerializer(data=obj_rival)
        if serializer.is_valid():
            serializer.save(creador=usuario)


    def registrar_rivales(self, data, usuario) -> None:
        nombre_equipo = data['nombre']
        liga_equipo = data['liga']
        for liga in settings.EQUIPO_DATA['ligas']:
            if liga['nombre'] == liga_equipo:
                for equipo in liga['equipos']:
                    if equipo != nombre_equipo:
                        self.guardar_rival(equipo, liga['equipos'][equipo], usuario)


    def get(self, request) -> Response:
        equipo = self.get_object(request.user)
        serializer = EquipoSerializer(equipo, many=False)
        return Response(serializer.data)

    def post(self, request) -> Response:
        serializer = EquipoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(creador=request.user)
            self.registrar_rivales(serializer.data, request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request) -> Response:
        equipo = self.get_object(request.user)
        serializer = EquipoSerializer(equipo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request) -> Response:
        equipo = self.get_object(request.user)
        equipo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class EquipoViewSet(viewsets.ModelViewSet):
    """
    Rutas personalizadas para realizar acciones especificas
    """
    queryset = Equipo.objects.all()
    serializer_class = EquipoSerializer

    @action(detail=False, methods=['GET'], name="Equipos disponibles")
    def disponibles(self, request):
        """
        Obtinene el JSON de las ligas y los equipos disponibles
        """
        return Response(settings.EQUIPO_DATA)

