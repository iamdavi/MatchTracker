from django.http.response import Http404
from rest_framework.views import APIView
from api.models import Equipo
from api.serializers import EquipoSerializer
from rest_framework import  status, permissions
from rest_framework.response import Response


# class EquipoViewSet(viewsets.ModelViewSet):
#     queryset = Equipo.objects.all()
#     serializer_class = EquipoSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

#     def perform_create(self, serializer):
#         serializer.save(creador=self.request.user)


class EquipoList(APIView):
    """
    Obtiene la información del equipo. Solo se obtiene la información del que
    ha creado el equipo usuario, ya que solo puede tener uno
    Se encarga de crear el equipo del usuario
    """
    queryset = Equipo.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


    def get(self, request):
        """
        Método que se encarga de obtener la información del equipo de usuario
        logeado.
        
        Devuelve    Response con la información del equipo, a pesar de no obtener ningún
                    equipo, no tira error, si no que devuelve []
        """
        equipo = Equipo.objects.filter(creador=request.user)
        serializer = EquipoSerializer(equipo, many=True)
        return Response(serializer.data)
    

    def post(self, request):
        tiene_equipo = Equipo.objects.filter(creador=request.user)
        serializer = EquipoSerializer(data=request.data)
        if tiene_equipo:
            return Response({ 'msg': 'Ya tienes un equipo!' }, status=status.HTTP_400_BAD_REQUEST)
        if serializer.is_valid():
            serializer.save(creador=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EquipoDetail(APIView):
    """
    Retrieve, update or delete a equipo instance.
    """
    def get_object(self, pk):
        try:
            return Equipo.objects.get(pk=pk)
        except Equipo.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = EquipoSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = EquipoSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)