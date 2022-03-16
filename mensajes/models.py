from django.db import models


class Usuario(models.Model):
    nombre = models.CharField(max_length=100)


class Mensaje(models.Model):
    usuario = models.CharField(max_length=255)
    usuario_obj = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True, blank=True)
    comentario = models.CharField(max_length=255)
    ubicacion = models.CharField(max_length=100, default='Santiago')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.usuario
