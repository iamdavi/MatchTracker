from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from api.models import Equipo
from api.serializers import EquipoSerializer


class EquipoViewSet(viewsets.ModelViewSet):
    queryset = Equipo.objects.all()
    serializer_class = EquipoSerializer

    # @action(detail=False, url_path="current", methods=["GET"])
    # def current_equipos(self, request):
    #     equipos = Equipo.active.all()
    #     serializer = self.get_serializer(equipos, many=True)

    #     return Response(serializer.data, status=status.HTTP_200_OK)

    # @action(detail=False, url_path="closed", methods=["GET"])
    # def closed_pools(self, request):
    #     questions = Question.closed.all()
    #     serializer = self.get_serializer(questions, many=True)

    #     return Response(serializer.data, status=status.HTTP_200_OK)