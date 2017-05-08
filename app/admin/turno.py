from django.contrib import admin
from app.models import Turno

class TurnoAdmin(admin.ModelAdmin):
    list_display = []
    for field in Turno._meta.fields :
        list_display.append(field.name)

admin.site.register(Turno, TurnoAdmin)
