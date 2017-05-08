from django.contrib import admin
from app.models import ChoicePeriodoTurno

class ChoicePeriodoTurnoAdmin(admin.ModelAdmin):
    list_display = []
    for field in ChoicePeriodoTurno._meta.fields:
        list_display.append(field.name)

admin.site.register(ChoicePeriodoTurno, ChoicePeriodoTurnoAdmin)
