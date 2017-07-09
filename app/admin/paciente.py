from django.contrib import admin
from app.models import Paciente

class PacienteAdmin(admin.ModelAdmin):
    list_display = []
    for field in Paciente._meta.fields:
        list_display.append(field.name)

admin.site.register(Paciente, PacienteAdmin)
