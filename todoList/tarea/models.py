from django.db import models

class Tarea(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    fecha_vencimiento = models.DateField(null=True, blank=True)
    completada = models.IntegerField(default=0)
    def __str__(self):
        return self.titulo

