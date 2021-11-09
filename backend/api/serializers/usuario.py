from django.contrib.auth.models import User
from rest_framework import serializers

from api.models.equipo import Equipo

class UsuarioSerializer(serializers.ModelSerializer):
    equipo = serializers.PrimaryKeyRelatedField(many=False, queryset=Equipo.objects.all())
    # equipo = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'equipo']