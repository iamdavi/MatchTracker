from rest_framework import status
from rest_framework.response import Response
from django.http.response import Http404
from rest_framework.views import APIView

from api.models import Partido
from api.serializers import PartidoSerializer


class PartidoList(APIView):
    queryset = Partido.objects.all()
    serializer_class = PartidoSerializer

    def get(self, request):
        partidos = Partido.objects.filter(creador=request.user)
        serializer = PartidoSerializer(partidos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PartidoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(creador=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PartidoDetail(APIView):
    queryset = Partido.objects.all()
    serializer_class = PartidoSerializer

    def get_object(self, pk):
        try:
            return Partido.objects.get(pk=pk)
        except Partido.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        partido = self.get_object(pk)
        serializer = PartidoSerializer(partido)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        partido = self.get_object(pk)
        serializer = PartidoSerializer(partido, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        partido = self.get_object(pk)
        partido.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)