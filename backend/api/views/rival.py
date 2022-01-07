from rest_framework import status
from rest_framework.response import Response
from django.http.response import Http404
from rest_framework.views import APIView

from api.models import Rival
from api.serializers import RivalSerializer


class RivalList(APIView):
    queryset = Rival.objects.all()
    serializer_class = RivalSerializer

    def get(self, request):
        rivales = Rival.objects.filter(creador=request.user)
        serializer = RivalSerializer(rivales, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RivalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(creador=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RivalDetail(APIView):
    queryset = Rival.objects.all()
    serializer_class = RivalSerializer

    def get_object(self, pk):
        try:
            return Rival.objects.get(pk=pk)
        except Rival.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        rival = self.get_object(pk)
        serializer = RivalSerializer(rival)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        rival = self.get_object(pk)
        serializer = RivalSerializer(rival, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        rival = self.get_object(pk)
        rival.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)