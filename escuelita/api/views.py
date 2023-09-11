from ..models import Jugador, Equipo
from rest_framework import viewsets, permissions
from .serializers import JugadorSerializer,EquipoSerializer

class JugadorViewSet(viewsets.ModelViewSet):
    queryset = Jugador.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = JugadorSerializer

class EquipoViewSet(viewsets.ModelViewSet):
    queryset = Equipo.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = EquipoSerializer
