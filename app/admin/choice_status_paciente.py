from django.contrib import admin
from app.models import ChoiceStatusPaciente

class ChoiceStatusPacienteAdmin(admin.ModelAdmin):
    list_display = []
    for field in ChoiceStatusPaciente._meta.fields:
        list_display.append(field.name)

admin.site.register(ChoiceStatusPaciente, ChoiceStatusPacienteAdmin)
