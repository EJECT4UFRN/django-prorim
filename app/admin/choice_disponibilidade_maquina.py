from django.contrib import admin
from app.models import ChoiceDisponibilidadeMaquina

class ChoiceDisponibilidadeMaquinaAdmin(admin.ModelAdmin):
    list_display = []
    for field in ChoiceDisponibilidadeMaquina._meta.fields :
        list_display.append(field.name)

admin.site.register(ChoiceDisponibilidadeMaquina, ChoiceDisponibilidadeMaquinaAdmin)