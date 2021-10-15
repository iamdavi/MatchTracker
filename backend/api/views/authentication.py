from rest_framework import generics, status, permissions
from rest_framework.response import Response
from ..serializers.authentication import LogoutSerializer

class LogoutAPIView(generics.GenericAPIView):
	serializer_class = LogoutSerializer
	permission_classes = (permissions.IsAuthenticated,)

	def post(self, request):
		serializer = self.serializer_class(data=request.data)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(status=status.HTTP_204_NO_CONTENT)