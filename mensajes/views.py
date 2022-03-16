from django.shortcuts import render
from rest_framework import viewsets, permissions
from mensajes.models import Mensaje, Usuario
from mensajes.serializers import MensajeSerializer, UsuarioSerializer


class MensajesViewSet(viewsets.ModelViewSet):
    queryset = Mensaje.objects.all()
    serializer_class = MensajeSerializer
    # permission_classes = [permissions.IsAuthenticated]


class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    # permission_classes = [permissions.IsAuthenticated]

