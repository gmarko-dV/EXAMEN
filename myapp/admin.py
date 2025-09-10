from django.contrib import admin
from .models import Paciente

class PacienteAdmi(admin.ModelAdmin):
    readonly_fields = ("created",)
# Register your models here.