from django.db import models

class Paciente(models.Model):
    name_pac = models.CharField(max_length=50)
    historial = models.TextField(blank=True)
    telefono = models.CharField(max_length=50)

    def __str__(self):
        return self.name_pac