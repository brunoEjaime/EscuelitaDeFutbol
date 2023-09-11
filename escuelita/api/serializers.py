from rest_framework import serializers
from ..models import *

class JugadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jugador
        fields = ('dni','nombre','apellido','fechaNacimiento','vigencia')
       


class EquipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipo
        fields = ('jugador','categoria','tira')
        